from tkinter import *
def changeColor():
    if btnCalculate["fg"] =="blue":
        btnCalculate["fg"] ="red"
        btnCalculate["bg"] ="yellow"
        btnCalculate["fg"] ="blue"
        btnCalculate["bg"] ="light green"
window = Tk()
window.title("Button Colors")
btnCalculate = Button(window,text = "Calculater",
fg ="blue", command=changeColor)
btnCalculate.grid(padx = 100, pady = 15)
window.mainloop()

        
