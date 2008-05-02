import simulator
from Tkinter import *
import time

scale = 5

def display():
    sim = simulator.Simulator()
    
    for i in range(0,200):
        time.sleep(0.5)
        canvas.create_rectangle(0, 0, 1000, 500, fill='white')
        carsAndSpeeds = sim.tick()
        positions = carsAndSpeeds[0]
        speeds = carsAndSpeeds[1]
        
        for speedPos in speeds:
            canvas.create_rectangle(speedPos*scale, 15, (speedPos*scale)+scale, 25, fill='red')
        
        for carPos in positions:
            canvas.create_rectangle(carPos*scale, 20, (carPos*scale)+scale, 20+scale)
        
               
        canvas.update()
 
frame = Frame()
frame.pack()
 
canvas = Canvas(frame, bg='white', width=1000, height=500)
canvas.pack()
 
button = Button(frame, fg="blue", text="GENERATE", command=display)
button.pack()
 
frame.mainloop()
