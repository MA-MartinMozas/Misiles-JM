import numpy as np
import ws


# Definimos una clase para el misil entero
class geometry(object):
    def __init__(self, M, rho, a, mu,d,la,lc,xe,lmaxu,xcanard,lrd,mfuselaje,mcabeza,maletas,mcanard,fin):
        self.M = M
        self.rho = rho
        self.a = a
        self.mu = mu
        self.d = d
        self.la = la

        self.lc = lc
        self.xe = xe
        self.lmaxu = lmaxu
        self.xcanard = xcanard
        self.lrd = lrd
        self.mfuselaje = mfuselaje
        self.mcabeza = mcabeza
        self.maletas = maletas
        self.mcanard = mcanard
        self.fin = fin

    # Primero se calcula el centro de gravedad.
    # Para calcular Xcg se divide el misil en cuatro partes: fuselaje, sección delantera, aletas, canard.
    # Posteriormente, se calcula el Xcg de cada parte, respecto a la proa, luego se calcula la masa del misil total y por último el Xcg del misil

    # Definimos el centro de masas del fuselaje respecto a la proa
    @property
    def Xcgfus(self):
        return self.la / 2 + self.lc

    # Definimos el centro de masas de la sección delantera respecto a la proa
    @property
    def Xcgcabeza(self):
        return self.lc * 2 / 3

    # Definimos el centro de masas de las aletas respecto a la proa
    @property
    def Xcgaletas(self):
        # Aquí hay que meter CONDICIONAAAL!
        if self.fin == "Delta":
            return self.xe + 2 * self.lmaxu / 3
        else:
            return self.xe + self.lmaxu / 2

    # Definimos el centro de masas del canard respecto a la proa
    @property
    def Xcgcanard(self):
        return self.xcanard + self.lrd / 2

    # Calculamos la masa del misil
    @property
    def m(self):
        return self.mfuselaje + self.mcabeza + self.maletas + self.mcanard

    # Definimos el centro de masas del misil completo respecto a la proa
    @property
    def Xcg(self):
        return (self.mfuselaje * self.Xcgfus + self.mcabeza * self.Xcgcabeza + self.maletas * self.Xcgaletas + self.mcanard * self.Xcgcanard) / self.m


    # Definimos el Reynolds
    @property
    def Rex(self):
        return (self.rho * self.M * self.a * self.Xcg) / self.mu

    # Definimos la superficie cilíndrica
    @property
    def supcil(self):
        return np.pi * self.d * self.la
    # Definimos la superficie de referencia
    @property
    def supref(self):
        return np.pi * self.d ** 2 / 4

# Definimos una clase para el tipo de cabeza que hereda de la clase para el misil entero
class cabeza(object):

    def __init__(self, d_inic):

        self.d_inic = d_inic
        self._supcono = 0

    # Definimos la superficie del cono porque es común a todos los tipos de cabeza
    @property
    def supcono(self):
        return np.pi*(self.d_inic.d/2)*np.sqrt((self.d_inic.d/2)**2+self.d_inic.lc**2)


# Definimos clase cónica que hereda de cabeza
class conica(cabeza):

    def __init__(self, d_inic):
        super().__init__(d_inic)

        self._angucono = 0
        self._CDWC = 0
        self._DWcono = 0

    # Cálculo del ángulo del cono
    @property
    def angucono(self):
        return np.tan(self.d_inic.d/(2*self.d_inic.lc))

    # Resistencia de onda cono

    # Cálculo del coeficiente de resistencia de onda cono
    @property
    def CDWC(self):
        return (0.083+0.096/(self.d_inic.M**2))*(self.angucono/10)**1.69

    # Cálculo de la Resistencia de onda cono
    @property
    def DWcono(self):
        return 0.5*self.d_inic.rho * (self.d_inic.M * self.d_inic.a)**2 * self.d_inic.supref * self.CDWC


# Definimos clase ojival que hereda de cabeza
class ojival(cabeza):

    def __init__(self, d_inic ):
        super().__init__(d_inic)
        self._anguojiva = 0
        self._CDWO = 0
        self._DWojiva = 0

    # Cálculo del ángulo de la ojiva
    @property
    def anguojiva(self):
        return 2*np.tan(self.d_inic.d/(2*self.d_inic.lc))

    # Resistencia de onda ojiva

    # Cálculo del coeficiente de resistencia de onda ojiva
    @property
    def CDWO(self):
        return ((0.083 + 0.096 / (self.d_inic.M ** 2)) * (self.anguojiva / 10) ** 1.69)*(1-(392*(self.d_inic.lc/2)**2-32)/(28*(self.d_inic.M+18)*(self.d_inic.lc/self.d_inic.d)**2))

    # Cálculo de la Resistencia de onda ojiva
    @property
    def DWojiva(self):
        return 0.5 * self.d_inic.rho * (self.d_inic.M * self.d_inic.a) ** 2 * self.d_inic.supref * self.CDWO




# Definimos una clase para Resistencia de fricción que hereda de objeto y es común a todos los tipos de cabeza
class r_friccion (object) :
    def __init__(self, d_inic):
        self.d_inic= d_inic

    # Cálculo de los coeficientes de fricción
    @property
    def CDfilam(self):
        return 0.664 / np.sqrt(self.d_inic.Rex)

    @property
    def CDfi(self):
        return 1.328 / np.sqrt(self.d_inic.Rex)

    @property
    def CDflam(self):
        return ((1/(1+0.17*self.d_inic.M**2))**0.12950)*self.CDfi

    # Cálculo de la Resistencia de fricción
    @property
    def Df(self):
        return 0.5 * self.d_inic.rho * (self.d_inic.M * self.d_inic.a) ** 2 * self.d_inic.supref * self.CDflam

# Definimos una clase para Margen de estabilidad estático que hereda de objeto y es común a todos los tipos de cabeza
# Repasar con cálculos a mano OJOOOOOOOOOOOOOOOOOOOOOOO. LUEGO BORRAR ESTA NOTITA
class m_estabilidad(object):
    def __init__(self, d_inic, b, Cnalphabeta):
        self.d_inic= d_inic
        self.b= b
        self._lt= 0
        self.Cnalphabeta = Cnalphabeta
        self._Cnalphawing = 0
        self._Xcpbeta = 0
        self._Xcpwing = 0
        self._Kwb = 0
        self._Kbw = 0
        self._Cnalpha = 0
        self._Cmalpha = 0
        self._h = 0

    @property
    def lt(self):
        return self.d_inic.la + self.d_inic.lc

    # Continuamos con el cálculo del margen de estabilidad estático
    @property
    def Cnalphawing(self):
        return (4/np.sqrt(self.d_inic.M**2-1))*(1-(1/(2*np.sqrt(self.d_inic.M**2-1)*(self.b/self.d_inic.lmaxu))))

    @property
    def Xcpbeta(self):
        return 2*self.d_inic.lc/3

    @property
    def Xcpwing(self):
        return self.lt - self.d_inic.lmaxu/2

    @property
    def Kwb(self):
        return 1 + self.d_inic.d/(self.b+self.d_inic.d)

    @property
    def Kbw(self):
        return (self.d_inic.d/(self.d_inic.d+self.b))*(1 + self.d_inic.d/(self.b+self.d_inic.d))

    @property
    def Cnalpha(self):
        return(self.Cnalphabeta + self.Cnalphawing*(self.Kwb + self.Kbw)*self.b*self.d_inic.lmaxu/self.d_inic.supref)

    @property
    def Cmalpha(self):
        return(self.Cnalphabeta*((self.d_inic.Xcg-self.Xcpbeta)/self.d_inic.d) + self.Cnalphawing*(self.Kwb + self.Kbw)*self.b*self.d_inic.lmaxu/self.d_inic.supref*((self.d_inic.Xcg-self.Xcpwing)/self.d_inic.d))

    @property
    def h(self):
        return(-self.Cmalpha/self.Cnalpha)


# Definimos una clase para Maniobrabilidad y Capacidad de maniobra máxima que hereda de Margen de estabilidad estático
# Repasar con cálculos a mano OJOOOOOOOOOOOOOOOOOOOOOOO
class manio_cap(m_estabilidad):

    def __init__(self, d_inic, b, Cnalphabeta, Cnsat):
        super().__init__(d_inic, b, Cnalphabeta)
        self.g = 9.81  # Este valor es invariable
        self.Cnsat = Cnsat
        self._Cndelta = 0
        self._Cmdelta = 0
        self._Kbm = 0
        self.Kmb = 1  # Este valor es invariable
        self._maniobrabilidad = 0
        self._alphasatur = 0
        self._nmaximo = 0
        self._deltamani = 0

    @property
    def Kbm(self):
        return self.d_inic.d / (self.d_inic.d + self.b)

    @property
    def Cndelta(self):
        return self.Cnalphawing * (self.Kmb + self.Kbm) * self.b * self.d_inic.lmaxu / self.d_inic.supref

    @property
    def Cmdelta(self):
        return self.Cnalphawing * (self.Kmb + self.Kbm) * self.b * self.d_inic.lmaxu / self.d_inic.supref * ((self.d_inic.Xcg - self.Xcpwing) / self.d_inic.d)

    @property
    def maniobrabilidad(self):
        return ((0.5*self.d_inic.rho*(self.d_inic.a*self.d_inic.M)**2*self.d_inic.supref)/self.d_inic.m*9.81)*(self.Cndelta+self.Cmdelta/self.h)

    @property
    def alphasatur(self):
        return -self.Cnsat/self.Cnalphawing

    @property
    def deltamani(self):
        return self.alphasatur/(self.Kwb*(-self.Cmdelta/self.Cmalpha)+self.Kmb)

    @property
    def nmaximo (self):
        return self.deltamani*self.maniobrabilidad


def principal(geo):
    """

    :param geo:
    :type geo: dict
    :return:
    """
    # el código fallará si introducimos un string en vez de un  número por lo que podría ser algo a mejorar
    for key, value in geo.items():
        if key == "tipo":
            pass
        elif key == "finType":
            pass
        else:
            geo[key] = np.float64(value)
    fin = geo["finType"]
    d = geo['d']
    M = geo['M']
    a = geo['a']
    mu = geo['mu']
    la = geo['la']
    rho = geo["rho"]
    xe = geo['xe']
    lmaxu = geo['lmaxu']
    xcanard = geo['xcanard']
    lrd = geo['lrd']
    mfuselaje = geo['mfuselaje']
    mcabeza = geo['mcabeza']
    maletas = geo['maletas']
    mcanard = geo['mcanard']
    lc = geo["lc"]
    d_inic = geometry( M,rho,a,mu,d,la, lc, xe,lmaxu,xcanard,lrd,mfuselaje,mcabeza,maletas,mcanard,fin)


    micabeza = cabeza(d_inic)
    miconica = conica(d_inic)
    c_fric= r_friccion(d_inic)
    miojiva = ojival(d_inic)

    b = geo['b']

    Cnalphabeta = geo['Cnalphabeta']
    mim_estabilidad = m_estabilidad(d_inic,b,Cnalphabeta)

    Cnsat = geo['Cnsat']
    mimanio_cap = manio_cap(d_inic, b, Cnalphabeta, Cnsat)

    resultados = {"tipo":"geo", "Rex": d_inic.Rex, "supcil": d_inic.supcil, "supref": d_inic.supref,
                  "supcono": micabeza.supcono,
                  "angucono": miconica.angucono, "CDWC": miconica.CDWC, "DWcono": miconica.DWcono,
                  "anguojiva": miojiva.anguojiva, "CDWO": miojiva.CDWO, "DWojiva": miojiva.DWojiva,
                  "CDfilam": c_fric.CDfilam, "CDfi": c_fric.CDfi, "CDflam": c_fric.CDflam,
                  "Xcgfus": d_inic.Xcgfus,"Xcgcabeza": d_inic.Xcgcabeza,"Xcgaletas": d_inic.Xcgaletas,
                  "Xcgcanard": d_inic.Xcgcanard,"m": d_inic.m,
                  "Xcg": d_inic.Xcg,"Cnalphawing": mim_estabilidad.Cnalphawing,"Xcpbeta": mim_estabilidad.Xcpbeta,
                  "Xcpwing": mim_estabilidad.Xcpwing,"Kwb": mim_estabilidad.Kwb,
                  "Kbw": mim_estabilidad.Kbw,"Cnalpha":mim_estabilidad.Cnalpha,"Cmalpha": mim_estabilidad.Cmalpha, "h": mim_estabilidad.h,
                  "Cndelta": mimanio_cap.Cndelta,"Cmdelta": mimanio_cap.Cmdelta,"Kbm": mimanio_cap.Kbm,"maniobrabilidad": mimanio_cap.maniobrabilidad,
                  "alphasatur": mimanio_cap.alphasatur,"nmaximo": mimanio_cap.nmaximo,"deltamani": mimanio_cap.deltamani,"lt": mim_estabilidad.lt}


    for key, value in resultados.items():
        if key == "tipo":
            resultados[key] = value
        else:
            # "%.3f" %value,
            resultados[key] = "%.3f" % value,

    return resultados

if __name__ == '__main__':
    #importante no cambiar nombre de d_inic
    d_inic = geometry( 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1)
    print(d_inic.Rex)
    # prueba de que con la barra baja no coge el valor obtenido en la función si no el dado en el init
    print(d_inic.supref)
    print(d_inic._supref)

    miconica= conica(d_inic)
    print(miconica.angucono)
    print(miconica.CDWC)
    print(miconica.DWcono)
    micabeza= cabeza(d_inic)
    print(cabeza.supcono)

    c_fric= r_friccion(d_inic)
    print(c_fric.CDfilam)
    print(c_fric.CDfi)
    print(c_fric.CDflam)
    print(c_fric.Df)