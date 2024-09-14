import pip


try:
    from flask import Flask

except ImportError:

    pip.main(["install","Flask"])

    from flask import Flask

try:
    from flask import  render_template
except ImportError:
     
    pip.main(["install","render_template"])

    from flask import  render_template  

'''
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main240820b__':
     app.run(debug=True)

@app.route('/')
def get_data():
    name1 = 'Alfonso'
    return render_template('index.html', name1)

'''
print("Iniciando")


import sys
import os
import os.path
import io
import string
import datetime
import math
import statistics
import random

import pip

try:
     import matplotlib

except ImportError:

    pip.main(["install","matplotlib"])

    import matplotlib

try:
    import pandas     

except ImportError:
    pip.main(["install","pandas"])
    import pandas


try:
    import numpy

except ImportError:
    pip.main(["install","numpy"])
    import numpy

try:
    import requests

except ImportError:
    pip.main(["install","requests"])
    import requests

print ("linea 55")



try:
    import matplotlib.pyplot
except ImportError:
    ##from pip._internal import main as pip
    pip.main(['install', 'matplotlib.pyplot'])
    import matplotlib.pyplot


try:
    import dateutil.parser

except ImportError:
    ##from pip._internal import main as pip
    pip.main(['install', 'dateutil.parser'])
    import dateutil.parser

print("linea 75")
try:
    import datetime
except ImportError:
    ##from pip._internal import main as pip
    pip(['install', '--user', 'datetime'])
    import datetime

try:
    import pathlib
except ImportError:
    ##from pip._internal import main as pip
    pip(['install', '--user', 'pathlib'])
    import pathlib

try:
    import os
except ImportError:
    ##from pip._internal import main as pip
    pip(['install', '--user', 'os'])
    import os

try:
    import json
except ImportError:
    ##from pip._internal import main as pip
    pip(['install', '--user', 'json'])
    import json

try:
    import time
except ImportError:
    ##from pip._internal import main as pip
    pip(['install', '--user', 'time'])
    import time

try:
    import pytz
except ImportError:
    ##from pip._internal import main as pip
    pip(['install', '--user', 'pytz'])
    import pytz







from xml.dom import registerDOMImplementation
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from dateutil import parser
import requests
from datetime import date  
from datetime import datetime
import pathlib  
import os

import json

from datetime import timedelta
from datetime import time
import pytz
from pathlib import Path

##prueba de aplicación flask

# descomentar es ok
from flask import Flask, render_template

app = Flask(__name__)

@app.route('../')
def home():
    variable = "¡Hola, mundo!"
    return render_template('index.html', variable=variable)

if __name__ == '__main__':
    app.run(debug=True)

#traspasar una varialbe a un template de flask

'''
class User(db.Model, UserMixin):
    """Model for user accounts."""
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True)
    username = db.Column(db.String,
                         nullable=False,
                         unique=False)
    email = db.Column(db.String(40),
                      unique=True,
                      nullable=False)
    password = db.Column(db.String(200),
                         primary_key=False,
                         unique=False,
                         nullable=False)
    def __repr__(self):
        return '<User {}>'.format(self.username)
'''
# ejecutar class User(db.Model, UserMixin):
# ejecutar db.create_all() para crear la tabla en la base de datos




newYorkTz = pytz.timezone("America/New_York") 
timeInNewYork = datetime.now(newYorkTz)
currentTimeInNewYork = timeInNewYork.strftime("%H:%M:%S")
print("The current time in New York is:", timeInNewYork)##currentTimeInNewYork)
##print("Esta version tiene señuelo para bolsausa")

d =date.today()
dos = datetime(d.year, d.month, d.day, hour=9, minute=30, tzinfo=newYorkTz,  fold=0)  ##hora de comienzo de new york cambiar hour a 9
##if timeInNewYork.hour==9:
    ##print ("tiene  buena pinta")
    ##dos = datetime(d.year, d.month, d.day, timeInNewYork.hour-1, minute=30, tzinfo=newYorkTz,  fold=0)

##if timeInNewYork.hour==10:
    ##print ("tiene  buena pinta")
    ##dos = datetime(d.year, d.month, d.day, timeInNewYork.hour-2, minute=30, tzinfo=newYorkTz,  fold=0)


print("hora comienzo new york",dos)
tiempooperacionnewyork = timeInNewYork > dos ## horacomienzonewyork ####es >, < es para pruebas

print(" linea 40 tiempooperacionnewyork ", timeInNewYork, " dos: ",dos) 
##else:
    ##print("la hora corriente en new york es ", timeInNewYork.hour)

print("La hora de comienzo de New York es ",dos)
horacomienzonewyork = dos

print ("comparacion tiempo new york > horacomienzonewyork ",tiempooperacionnewyork)


diahoy = date.today().isoformat()
momentohoy = str(datetime.now())
numdiasemana=date.fromisoformat(diahoy).isoweekday() #del 1 lunes a 7 domingo

sabadoodomingo =  False #date.fromisoformat(diahoy).isoweekday()>5 ##>5

#print(numdiasemana)
#print(momentohoy)
datos_resumen_fon ={} ##datos resumen del fondo
clave_unica=""
datosaccenelfondo={}
cotiz_dacci ={}
diccotiz={}
dictfondos= {}
dictacciones={} #numero de acciones fondo
dicfontic={} 
#acciones keys, y fondos values
coberturaFondo={} #participación del fondo en una acción
indicebolsafontic=""
bolsafontic={}
tickersunicos={}
fondossinorden={}
cotizaaccion=[]
fonvariacion={}
dicaccfon={} ##fondos con sus acciones
listatodosdatosaccenelfondo=[]
cadenalinealistadohistoricobak=''
txtlistadohistoricobak=[] #para escribir el historictickersocotiza.csv
itemhistorico=[]          #para hacer y tratar con python graficas
contador = 0
fonvariacion={}


'''

archivonombresfondos ='/home/jose/Fondos/Auxiliares/nombreFondos_AMA_BOLSA.csv'
archivotickers ='/home/jose/Fondos/Auxiliares/tickers_AMA_BOLSA.csv'
rhcsv = '/home/jose/Fondos/Auxiliares/resumenhistoricocsv_AMA_BOLSA.csv'
cotizahoypython='/home/jose/Fondos/Auxiliares/cotizahoypy_AMA_BOLSA.csv'
resucsv ='/home/jose/Fondos/Auxiliares/resumencsv_AMA_BOLSA.csv'
tikercsv = '/home/jose/Fondos/Auxiliares/tikercsv_AMA_BOLSA.csv'

##cotizahoypython='C://Auxiliares/cotizahoypy.csv'from
archivonombresfondos ='C:\\Auxiliares\\nombreFondos_JOSE_BOLSA.csv'
archivotickers ='C:\\Auxiliares\\tickers_para_pruebas.csv '
rhcsv = 'C:\\Auxiliares\\resumenhistoricocsv_JOSE_BOLSA.csv'
cotizahoypython='C:\\Auxiliares\\cotizahoypy_JOSE_BOLSA.csv'
resucsv ='C:\\Auxiliares\\resumencsv_JOSE_BOLSA.csv'
tikercsv = 'C:\\Auxiliares\\tikercsv_JOSE_BOLSA.csv'
tickers_no_hallados = 'C:\\Auxiliares\\tickers_no_hallados_JOSE_BOLSA.csv'
'''

archivonombresfondos ='nombreFondos_JOSE_BOLSA.csv'
archivotickers ='tickers.csv'
rhcsv = 'resumenhistoricocsv_JOSE_BOLSA.csv'
cotizahoypython='cotizahoypy_JOSE_BOLSA.csv'
resucsv ='resumencsv_JOSE_BOLSA.csv'
tikercsv = 'tikercsv_JOSE_BOLSA.csv'
tickers_no_hallados = 'tickers_no_hallados_JOSE_BOLSA.csv'
prueba= "prueba2409131858.csv"



myFiles = [archivonombresfondos, archivotickers, rhcsv,cotizahoypython,resucsv,tikercsv, tickers_no_hallados] 
for filename in myFiles:

    if not os.path.exists(filename):
        print("creando ", filename)
        fil=open(filename, 'w')
        fil.close()
    
    tnh = open(tickers_no_hallados, 'w')
    tnh.close()
    
class construirtikercvs():

    def cabeceratikercsv(self):
        
        ##borrado de fichero
        hmt = open(tikercsv, 'w')
        cabecera=( 'Fecha'+";"+'Fondo'+";"+'Ticker'+";"+'accion'+';'+'porcentaje'+";"+"Modif_porc"+";"+'Peso_absoluto'+";"+"Precio"+";"+"banco"+";"+"cnmv"+'\n')
        ##print("CABECERA DE HISTORICO ",cabecera)
        hmt.write(cabecera)
        hmt.close()
    
    def cuerpotikercsv(self, dicfontic):

        ##cotiz_dacci[dacci]=[dacci,marketPriceArmp,changePercentA]
        hmc= open(tikercsv,'a')
        
        ##claveunicasorted = sorted(dicfontic.keys())

        for claveunica in dicfontic.keys(): ## debes esta el tickers.csv ordenado por fondos y porcentajes:

            if "ondo" not in claveunica:
                 
                if tiempooperacionnewyork ==False: ##True: ##False: ##False: 
                        #True: ##//no carga usa y descuajeringa Pru1ods
                        ##print("121")
                        if "^" in dicfontic[claveunica][2] or "." in claveunica:
                            tic =dicfontic[claveunica][4]
                ##print("133 ",tic)
                            part=float(dicfontic[claveunica][5])
                            ##print("135 ",part)
                            vari=float(cotiz_dacci[tic][2])

                            precio=float(cotiz_dacci[tic][1])
                            ##print("140 ",precio)
                            if  "ALPHA" not in claveunica:########and "BESTIDEAS" not in claveunica: ##### and "^" not in claveunica:
                                lineacuerpo = ""+str(datetime.now())+";"+dicfontic[claveunica][2]+";"+ dicfontic[claveunica][4]+";"+dicfontic[claveunica][3]+";"+dicfontic[claveunica][5]+";"+str(vari)+";"+str(vari*part)+";"+str(precio) +";"+"IBERCAJA"+";"+"NOSE"+"\n"
                                hmc.write(lineacuerpo)
                            ##print("linea 93 "+ lineacuerpo)
                
                                    ### nueveymedia_list_dacci.append(dacci)
                else:
                    ###print("125")

            ###set_dacci=set(list_dacci)

                    tic =dicfontic[claveunica][4]
                    ##print("133 ",tic)
                    part=float(dicfontic[claveunica][5])
                    ##print("135 ",part)
                    vari=float(cotiz_dacci[tic][2])

                    precio=float(cotiz_dacci[tic][1])
                    ##print("140 ",precio)
                    if  "ALPHA" not in claveunica:### and "BESTIDEAS" not in claveunica: ##### and "^" not in claveunica:
                        lineacuerpo = ""+str(datetime.now())+";"+dicfontic[claveunica][2]+";"+ dicfontic[claveunica][4]+";"+dicfontic[claveunica][3]+";"+dicfontic[claveunica][5]+";"+str(vari)+";"+str(vari*part)+";"+str(precio) +";"+"IBERCAJA"+";"+"NOSE"+"\n"
                        hmc.write(lineacuerpo)
                    ##print("linea 93 "+ lineacuerpo)

        hmc.close()

class ver_comp():

    
    def ver_c(self,ave):

        vercomposicion='BOLSAESPANA'

        
        while vercomposicion!='':

            vercomposicion= vercomposicion.upper()

            for fon in datos_fon.lista_fondos: ##dictaccfon: 

                if vercomposicion in fon:

                    n_acciones_fondo =0

                    lista_datos_fondo=[]

                    valorparticipaciones =0.0 

                    valorpesoglobal=0.0          


                    datos_fon.peso_acumulado=0.0

                    ####datos_fon.variacion_ponderada=0.0000
                    
                    n_acciones_fondo=0


                    print("Fondo","\t\t\t", "Part.", "\t", "Var","\t", "Peso","\t","Acción","\t","Precio")

                    for daccikey in datos_fon.dicaccfoncl[fon]:

                        if tiempooperacionnewyork ==False: ##False: 
                #True: ##//no carga usa y descuajeringa Pru1ods
               
                            if "^" in fon or "." in daccikey: 

                                if vercomposicion in fon:

                                        n_acciones_fondo =n_acciones_fondo + 1
                            
                                            
                                        claveunica = fon+"_"+daccikey

                                        ##print("linea 428 ",claveunica)
                                        peso_accion_fondo= datos_fon.dictfontic[claveunica][5]           

                                        ##print(claveunica ," linea 160")
                                        
                                        var_ac=round(cotiz_dacci[daccikey][2]*100,4)
                                        peso_var_ac=round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2])*100,4)
                                        precio =round(cotiz_dacci[daccikey][1],4)

                                        print(("{:}\t\t{:}\t{:5.3f}\t{:5.3f}\t{:10}\t{:7.4f}").format(fon,peso_accion_fondo, var_ac,peso_var_ac,cotiz_dacci[daccikey][0],precio))
                                        
                                        valorparticipaciones=valorparticipaciones+   round(float(peso_accion_fondo), 4)

                                        valorpesoglobal= valorpesoglobal+round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2])*100,4)                    
                        else:
                             if vercomposicion in fon:
    
                                        n_acciones_fondo =n_acciones_fondo + 1
                            
                                            
                                        claveunica = fon+"_"+daccikey

                                        ##print("linea 428 ",claveunica)
                                        peso_accion_fondo= datos_fon.dictfontic[claveunica][5]           

                                        ##print(claveunica ," linea 160")
                                        
                                        var_ac=round(cotiz_dacci[daccikey][2]*100,4)
                                        peso_var_ac=round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2])*100,4)
                                        precio =round(cotiz_dacci[daccikey][1],4)

                                        print(("{:}\t{:}\t{:5.3f}\t{:5.3f}\t{:10}\t{:7.4f}").format(fon,peso_accion_fondo, var_ac,peso_var_ac,cotiz_dacci[daccikey][0],precio))
                                        
                                        valorparticipaciones=valorparticipaciones+   round(float(peso_accion_fondo),4)

                                        valorpesoglobal= valorpesoglobal+round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2])*100,4)                    

                    print("numero de acciones ", n_acciones_fondo, " peso de participaciones ",round(valorparticipaciones,4), " variacion global ",round(valorpesoglobal/100,4))   
 
            
            vercomposicion = input("Ver composicion del fondo =")



class mostrarchartfondo():

    fonvariacion={}


    def mcf(self):

        ##alprint ("linea 124 ")

        ki = open(rhcsv,'r',encoding="utf8", errors='ignore')

        lineas = ki.readlines()

        saltarheader = 0 #numero de lineas o accion-fondo
        
        for linea in lineas:

            if "ondo" in linea:
                saltarheader += 1
                next  

            if saltarheader <2:
                next

            ##print("linea 141 ",linea)

            trozos= linea.split(';')

            print(trozos)   

            for trozo in trozos:
                print(trozo)

            print("linea 281")
            
            datos_accion_sinorden =[]

            if "ondo" not in trozos[1]:

                for fn in trozos[1]:

                    acciones_fondo={}

                  


                    datos_accion_sinorden.append(trozos[4]) ##var porcentual

                
                    mostrarchartfondo.fonvariacion[trozos[4]]=datos_accion_sinorden

              
        ki.close()   
    
        return mostrarchartfondo.fonvariacion

    def antiguocf(self):

        ###df = pd.read_csv(rhcsv, header =0, index_col =5, sep=';',decimal='.')

        df = pd.read_csv(rhcsv, header =0, sep=';',decimal='.', encoding='ISO-8859-1')

        print(df)

        print(df.columns)

        ##input("linea 314 columnas de rhcsv")

        nombrefondos = df['Fondo'].tolist() ##ondo?

        print(nombrefondos)


        eleccionfondo = 'esp'    

        while eleccionfondo !='':

            mayusculasf =eleccionfondo.upper()
            
            if mayusculasf =='':
                break
           
            for ni in nombrefondos:
                if mayusculasf in "TODOS":
                    ddfalfa= df.groupby('Fondo').get_group(ni) ##fecha por Fondo
                    ##print("linea 194 ", ni)
                    estadisticadfalfa= ddfalfa['Var_Por'].describe() ##Peso por Var_Por
                
                    ##print(estadisticadfalfa)

                                   
                    l=ddfalfa['Var_Por'] ##peso por Var_Por
                
                    cs= l.cumsum()
                    
                    n = ddfalfa['Var_Por'].count() ##peso por Var_Por
                
                    y=list(range(n))
                    


                    Var_p=list(ddfalfa['Var_Por'])[-1]

                    ##print("ultima variación ",Var_p)
                    cad_titulo = ni+"  Variación: "+str(round(float(Var_p),4))

                    fig, ax = plt.subplots()
                    ax.plot(y,l)
                    ax.plot(y,cs)
                    ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')

                    ax.set_title(cad_titulo, loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
                    plt.show()

                    eleccionfondo = input(" 251 Gráficos y estadísticas del fondo = ")

                    mayusculasf =eleccionfondo.upper()
                    
                    if mayusculasf =='':
                        break

                if mayusculasf in  ni:
                    dfalfa= df.groupby('Fondo').get_group(ni)
                    
                    print(ni)
                    
                    print("linea 194 ", dfalfa.columns)
                    
                    estadisticadfalfa= dfalfa['Var_Por'].describe()
                
                    ##print(estadisticadfalfa)
                
                    input(" Estadistica")
                    l=dfalfa['Var_Por']

                    cs= l.cumsum()
                    
                    n = dfalfa['Var_Por'].count()
                
                    y=list(range(n))
                    
                    Var_p=list(dfalfa['Var_Por'])[-1]

                    print("ultima variación ",Var_p)
                    cad_titulo = ni+" "+str(round(float(Var_p),4))

                    fig, ax = plt.subplots()
                    ax.plot(y,l)
                    ax.plot(y,cs)
                    ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')

                    ax.set_title(cad_titulo, loc = "left", fontdict = {'fontsize':14, 'fontweight':'bold', 'color':'tab:blue'})
                    plt.show()

                    eleccionfondo = input(" 251 Gráficos y estadísticas del fondo = ")

                    mayusculasf =eleccionfondo.upper()
                    
                    if mayusculasf =='':
                        break

              

            eleccionfondo = input(" 251 Gráficos y estadísticas del fondo = ")
  
            mayusculasf =eleccionfondo.upper()
            
            if mayusculasf =='':
            
                break


   
class dicacc():
    
    def cvf(self):
        
        fat = open(archivotickers, 'r',encoding="utf8", errors='ignore')

        lineas = fat.readlines()

        saltarheader = 0 #numero de lineas o accion-fondo
        
        num_fon=0 ## numero fondo
        num_acc=0 ## "numero accion"
    
        acciones_fondo= {}

        dictacciones={}

        for linea in lineas:

            if "Fondo" in linea:
                saltarheader += 1
                next  
            if saltarheader <2:
                next

            trozos= linea.split(';')
            

            if "Fondo" not in trozos[2]:

                acciones_fondo={}

                datos_accion_sinorden =[]


                datos_accion_sinorden.append(trozos[2]) ##fondo

                datos_accion_sinorden.append(trozos[4]) ##accion

                datos_accion_sinorden.append(trozos[5]) ##peso accion fondo

                stri = ""+trozos[2]+"_"+trozos[4]

                
                acciones_fondo[stri]= {0:datos_accion_sinorden[0],1:datos_accion_sinorden[1], 2:datos_accion_sinorden[2]}

                dictacciones[trozos[4]]=(trozos[0],trozos[1],trozos[2],trozos[3],trozos[4],trozos[5],trozos[6],trozos[7])

                num_acc =num_acc+1
                for t2 in dictacciones.values():

                    if t2 == trozos[2]:
                        claveunica = ""+trozos[2]+"_"+trozos[4]
                        s[claveunica]=(trozos[0],trozos[1],trozos[2],trozos[3],trozos[4],trozos[5],trozos[6],trozos[7],"trozos8","trozos9","trozos10","trozos11")
                        print(dicfontic[claveunica])
                        #input("406")
                    num_fon = num_fon +1
                
       

       

        fat.close()     
        csflist=[]
        csflist=[num_fon, num_acc]
        return acciones_fondo


class dicaccfonclase():
    
    def cvf(self):
        
        dicaccfoncl={}

        fat = open(archivotickers, 'r',encoding="utf8", errors='ignore')

        lineas = fat.readlines()

        saltarheader = 0 #numero de lineas o accion-fondo
        
        num_fon=0 ## numero fondo
        num_acc=0 ## "numero accion"


        for linea in lineas:

            if "Fondo" in linea:
                saltarheader += 1
                next  
            if saltarheader <2:
                next

            trozos= linea.split(';')
            
                                                                    
            trozos8=0.0 ##precio
            trozos9=0.0 ##variacion

        
            if "Fondo" not in trozos[2]:

                

                fondossinorden[trozos[2]]=0

                dictacciones[trozos[4]]=(trozos[0],trozos[1],trozos[2],trozos[3],trozos[4],trozos[5],trozos[6],trozos[7],trozos8,trozos9)

                num_acc =num_acc+1
                if True: ##for t2 in dictacciones.values():

                    if True: ##t2 == trozos[2]:
                        claveunica =trozos[2]+"_"+trozos[4]
                        dicfontic[claveunica]=[trozos[0],trozos[1],trozos[2],trozos[3],trozos[4],trozos[5],trozos[6],trozos[7],trozos8,trozos9]
                       
                    num_fon = num_fon +1
                
        listadicaccfon=[]

        dicaccfoncl={}

        for fon in sorted(fondossinorden.keys()):
        
            

            for linea in lineas:

                trozos2 = linea.split(";")
                ##print(trozos2)
                ##print("165")
           
                if trozos2[2]==fon:
                    
                    listadicaccfon.append(trozos2[4])
                    ##print(fon, " ",listadicaccfon)
                    ##print ("171")
            dicaccfoncl[fon]=listadicaccfon
            ##print(dicaccfoncl[fon])
           
            listadicaccfon=[]
        lista_fondos =sorted(fondossinorden.keys())
        
        fat.close()   

        csflist=[]
        csflist=[num_fon, num_acc]
        '''
        ctv=construirtikercvs()
        ctv.cabeceratikercsv()
        fg=dicaccfonclase()
        fgcvf=fg.cvf()
        ctv.cuerpotikercsv(fgcvf[0])
        '''
        return [dicfontic,dicaccfoncl,lista_fondos]   ##dicaccfon


class datos_fon(): 


    el = dicacc()
    
    dicaccfon=  el.cvf()

    cl=dicaccfonclase()  ## listado de acciones de un fondo

    dictaccfon = cl.cvf() ##dicfontic acciones_fondo dict clave unica

    dictfontic = cl.cvf()[0]         ## dicfontic claveunica acciones
    dicaccfoncl=cl.cvf()[1] ## diccionario accuibes del fondo
    lista_fondos = cl.cvf()[2]

    tuli =dicacc()

    acciones_fondo = tuli.cvf()

    peso_acumulado= 0.0

    variacion_ponderada =0.0

    peso_accion_fondo=0.0
    
    changePercentA=0.0

    abi = "" ##accion

    abidic= {}
     


    def cot_acc(self, dacci):
                        if  sabadoodomingo:
                            print("Hoy es fin de semana y no hay cotización")
                        else:
                            


                            url = "https://query1.finance.yahoo.com/v8/finance/chart/"+str(dacci)+"?metrics=high?"+"/&interval=1d&range=1d";

                            r = requests.get(url,  headers={'User-agent': 'Mozilla/5.0'})
                           
                            contenido   = r.json()

                            data = json.dumps(contenido)

                            ##print(data)

                            if "regularMarketPrice" not in data:

                                print(dacci," no encontrado")
                                ##input("no encontrada")
                                tnh = open(tickers_no_hallados, 'a')
                                tnh.write(dacci)
                                tnh.close()
                                next
                            

                            else:
                                
                                ##print( " ", dacci," 511")
                                busqueda =""
                                
                                symb = ""
                                
                                            
                                symbA = dacci
            
                                resultado = json.loads(data)

       
                                for meta, meta in resultado.items():
                                    i = 0
                                    #print ("linea 643 ",meta,"\n")  

                                    #print( " linea 645 ",meta['result'],"\n")

                                    #print( " linea 647 ",meta['result'][0],"\n")

                                    #for key, value in meta['result'][0].items():
                                        
                                        #print ("linea 651 ",key, "\n")
                                       
                                        #print ( "linea 653 ",value, "\n");


                                    #print (" linea 656 ",meta['result'][0]['meta'],"\n")
                                      

                                    #print (" linea 658 ",meta['result'][0]['meta']['symbol'], "\n")

                                    
                                    regularPrice = meta['result'][0]['meta']['regularMarketPrice']

                                    chartPrevious = meta['result'][0]['meta']['chartPreviousClose'] 

                                    changePercentA = (float(regularPrice)-float(chartPrevious))/float(chartPrevious) ##(float(marketPriceArmp)-float(changePercentA))/float(changePercentA) ##(marketPriceArmp-float(variableA))/float(variableA)   
                        
                                 
                                                    

                                cotiz_dacci[dacci]=[dacci,regularPrice,changePercentA]
                                print ("635 ", dacci, " Precio mercado: ", regularPrice, " Variación: ", changePercentA) 
                                return cotiz_dacci[dacci]

                                

    def dat_acc(self):

        peso_accion_fondo=0.0

        datosaccenelfondo={}

        
        list_dacci=[]

        nueveymedia_list_dacci = [] 


        for fon in fondossinorden:
        
            for dacci in datos_fon.dicaccfoncl[fon]:
                  print(dacci)
                  print("656")
                  list_dacci.append(dacci)
           
        if tiempooperacionnewyork ==False: ##False: 
                #True: ##//no carga usa y descuajeringa Pru1ods
            for dacci in list_dacci:    
                if "^" in fon or "." in dacci: 
                    nueveymedia_list_dacci.append(dacci)
        else:

            for dacci in list_dacci:
                nueveymedia_list_dacci.append(dacci)

        print(nueveymedia_list_dacci) 
        print("891")       
            
        numerodeaccion=1

        ##print(list_dacci)

        ##print("590")
        
        ###set_dacci=set(list_dacci)

        ##print(set_dacci)

        ##print ("596")   
        
        
        ###set_dacci=set(list_dacci)

        list_dacci_sin_duplicados = []

        list_dacci_sin_duplicados =list(nueveymedia_list_dacci)

        ##print(list_dacci_sin_duplicados)

        ##print("604 list_dacci_sin_duplicados")

        list_dacci_sin_duplicados.sort()

        ##print(list_dacci_sin_duplicados)
        ##print("sort 697")

        set_dacci=set(list_dacci_sin_duplicados)

        ##print(set_dacci) ##list_dacci_sin_duplicados)
        ##print("701")
        list_dacci_sorted = list(set_dacci)
        list_dacci_sorted.sort()
        print(list_dacci_sorted)
        ##input("705 set_dacci")

        #acciones_ordenadas = acciones_ordenadas.sort(reverse=False, key=any)

        for dacci in list_dacci_sorted: ##list_dacci_sin_duplicados:##(dicc_dacci.keys()).sort(): ##datos_fon.dicaccfoncl[fon]: 
                    ##print(" 573 ", dacci)
                    ##print("número de acción",numerodeaccion, " ", dacci)

                    ##numerodeaccion= numerodeaccion +1

                    
                    if tiempooperacionnewyork ==False: ##False: 
                        #True: ##//no carga usa y descuajeringa Pru1ods
                        

                        if "^" in dacci or "." in dacci: ##fon zv

                            cotiz_deacci=datos_fon.cot_acc(self,dacci) ##cotiz_deacci

                            print("número de acción no usa ",numerodeaccion, " ", dacci)

                            numerodeaccion= numerodeaccion +1

                    else:

                        cotiz_deacci=datos_fon.cot_acc(self,dacci) ##cotiz_deacci
                        
                        print("número de acción incluido usa ",numerodeaccion, " ", dacci)

                        numerodeaccion= numerodeaccion +1

                    ##print(cotiz_deacci)

        print("numero de acciones sin repetición ")
        print( len(list_dacci_sin_duplicados))        
        ##input("677")
        for fon in datos_fon.lista_fondos: ##dictaccfon: 

            n_acciones_fondo =0

            lista_datos_fondo=[]

            
            datos_fon.peso_acumulado=0.0

            ####datos_fon.variacion_ponderada=0.0000
            #####print(datos_fon.dicaccfoncl[fon])
            #####print(fon)
            ##input(689)

            for daccikey in nueveymedia_list_dacci: ###set_dacci:
                
                if daccikey in datos_fon.dicaccfoncl[fon]:

                    n_acciones_fondo =n_acciones_fondo+1
                
                    if True:
                        for fon in datos_fon.lista_fondos: ##dictaccfon: 


                            if "ondo"  not in fon:

                                n_acciones_fondo =1

                                lista_datos_fondo=[]

                                valorparticipaciones =0.0 

                                valorpesoglobal=0.0          


                                datos_fon.peso_acumulado=0.0

                                ####datos_fon.variacion_ponderada=0.0000
                                
                                n_acciones_fondo = 0

                                n_acciones_menos2_5 = 0

                                n_acciones_menos1_5 = 0

                                n_acciones_mas1_5 = 0

                                for daccikey in datos_fon.dicaccfoncl[fon]:

                                    if daccikey in list_dacci_sin_duplicados:

                                    ###if True:

                                            n_acciones_fondo =n_acciones_fondo + 1
                                
                                                
                                            claveunica = fon+"_"+daccikey

                                            ##print("linea 428 ",claveunica)
                                            peso_accion_fondo= datos_fon.dictfontic[claveunica][5]           

                                            ##print(claveunica ," linea 160")

                                            ##print("Fondo ","\t\t", "\t", "Part.", "\t", "Var","\t", "Peso","\t","Accion","\t","Precio")
                        
                                          
                                            valorparticipaciones=valorparticipaciones +   round(float(peso_accion_fondo),   4)

                                            valorpesoglobal= valorpesoglobal+round(float(peso_accion_fondo)*float(cotiz_dacci[daccikey][2]),4)   

                                            if float(cotiz_dacci[daccikey][2]) < -2.5/100:
                                                n_acciones_menos2_5 +=1
                                        
                                            if float(cotiz_dacci[daccikey][2]) < -1.5/100:
                                                n_acciones_menos1_5 +=1    
                                        
                                            if float(cotiz_dacci[daccikey][2]) > 1.5/100:
                                                n_acciones_mas1_5 +=1 
                                
                                lista_datos_fondo.append(fon)
                                lista_datos_fondo.append(n_acciones_fondo)
                                lista_datos_fondo.append(valorparticipaciones)
                                lista_datos_fondo.append(valorpesoglobal)
                                lista_datos_fondo.append(datetime.now())
                                lista_datos_fondo.append(n_acciones_menos2_5)
                                lista_datos_fondo.append(n_acciones_menos1_5)
                                lista_datos_fondo.append(n_acciones_mas1_5) 
                                ##print("linea 880 ",n_acciones_fondo, " ", valorparticipaciones, " ", valorpesoglobal, " ", datetime.now(), " ", n_acciones_menos2_5, " ", n_acciones_menos1_5, "  acciones +1.5 ", n_acciones_mas1_5)
                                ##input("linea 880")
                                if n_acciones_fondo <= 0:
                                    lista_datos_fondo.append(round(float(n_acciones_menos2_5/1),2))
                                    lista_datos_fondo.append(round(float(n_acciones_menos1_5/1),2))  
                                    lista_datos_fondo.append(round(float(n_acciones_mas1_5/1),2))
                                else:
                                    lista_datos_fondo.append(round(float(n_acciones_menos2_5/n_acciones_fondo),2))
                                    lista_datos_fondo.append(round(float(n_acciones_menos1_5/n_acciones_fondo),2))  
                                    lista_datos_fondo.append(round(float(n_acciones_mas1_5/n_acciones_fondo),2))


                                
                                datos_resumen_fon[fon]=lista_datos_fondo

                                ##print("Fondo","\t\t\t", "Part.", "\t", "Var","\t", "Peso","\t","Acción","\t","Precio")
                                print("linea 1062 fondo: ",fon, "\t Var: ", valorpesoglobal, "\t N ", n_acciones_fondo, "\t Porcentaje ", valorparticipaciones)
                                print("linea 1063 ", datetime.now(), "\t menos1_5  ", n_acciones_menos2_5, "\t menos1_5 ", n_acciones_menos1_5, "\t  acciones +1.5 ", n_acciones_mas1_5)
                                if n_acciones_fondo <= 0:
                                    print("linea 1064 -2.5:", round(float(n_acciones_menos2_5/1),2), " -1.5:", round(float(n_acciones_menos1_5/1),2), " +1.5: ", round(float(n_acciones_mas1_5/1),2))
                                else:
                                    print("linea 1064 -2.5:", round(float(n_acciones_menos2_5/n_acciones_fondo),2), " -1.5:", round(float(n_acciones_menos1_5/n_acciones_fondo),2), " +1.5: ", round(float(n_acciones_mas1_5/n_acciones_fondo),2))  

                
            lista_datos_fondo =[]
    
                
        
                    
                    
                    
                    
                    
                    
                    
                    
                       
                       
                       
                       
        return [datos_resumen_fon, datosaccenelfondo] ##resumen y detalle               
                
          


class manejarhistorico():
    
    contador =0
    
    txtlistadohistoricobak=[]

    def chuparmh(self): ##re dic datos hoy

        historicocotizapython = rhcsv   

              
    

        h = open(rhcsv, 'r',encoding="utf8", errors='ignore')

        lineah= h.readlines()

        saltarcabecera =0

        for line in lineah:
            
            
            saltarcabecera = saltarcabecera +1
      
            if saltarcabecera==1:
                continue

            trozoslin=line.split(';')

            if trozoslin[0] is None or len(trozoslin[0])<4:
                continue

            
            if (not (trozoslin[0] is None)) and len(trozoslin[0])>4:##and ('/' in trozoslin[0]) :

                if '-' in trozoslin[0]:

                    primerslash = trozoslin[0].index('-')
                    segundoslash = trozoslin[0].rfind('-')

                    diahoyprimerguion= (diahoy).index('-')
                    diahoysegundoguion = ( diahoy).rfind("-")

                    #print("linea 718 ano historico",str(int(trozoslin[0][0:primerslash])))
                    #print("linea 719 mes historico ",str((trozoslin[0][primerslash+1:segundoslash])))
                    #print("linea 720 dia historico", str(int (trozoslin[0][segundoslash+1:])))

                    anoh=(int(trozoslin[0][0:primerslash])) ##aqui hemos cambiado diah por anoh al ser guion
                    mesh=(int(trozoslin[0][primerslash+1:segundoslash]))
                    diah=(int (trozoslin[0][segundoslash+1:])) ##aqui hemos cambiado anoh por diah al ser guion



                    anohoy =(int(diahoy[0:diahoyprimerguion]))
                    meshoy=(int(diahoy[diahoyprimerguion+1: diahoysegundoguion]))
                    diahoynum= (int(diahoy[diahoysegundoguion+1:]))

                    
                    ##print("linea 561 dia hoy  ",(diahoynum))
                    ##print("linea 562 meshoy ",(mesh))
                    ##print("lineahoy 563 anohoy ", (anoh))

                    ##print("linea 574 ", trozoslin[1], trozoslin[0])

                    #print(("linea 739 con guiones ",(datetime.isoweekday(datetime(anoh,mesh,diah)))), "  ", datetime(anoh,mesh,diah), " today ",datetime(anohoy,meshoy,diahoynum))
                            

                    if  (datetime(anoh,mesh,diah)<datetime(anohoy, meshoy, diahoynum)):
                        registro = trozoslin[0]+";"+trozoslin[1]+";"+trozoslin[2]+";"+trozoslin[3].replace(',','.')+";"+(trozoslin[4].replace(',','.'))
                        registro = registro ##+";\n"

                        
                        manejarhistorico.txtlistadohistoricobak.append(registro)
                        ##print("linea 554 ",txtlistadohistoricobak)
                        itemhistorico.append([trozoslin[0],trozoslin[1],trozoslin[2],trozoslin[3],trozoslin[4]])
    


                if '/' in trozoslin[0]:    
                   
                    primerslash = trozoslin[0].index('/')
                    segundoslash = trozoslin[0].rfind('/')

                    diahoyprimerguion= (diahoy).index('-')
                    diahoysegundoguion = ( diahoy).rfind("-")

                    #print("linea 760 dia historico",str(int(trozoslin[0][0:primerslash])))
                    #print("linea 761 mes historico ",str((trozoslin[0][primerslash+1:segundoslash])))
                    #print("linea 762 ano historico", str(int (trozoslin[0][segundoslash+1:])))

                    diah=(int(trozoslin[0][0:primerslash]))
                    mesh=(int(trozoslin[0][primerslash+1:segundoslash]))
                    anoh=(int (trozoslin[0][segundoslash+1:]))



                    anohoy =(int(diahoy[0:diahoyprimerguion]))
                    meshoy=(int(diahoy[diahoyprimerguion+1: diahoysegundoguion]))
                    diahoynum= (int(diahoy[diahoysegundoguion+1:]))

                    
                    ##print("linea 561 dia hoy  ",(diahoynum))
                    ##print("linea 562 meshoy ",(mesh))
                    ##print("lineahoy 563 anohoy ", (anoh))

                    ##print("linea 574 ", trozoslin[1], trozoslin[0])

                    #print(("linea 781",(datetime.isoweekday(datetime(anoh,mesh,diah)))), "  ", datetime(anoh,mesh,diah), " yesteday  ",(datetime.today()-timedelta(days=0, seconds=0, microseconds=0,           milliseconds=0, minutes=0, hours=23, weeks=0)))
                            

                    if   ((datetime.isoweekday(datetime(anoh,mesh,diah)))<6) and datetime(anoh,mesh,diah)<(datetime.today()-timedelta(days=0, seconds=0, microseconds=0,  milliseconds=0, minutes=0, hours=23, weeks=0)):
                        registro = trozoslin[0]+";"+trozoslin[1]+";"+trozoslin[2]+";"+trozoslin[3].replace(',','.')+";"+(trozoslin[4].replace(',','.'))
                        registro = registro ##+";\n"
                        ### print("linea 568 ",registro)
                        manejarhistorico.txtlistadohistoricobak.append(registro)
                        ##print("linea 554 ",txtlistadohistoricobak)
                        itemhistorico.append([trozoslin[0],trozoslin[1],trozoslin[2],trozoslin[3],trozoslin[4]])
    
        h.close()
        return manejarhistorico.txtlistadohistoricobak

    def recrearficheromh(self):
        
        ##borrado de fichero
        hm = open(rhcsv, 'w')
        cabecera=( 'Fecha'+";"+'Fondo'+";"+'N'+";"+'Peso'+';'+'Var_Por'+";\n") ##Día
        ##print("CABECERA DE HISTORICO ",cabecera)
        hm.write(cabecera)
        hm.close()
        

    def incorporarmh(self):  ##manejarhistorico.txtlistadohistoricobak historico

    
        
        #reconstitución de fichero
               
        h = open(rhcsv, 'a')

        for registro in manejarhistorico.txtlistadohistoricobak:
            ##print("linea 609 incorporando viejos rhcsv ", registro)
            ll=h.write(registro)##+";\n")
            #print("576 ", ll)
            ##print("642",registro)

        h.close()

    def incorporarhoy(self):      

        re = datos_resumen_fon
        
        h= open(rhcsv,'a')

        for cad in re.keys(): ## las keys son los fondos
            #print("linea 283 ", cad)
            if  sabadoodomingo:
                print("Hoy es fin de semana y no hay cotización")
            else: #elimina los de hoy  y fines para que no se dupliquen
         
                recad=datos_resumen_fon[cad]
                ##print(recad)
                cadenaretxt= str(diahoy)+";"+str(recad[0])+";"+str(recad[1])+";"+str(recad[2])+";"+str(recad[3])+";\n"###+momentohoy+";\n"
                ##print ("REGISTROS DE HOY ",cadenaretxt)

                ##print ("589 ",cadenaretxt)
                
                h.write(cadenaretxt)
                itemhistorico.append(re[cad])
        
        h.close()

        print("linea 1036  imprimientdo iten historico´´´´´´´´´´´´´´")

        ##for item in itemhistorico:
            ##print(item) 
            ##print("linea 1040") 
        
       

class preguntarchartfondo():

    mayusculasf =""


    ## fufu =mostrarchartfondo()
    def pcf(self):
        
        repetir = 'S'

        while repetir in 'SI':

            eleccionfondo ='BOLSAESPANA'

            ##eleccionfondo = 'si'    

            while eleccionfondo !='':
              
                mayusculasf =eleccionfondo.upper()
                if mayusculasf =='':
                    repetir ="no"
                    break
                
                
        
            repetir = input("De qué fondo desea ver más gráficos?")

       


class maino():
    saltarheader2=0
    
    def creaccionnombresfondos(self):
        
        

        fsog = open(archivonombresfondos,'w')

        fsog.close()

        ##print ("646 fichero renovado ", archivonombresfondos)

    def anadidosfondos(self):

        ##print("650 ejecutando anadidosfondos")
               
        arcnomfon =archivonombresfondos

        er = dicaccfonclase()
        listafondos = er.cvf()[2]
   
        fso = open(arcnomfon, 'a')

    

        for fond9 in listafondos: ##archivo nombres fondos
            
            cadfon =fond9+"\n"
            py =fso.write(cadfon)
          
        fso.close()

    
    def creacotizahoypython(self):


        f = cotizahoypython
        ##if os.path.isfile(f):
            ##  os.remove(f)

        chp = cotizahoypython

        g=open(chp,'w')
        
        g.write( 'Fecha'+";"+'Fondo'+";"+'n'+";"+'Peso'+';'+'Var_Por'+";"+"Actualizacion"+";"+'n_menos2_5'+";"+'n_menos1_5'+";"+'n_mas1_5'+";"+'porc_menos2_5'+";"+'porc_menos1_5'+";"+'porc_mas1_5'+'\n')
        g.close()

        resumcsv = open(resucsv,'w')
        resumcsv.close()

        resumcsv = open(resucsv,'a')

        resumcsv.write("dia;fondo;n;peso;Var_Por;actualizacion;n_menos2_5;n_menos1_5;n_mas1_5;porc_menos2_5;porc_menos1_5;porc_mas1_5\n")  

        resumcsv.close()    

    def anadircotizahoypython(self):
        
       
        cothoypyt = cotizahoypython

        
        re = datos_resumen_fon

        ##print (re)

        gi = open(cothoypyt, 'a')

        resum_csv = open(resucsv,'a')


        for resumen in re: ## las resume son los fondos
        
            ##print(resumen)

            listado = re[resumen]
            
            ##print(listado)

    
            linea_resumen = ""+str(diahoy)+";"+str(listado[0])+";"+ str(listado[1])+";" +str(listado[2])+";"+str(listado[3])+";" +str(listado[4])+";"+ str(listado[5])+";"+ str(listado[6])+";"+ str(listado[7])+";"+ str(listado[8])+";"+ str(listado[9])+ ";"+str(listado[10])+"\n"

            ##print(linea_resumen)

            ilo = gi.write (linea_resumen)

            ulo = resum_csv.write(linea_resumen)    
            
      
        gi.close()

        resum_csv.close()
        
        
        '''
        
        if os.path.isfile(resucsv):
            os.remove(resucsv)


        resumcsv = open(resucsv,'w')
        resumcsv.close()

        resumcsv = open(resucsv,'a')

        resumcsv.write("dia;fondo;n;peso;Var_Por;actualizacion;n_menos2_5;n_menos1_5;n_mas1_5;porc_menos2_5;porc_menos1_5;porc_mas1_5\n")   

        

        for resumen in datos_fon.dat_acc()[0]:            
            ##print(resumen)

            listado = re[resumen]
            
            ##print(listado)

            linea_resumen = ""+str(diahoy)+";"+str(listado[0])+";"+ str(listado[1])+";" +str(listado[2])+";"+str(listado[3])+";" +str(momentohoy)+"\n"

            ##print(linea_resumen)

            ilo = resumcsv.write (linea_resumen)
            
      
        resumcsv.close()
        '''
    def pantallahoy(self):

        h = open(cotizahoypython, 'r',encoding="utf8", errors='ignore')

        lineah= h.readlines()

        eliminadorcabeza=0;

        for line in lineah:

            campos= line.split(";")
            
            if eliminadorcabeza==0:
                eliminadorcabeza= eliminadorcabeza +1
                fecha = str(campos[0])
                fondos = campos[1],
                n=campos[2]
              
              
                
                
              
                print('{:3}\t\t{:4}\t{:4}\t{:4}\t{:}'.format(str(campos[0]),str(campos[2]),str(campos[3]),str(campos[4]),'\t',campos[1]))
                next

                       
            else: 

                pesof=round(float(campos[3]),4)
                variacionf=round(float(campos[4]),4)
                fecha = str(campos[0])
                fondos = campos[1]
                n=str(int(campos[2]))
                var = str(round(float(campos[3]),4))
                


                ##print(pesof,  "  var: ",variacionf)

                print('{:3}\t{:4}\t{:4}\t{:4}\t{:}'.format(fecha,n,pesof,variacionf,fondos))
                
                ##print(str(campos[0]),'\t',campos[1],'\t',str(campos[2]),'\t',str(pesof), '\t',str(variacionf))
        ##print(tabulate(lineah, headers = ['fecha','fondo','n','Peso','Variacion']))
        h.close()

    def procesomanejarhistorico(self):
       
      
        mhu=manejarhistorico()
        bu =mhu.mh()


class mostrar_resumen_csv_precendente():
    
        def mrcp(self):
            datosderesumencsv = pd.read_csv( resucsv, header =0,  sep=';',decimal='.', encoding='ISO-8859-1')
    
            print(datosderesumencsv)
    
            ##input("linea 1314 datos resumen csv precendente")

class mainje():  

    def maindef(self): 

        mdrp = mostrar_resumen_csv_precendente()
        mdrp.mrcp()
        
        actualizardatos = "S" ##input("Actualizar datos? (s) ")
        if actualizardatos  in "Sisi":      
            momentoinicio = str(datetime.now())
            print(momentoinicio)
            print("trabajando ...")
            gir=datos_fon()
            ejec0 = gir.dat_acc() ##da datos_resume_fon
            ctv=construirtikercvs()
            ctv.cabeceratikercsv()
            fg=dicaccfonclase()
            fgcvf=fg.cvf()
            ctv.cuerpotikercsv(fgcvf[0])
            ejecutar = maino()
            ejec1 = ejecutar.creaccionnombresfondos()
            ejec2 = ejecutar.anadidosfondos()
            ejec3= ejecutar.creacotizahoypython()
            ejec4= ejecutar.anadircotizahoypython()
            ejec5= ejecutar.pantallahoy()
                    
            mhejecutar =manejarhistorico()
            meje1= mhejecutar.chuparmh()
            meje2= mhejecutar.recrearficheromh()
            meje3= mhejecutar.incorporarmh()
        
            meje4= mhejecutar.incorporarhoy();
            print(momentoinicio)
            momentofinalizacion = str(datetime.now())
            print(momentofinalizacion)

            datosderesumencsv = pd.read_csv( resucsv, header =0,  sep=';',decimal='.', encoding='ISO-8859-1')

            print(datosderesumencsv)

            #input("873")
            ##hy=ver_comp()
            #hy.ver_c(ejec0[1])

        ##repetir = input( " 875 Quiere ver el gráfico de algún fondo (n = ninguno) ")
        '''
        while repetir not in "Nn":
            ##io = preguntarchartfondo()
            ##iou= io.pcf()
            jijo=mostrarchartfondo()
            ##jijomcf=jijo.mcf( )   
            ##jijomoc0= jijo.antiguocf()

            presentacion_final = pd.read_csv( resucsv, header =0,  sep=';',decimal='.', encoding='ISO-8859-1')  
            
            repetir = "N" ##input( " 883 Quiere ver el gráfico de algún fondo (n = ninguno) ")
        '''
    momentohoy = str(datetime.now())
    print(momentohoy)

if False: ##numdiasemana>5: ## el fin de semana no se actualiza
    print("el fin de semana esto no funciona")
    #input("854")
    exit()
cl= mainje()
cl.maindef()

   
