import tkinter as tk
import random
 
def setY(event):
    global Gravity
    Gravity = -6

def move_window():
    global y,Gravity,pipe_x,rand_pos
    pipe_x -=2  
    Gravity += 0.2
    bx,by = root.winfo_x(),root.winfo_y()
    p1x= pipe1.winfo_x()
    y = int(y + Gravity)
    if y > 900: 
        root.destroy()
        pipe1.destroy()
        pipe2.destroy()
    elif p1x + 100 > 200 and p1x < 400 and (by < rand_pos or by+100 > rand_pos+300):
        root.destroy()
        pipe1.destroy()
        pipe2.destroy()
    if p1x < 0:
        rand_pos = random.randint(100,550)
        pipe_x = 650
        pipe1.geometry(f"{100}x{rand_pos}+{pipe_x}+0")
        pipe2.geometry(f"{100}x{500}+{pipe_x}+{rand_pos+300}")
    pipe1.geometry(f"{100}x{rand_pos}+{pipe_x}+0")
    pipe2.geometry(f"{100}x{500}+{pipe_x}+{rand_pos+300}")
    root.bind("<space >",setY)
    root.geometry(f"{window_width}x{window_height}+{200}+{y}")
    root.after(10, move_window)

pipe_x = 650
rand_pos = random.randint(100,550)
pipe1 = tk.Tk()
pipe2 = tk.Tk()
pipe1.configure(bg="green")
pipe2.configure(bg="green")



#Don't touch this code
root = tk.Tk()
root.title("BIRD")
root.geometry("200x100")
root.configure(bg="orange")
label = tk.Label(root, text="It's a BIRD", font=("Arial", 16))
label.pack(pady=20)
root.geometry(f"+{600}+{400}")
y = 0
Gravity = 1
window_width = 200
window_height = 150


move_window()

root.mainloop()
