# Script en Python 3.7 
#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
# Crea un informe con el contenido de los archivos .txt contenidos en la carpeta
# Version 0.2: Recibe como parametro el directorio donde trabaja, sino recibe parametro trabaja sobre el directorio actual

import datetime
import sys, hashlib
from os import walk
global arch_inf
global contf
global non_bmp_map

def cabecera(directorio):
        global arch_inf
        global contf
        global non_bmp_map
        arch_inf = open(directorio + "/informe.txt", "w+", encoding='utf-8')
        contf = 0

        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        s3 = hashlib.sha256()

def abrir_inf():
        global arch_inf
        hini = str(datetime.datetime.now())
        arch_inf.write("--- INICIO DE INFORME --- \n" + hini + "\r\n\r\n")
        arch_inf.write("-- ARCHIVOS \'.txt\' ENCONTRADOS:        \n\n ")


def cerrar_inf():
        global arch_inf
        global contf
        hfin = str(datetime.datetime.now())
        arch_inf.write(hfin+ "\n--- FIN DE INFORME ---")

        arch_inf.seek(92,0)
        arch_inf.write(str(contf) + " --")
        
        arch_inf.close()
        print("Informe generado")



def sacalo(dato):
        global arch_inf
        global contf
        hor = str(datetime.datetime.now())
        with open(dato, "rb") as afile:
                buf = afile.read()
                leido = hashlib.sha256(buf)

        
        afile.close()
        texto1 = "\r\n---------ARCHIVO ENCONTRADO--------- \nArchivo \'" + dato + "\' \n"
        texto2 = "sha256:" + leido.hexdigest() + "\n\n"
        print(texto1)
        print(texto2)
        arch_inf.write(texto1)
        arch_inf.write(texto2 + "   CONTENIDO:- \n\n")
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
        global arch_inf
        global contf
        cabecera(argv)
        abrir_inf()
        #print(argv[2])
        for root, dirs, files in walk(argv):
                print("Identificando archivos con extensión \'.txt\'...\n")
        for uno in files:
                exten = uno[-3:len(uno)].lower()
                if exten == "txt" and uno != "informe.txt":
                        name_tmp = root+ "/" + uno
                        #print(name_tmp)
                        sacalo(name_tmp)
                        arch_inf.write("---------FIN DEL ARCHIVO--------- \n\n\n")
        

        cerrar_inf()



if __name__ == "__main__":
        _script_argv = sys.argv[1:]
        if len(_script_argv) == 0:
                main(".")
                
        else:
                main(sys.argv[1])
