"""
Created on Thu Sep 24 18:03:01 2020

@author: iakar
"""

#Para importar el archivo de excel

import csv
lista_datos=[]

with open("synergy_logistics_database.csv", "r", encoding='utf-8-sig') as archivo_log:
    lector_log = csv.reader(archivo_log)
    
    for linea in lector_log:
        lista_datos.append(linea)
        
    datos=lista_datos.pop(0)




#Opcion 1: Rutas de importacion y exportacion 
#10 rutas mas demandas acorde a los flujos de importacion y exportacion 



def rutas(direccion):
    contador =0
    contador2=0
    rutas_contadas = []
    conteo_rutas = []
    
    for ruta in lista_datos:
        if ruta[1] == direccion:
            ruta_actual = [ruta[2], ruta[3]]
            #localizar las rutas
            if ruta_actual not in rutas_contadas:
                for movimiento in lista_datos:
                    if ruta_actual == [movimiento[2], movimiento[3]] and movimiento[1] == direccion:
                        contador += 1
                        contador2 += int(movimiento[9])
                        
                rutas_contadas.append(ruta_actual)
                conteo_rutas.append([ruta[2], ruta[3], contador, int(contador2)])
                contador = 0
                contador2 = 0

    return conteo_rutas


print("Bienvenido")
im= int(input("Coloca el número 1 para observar las importaciones:"))
if im==1:
    lista_impo = rutas("Imports")
    print(lista_impo)
else:
    print("Te equivocaste")
    
ex= int(input("Ahora para ver las exportaciones coloca el número 2:"))
if  ex==2:
    lista_expo = rutas("Exports")
    print(lista_expo)
else:
    print("Te equivocaste")


#Para ordenar se usa un sort

#importaciones              
lista_impo.sort(reverse = True, key = lambda x:x[2])
#exportaciones           
lista_expo.sort(reverse = True, key = lambda x:x[2])

#Para llevarlas a un excel nuevo 

with open("impo.csv","w") as f:
       wr = csv.writer(f,delimiter="\n")
       wr.writerow(lista_impo)

with open("expo.csv","w") as f:
       wr = csv.writer(f,delimiter="\n")
       wr.writerow(lista_expo)


#Opcion 2: Medio de transporte utilizado 
#Tres medio de transporte más importantes para Sydney considerando el valor de las importaciones y exportaciones 
#Cual medio de transporte pueden reducir

def transportmode(transporte, direccion):
    contador = 0
    transport_contados = []
    conteo_transport = []
    
    for dire in lista_datos:
        if dire[1] == direccion:
    
            for trans in lista_datos:
                if trans[7] == transporte:
                    trans_actual = [trans[7]]
                    #localizar las rutas
                    if trans_actual not in transport_contados:
                        for mediot in lista_datos:
                            if trans_actual == [mediot[7]] and mediot[1] == direccion:
                                contador += int(mediot[9])
                                
                        transport_contados.append(trans_actual)
                        conteo_transport.append([trans[7], contador])
                        contador = 0

            return conteo_transport

        
print("Ahora se muestran se muestra el valor de las importaciones y exportaciones por medio de transporte")
opc_tr= int(input("Elige una opción de transporte: (1)air, (2)sea, (3)rail (4)road:"))
opc_dir= int(input("Elige una: (1)importaciones o (2)exportaciones:"))

if opc_tr==1 and opc_dir == 1:
    lista_air_i = transportmode("Air","Imports")
    print(lista_air_i)
elif opc_tr==1 and opc_dir == 2:
    lista_air_e = transportmode("Air","Exports")
    print(lista_air_e)
elif opc_tr==2 and opc_dir == 1:
    lista_sea_i = transportmode("Sea","Imports")
    print(lista_sea_i)
elif opc_tr==2 and opc_dir == 2:
    lista_sea_e = transportmode("Sea","Exports")
    print(lista_sea_e)
elif opc_tr==3 and opc_dir == 1:
    lista_rail_i = transportmode("Rail","Imports")
    print(lista_rail_i)
elif opc_tr==3 and opc_dir == 2:
    lista_rail_e = transportmode("Rail","Exports")
    print(lista_rail_e)
elif opc_tr==4 and opc_dir == 1:
    lista_road_i = transportmode("Road","Imports")
    print(lista_road_i)
elif opc_tr==3 and opc_dir == 2:
    lista_road_e = transportmode("Road","Exports")
    print(lista_road_e)   
else:
    print("Te equivocastee")


#Opcion 3: valor de importaciones y exportaciones
###Valor total de importaciones y exportaciones 
##paises que generan el 80% del valor de las exportaciones e importaciones

#PAISES DE EXPORTACIONES Y PAISES DE IMPORTACIONES
def ladireccion(usuario_direccion):
    paises_dir=[]
    for lpais in lista_datos:
        if lpais[2] not in paises_dir and lpais[1] == usuario_direccion:
            paisexp= lpais[2]
            paises_dir.append(paisexp)    
    return paises_dir

#lista de paises de exportacion
lasexports = ladireccion("Exports")

#lista de paises de importacion
lasimports = ladireccion("Imports")


#Lista de importaciones con porcentajes
n_impo=[]
for i in lista_impo:
    nimp = i[3]
    n_impo.append(nimp)

numero_imp = len(n_impo)
total_imp = sum(n_impo)

p_impo=[]
for i in lista_impo:
    p_impo.append([i[0], i[1], i[2], i[3], ((i[3]/total_imp)*100)])
    
#importaciones              
p_impo.sort(reverse = True, key = lambda x:x[4])
print(p_impo)    



#Lista de exportaciones con porcentajes
n_expo=[]
for i in lista_expo:
    nexp = i[3]
    n_expo.append(nexp)

numero_exp = len(n_expo)
total_exp = sum(n_expo)

p_expo=[]
for i in lista_expo:
    p_expo.append([i[0], i[1], i[2], i[3], ((i[3]/total_exp)*100)])
    
#importaciones              
p_expo.sort(reverse = True, key = lambda x:x[4])
print(p_expo)    