# Script en Python 3.7 
#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# Crea un informe con el contenido de los archivos .txt contenidos en la carpeta
# Version 0.2: Recibe como parametro el directorio donde trabaja, sino recibe parametro trabaja sobre el directorio actual

import datetime
import sys, hashlib
from os import walk
global non_bmp_map

def cabecera(directorio):
        global non_bmp_map
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        s3 = hashlib.sha256()
        hini = str(datetime.datetime.now())
        print("\n-----------------------------------------")
        print("--- INFORME GENERADO CON parseWAtxt   ---")
        print("--- " + hini + "        ---")
        print("-----------------------------------------\n")
        print("--- INICIO DE INFORME --- ")


def cerrar_inf():
        hfin = str(datetime.datetime.now())
        print(hfin+ "\n--- FIN DE INFORME ---")

def sacalo(dato):
        
        hor = str(datetime.datetime.now())
        with open(dato, "rb") as afile:
                buf = afile.read()
                leido = hashlib.sha256(buf)

        
        afile.close()
        texto1 = "\r\n---------ARCHIVO ENCONTRADO--------- \nArchivo \'" + dato + "\' \n"
        texto2 = "sha256:" + leido.hexdigest() + "\n\n"
        print(texto1)
        print(texto2)
        print("   CONTENIDO:- \n\n")
        arch = open(dato, "r", encoding="utf-8") #, errors="replace")
        lines = arch.readlines()
        
        arch.close()

        for line in lines:
                try:
                       texto = line.translate(non_bmp_map)
                       print(texto)
                except:
                        pass



def main(argv):
        contf = 0
        cabecera(argv)
        for root, dirs, files in walk(argv):
                print("Identificando archivos con extensión \'.txt\'...\n")
        for uno in files:
                exten = uno[-3:len(uno)].lower()
                if exten == "txt" and uno != "informe.txt":
                        contf+=1
        print("-- ARCHIVOS \'.txt\' ENCONTRADOS: " + str(contf))
        for uno in files:
                exten = uno[-3:len(uno)].lower()
                if exten == "txt" and uno != "informe.txt":
                        name_tmp = root+ "/" + uno
                        #print(name_tmp)
                        sacalo(name_tmp)
                        print("---------FIN DEL ARCHIVO--------- \n\n\n")
        

        cerrar_inf()



if __name__ == "__main__":
        _script_argv = sys.argv[1:]
        if len(_script_argv) == 0:
                main(".")
                
        else:
                main(sys.argv[1])
