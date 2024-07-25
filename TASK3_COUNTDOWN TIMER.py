from tkinter import *
from playsound import playsound
import time

root = Tk()
root.title("COUNTDOWN TIMER")
root.geometry("600x600")
root.config(bg="#000")
root.resizable(False, False)

# Function to update the clock
def update_clock():
    current_time.config(text=time.strftime('%H:%M:%S %p'))
    current_time.after(1000, update_clock)

# Clock
Label(root, font=("TimesNewRoman", 20, "bold"), text="CURRENT TIME:", bg="papaya whip").place(x=150, y=70)
current_time = Label(root, font=("TimesNewRoman", 20, "bold"), text="", fg="#000", bg="#fff")
current_time.place(x=370, y=70)
update_clock()

# Timer
hrs = StringVar()
Entry(root, textvariable=hrs, width=2, font="TimesNewRoman 30", bg="#000", fg="#fff", bd=0).place(x=180, y=150)
hrs.set("00")
mins = StringVar()
Entry(root, textvariable=mins, width=2, font="TimesNewRoman 30", bg="#000", fg="#fff", bd=0).place(x=280, y=150)
mins.set("00")
sec = StringVar()
Entry(root, textvariable=sec, width=2, font="TimesNewRoman 30", bg="#000", fg="#fff", bd=0).place(x=380, y=150)
sec.set("00")

Label(root, text="hours", font="TimesNewRoman 12", bg="#000", fg="#fff").place(x=230, y=200)
Label(root, text="mins", font="TimesNewRoman 12", bg="#000", fg="#fff").place(x=330, y=200)
Label(root, text="secs", font="TimesNewRoman 12", bg="#000", fg="#fff").place(x=430, y=200)

# Function to start the timer countdown
def start_timer():
    # Disable the START button while countdown is active
    button.config(state=DISABLED)
    
    # Get total time in seconds
    total_seconds = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
    
    def countdown():
        nonlocal total_seconds
        if total_seconds > 0:
            # Calculate hours, minutes, seconds
            hours = total_seconds // 3600
            minutes = (total_seconds % 3600) // 60
            seconds = total_seconds % 60
            
            # Update the timer display
            hrs.set(f"{hours:02d}")
            mins.set(f"{minutes:02d}")
            sec.set(f"{seconds:02d}")
            
            # Update total_seconds and schedule the next update
            total_seconds -= 1
            root.after(1000, countdown)  # Schedule the countdown function again after 1 second
        else:
            # When countdown is over, enable the START button
            button.config(state=NORMAL)
            # Optionally, play a sound here
            playsound("timer.mp3")
    
    countdown()

# Functions to set preset times
def brush():
    hrs.set("00")
    mins.set("02")
    sec.set("00")

def face():
    hrs.set("00")
    mins.set("15")
    sec.set("00")

def eggs():
    hrs.set("00")
    mins.set("10")
    sec.set("00")

# START button
button = Button(root, text="START", font="TimesNewRoman 10 bold", bd=0, bg="#ea3548", fg="#fff", width=20, height=3, command=start_timer)
button.pack(padx=5, pady=40, side=BOTTOM)

# Buttons for preset times
Image1 = PhotoImage(file="brush.png")
button1 = Button(root, image=Image1, bg="#000", bd=0, command=brush)
button1.place(x=50, y=300)

Image2 = PhotoImage(file="face.png")
button2 = Button(root, image=Image2, bg="#000", bd=0, command=face)
button2.place(x=250, y=300)

Image3 = PhotoImage(file="eggs.png")
button3 = Button(root, image=Image3, bg="#000", bd=0, command=eggs)
button3.place(x=450, y=300)

root.mainloop()
