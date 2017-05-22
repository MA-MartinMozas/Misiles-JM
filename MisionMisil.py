import numpy as np

# Definimos una clase para misión
class mision(object):
    def __init__(self , etamnmax, vm, vt, deltato, ro):
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
        self._ri = 0
        self._xt = 0

    @property
    def K(self):
        _K = self.d_inic.vm / self.d_inic.vt
        valor = "NO HAY IMPACTO"
        #Si 1<K<2 sí puede haber impacto, y continúa con las operaciones, sino no, y se paran los cálculos.
        if 1<_K<2:
            valor = _K
        return valor

    @property
    def deltati(self):
        return np.arccos(self.K/2)

    @property
    def etamnm(self):
        # Si deltato<deltati entonces nunca se dará deltati, ya que el ángulo deltat decrece con el tiempo, por lo que etanm máxima se da en el lanzamiento
        if self.d_inic.deltato < self.deltati:
            _etamnm = self.d_inic.vt*self.d_inic.vm*np.sin(self.d_inic.deltato)/self.d_inic.ro
            caso = "NO HAY IMPACTO"
            # Si etamnmx>etamn sí se producirá impacto, sino no, y se paran los cálculos.
            if d_inic.etamnmax>_etamnm :
                caso = _etamnm
                return caso
        # Si deltato>deltati entonces etanm máxima se dará en t=0
        else:
            _etamnm = self.d_inic.vt * self.d_inic.vm * np.sin(self.deltati) / self.ri
            caso = "NO HAY IMPACTO"
            # Si etamnmx>etamn sí se producirá impacto, sino no, y se paran los cálculos.
            if d_inic.etamnmax > _etamnm:
                caso = _etamnm
                return caso
    # Calculamos el tiempo de impacto
    @property
    def t(self):
        return ((-self.d_inic.ro*np.sin(self.d_inic.deltato))/(2*self.d_inic.vt*(np.tan(self.d_inic.deltato))**2))*(((np.tan(self.deltat/2))**(self.K-1))/(self.K-1)+((np.tan(self.deltat/2))**(self.K+1))/(self.K+1)-((np.tan(self.d_inic.deltato/2))**(self.K-1))/(self.K-1)-((np.tan(self.d_inic.deltato/2))**(self.K+1))/(self.K+1))
        #En impacto deltat=0º,r=0 y etamn=0

    # ri es para el caso de self.d_inic.deltato>self.deltati:
    @property
    def ri(self):
        return self.d_inic.ro*(np.tan(self.deltati/2)/np.tan(self.d_inic.deltato/2))**self.K*(np.sin(self.d_inic.deltato)/np.sin(self.deltati))

    # Calculamos la posición del objetivo en el impacto
    @property
    def xt(self):
        return self.d_inic.vt/self.t

# Definimos una clase para Navegación Proporcional que hereda de la clase misión
class naveproporc(mision):
    def __init__(self, deltamo, etatn, a, t, d_inic):
        self.d_inic = d_inic
        self.deltamo = deltamo
        self.etatn = etatn
        self.a = a
        self.t = t
        self._deltamc = 0
        self._incrementodeltam = 0
        self._ti = 0
        self._etamncalculado = 0
#Existen dos aceleraciones de maniobra que el misil deberá cumplir para garantizar el impacto. SE DEBEN CUMPLIR AMBAS CONDICIONES

    # Si es MANIOBRANTE, la máxima aceleración de maniobra se requiere en el momento de impacto.
    #ATENCIÓN a!=2 si se puede emplear la fórmula poner en INPUT
    @property
    def etmncalculado(self):
        _etamnmcalculado = self.etatn*self.a/(self.a-2)*(1-(1-self.t/self.ti)**(self.a-2))
        suceso = "NO HAY IMPACTO"
        # Si etamnmx>etamn sí se producirá impacto, sino no, y se paran los cálculos.
        if d_inic.etamnmax > _etamnmcalculado:
            suceso = _etamnmcalculado
            return suceso

    #Si es NO MANIOBRANTE, la máxima aceleración se requiere en t=0

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
        _etamnmcalculado = (self.a*self.d_inic.vm/self.ti)*(self.incrementodeltam*np.pi/180)
        suceso = "NO HAY IMPACTO"
        # Si etamnmx>etamn sí se producirá impacto, sino no, y se paran los cálculos
        if d_inic.etamnmax > _etamnmcalculado:
            suceso = _etamnmcalculado
            return suceso

d_inic= mision(1,1,0.75,1,1)
algo= ppura(1,d_inic)
print(algo.t)