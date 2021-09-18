#importamos librerias
from tkinter import Label, Tk, Widget, font
from time import strftime
from typing import Text

#inicio de la ventana
ventana = Tk()
ventana.title("HORA") #titulo de la ventana
ventana.config(bg='white') #color de fondo
ventana.geometry('800x350+10+10') #tamaño de la ventana
ventana.minsize(width=250, height=200)  # width'ancho', height'altura': definos el ancho y la altura de la ventana
 
ventana.columnconfigure(0, weight=15)
ventana.rowconfigure(0, weight=15)

ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)

def tiempo():
    hora = strftime('%H:%M:%S')
    dia = strftime('%A')
    fecha = strftime('%d-%m-%y')

    x = texto_hora.winfo_height()
    t = int((x-5)*0.32)

    if dia == 'Monday':
        dia = 'Lunes'

    elif dia == 'Tuesday':
        dia = 'Martes'

    elif dia == 'Wednesday':
        dia = 'Miercoles'

    elif dia == 'Thursday':
        dia = 'Jueves'

    elif dia == 'Friday':
        dia = 'Viernes'

    elif dia == 'Saturday':
        dia = 'Sabado'

    elif dia == 'Sunday':
        dia = 'Domingo'

    #donde dice 'font' significa los tipos de letras que vasa usar y que este instalado  en el sistema
    texto_hora.config(text=hora, font= ('The Impostor', t))
    texto_dia.config(text=dia)
    texto_fecha.config(text=fecha)

    texto_hora.after(1000, tiempo)

texto_hora = Label(ventana, fg = 'red', bg='black')
texto_hora.grid(row=0, sticky="nsew", ipadx=5, ipady=20)

texto_dia = Label(ventana,fg= 'green2', bg='gray2', font=('The Impostor',20))
texto_dia.grid(row=1, sticky="nsew")

texto_fecha = Label(ventana,fg= 'green2', bg='gray3', font=('The Impostor',20, 'bold'))
texto_fecha.grid(row=2, sticky="nsew")

tiempo()

ventana.mainloop() #obligatorio para ejecutar