
import numpy as np

# Definir clases para la Sección delantera
from sklearn.ensemble._gradient_boosting import np_bool


class Operacion(object):
    def __init__(self, M, rho, a, mu,lx):
        self.M = M
        self.rho = rho
        self.a = a
        self.mu = mu
        self.lx = lx
        self.Rex = 0
    # Definimos el Reynolds
    @property
    def Rex(self):
        return (self.rho * self.M * self.a * self.lx) / self.mu


class Cabeza(object):

    def __init__(self, d, la, ln, lx, Cnalphabeta, b, c, lt, Cnsat, delta, m, mi_op):

        self.mi_op = mi_op

        self._supcil = 0
        self._Rex = 0
        self.d = d
        self.la = la
        self.ln = ln
        self._supref = 0
        self.lx = lx

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
        self.g = 9.81   #Este valor es invariable
        self._Cnalphawing = 0
        self._Xcpbeta = 0
        self._Xcpwing = 0
        self._Kwb = 0
        self._Kbw = 0
        self._Cnalpha = 0
        self._Cmalpha = 0
        self._h =0
        self._Cnalphadelta = 0
        self._Cmalphadelta = 0
        self._Kbm = 0
        self.Kmb = 1    #Este valor es invariable
        self._maniobrabilidad = 0
        self._alphasatur = 0
        self._nmaximo = 0
        self._Xcg = 0
        self._deltamani = 0



    @property
    def supcil(self):
        return np.pi*self.d*self.la

    @property
    def supref(self):
        return np.pi*self.d**2/4

    @property
    def Xcg(self):
        return #FALTA COMPLETAR!!

class conica(Cabeza):

    # Datos geometría
    def __init__(self, d, la, ln, lx, Cnalphabeta, b, c, lt, Cnsat, delta, m, mi_op,lc):
        super().__init__(d, la, ln, lx, Cnalphabeta, b, c, lt, Cnsat, delta, m, mi_op)

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
    def CDWC(self):
        return (0.083+0.096/(self.mi_op.M**2))*(self._angucono/10)**1.69

    # Cálculo de la Resistencia de onda cono
    @property
    def DWcono(self):
        return 0.5*self.mi_op.rho * (self.mi_op.M * self.mi_op.a)**2 * self._supref * self._CDWC





# # Definir clases para Canard
#
# class canard:
#     pass
#
# #Definir clases para Tipo de aleta
#
# class delta:
#     pass
#
# class flecha:
#     pass
#
# class rectangular:
#     pass
#
# # Resistencia de Fricción
#
#
#
#     #Cálculo de los coeficientes de fricción
#     @property
#     def cdfilam(self, self._Rex):
#         return 0.664 / np.sqrt(self._Rex)
#
#     @property
#     def CDfi(self, self._Rex):
#         return 1.328 / np.sqrt(self._Rex)
#
#     @property
#     def CDflam(self, self._CDfi):
#         return ((1/(1+0.17*self.M**2))**0.12950)*self._CDfi
#
#     # Cálculo de la Resistencia de fricción
#     @property
#     def Df(self, self._supref, self._CDflam):
#         return 0.5 * self.rho * (self.M * self.a) ** 2 * self._supref * self._CDflam
#
# # Margen de estabilidad estático
#
#     @property
#     def Cnalphawing(self):
#         return (4/np.sqrt(self.M**2-1))*(1-(1/(2*np.sqrt(self.M**2-1)*(self.b/self.c))))
#
#     @property
#     def Xcpbeta(self):
#         return 2*self.ln/3
#
#     @property
#     def Xcpwing(self):
#         return self.lt - self.c/2
#
#     @property
#     def Kwb(self):
#         return 1 + self.d/(self.b+self.d)
#
#     @property
#     def Kbw(self):
#         return (self.d/(self.d+self.b))(1 + self.d/(self.b+self.d))
#
#     @property
#     def Cnalpha(self, self._Cnalphawing, self._Kwb, self._Kbw, self._supref):
#         return(self.Cnalphabeta + self_Cnalphawing*(self._Kwb + self._Kbw)*self.b*self.c/self._supref)
#
#     @property
#     def Cmalpla(self, self._Cnalphawing, self._Kwb, self._Kbw, self._supref, self_Xcg, self._Xcpbeta, self._Xcpwing):
#         return(self.Cnalphabeta*((self._Xcg-self._Xcpbeta)/self.d) + self_Cnalphawing*(self._Kwb + self._Kbw)*self.b*self.c/self._supref*((self._Xcg-self._Xcpwing)/self.d))
#
#     @property
#     def h (self, self._Cnalpha, self._Cmalpha):
#         return(-self._Cmalpha/self._Cnalpha)
#
# # Maniobrabilidad y Capacidad de maniobra máxima
#
#     @property
#     def Kbm(self):
#         return self.d / (self.d + self.b)
#
#     @property
#     def Cndelta(self, self._Cnalphawing, self._Kbm, self._supref):
#         return self_Cnalphawing * (self.Kmb + self._Kbm) * self.b * self.c / self._supref
#
#     @property
#     def Cmdelta(self, self._Cnalphawing, self._Kbm, self._supref, self_Xcg, self._Xcpwing):
#         return self_Cnalphawing * (self.Kmb + self._Kbm) * self.b * self.c / self._supref * ((self._Xcg - self._Xcpwing) / self.d))
#
#     @property
#     def maniobrabilidad(self, self._supref, self._Cndelta, self._Cmdelta, self._h)
#         return ((0.5*self.rho*(self.a*self*M)**2*self._supref)/self.m*self.g)*(self._Cndelta+self._Cmdelta/self._h)
#
#     @property
#     def alphasatur (self, self._Cnalphawing)
#         return -self.Cnsat/self._Cnalphawing
#
#     @property
#     def deltamani (self, self._alphasatur, self._Kwb, self._Cmdelta, self._Cmalpha)
#         return self._alphasatur/(self._Kwb*(-self._Cmdelta/self._Cmalpha)+self.Kmb)
#
#     @property
#     def nmaximo (self, self._deltamani, self._maniobrabilidad)
#         return self._deltamani*self._maniobrabilidad



mi_op = Operacion(1, 2, 300, 5)
    #
    # Cabeza.M = 2
    # print(supcil)
    # micabeza = conica(d, la, mioperacion)
    # micabeza.M = 3
    # micabeza2 = conica(d, 2*la, mioperacion)
    #
    # Cabeza.M = 4
    #
    # # micabeza.supcil
    # print(micabeza.M)
    # print(micabeza2.M)
    #
    # # print(micabeza.supcil)
    # micabeza.d = 4
    #
    #
    # # print(micabeza.supcil)
    #
    # print(isinstance(micabeza, Cabeza))
    # print(isinstance(micabeza, ojival))
    #
    # miojival = ojival(d, la)

micabeza = conica(1,1,1,1,1,1,1,1,1,1,1,mi_op,1)
print(micabeza.DWcono)
