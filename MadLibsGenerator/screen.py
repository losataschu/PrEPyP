# importar librería
from tkinter import *

# esta función crea la ventana final, con la historia incluida
def final(resultado: Toplevel, nombre, juego, ciudad, tema, comida, otro_nombre):
 
  text = f'''
       Un día, mi amigo {nombre} y yo quisimos jugar {juego} en {ciudad}.
       Terminamos sentados, conversando sobre {tema}.
       Luego comimos {comida} y fuimos a visitar a {otro_nombre}. 
       A pesar de fracasar con nuestro plan original, ¡lo pasamos muy bien! '''
 
  resultado.geometry(newGeometry='500x550')
 
  Label(resultado, text='Historia resultante:', wraplength=resultado.winfo_width()).place(x=160, y=310)
  Label(resultado, text=text, wraplength=resultado.winfo_width()).place(x=0, y=330)

# crear función para la primera historia
def Historia1(win):
 
  NewScreen = Toplevel(win, bg='cornsilk1')
  NewScreen.title("Un día en el parque")
  NewScreen.geometry('500x500')
# crear ventanas con mensaje informativo para el texto a ingresar
  Label(NewScreen, text='Día del recuerdo').place(x=100, y=0)
  Label(NewScreen, text='Nombre:').place(x=0, y=35)
  Label(NewScreen, text='Juego:').place(x=0, y=70)
  Label(NewScreen, text='Ciudad:').place(x=0, y=110)
  Label(NewScreen, text='Temática:').place(x=0, y=150)
  Label(NewScreen, text='Comida:').place(x=0, y=190)
  Label(NewScreen, text='Nombre de un/a amigo/a:').place(x=0, y=230)
# crear las ventanas para ingresar texto
  nombre = Entry(NewScreen, width=17)
  nombre.place(x=250, y=35)
  juego = Entry(NewScreen, width=17)
  juego.place(x=250, y=70)
  ciudad = Entry(NewScreen, width=17)
  ciudad.place(x=250, y=105)
  tema = Entry(NewScreen, width=17)
  tema.place(x=250, y=150)
  comida = Entry(NewScreen, width=17)
  comida.place(x=250, y=190)
  nombre2 = Entry(NewScreen, width=17)
  nombre2.place(x=250, y=220)
# crear botón que arma la historia con el texto ingresado. Usa la función 'final' definida anteriormente
  SubmitButton = Button(NewScreen, text="Enviar", background="darkgoldenrod", font=('Times', 12), command=lambda:final(NewScreen, nombre.get(), juego.get(), ciudad.get(), tema.get(), comida.get(), nombre2.get()))
  SubmitButton.place(x=250, y=270)
 
  NewScreen.mainloop()

# crear ventana
Ventana = Tk()
# crear título
Ventana.title("PythonGeeks Mad Libs Generator")
Ventana.geometry('400x400')
Ventana.config(bg="bisque1")
Label(Ventana, text='PythonGeeks Mad Libs Generator', font=("Roboto")).place(x=100, y=20)
# crear botones
botonHistoria1 = Button(Ventana, text='Un día en el parque', font=("Lato", 13),command=lambda: Historia1(Ventana), bg='cadetblue1')
botonHistoria1.place(x=130, y=90)

Ventana.update()
Ventana.mainloop()
