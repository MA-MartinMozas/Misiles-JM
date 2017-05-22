import numpy as np

# Definimos una clase para el misil entero
class geometry(object):
    def __init__(self, M, rho, a, mu,d,la,lx):
        self.M = M
        self.rho = rho
        self.a = a
        self.mu = mu
        self.d = d
        self.la = la
        self._supcil = 0
        self._Rex = 0
        self._supref = 0
        self.lx = lx

    # Definimos el Reynolds
    @property
    def Rex(self):
        return (self.rho * self.M * self.a * self.lx) / self.mu
    # Definimos la superficie cilíndrica
    @property
    def supcil(self):
        return np.pi * self.d * self.la
    # Definimos la superficie de referencia
    @property
    def supref(self):
        return np.pi * self.d ** 2 / 4
    # Definimos el centro de masas
    @property
    def Xcg(self):
        return  # FALTA COMPLETAR!!

# #Para calcular Xcg se divide el misil en cuatro partes: fuselaje, sección delantera, alas, canard
#  1)El usuario mete como variable el peso de cada parte
#  2)Se calcula el Xcg de cada parte con el peso y la longitud
#  3)Se hace la media??
#   TENGO QUE PREGUNTAR MAÑANA EN LA ESCUELAA!!

# Definimos una clase para el tipo de cabeza que hereda de la clase para el misil entero
class cabeza(object):

    def __init__(self, lc , ln, d_inic):

        self.d_inic = d_inic
        self.ln = ln
        self.lc = lc
        self._supcono = 0

    # Definimos la superficie del cono porque es común a todos los tipos de cabeza
    @property
    def supcono(self):
        return np.pi*(self.d_inic.d/2)*np.sqrt((self.d_inic.d/2)**2+self.lc**2)


# Definimos clase cónica que hereda de cabeza
class conica(cabeza):

    def __init__(self, lc , ln, d_inic):
        super().__init__(lc , ln, d_inic)

        self._angucono = 0
        self._CDWC = 0
        self._DWcono = 0

    # Cálculo del ángulo del cono
    @property
    def angucono(self):
        return np.tan(self.d_inic.d/(2*self.ln))

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

    def __init__(self, lc, ln, d_inic ):
        super().__init__(lc, ln, d_inic)
        self._anguojiva = 0
        self._CDWO = 0
        self._DWojiva = 0

    # Cálculo del ángulo de la ojiva
    @property
    def anguojiva(self):
        return 2*np.tan(self.d_inic.d/(2*self.ln))

    # Resistencia de onda ojiva

    # Cálculo del coeficiente de resistencia de onda ojiva
    @property
    def CDWO(self):
        return ((0.083 + 0.096 / (self.d_inic.M ** 2)) * (self.anguojiva / 10) ** 1.69)*(1-(392*(self.ln/2)**2-32)/(28*(self.d_inic.M+18)*(self.ln/self.d_inic.d)**2))

    # Cálculo de la Resistencia de onda ojiva
    @property
    def DWojiva(self):
        return 0.5 * self.d_inic.rho * (self.d_inic.M * self.d_inic.a) ** 2 * self.d_inic.supref * self.CDWO


# class aleta (objeto):
# # aquí metemos las características para la aletas de cálculo de su Xcg
# class delta(aleta):
# #   subclase que hereda de aleta y donde metemos las características para que sea delta
# class rectangular(aleta):
# #     aquí como la anterior pero dado que el canard solo lo vamos a hacer tipo rectangular usamos tambien esta clase para hacer sus cálculos


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
# Repasar con cálculos a mano OJOOOOOOOOOOOOOOOOOOOOOOO
class m_estabilidad(object):
    def __init__(self, d_inic, b, c, lt, ln, Cnalphabeta):
        self.d_inic= d_inic
        self.b= b
        self.c= c
        self.lt= lt
        self.ln = ln
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
    def Cnalphawing(self):
        return (4/np.sqrt(self.d_inic.M**2-1))*(1-(1/(2*np.sqrt(self.d_inic.M**2-1)*(self.b/self.c))))

    @property
    def Xcpbeta(self):
        return 2*self.ln/3

    @property
    def Xcpwing(self):
        return self.lt - self.c/2

    @property
    def Kwb(self):
        return 1 + self.d_inic.d/(self.b+self.d_inic.d)

    @property
    def Kbw(self):
        return (self.d_inic.d/(self.d_inic.d+self.b))(1 + self.d_inic.d/(self.b+self.d_inic.d))

    @property
    def Cnalpha(self):
        return(self.Cnalphabeta + self.Cnalphawing*(self.Kwb + self.Kbw)*self.b*self.c/self.d_inic.supref)

    # !!!!!atención en esta se usa xcg que no está definido porque es el xcg de la aleta y no hemos hecho esa clasee corregir!!!!
    @property
    def Cmalpha(self):
        return(self.Cnalphabeta*((self.d_inic.Xcg-self.Xcpbeta)/self.d_inic.d) + self.Cnalphawing*(self.Kwb + self.Kbw)*self.b*self.c/self.d_inic.supref*((self.d_inic.Xcg-self.Xcpwing)/self.d_inic.d))

    @property
    def h(self):
        return(-self.Cmalpha/self.Cnalpha)


# Definimos una clase para Maniobrabilidad y Capacidad de maniobra máxima que hereda de Margen de estabilidad estático
# Repasar con cálculos a mano OJOOOOOOOOOOOOOOOOOOOOOOO
class manio_cap(m_estabilidad):

    def __init__(self, d_inic, b, c, lt, m, Cnsat):
        super().__init__(d_inic, b, c, lt)
        self.m = m
        self.g = 9.81  # Este valor es invariable
        self.Cnsat = Cnsat
        self._maniobrabilidad = 0
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
        return self.Cnalphawing * (self.Kmb + self.Kbm) * self.b * self.c / self.d_inic.supref
    # !!!!!atención en esta se usa xcg que no está definido porque es el xcg de la aleta y no hemos hecho esa clasee corregir!!!!
    @property
    def Cmdelta(self):
        return self.Cnalphawing * (self.Kmb + self.Kbm) * self.b * self.c / self.d_inic.supref * ((self.d_inic.Xcg - self.Xcpwing) / self.d_inic.d)

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





#importante no cambiar nombre de d_inic
d_inic = geometry( 1,1,1,1,1,1,1)
print(d_inic.Rex)
# prueba de que con la barra baja no coge el valor obtenido en la función si no el dado en el init
print(d_inic.supref)
print(d_inic._supref)

miconica= conica(2,3,d_inic)
print(miconica.angucono)
print(miconica.CDWC)
print(miconica.DWcono)

c_fric= r_friccion(d_inic)
print(c_fric.CDfilam)
print(c_fric.CDfi)
print(c_fric.CDflam)
print(c_fric.Df)