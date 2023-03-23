from logging import root
from tkinter import *
import tkinter as tk
from tkinter import ttk
from turtle import width

ventana= tk.Tk()
ventana.title("DIVISAS")
ventana.geometry("400x200")
ventana.minsize(width=430,height=200)
ventana.configure(bg="blue")

Aa= StringVar()
Bb= StringVar()

def trueque():
    global Bb,Aa

    if Mon_entrada.get()=="MXN" and Mon_cambia.get()=="DOLAR":
        Bb.set(float(Aa.get())*0.054)

    if Mon_entrada.get()=="MXN" and Mon_cambia.get()=="EURO":
        Bb.set(float(Aa.get())*0.047)

    if Mon_entrada.get()=="DOLAR" and Mon_cambia.get()=="MXN":
        Bb.set(float(Aa.get())*18.62)
    
    if Mon_entrada.get()=="DOLAR" and Mon_cambia.get()=="EURO":
        Bb.set(float(Aa.get())*0.97)

    if Mon_entrada.get()=="EURO" and Mon_cambia.get()=="MXN":
        Bb.set(float(Aa.get())*19.96)

    if Mon_entrada.get()=="EURO" and Mon_cambia.get()=="DOLAR":
        Bb.set(float(Aa.get())*1.03)
    


MonA= Label(ventana,text="Cantidad:",bg="#42AB49",font=("Roboto",10)).grid(row=11,column=5)
Maaa= Entry(ventana,textvariable=Aa).grid(row=15,column=5)

res= Label(ventana,text="Cambio:",font=("Roboto",10)).grid(row=18,column=5)
resB= Entry(ventana,textvariable=Bb,font=("Roboto",10)).grid(row=22,column=5)


tumon= Label(ventana,text="Tu moneda:",font=("Roboto",10)).grid(row=24,column=1)
Mon_entrada= tk.StringVar()
desplegable_entrada= ttk.Combobox(ventana,font=("Roboto",10),width=17,
                                  values=["MXN","DOLAR","EURO"],
                                  state="readonly",textvariable=Mon_entrada)
desplegable_entrada.grid(row=25,column=1)
desplegable_entrada.set("MXN")

moncam= Label(ventana,text="Moneda a cambiar:",font=("Roboto",10)).grid(row=24,column=9)
Mon_cambia= tk.StringVar()
desplegable_cambia= ttk.Combobox(ventana,font=("Roboto",10),width=17,
                                  values=["MXN","DOLAR","EURO"],
                                  state="readonly",textvariable=Mon_cambia)
desplegable_cambia.grid(row=25,column=9)
desplegable_entrada.set("MXN")

boton1= Button(ventana,text="Cambiar",command=trueque).grid(row=50,column=5)


ventana.mainloop()