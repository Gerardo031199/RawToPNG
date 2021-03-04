#Librerias utilizadas
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import os
import binascii
from tkinter import messagebox as MessageBox
from PIL import ImageTk, Image, ImageOps
from tkinter import ttk
from pathlib import Path
import webbrowser
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox as mb
import sys
import zlib
import struct
from time import sleep


file1=askopenfile(title = "Seleccione archivo",mode='rb',filetypes = (("all files","*.*"),
                    ("str files","*.str")))

content1 = file1.read()

#print(content1)

head_paleta= b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x80\x00\x00\x00\x80\x08\x03\x00\x00\x00\xf4\xe0\x91\xf9\x00\x00\x03\x00PLTE'
paleta=(content1[128:1152]).hex()



nueva_paleta=""
indice=0
while indice<len(paleta)-1:
    nueva_paleta+=paleta[indice:indice+6]
    indice+=8

nueva_paleta_hxd = binascii.unhexlify(nueva_paleta)


for i in range(0, 1024, 96):
    p1= (nueva_paleta_hxd[i:i + 24])
    p2= (nueva_paleta_hxd[i + 24:i + 48])
    p3= (nueva_paleta_hxd[i + 48:i + 72])
    p4= (nueva_paleta_hxd[i + 72:i + 96])

    one=(p1+p3+p2+p4).hex()


    print(one)



long_paleta = zlib.crc32(nueva_paleta_hxd)
#print(long_paleta)
long_paleta_zlib32 = long_paleta.to_bytes(4, byteorder='big', signed=False)
#print(long_paleta_zlib32)


end= b'\x00\x00\x01\x00'

end2 = b'tRNS'

ff=(b'\xff' * 256)

texture= (content1[1152:17535]).hex()


#print(ff)


def dividirCadena(cadena, separador, numeroCaracteres):
    cifra = ""
    contador = 0
    for numero in cadena:
        if contador == numeroCaracteres:
            cifra += separador
            contador = 0
            
        contador += 1
        cifra += numero

    return (cifra)

funcion = dividirCadena(texture, "00", 256)


newFuncion=("00"+funcion)
funcion_hxd = binascii.unhexlify(newFuncion)

end_ff= b'IDAT'

long_trns = zlib.crc32(end2+ff)
#print(long_trns)
long_trns_zlib32 = long_trns.to_bytes(4, byteorder='big', signed=False)
#print(long_trns_zlib32)



funcion_hxd_compress=zlib.compress(funcion_hxd, 9)


long_texture = len(funcion_hxd_compress)

carga_texture = long_texture.to_bytes(4, byteorder='big', signed=True)
#print(carga_texture)


end_png = b'IEND'


file1=open("Face_Pes.png",'wb')
file1.write(head_paleta)
file1.write(nueva_paleta_hxd)
file1.write(long_paleta_zlib32)
file1.write(end)
file1.write(end2)
file1.write(ff)
file1.write(long_trns_zlib32)
file1.write(carga_texture)
file1.write(end_ff)
file1.write(funcion_hxd_compress)
file1.write(end_png)
file1.close()
