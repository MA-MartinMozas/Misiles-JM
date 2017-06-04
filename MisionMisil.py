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

    @property
    def K(self):
        return self.vm / self.vt


    @property
    def deltati(self):
        return np.arccos (self.K/2)

    @property
    def etamnm(self):
        # Si deltato<deltati entonces nunca se dará deltati, ya que el ángulo deltat decrece con el tiempo, por lo que etanm máxima se da en el lanzamiento
        if self.deltato < self.deltati:
            return self.vt*self.vm*np.sin(self.deltato*np.pi/180)/self.ro

            # Si etamnmx>etamn sí se producirá impacto, sino no, y se paran los cálculos.

        # Si deltato>deltati entonces etanm máxima se dará en t=0
        elif self.deltato > self.deltati:
            return self.vt * self.vm * np.sin(self.deltati) / self.ri

            # Si etamnmx>etamn sí se producirá impacto, sino no, y se paran los cálculos.


    # Calculamos el tiempo de impacto
    @property
    def t(self):
        return ((-self.ro*np.sin(self.deltato*np.pi/180))/(2*self.vt*(np.tan(self.deltato*np.pi/180))**2))*(((np.tan(self.deltat*np.pi/180/2))**(self.K-1))/(self.K-1)+((np.tan(self.deltat*np.pi/180/2))**(self.K+1))/(self.K+1)-((np.tan(self.deltato*np.pi/180/2))**(self.K-1))/(self.K-1)-((np.tan(self.deltato*np.pi/180/2))**(self.K+1))/(self.K+1))
        #En impacto deltat=0º,r=0 y etamn=0

    # ri es para el caso de self.d_inic.deltato>self.deltati:
    @property
    def ri(self):
        return (self.ro*(np.tan(self.deltati/2)/np.tan(self.deltato*np.pi/180/2))**self.K)*(np.sin(self.deltato*np.pi/180)/np.sin(self.deltati))

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

    #Existen dos aceleraciones de maniobra que el misil deberá cumplir para garantizar el impacto. SE DEBEN CUMPLIR AMBAS CONDICIONES

    # Si es MANIOBRANTE, la máxima aceleración de maniobra se requiere en el momento de impacto.
    #ATENCIÓN a!=2 si se puede emplear la fórmula poner en INPUT

    @property
    def etmncalculado(self):
        if self.blanco == "maniobrante":
            return self.etatn*self.am/(self.am-2)

            # Si etamnmx>etamn sí se producirá impacto, sino no, y se paran los cálculos.

        else:
            return (self.am * self.vm / self.ti) * (self.incrementodeltam)

            # Si etamnmx>etamn sí se producirá impacto, sino no, y se paran los cálculos

    #Si es NO MANIOBRANTE, la máxima aceleración se requiere en t=0


    @property
    def deltamc(self):
        return np.arcsin(self.vt*np.sin(self.deltato*np.pi / 180)/self.vm)


    @property
    def incrementodeltam(self):
        if self.blanco == "No_maniobrante":
            return self.deltamo*np.pi / 180-self.deltamc
        else:
            return 0

    @property
    def ti(self):
        return self.ro/(self.vm*np.cos(self.deltamo*np.pi / 180)-self.vt*np.cos(self.deltato*np.pi / 180))




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
        elif mis[key]== mis["mision"]:
            mis[key] = value
        else:
            mis[key] = np.float64(value)
    blanco = mis["blanco"]
    mision = mis["mision"]
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
    resultados = {"fun": "hay_impacto", "mis": mision , "K": mippura.K,"deltati": mippura.deltati,"etamnm": mippura.etamnm,"t": mippura.t,"ri": mippura.ri,"xt": mippura.xt,
                  "deltamc": minaveproporc.deltamc,"incrementodeltam": minaveproporc.incrementodeltam,
                  "ti": minaveproporc.ti, "etamncalculado": minaveproporc.etmncalculado

                  }

    print("resultados=" , resultados)
    # realizaremos condicionales para mandar solo los resultados necesarios para el tipo de misión
    if mision == "P_Pura":
        resultados = {"fun": "hay_impacto","mis": mision , "K": mippura.K, "deltati": mippura.deltati, "etamnm": mippura.etamnm,
                      "t": mippura.t, "ri": mippura.ri, "xt": mippura.xt
                      }
        if resultados["etamnm"] > etamnmax:
            resultados["fun"] = "no_impacto(ac>acmax)"
            return resultados
        elif resultados["K"] < 1 :
            resultados["fun"] = "no_impacto(v.misil<vtarget)"
            return resultados
        elif resultados["K"] > 2:
            resultados["fun"] = "no_impacto(v.misil<vtarget)"
            return resultados
        else:

            for key, value in resultados.items():
                if resultados[key] == resultados["fun"]:
                    resultados[key] = value
                elif resultados[key] == resultados["mis"]:
                    resultados[key] = value
                else:
                    # "%.3f" %value,
                    resultados[key] = "%.3f" % value,
            return resultados

    else:
        resultados = {"fun": "hay_impacto","mis": mision ,
                      "deltamc": minaveproporc.deltamc, "incrementodeltam": minaveproporc.incrementodeltam,
                      "ti": minaveproporc.ti, "etamncalculado": minaveproporc.etmncalculado
                      }
        if resultados["etamncalculado"] > etamnmax:
            resultados["fun"] = "no_impacto(ac>acmax)"
            return resultados

        for key, value in resultados.items():
            if resultados[key]== resultados["fun"]:
                resultados[key] = value
            elif resultados[key] == resultados["mis"]:
                resultados[key] = value
            else:
                # "%.3f" %value,
                resultados[key] = "%.3f" % value,
        return resultados


# esta parte sirve para que se ejecute en caso de no hacer import, es decir si solo corremos esta .py
if __name__ == '__main__':
    mippura = ppura(0, 180, 950, 500, 40, 2000)
    print(mippura.K,mippura.etamnm)

