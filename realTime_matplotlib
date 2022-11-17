import serial
import random
import time
import threading
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from tkinter import Tk, Canvas


class realTimePlot():

    def __init__(self, master):
        self.master = master
        
        self.data = []

        fig = Figure(figsize=(8,10))
        self.plot = fig.add_subplot(111)
        self.plot.set_title('Title')
        self.plot.set_ylabel('Y Label')
        self.plot.set_xlabel('X Label')
        self.plot.set_ylim(0, 100)
        self.line, = self.plot.plot([], [], 'c', marker='o')

        self.plotCanvas = FigureCanvasTkAgg(fig, master=self.master)
        self.plotCanvas.get_tk_widget().pack()

        # anim = FuncAnimation(fig, self.update_graph, interval=2000)
        # plotCanvas.draw()

    def update_graph(self):
        self.line.set_data(range(len(self.data)), self.data)
        self.plot.set_xlim(0, len(self.data))

        self.plotCanvas.draw()

        

    def set(self, newValue):
        self.data.append(newValue)

    
    
def serialUpdater():

    # Initialize Serial Comms
    ser = serial.Serial(
        port='COM5', 
        baudrate=115200, 
        timeout=1
    )

    # Declare real time plot object
    # graph = realTimePlot(window)


    while True:
        # Inside this loop you will read from serial port and update variables as new data is recieved
        rx_data = ser.readline().decode('ascii')
        print(rx_data)

        # potentialnow = random.randint(0,100) #this will be replaced by reading the actual value from the ESP8266
        # powernow = random.randint(0,100)
        # percentUnused = random.randint(0,100)
        # date = random.randint(0,100)

        # global timenow
        # global t_values
        # global p_values
        # global pplot
        # global plotcanvas

        # timenow = timenow + 1
        # t_values.append(timenow)
        # p_values.append(powernow)

        # new_data = random.randint(1, 100)

        # graph.set(new_data)
        # graph.update_graph()

        # canvas.itemconfigure(dateText, text=f"{date}")
        # canvas.itemconfigure(timenowText, text=f"{timenow}")
        # canvas.itemconfigure(potentialNowText, text=f"{potentialnow} mW")
        # canvas.itemconfigure(powernowText, text=f"{powernow} mW")
        # canvas.itemconfigure(percentunusedText, text=f"{percentUnused}%")
        # canvas.itemconfigure(plotcanvas, t_values = t_values, p_values = p_values)
    



def updatevalues():

    graph = realTimePlot(window)

    while True:
        new_data = random.randint(1, 100)

        graph.set(new_data)
        graph.update_graph()

        time.sleep(1)


if __name__=='__main__':

    window = Tk()
    window.geometry("1200x800")

    canvas = Canvas(
        window,
        bg = "#FFFFFF",
        height = 800,
        width = 1200,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.place(x = 0, y = 0)

    # Run background Thread to update values
    updateThread = threading.Thread(target=updatevalues, name='Update Thread', daemon=True)
    updateThread.start()

    # Run main tkinter window
    window.mainloop()
