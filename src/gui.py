from simulator import *
from tkinter import *
import random

class Menu:

    def __init__(self):
        self.master = Tk()
        self.master.title('Charged Plates Simulator')
        self.master.geometry('225x380')

        l1 = Label(self.master, text='Potential Difference (V)')
        l1.pack()
        self.PD = Entry(self.master)
        self.PD.insert(0,1000)
        self.PD.pack()

        l2 = Label(self.master, text='Distance between plates (m)')
        l2.pack()
        self.spacing = Entry(self.master)
        self.spacing.insert(0,0.1)
        self.spacing.pack()

        l3 = Label(self.master, text='Length of Plates (m)')
        l3.pack()
        self.length = Entry(self.master)
        self.length.insert(0,1)
        self.length.pack()

        l4 = Label(self.master, text='Particle Mass')
        l4.pack()
        self.mass = Entry(self.master)
        self.mass.insert(0,'1.67 * 10^-27')
        self.mass.pack()

        l5 = Label(self.master, text='Particle Charge (C)')
        l5.pack()
        self.charge = Entry(self.master)
        self.charge.insert(0,'1.6 * 10^-19')
        self.charge.pack()

        l6 = Label(self.master, text='Horizontal Velocity (m/s)')
        l6.pack()
        self.velocity = Entry(self.master)
        self.velocity.insert(0,'1.1 * 10^7')
        self.velocity.pack()


        b = Button(self.master, text='Simulate', command = lambda : self.setupSimulation())
        b.pack()
   

    def setupSimulation(self):
        particle = Particle(eval(self.mass.get().replace('^', "**")), eval(self.charge.get().replace('^', "**")), eval(self.velocity.get().replace('^', "**")), 0, -250)
        environment = Simulation(Toplevel(), self.PD.get(), self.spacing.get(), self.length.get(), particle)


