# Script en Python 3.7 
#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# Crea un informe con el contenido de los archivos .txt contenidos en la carpeta

import datetime
import sys, hashlib
from os import walk
global arch_inf

arch_inf = open("informe.txt", "w+", encoding='utf-8')
contf = 0

non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
s3 = hashlib.sha256()

def abrir_inf():

        hini = str(datetime.datetime.now())
        arch_inf.write("--- INICIO DE INFORME --- \n" + hini + "\r\n\r\n")
        arch_inf.write("-- ARCHIVOS \'.txt\' ENCONTRADOS:        \n\n ")


def cerrar_inf():
        global contf
        hfin = str(datetime.datetime.now())
        arch_inf.write(hfin+ "\n--- FIN DE INFORME ---")

        arch_inf.seek(92,0)
        arch_inf.write(str(contf) + " --")
        
        arch_inf.close()



def sacalo(dato):
        global contf
        hor = str(datetime.datetime.now())
        with open(dato, "rb") as afile:
                buf = afile.read()
                leido = hashlib.sha256(buf)

        
        afile.close()
        arch_inf.write("\r\n---------ARCHIVO ENCONTRADO--------- \nArchivo \'" + dato + "\' \n")
        arch_inf.write("sha256:" + leido.hexdigest() + "\n\n   CONTENIDO:- \n\n")
        arch = open(dato, "r", encoding="utf-8") #, errors="replace")
        lines = arch.readlines()
        contf += 1
        arch.close()

        for line in lines:
                try:
                       texto = line.translate(non_bmp_map)
                       arch_inf.write(texto)
                except:
                        pass



def main(argv):
        abrir_inf()
        for root, dirs, files in walk(argv[0]):
                print("Identificando archivos con extensión \'.txt\'...\n")
             
        for uno in files:
                exten = uno[-3:len(uno)].lower()
                if exten == "txt" and uno != "informe.txt":
                        sacalo(uno)
                        arch_inf.write("---------FIN DEL ARCHIVO--------- \n\n\n")
        

        cerrar_inf()



if __name__ == "__main__":
        _script_argv = sys.argv[1:]
        if len(_script_argv) == 0:
                main(".")
                
        else:
                print("De momento sólo es funcional desde el mismo directorio.\nPor favor, copie este script en el directorio a buscar datos y ejecute sin argumentos.")
                # main(_script_argv)
