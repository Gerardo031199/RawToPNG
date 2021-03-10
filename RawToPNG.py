#Librerias utilizadas
from tkinter import filedialog
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import os
import tkinter
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

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("WE-PES Face Converter PS2")
        self.ventana1.resizable(width=False, height=False)

        self.style = Style()
        
        self.style.configure('W01.TLabel', font =('Arial', 11,'bold'),foreground = 'black')
        self.label1=ttk.Label(self.ventana1, text="WE-PES FACE CONVERTER PS2",style = 'W01.TLabel')
        self.label1.grid(column=0, row=0)

        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Pes2We Face")
        self.labelframe1.grid(column=0, row=1, padx=10, pady=10)
        self.agregar_componentes()

        self.labelframe1=ttk.LabelFrame(self.ventana1, text="We2Pes Face")
        self.labelframe1.grid(column=0, row=2, padx=10, pady=10)
        self.agregar_componentes2()


        self.labelframe1=ttk.LabelFrame(self.ventana1, text="Información")
        self.labelframe1.grid(column=0, row=3, padx=10, pady=10)
        self.creditos()
        self.agregar_menu()
        self.ventana1.mainloop()
    
        
    def agregar_componentes(self):

        
        # This will be adding style, and 
        # naming that style variable as 
        # W.Tbutton (TButton is used for ttk.Button).
        self.style.configure('W.TButton', font =('Arial', 10, 'bold'),foreground = 'black')

        self.boton0=ttk.Button(self.labelframe1, text="Open file",style = 'W.TButton', command=self.facePes2We)
        self.boton0.grid(column=1, row=1, padx=53, pady=10, sticky="we",ipadx=20, ipady=10)

        
    def agregar_componentes2(self):
        self.style.configure('W1.TButton', font =('Arial', 10,'bold'),foreground = 'black')

        self.boton0=ttk.Button(self.labelframe1, text="Open file",style = 'W1.TButton', command=self.faceWe2Pes)
        self.boton0.grid(column=1, row=2, padx=53, pady=10, sticky="we",ipadx=20, ipady=10)

  



    def creditos(self):
        self.label1=ttk.Label(self.labelframe1, text="Program developed by Gerardo Contreras")
        self.label1.grid(column=0, row=0, padx=10, pady=10, sticky="e")

        self.label1=ttk.Label(self.labelframe1, text="Python version: 3.7.4")
        self.label1.grid(column=0, row=1, padx=10, pady=10, sticky="we")

        self.label1=ttk.Label(self.labelframe1, text="Tk version: 8.6.9")
        self.label1.grid(column=0, row=1, padx=10, pady=10, sticky="e")
        
   
    def agregar_menu(self):
        self.menubar1 = tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar1)
        self.opciones1 = tk.Menu(self.menubar1, tearoff=0)
        self.opciones2 = tk.Menu(self.menubar1, tearoff=0)


        self.opciones2.add_command(label="Acerca de...", command=self.acerca)
        self.opciones2.add_command(label='YouTube', command=self.f_web)

        self.opciones1.add_command(label="Salir", command=self.salir)
        

        
        self.menubar1.add_cascade(label="Inicio", menu=self.opciones1)
        self.menubar1.add_cascade(label="Ayuda", menu=self.opciones2)
    


    def f_web(self):     
        pag1 = 'https://www.youtube.com/channel/UCzHGN5DBIXVviZQypFH_ieg'
        webbrowser.open_new(pag1)
        
    def acerca(self):
        mb.showinfo("Información", "Este programa fue desarrollado por Gerardo Contreras")

    def salir(self):
        respuesta=mb.askyesno("¡Alerta!", "¿Quiere salir del programa?")
        if respuesta==True:
            sys.exit()

    def facePes2We(self):
        head_texture_pes6= b'\x94r\x85)\x01\x00\x00\x00\x80$\x00\x00\x01\x00\x00\x00\x80\x04\x80\x00@\x00\x80\x00\x02\x13\x06\x07\x01\x00\x10\x10\x00\x02\x00\x00@\x00\x00\x00@\x00\x80\x00\x02\x13\x03\x10@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

        
        archivo1=askopenfile(title = "Seleccione archivo",mode='rb',filetypes = (("all files","*.*"),
                    ("str files","*.str")))  

        if archivo1 is not None:
            
            #print(file_path)
            content1 = archivo1.read()

            indic0=(content1[0:4])
            indic3=(content1[12:32])
            #print(indic0)


            my_data = content1[32:len(content1)]

            
            com_data = (my_data[0:2])
            
            

            if (com_data) == (b'x\xda'):


                file_name = (archivo1.name)
                #print(file_name)

                save_path0 = Path(file_name).parent.absolute()

                nameFile=(Path(file_name).resolve().stem)
                #print(nameFile)

                var = StringVar()
                var.set(nameFile)

                decompressed_data = zlib.decompress(my_data)

                posctxs = decompressed_data.find(b'\x94r\x85)\x01')
                

                imgcode = decompressed_data[posctxs:len(decompressed_data)]
                #print(imgcode)

                
                base3d=(decompressed_data[0:posctxs])
                #print(base3d)


                

                
          

                #self.etiquetamore = tk.Label(self.ventana1, text="Archivo cargado:").place(x=20,y=93)
                #self.etiqueta = tk.Label(self.ventana1, textvariable= var).place(x=115,y=93)

                completeName = os.path.join(save_path0, nameFile)

        
                archivo4=open(nameFile+".zlib_000",'wb')
                archivo4.write(imgcode)
                archivo4.close()

                
                archivo5 = open(nameFile+".zlib_000",'rb')
                
                content11 = archivo5.read()

                #print(content1)

                head_paleta= b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x80\x00\x00\x00\x80\x08\x03\x00\x00\x00\xf4\xe0\x91\xf9\x00\x00\x03\x00'
                plte = b'PLTE'

                head_paleta_new=(head_paleta+plte)

                #print(content1)
                paleta_original=(content11[128:1152])
                paleta=(content11[128:1152]).hex()

                nueva_paleta=""
                indice=0
                while indice<len(paleta)-1:
                    nueva_paleta+=paleta[indice:indice+6]
                    indice+=8

                #print(nueva_paleta)
                nueva_paleta_hxd = binascii.unhexlify(nueva_paleta)



                
                with open(nameFile+".plte", "wb") as archivo10:    
                    for i in range(0, 1024, 96):
                        p1= (nueva_paleta_hxd[i:i + 24])
                        p2= (nueva_paleta_hxd[i + 24:i + 48])
                        p3= (nueva_paleta_hxd[i + 48:i + 72])
                        p4= (nueva_paleta_hxd[i + 72:i + 96])

                        one=(p1+p3+p2+p4)
                    
                        archivo10.write(one)         
                        



                end= b'\x00\x00\x01\x00'

                end2 = b'tRNS'

                ff=(b'\xff' * 256)

                texture= (content11[1152:17536]).hex()


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


                newFuncion=("00"+funcion+"00")
                funcion_hxd = binascii.unhexlify(newFuncion)

                funcion_hxd_compress=zlib.compress(funcion_hxd, 9)

                file10=open(nameFile+'.idat','wb')
                file10.write(funcion_hxd)
                file10.close()


                file11=open(nameFile+'_compress.idat','wb')
                file11.write(funcion_hxd_compress)
                file11.close()




                long_trns = zlib.crc32(end2+ff)
                #print(long_trns)
                long_trns_zlib32 = long_trns.to_bytes(4, byteorder='big', signed=False)
                #print(long_trns_zlib32)


                end_ff= b'IDAT'

                long_idat = zlib.crc32(end_ff+funcion_hxd_compress)
                carga_idat = long_idat.to_bytes(4, byteorder='big', signed=False)





                long_texture = len(funcion_hxd_compress)
                carga_texture = long_texture.to_bytes(4, byteorder='big', signed=True)
                #print(carga_texture)


                end_png = b'IEND\xaeB`\x82'

                fend= b'\x00\x00\x00\x00'
                file2=open(nameFile+".plte",'rb')
                palette=file2.read()
                file2.close()
                

                long_paleta = zlib.crc32(plte+palette)
                #print(long_paleta)
                long_paleta_zlib32 = long_paleta.to_bytes(4, byteorder='big', signed=False)
                #print(long_paleta_zlib32)

                file1=open(nameFile+".png",'wb')
                file1.write(head_paleta_new)
                file1.write(palette)
                file1.write(long_paleta_zlib32)
                file1.write(end)
                file1.write(end2)
                file1.write(ff)
                file1.write(long_trns_zlib32)
                file1.write(carga_texture)
                file1.write(end_ff)
                file1.write(funcion_hxd_compress)
                file1.write(carga_idat)
                file1.write(fend)
                file1.write(end_png)
                file1.close()
                

                img = Image.open(nameFile+".png")
                new_img = img.resize((64,128))
                new_img.save(nameFile+"_64.png")



                img = Image.open(nameFile+".png")
                new_img = img.resize((32,64))
                new_img.save(nameFile+"_32.png")


                ###
                file001=open(nameFile+"_64.png",'rb')
                palette001=file001.read()
                file001.close()
                my_data001 = palette001[1089:len(palette001)]
                #print(my_data001)

                decompressed_data001 = zlib.decompress(my_data001)

                file002=open(nameFile+"_64.idat",'wb')
                file002.write(decompressed_data001)
                file002.close()

                file003=open(nameFile+"_64.idat",'rb')
                palette002=file003.read()
                file003.close()
                my_data002 = palette002[1:len(palette002)]
                my_data002_hex= my_data002.hex()


                nueva_idat=""
                indice2=0
                while indice2<len(my_data002_hex)-1:
                    nueva_idat+=my_data002_hex[indice2:indice2+128]
                    indice2+=130
                #print(nueva_paleta2)
                nueva_idat_64x128 = binascii.unhexlify(nueva_idat)
                #print(nueva_paleta2_64x128)





                file01=open(nameFile+"_32.png",'rb')
                palette01=file01.read()
                file01.close()
                
                my_data01 = palette01[1089:len(palette01)]
                #print(my_data001)

                decompressed_data01 = zlib.decompress(my_data01)

                file02=open(nameFile+"_32.idat",'wb')
                file02.write(decompressed_data01)
                file02.close()

                file03=open(nameFile+"_32.idat",'rb')
                palette02=file03.read()
                file03.close()
                my_data02 = palette02[1:len(palette02)]
                my_data02_hex= my_data02.hex()
                #print(my_data02_hex)


                nueva_idat_32=""
                indice2=0
                while indice2<len(my_data02_hex)-1:
                    nueva_idat_32+=my_data02_hex[indice2:indice2+64]
                    indice2+=66
                #print(nueva_paleta2)
                nueva_idat_32x64 = binascii.unhexlify(nueva_idat_32)
                #print(nueva_idat_32x64.hex())



                

                #####
                my_data = (base3d + head_texture_pes6 + paleta_original+ nueva_idat_64x128 + nueva_idat_32x64)

                #print(my_data)

                size_decompress =(len(my_data))
                tes_temp = size_decompress.to_bytes(4, byteorder='little', signed=True)
                #print(tes_temp)

                base3d_textura6_compress = zlib.compress(my_data, 9)

                size_compress=(len(base3d_textura6_compress))
                tes = size_compress.to_bytes(4, byteorder='little', signed=True)

                indic_size=(tes+tes_temp)

                #####

                
 
                archivo5.close()



                completeName1 = os.path.join(completeName+"_new.bin")                
                archivo=open(completeName1,'wb')
                archivo.write(indic0)
                archivo.write(indic_size)
                archivo.write(indic3)
                archivo.write(base3d_textura6_compress)
                MessageBox.showinfo("¡Aviso!", "Face de PES convertida a WE") # título, mensaje
                archivo.close()

                sleep(.1)
                for archivos in os.listdir():
                    if archivos.endswith('.plte'):
                        os.remove(archivos)
                    else:
                        for archivos in os.listdir():
                            if archivos.endswith('.idat'):
                                os.remove(archivos)
                            else:
                                for archivos in os.listdir():
                                    if archivos.endswith('.zlib_000'):
                                        os.remove(archivos)
                                    else:
                                        for archivos in os.listdir():
                                            if archivos.endswith('.png'):
                                                os.remove(archivos)

                                                                    
            else:
                MessageBox.showerror("Error -3 al descomprimir:", "verificación de encabezado incorrecta")
        else:
            print("No selecciono ningun archivo")
            #MessageBox.showwarning("Alerta", "No selecciono ningun archivo")




            
    def faceWe2Pes(self):

        head_texture_pes14=b'\x94r\x85)\x01\x00\x00\x00\x80D\x00\x00\x01\x00\x00\x00\x80\x04\x80\x00\x80\x00\x80\x00\x02\x13\x07\x07\x01\x00\x10\x10\x00\x04\x00\x00@\x00\x00\x00\x80\x00\x80\x00\x02\x13\x03\x10@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
       

        archivo1=askopenfile(title = "Seleccione archivo",mode='rb',filetypes = (("all files","*.*"),
                    ("str files","*.str")))  


        if archivo1 is not None:
            
            #print(file_path)
            content1 = archivo1.read()


            indic0=(content1[0:4])
            
            indic3=(content1[12:32])
            


            my_data = content1[32:len(content1)]

            
            com_data = (my_data[0:2])
            
            

            if (com_data) == (b'x\xda'):


                file_name = (archivo1.name)
                #print(file_name)

                save_path0 = Path(file_name).parent.absolute()

                nameFile=(Path(file_name).resolve().stem)
                #print(nameFile)

                var = StringVar()
                var.set(nameFile)

                decompressed_data = zlib.decompress(my_data)

                posctxs = decompressed_data.find(b'\x94r\x85)\x01')
                #print(posctxs)
                

                imgcode = decompressed_data[posctxs:len(decompressed_data)]
                #print(imgcode)

                completeName = os.path.join(save_path0, nameFile)

                archivo4=open(nameFile+".zlib_000",'wb')
                archivo4.write(imgcode)
                archivo4.close()

                
                base3d=(decompressed_data[0:posctxs])
                #print(base3d)



                #self.etiquetamore = tk.Label(self.ventana1, text="Archivo cargado:").place(x=20,y=93)
                #self.etiqueta = tk.Label(self.ventana1, textvariable= var).place(x=115,y=93)

                completeName = os.path.join(save_path0, nameFile)

        
                archivo4=open(nameFile+".zlib_000",'wb')
                archivo4.write(imgcode)
                archivo4.close()

                
                archivo5 = open(nameFile+".zlib_000",'rb')
                content11 = archivo5.read()
                
                head_paleta= head_paleta= b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00@\x00\x00\x00\x80\x08\x03\x00\x00\x00\x8c_\x9fX\x00\x00\x03\x00'

                plte = b'PLTE'

                head_paleta_new=(head_paleta+plte)

  
                #print(content1)

                paleta_original=(content11[128:1152])
                paleta=(content11[128:1152]).hex()

                nueva_paleta=""
                indice=0
                while indice<len(paleta)-1:
                    nueva_paleta+=paleta[indice:indice+6]
                    indice+=8

                #print(nueva_paleta)
                nueva_paleta_hxd = binascii.unhexlify(nueva_paleta)



                with open(nameFile+".plte", "wb") as archivo_plte:
                    
                    for i in range(0, 1024, 96):
                        p1= (nueva_paleta_hxd[i:i + 24])
                        p2= (nueva_paleta_hxd[i + 24:i + 48])
                        p3= (nueva_paleta_hxd[i + 48:i + 72])
                        p4= (nueva_paleta_hxd[i + 72:i + 96])

                        one=(p1+p3+p2+p4)
                        archivo_plte.write(one)


                end= b'\x00\x00\x01\x00'

                end2 = b'tRNS'

                ff=(b'\xff' * 256)

                texture= (content11[1152:9344]).hex()


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

                funcion = dividirCadena(texture, "00", 128)


                newFuncion=("00"+funcion+"00")
                funcion_hxd = binascii.unhexlify(newFuncion)
                
                funcion_hxd_compress=zlib.compress(funcion_hxd, 7)

                file10=open(nameFile+'.idat','wb')
                file10.write(funcion_hxd)
                file10.close()

                long_trns = zlib.crc32(end2+ff)
                #print(long_trns)
                long_trns_zlib32 = long_trns.to_bytes(4, byteorder='big', signed=False)
                #print(long_trns_zlib32)

                end_ff= b'IDAT'
                long_idat = zlib.crc32(end_ff+funcion_hxd_compress)
                carga_idat = long_idat.to_bytes(4, byteorder='big', signed=False)






                long_texture = len(funcion_hxd_compress)
                carga_texture = long_texture.to_bytes(4, byteorder='big', signed=True)
                #print(carga_texture)


                end_png = b'IEND\xaeB`\x82'
                fend= b'\x00\x00\x00\x00'

                file2=open(nameFile+".plte",'rb')
                palette=file2.read()
                file2.close()

                long_paleta = zlib.crc32(plte+palette)
                #print(long_paleta)
                long_paleta_zlib32 = long_paleta.to_bytes(4, byteorder='big', signed=False)
                #print(long_paleta_zlib32)

                file1=open(nameFile+".png",'wb')
                file1.write(head_paleta_new)
                file1.write(palette)
                file1.write(long_paleta_zlib32)
                file1.write(end)
                file1.write(end2)
                file1.write(ff)
                file1.write(long_trns_zlib32)
                file1.write(carga_texture)
                file1.write(end_ff)
                file1.write(funcion_hxd_compress)
                file1.write(carga_idat)
                file1.write(fend)
                file1.write(end_png)
                file1.close()

                img = Image.open(nameFile+".png")
                new_img = img.resize((128,128))
                new_img.save(nameFile+"_128.png")
                
                img = Image.open(nameFile+".png")
                new_img = img.resize((64,64))
                new_img.save(nameFile+"_64.png")


                ###
                file001=open(nameFile+"_128.png",'rb')
                palette001=file001.read()
                file001.close()
                my_data001 = palette001[1089:len(palette001)]
                #print(my_data001)

                decompressed_data001 = zlib.decompress(my_data001)

                file002=open(nameFile+"_128.idat",'wb')
                file002.write(decompressed_data001)
                file002.close()

                file003=open(nameFile+"_128.idat",'rb')
                palette002=file003.read()
                file003.close()
                my_data002 = palette002[1:len(palette002)]
                my_data002_hex= my_data002.hex()


                nueva_idat=""
                indice2=0
                while indice2<len(my_data002_hex)-1:
                    nueva_idat+=my_data002_hex[indice2:indice2+256]
                    indice2+=258
                #print(nueva_idat)
                nueva_idat_64x128 = binascii.unhexlify(nueva_idat)
                #print(nueva_paleta2_64x128)





                file01=open(nameFile+"_64.png",'rb')
                palette01=file01.read()
                file01.close()
                
                my_data01 = palette01[1089:len(palette01)]
                #print(my_data001)

                decompressed_data01 = zlib.decompress(my_data01)

                file02=open(nameFile+"_64.idat",'wb')
                file02.write(decompressed_data01)
                file02.close()

                file03=open(nameFile+"_64.idat",'rb')
                palette02=file03.read()
                file03.close()
                my_data02 = palette02[1:len(palette02)]
                my_data02_hex= my_data02.hex()
                #print(my_data02_hex)


                nueva_idat_32=""
                indice2=0
                while indice2<len(my_data02_hex)-1:
                    nueva_idat_32+=my_data02_hex[indice2:indice2+128]
                    indice2+=130
                #print(nueva_paleta2)
                nueva_idat_32x64 = binascii.unhexlify(nueva_idat_32)
                #print(nueva_idat_32x64.hex())



                

                #####
                my_data = (base3d + head_texture_pes14 + paleta_original+ nueva_idat_64x128 + nueva_idat_32x64)

                #print(my_data)

                size_decompress =(len(my_data))
                tes_temp = size_decompress.to_bytes(4, byteorder='little', signed=True)
                #print(tes_temp)

                base3d_textura6_compress = zlib.compress(my_data, 9)

                size_compress=(len(base3d_textura6_compress))
                tes = size_compress.to_bytes(4, byteorder='little', signed=True)

                indic_size=(tes+tes_temp)

                #####

                archivo5.close()
                
                completeName1 = os.path.join(completeName+"_new.str")
                
                archivo=open(completeName1,'wb')
                archivo.write(indic0)
                archivo.write(indic_size)
                archivo.write(indic3)
                archivo.write(base3d_textura6_compress)
                MessageBox.showinfo("¡Aviso!", "Face de PES convertida a WE") # título, mensaje
                archivo.close()

                
                sleep(.1)
                for archivos in os.listdir():
                    if archivos.endswith('.plte'):
                        os.remove(archivos)
                    else:
                        for archivos in os.listdir():
                            if archivos.endswith('.idat'):
                                os.remove(archivos)
                            else:
                                for archivos in os.listdir():
                                    if archivos.endswith('.zlib_000'):
                                        os.remove(archivos)
                                    else:
                                        for archivos in os.listdir():
                                            if archivos.endswith('.png'):
                                                os.remove(archivos)
                
                



                                                                    
            else:
                MessageBox.showerror("Error -3 al descomprimir:", "verificación de encabezado incorrecta")
        else:
            print("No selecciono ningun archivo")
            #MessageBox.showwarning("Alerta", "No selecciono ningun archivo")

        
aplicacion1=Aplicacion() 



