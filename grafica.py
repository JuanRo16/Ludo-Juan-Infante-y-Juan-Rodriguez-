def graficar():
  
  from tkinter import *  
  from tkinter import messagebox
  import sys
  import os
  import random
  import tkinter.messagebox

  root = Tk()

  root.resizable(width=False, height=False)
  root.geometry('1000x750')
  root.configure(background='negro')

  casilla_blanca = PhotoImage(file=".gif")      
  base_roja = PhotoImage(file=".gif")     
  base_azul = PhotoImage(file=".gif")         
  base_verde = PhotoImage(file=".gif")
  base_amarilla = PhotoImage(file=".gif")
  seguro = PhotoImage(file=".gif")
  meta = PhotoImage(file=".gif")
  casilla_roja = PhotoImage(file=".gif")
  casilla_verde = PhotoImage(file=".gif")
  casilla_azul = PhotoImage(file=".gif")
  casilla_amarilla = PhotoImage(file=".gif")

  Label(image = base_roja, width=298, height=298).place(x=-1, y=-1)               
  Label(image = base_azul, width=300, height=300).place(x=(-2), y=(448))
  Label(image = base_verde, width=296, height=296).place(x=(450), y=(0))
  Label(image = base_amarilla, width=294, height=294).place(x=(450), y=(450))
  Label(image = meta, width=150, height=150).place(x=(298), y=(298))
