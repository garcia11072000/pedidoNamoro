from tkinter import *
from tkinter import messagebox
import random


def sim():
    messagebox.showinfo(' ', 'Te amo meu amor, pago um lanche mais tarde!')
    quit()


def motionMouse(event):
    btnNao.place(x=random.randint(0, 500), y=random.randint(0, 500))


root = Tk()
root.title('Pedido de Namoro')
root.geometry('600x600')
root.resizable(width=False, height=False)
root['bg'] = 'white'
root.configure(background='#ffc8dd')

label = Label(root, text='Aceita a namorar comigo?',
              font='Arial 20 bold', bg='white').pack()
btnNao = Button(root, text='Não', font='Arial 20 bold')
btnNao.place(x=170, y=100)
btnNao.bind('<Enter>', motionMouse)
btnSim = Button(root, text='Sim', font='Arial 20 bold',
                command=sim).place(x=350, y=100)

root.mainloop()
