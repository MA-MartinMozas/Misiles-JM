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
    def __init__(self, deltat,etamnmax, vm, vt, deltato, ro):
        super().__init__( etamnmax, vm, vt, deltato, ro)

        self.deltat = deltat
        self._K = 0
        self._deltati = 0
        self._etamnm = 0
        self._t = 0
        self._ri = 0
        self._xt = 0

    @property
    def K(self):
        _K = self.vm / self.vt
        valor = 0
        #Si 1<K<2 sí puede haber impacto, y continúa con las operaciones, sino no, y se paran los cálculos.
        if 1<_K<2:
            valor = _K
        return valor

    @property
    def deltati(self):
        return np.arccos (self.K/2)

    @property
    def etamnm(self):
        # Si deltato<deltati entonces nunca se dará deltati, ya que el ángulo deltat decrece con el tiempo, por lo que etanm máxima se da en el lanzamiento
        if self.deltato < self.deltati:
            _etamnm = self.vt*self.vm*np.sin(self.deltato*np.pi/180)/self.ro
            caso = 0
            # Si etamnmx>etamn sí se producirá impacto, sino no, y se paran los cálculos.
            if self.etamnmax >_etamnm :
                caso = _etamnm
                return caso
            else:
                return caso
        # Si deltato>deltati entonces etanm máxima se dará en t=0
        else:
            _etamnm = self.vt * self.vm * np.sin(self.deltati) / self.ri
            caso = 0
            # Si etamnmx>etamn sí se producirá impacto, sino no, y se paran los cálculos.
            if self.etamnmax > _etamnm:
                caso = _etamnm
                return caso
            else:
                return caso

    # Calculamos el tiempo de impacto
    @property
    def t(self):
        return ((-self.ro*np.sin(self.deltato*np.pi/180))/(2*self.vt*(np.tan(self.deltato*np.pi/180))**2))*(((np.tan(self.deltat*np.pi/180/2))**(self.K-1))/(self.K-1)+((np.tan(self.deltat*np.pi/180/2))**(self.K+1))/(self.K+1)-((np.tan(self.deltato*np.pi/180/2))**(self.K-1))/(self.K-1)-((np.tan(self.deltato*np.pi/180/2))**(self.K+1))/(self.K+1))
        #En impacto deltat=0º,r=0 y etamn=0

    # ri es para el caso de self.d_inic.deltato>self.deltati:
    @property
    def ri(self):
        return self.ro*(np.tan(self.deltati/2)/np.tan(self.deltato*np.pi/180/2))**self.K*(np.sin(self.deltato*np.pi/180)/np.sin(self.deltati))

    # Calculamos la posición del objetivo en el impacto
    @property
    def xt(self):
        return self.vt/self.t

# Definimos una clase para Navegación Proporcional que hereda de la clase misión
class naveproporc(mision):
    def __init__(self, deltamo, etatn, am,etamnmax, vm, vt, deltato, ro, blanco):
        super().__init__(etamnmax, vm, vt, deltato, ro)

        self.deltamo = deltamo
        self.blanco = blanco
        self.etatn = etatn
        self.am = am
        self._deltamc = 0
        self._incrementodeltam = 0
        self._ti = 0
        self._etamncalculado = 0
    #Existen dos aceleraciones de maniobra que el misil deberá cumplir para garantizar el impacto. SE DEBEN CUMPLIR AMBAS CONDICIONES

    # Si es MANIOBRANTE, la máxima aceleración de maniobra se requiere en el momento de impacto.
    #ATENCIÓN a!=2 si se puede emplear la fórmula poner en INPUT

    @property
    def etmncalculado(self):
        if self.blanco == "maniobrante":
            _etamnmcalculado = self.etatn*self.am/(self.am-2)
            suceso = 0
            # Si etamnmx>etamn sí se producirá impacto, sino no, y se paran los cálculos.
            if self.etamnmax > _etamnmcalculado:
                suceso = _etamnmcalculado
                return suceso
            else:
                return suceso
        else:
            _etamnmcalculado = (self.am * self.vm / self.ti) * (self.incrementodeltam)
            suceso = 0
            # Si etamnmx>etamn sí se producirá impacto, sino no, y se paran los cálculos
            if self.etamnmax > _etamnmcalculado:
                suceso = _etamnmcalculado
                return suceso
            else:
                return suceso
    #Si es NO MANIOBRANTE, la máxima aceleración se requiere en t=0


    @property
    def deltamc(self):
        if self.blanco == "No_maniobrante":
            return np.arcsin(self.vt*np.sin(self.deltato*np.pi / 180)/self.vm)
        else:
            return 0

    @property
    def incrementodeltam(self):
        if self.blanco == "No_maniobrante":
            return self.deltamo*np.pi / 180-self.deltamc
        else:
            return 0

    @property
    def ti(self):
        if self.blanco == "No_maniobrante":
            return self.ro/(self.vm*np.cos(self.deltamo*np.pi / 180)-self.vt*np.sin(self.deltato*np.pi / 180))
        else:
            return 0




def principal2(mis):
    """

    :param mis:
    :type mis: dict
    :return:
    """
    # el código fallará si introducimos un string en vez de un  número por lo que podría ser algo a mejorar
    for key, value in mis.items():
        if mis[key]== mis["tipo"]:
            mis[key] = value
        elif mis[key]== mis["blanco"]:
            mis[key] = value
        else:
            mis[key] = np.float64(value)
    blanco = mis["blanco"]
    # aquí metemos cada variable que se tiene que introducir le asignamos su valor asignandole el marcador del diccionario mis
    etamnmax = mis['etamnmax']
    vm = mis['vm']
    vt = mis['vt']
    deltato = mis['deltato']
    ro = mis['ro']


    deltat = mis['deltat']
    mippura = ppura(deltat, etamnmax, vm, vt, deltato, ro)

    deltamo = mis['deltamo']
    etatn = mis['etatn']
    am = mis['am']
    minaveproporc = naveproporc(deltamo, etatn, am, etamnmax, vm, vt, deltato, ro, blanco)

    # aquí tenemos que introducir un marcador por cada resultado que queramos sacar y le asignamos el valor
    resultados = {"fun": "hay_impacto", "K": mippura.K,"deltati": mippura.deltati,"etamnm": mippura.etamnm,"t": mippura.t,"ri": mippura.ri,"xt": mippura.xt,
                  "deltamc": minaveproporc.deltamc,"incrementodeltam": minaveproporc.incrementodeltam,
                  "ti": minaveproporc.ti, "etamncalculado": minaveproporc.etmncalculado

                  }
    print(resultados)
    if resultados["etamnm"] == 0:
        resultados = {"fun":"no_impacto"}
        return resultados
    elif resultados["K"]== 90:
        resultados = {"fun": "no_impacto"}
        return resultados
    elif resultados["etamncalculado"]== 0:
        resultados = {"fun": "no_impacto"}
        return resultados
    else:
        for key, value in resultados.items():
            if resultados[key]== resultados["fun"]:
                resultados[key] = value
            else:
                # "%.3f" %value,
                resultados[key] = "%.3f" % value,
        return resultados


# esta parte sirve para que se ejecute en caso de no hacer import, es decir si solo corremos esta .py
# if __name__ == '__main__':
#
#
# pass