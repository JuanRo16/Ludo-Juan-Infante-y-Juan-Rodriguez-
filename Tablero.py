from graficar import *

def tablero():                           

    tkinter.messagebox.showinfo(title=None, message="Inicie el juego undiendo cualquier tecla")
    v = 0
    z = 0

    while (v != 300):           
        z = 0
        while (z != 150):
            Label(image=casilla_blanca, width=46, height=46).place(x=(300 + z), y=(0 + v))
            z = z + 50
        v = v + 50

    z = 0
    v = 0
    while (v != 300):          
        z = 0
        while (z != 150):
            Label(image=casilla_blanca, width=46, height=46).place(x=(0 + v), y=(300 + z))
            z = z + 50
        v = v + 50

    v = 0
    z = 0

    while (v != 300):         
        z = 0
        while (z != 150):
            Label(image=casilla_blanca, width=46, height=46).place(x=(300 + z), y=(450 + v))
            z = z + 50
        v = v + 50

    z = 0
    v = 0
    while (v != 300):         
        z = 0
        while (z != 150):
            Label(image=casilla_blanca, width=46, height=46).place(x=(450 + v), y=(300 + z))
            z = z + 50
        v = v + 50

    v = 0
    while (v != 250):     
        Label(image=base_verde, width=46, height=46).place(x=(350), y=(50 + v))
        v = v + 50

    Label(image=base_verde, width=46, height=46).place(x=(300), y=(100))
    Label(image=seguro, width=46, height=46).place(x=(400), y=(50))

    v = 0
    while (v != 250):     
        Label(image=base_amarilla, width=46, height=46).place(x=(450 + v), y=(350))
        v = v + 50

    Label(image=base_amarilla, width=46, height=46).place(x=(600), y=(300))
    Label(image=seguro, width=46, height=46).place(x=(650), y=(400))

    v = 0
    while (v != 250):   
        Label(image=base_azul, width=46, height=46).place(x=(50 + v), y=(350))
        v = v + 50

    Label(image=base_azul, width=46, height=46).place(x=(100), y=(400))
    Label(image=seguro, width=46, height=46).place(x=(50), y=(300))

    v = 0
    while (v != 250):    #Drawing Blue Boxes
        Label(image=base_roja, width=46, height=46).place(x=(350), y=(450 + v))
        v = v + 50

    Label(image=base_roja, width=46, height=46).place(x=(300), y=(650))
    Label(image=seguro, width=46, height=46).place(x=(400), y=(600))
