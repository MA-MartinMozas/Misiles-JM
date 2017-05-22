import numpy as np

# Definimos una clase para misión
class mision(object):
    def __init__(self, , etamnmax, vm, vt, deltato, ro):
        self.etamnmax = etamnmax
        self.vm = vm
        self.vt = vt
        self.deltato = deltato
        self.ro = ro

# Definimos una clase para Persecución Pura que hereda de la clase misión
class ppura(mision):
    def __init__(self, deltat, d_inic):
        self.d_inic = d_inic
        self.deltat = deltat
        self._K = 0
        self._deltati = 0
        self._etamnn = 0
        self._t = 0
        self._r = 0
        self._xt = 0

    @property
    def K(self):
        return self.d_inic.vm / self.d_inic.vt

    @property
    def deltati(self):
        return np.arccos(self.K/2)

    @property
    def etamnm(self):
        return self.d_inic.vt*self.d_inic.vm*np.sin(self.d_inic.deltato)/self.d_inic.ro

    @property
    def t(self):
        return ((-self.d_inic.ro*np.sin(self.d_inic.deltato))/(2*self.d_inic.vt*(np.tan(self.d_inic.deltato))**2))*(((np.tan(self.deltat/2))**(self.K-1))/(self.K-1)+((np.tan(self.deltat/2))**(self.K+1))/(self.K+1))

    @property
    def r(self):
        return self.d_inic.ro*(np.tan(self.deltati/2)/np.tan(self.d_inic.deltato/2))**self.K*(np.sin(self.d_inic.deltato)/np.sin(self.deltati))

    @property
    def xt(self):
        return self.d_inic.vt/self.t

# Definimos una clase para Navegación Proporcional que hereda de la clase misión
class naveproporc(mision):
    def __init__(self, deltamo, etatn, a, d_inic):
        self.d_inic = d_inic
        self.deltamo = deltamo
        self.etatn = etatn
        self.a = a
        self._deltamc = 0
        self._incrementodeltam = 0
        self._ti = 0
        self._etamncalculado = 0

    #Si es maniobrante FALTAAA!!
    #Si es NO maniobrante

    @property
    def deltamc(self):
        return np.arcsin(self.d_inic.vt*np.sin(self.d_inic.deltato)/self.d_inic.vm)

    @property
    def incrementodeltam(self):
        return self.deltamo-self.deltamc

    @property
    def ti(self):
        return self.d_inic.ro/(self.d_inic.vm*np.cos(self.deltamo)-self.d_inic.vt*np.sin(self.d_inic.deltato))

    @property
    def etamncalculado(self):
        return (self.a*self.d_inic.vm/self.ti)*(self.incrementodeltam*np.pi/180)*(1-self.t/self.ti)**(self.a-2)
    #atencion tengo que definir t!!
