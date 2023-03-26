## Koine Greek Flash Cards 1.0.0 Copyright (C) 2018-2023 Noah Rahm
##
## This program is free software: you can redistribute it and/or modify it 
## under the terms of the GNU General Public License as published by 
## the Free Software Foundation; either version 3 of the License, 
## or (at your option) any later version.
##
## This program is distributed in the hope that it will be useful, 
## but WITHOUT ANY WARRANTY; without even the implied warranty 
## of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
##  
## See the GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License 
## along with this program. If not, see: http://www.gnu.org/licenses/

#!python3
import os
import random
from collections import *
from tkinter import *
from tkinter.constants import *
from tkinter import ttk, messagebox


class Main(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Koine Greek Alphabet - v1.0')
        self.wm_iconbitmap('images\\Icon.ico')
        self.geometry('400x330')
        self.resizable(width=False, height=False)

        ## Build the GUI
        GUI = self.Build_GUI()

        ## Binding for about dialog
        self.bind("<Button-3>", lambda event: self.About_Program())


    def About_Program(self):
        messagebox.showinfo('About Program', '''
        Koine Greek Alphabet Flash Cards v1.0.0

        By the grace of Yahweh, our Heavenly Father, developed by: Noah Rahm, 2018

        This program is licensed under the GNU General Public License
        which can be found at: http://www.gnu.org/licenses/
        ''')

        
    def Build_GUI(self):
        CanvasFrame = Frame(self, relief=GROOVE, bd=2)
        CanvasFrame.pack(padx=4, pady=4, fill=BOTH)

        canvas = Canvas(CanvasFrame, width=200, height=200, bg='white')
        canvas.pack(padx=4, pady=4)

        self.CurrentCard_Label = Label(CanvasFrame, text="    ")
        self.CurrentCard_Label.pack(padx=4, pady=4)

        NextCard_Button = ttk.Button(self, text='<Next>', command=lambda: self.Show_Cards(canvas))
        NextCard_Button.pack(padx=4, pady=4)

        self.var = IntVar()
        self.ShowLabelCheckBox = ttk.Checkbutton(self, text='Show Letter Names', variable=self.var)
        self.ShowLabelCheckBox.pack(padx=8, pady=8)


    def Get_Card(self):
        Value = random.randrange(22)
        Var = self.var.get()

        ## Reset label
        self.CurrentCard_Label.configure(text="    ") 

        ## Get Card
        if Value == 0:
            self.Current_Card = PhotoImage(file='images\\Alpha.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Alpha") 

        if Value == 1:
            self.Current_Card = PhotoImage(file='images\\Beta.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Beta") 

        if Value == 2:
            self.Current_Card = PhotoImage(file='images\\Gamma.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Gamma") 

        if Value == 3:
            self.Current_Card = PhotoImage(file='images\\Delta.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Delta")

        if Value == 4:
            self.Current_Card = PhotoImage(file='images\\Epsilon.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Epsilon")

        if Value == 5:
            self.Current_Card = PhotoImage(file='images\\Zeta.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Zeta")

        if Value == 6:
            self.Current_Card = PhotoImage(file='images\\Eta.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Eta")

        if Value == 7:
            self.Current_Card = PhotoImage(file='images\\Theta.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Theta")

        if Value == 8:
            self.Current_Card = PhotoImage(file='images\\Iota.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Iota")

        if Value == 9:
            self.Current_Card = PhotoImage(file='images\\Kappa.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Kappa")

        if Value == 10:
            self.Current_Card = PhotoImage(file='images\\Lambda.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Lambda")

        if Value == 11:
            self.Current_Card = PhotoImage(file='images\\Mu.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Mu")

        if Value == 12:
            self.Current_Card = PhotoImage(file='images\\Nu.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Nu")

        if Value == 13:
            self.Current_Card = PhotoImage(file='images\\Xi.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Xi")

        if Value == 14:
            self.Current_Card = PhotoImage(file='images\\Omicron.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Omicron")

        if Value == 15:
            self.Current_Card = PhotoImage(file='images\\Pi.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Pi")

        if Value == 16:
            self.Current_Card = PhotoImage(file='images\\Rho.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Rho")

        if Value == 17:
            self.Current_Card = PhotoImage(file='images\\Sigma.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Sigma")

        if Value == 18:
            self.Current_Card = PhotoImage(file='images\\Tau.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Tau")

        if Value == 19:
            self.Current_Card = PhotoImage(file='images\\Upsilon.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Upsilon")

        if Value == 19:
            self.Current_Card = PhotoImage(file='images\\Phi.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Phi")

        if Value == 20:
            self.Current_Card = PhotoImage(file='images\\Chi.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Chi")

        if Value == 21:
            self.Current_Card = PhotoImage(file='images\\Psi.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Psi")

        if Value == 22:
            self.Current_Card = PhotoImage(file='images\\Omega.png')
            if Var == 1:
                self.CurrentCard_Label.configure(text="Omega")

        
    def Show_Cards(self, canvas):
        self.Get_Card()
        canvas.create_image(0, 0, image=self.Current_Card, anchor=NW)



if __name__ == '__main__':
    App = Main()
    App.mainloop()
