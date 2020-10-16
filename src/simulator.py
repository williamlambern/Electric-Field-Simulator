from tkinter import *
import math

class Simulation:
    def __init__(self, master, pd, spacing, length, particle):

        self.master = master
        self.w = Canvas(master, width=500, height=300)
        self.w.pack()
        height = 5
        width = 7

        self.pd = float(pd)
        self.spacing = float(spacing)
        self.length = float(length)
        self.particle = particle

        # Initial Graphics
        self.w.create_line(100, 100, 400, 100)
        self.w.create_line(100, 200, 400, 200)
        self.w.create_text(100,80,text="{} V".format(self.pd))
        self.w.create_text(100,220,text="0 V".format(self.pd))
        self.w.create_text(380,80,text="L = {}m".format(self.length))
        self.w.create_text(380,220,text="x = {}m".format(self.spacing))
        self.w.create_text(200,280,text="PARTICLE DATA: Mass = {}kg , Charge = {}C, Initial X Velocity = {}m/s".format(self.round_sig(self.particle.mass), self.round_sig(self.particle.charge), self.round_sig(self.particle.velocity)))
        self.w.create_oval(45, 145, 55, 155, fill='blue')
        self.w.create_line(55, 150, 100, 150, fill='blue')

        # Constant
        self.force = (self.pd/self.spacing)*(self.particle.charge)
        if self.particle.charge > 0:
            self.particle.acceleration = abs(self.force / self.particle.mass)
        else:
            self.particle.acceleration = -1 * abs(self.force / self.particle.mass)

        self.simulate()

    def simulate(self):
        t = self.length / self.particle.velocity
        t_y = ((self.spacing)/abs(self.particle.acceleration))**0.5
        if float(t_y) > float(t):
            vx = self.particle.acceleration * t
            theta = math.tan(vx/self.particle.velocity)
            theta = math.degrees(theta)
            self.w.create_text(400, 180, fill='blue', text='Angle leaving plates: {}°'.format(self.round_sig(theta)))
        else:
            d_y = self.particle.velocity * t_y

        # Line Plotting
        per_y = (self.spacing/2)/50
        per_x = (self.length)/300
        v_y = 0
        polygon = [100,150]
        pos = [100,150]
        collided = False
        for i in range(100):
            v_y += (self.particle.acceleration) * (t/100)
            change_in_y = v_y * t/100
            change_in_y_pixels = change_in_y / per_y
            pos[1] += change_in_y_pixels
            change_in_x = self.particle.velocity * t/100
            change_in_x_pixels = change_in_x / per_x
            pos[0] += change_in_x_pixels    
            if pos[1] > 200 or pos[1] < 100:
                self.w.create_text(int(pos[0])+50, 150, fill='blue', text='Collision at {}m'.format(self.round_sig((pos[0] - 100)*per_x)))
                if pos[1] > 200:
                    polygon.append(pos[0]) ; polygon.append(200)
                else:
                    polygon.append(pos[0]) ; polygon.append(100)
                break
            else:
                polygon.append(pos[0]) ; polygon.append(pos[1])
        self.w.create_line(polygon, smooth='true')
           

    def move(self):
        pass

    def round_sig(self, x, sig=2):
        return round(x, sig-int(math.floor(math.log10(abs(x))))-1)


class Particle:
    def __init__(self, mass, charge, vel, x, y):
        self.mass = float(mass)
        self.charge = float(charge) 
        self.velocity = float(vel)
        self.x , self.y = float(x),float(y)
        

