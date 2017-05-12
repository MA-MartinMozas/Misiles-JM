
import numpy as np

# Definir clases para la Sección delantera
from sklearn.ensemble._gradient_boosting import np_bool


class Cabeza(object):

    def __init__(self, d, la, ln, M, rho, a, lx, mu, Cnalphabeta, b, c, lt, Cnsat, delta, m):
        self._supcil = 0
        self._Rex = 0
        self.d = d
        self.la = la
        self.M = M
        self.ln = ln
        self.rho = rho
        self.a = a
        self.supref = 0
        self.lx = lx
        self.mu = mu
        self._cdfilam = 0
        self._CDfi = 0
        self._CDflam = 0
        self._Df = 0
        self.Cnalphabeta = Cnalphabeta
        self.b = b
        self.c = c
        self.lt = lt
        self.Cnsat = Cnsat
        self.delta = delta
        self.m = m
        self.g = 9.81

    # @property
    # def d(self):
    #     return self._d
    # @d.setter
    # def d(self, d):
    #     self._d = d

    @property
    def supcil(self):
        return np.pi*self.d*self.la


class conica(Cabeza):

    # Datos geometría
    def __init__(self, lc):
        self._supcono = 0
        self.lc = lc
        self._angucono = 0
        self._CDWC = 0
        self._DWcono = 0

    @property
    def supcono(self):
        return np.pi*(self.d/2)*np.sqrt((self.d/2)**2+self.lc**2)

    @property
    def angucono(self):
        return np.tan(self.d/(2*self.ln))

    # Resistencia de onda cono

    # Cálculo del coeficiente de resistencia de onda cono
    @property
    def CDWC(self,self._angucono):
        return (0.083+0.096/(self.M**2))*(self.angucono/10)**1.69

    # Cálculo de la Resistencia de onda cono
    @property
    def DWcono(self, CDWC):
        return 0.5*self.rho * (self.M * self.a)**2 * self.supref*self.CDWC


class ojival(Cabeza):
    # Datos geometría

    def __init__(self):
        self._anguojiva = 0
        self._CDWO = 0
        self._DWojiva = 0

    @property
    def anguojiva(self):
        return 2*np.tan(self.d/(2*self.ln))

    # Resistencia de onda ojiva

    # Cálculo del coeficiente de resistencia de onda ojiva
    @property
    def CDWO(self, anguojiva):
        return ((0.083 + 0.096 / (self.M ** 2)) * (self.anguojiva / 10) ** 1.69)*(1-(392*(self.ln/2)**2-32)/(28*(self.M+18)*(self.ln/self.d)**2))

    # Cálculo de la Resistencia de onda ojiva
    @property
    def DWojiva(self, CDWO):
        return 0.5 * self.rho * (self.M * self.a) ** 2 * self.supref * self.CDWO

# Definir clases para Canard

class canard:
    pass

#Definir clases para Tipo de aleta

class delta:
    pass

class flecha:
    pass

class rectangular:
    pass

# Resistencia de Fricción

    #Definimos el Reinolds
    @property
    def Rex(self):
        return (self.rho * self.M * self.a * self.lx) / self.mu

    #Cálculo de los coeficientes de fricción
    @property
    def cdfilam(self, Rex):
        return 0.664 / np.sqrt(self.Rex)

    @property
    def CDfi(self, Rex):
        return 1.328 / np.sqrt(self.Rex)

    @property
    def CDflam(self, M, CDfi):
        return ((1/(1+0.17*self.M**2))**0.12950)*self.CDfi

    # Cálculo de la Resistencia de fricción
    @property
    def Df(self, rho, a, M, sref, CDflam):
        return 0.5 * self.rho * (self.M * self.a) ** 2 * self.supref * self.CDflam

# Margen de estabilidad estático

    @property
    def

if __name__ == "__main__":
    supcono = 0
    supcil = 0
    angucono = 0
    anguojiva = 0
    d = 0
    lc = 1
    la = 2

    print(supcil)
    micabeza = conica(d, la)
    micabeza.supcil

    print(micabeza.supcil)
    micabeza.d = 4


    print(micabeza.supcil)

    print(isinstance(micabeza, Cabeza))
    print(isinstance(micabeza, ojival))

    miojival = ojival(d, la)