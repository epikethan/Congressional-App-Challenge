import time
import tkinter as tk
from tkinter import Entry, messagebox
from pygame import mixer

host_path = r"C:\Windows\System32\drivers\etc\hosts"
ip_address = '72.193.127.160'
website_list = ["youtube.com"]
root = tk.Tk()

mixer.init()
mixer.music.load(r"C:\Users\ethan\OneDrive\Desktop\Ethan's Congressional App Challenge\alarm_beep-clock-165474.mp3"
)
mixer.music.set_volume(2.5)

root.wm_title("Window")
root.geometry("500x500")

hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()

hour.set("00")
minute.set("00")
second.set("00")
# title in window
Welcome = tk.Label(root,text="Welcome to your Personal Work Timer",font=("Times", 20))
Welcome.pack()
# boxes for hour, minute, seconds
hourEntry = Entry(root,width=3,font=("Times", 30, ""),bd='5',textvariable=hour)
hourEntry.place(x=140, y=175)

minuteEntry = Entry(root,width=3,font=("Times", 30, ""),bd='5',textvariable=minute)
minuteEntry.place(x=220, y=175)

secondEntry = Entry(root,width=3,font=("Times", 30, ""),bd='5',textvariable=second)
secondEntry.place(x=300, y=175)


def submit():
  try:
    temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
  except:
    print("Please input the right value")
  while temp > -1:
    mins, secs = divmod(temp, 60)
    # Converting the input entered in mins or secs to hours,
    # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
    # 50min: 0sec)
    hours = 0
    if mins > 60:
      # divmod(firstvalue = temp//60, secondvalue
      # = temp%60)
      hours, mins = divmod(mins, 60)
    # using format () method to store the value up to
    # two decimal places
    hour.set("{0:2d}".format(hours))
    minute.set("{0:2d}".format(mins))
    second.set("{0:2d}".format(secs))
    # updating the GUI window after decrementing the temp value every time
    root.update()
    # blocking the actual website
    with open(host_path, "r+") as file:
      content = file.read()
      for website in website_list:
        if website in content:
          pass
        else:
          file.write(ip_address + " " + website + "\n")
    file.close()

    time.sleep(1)
    # when temp value = 0; then a messagebox pop's up
    # with a message:"Time's up"
    
    changes = None
    thing_to_remove = None

    if (temp == 0):
        mixer.music.play()
        messagebox.showinfo("Time Countdown", "Time's up ")
        with open(host_path, "r+") as file:
            filedata = file.read()
            file.close()
            for website in website_list:
              thing_to_remove = (ip_address + " " + website)
              text_to_replace = ("---------------------------------------------")
              changes = filedata.replace(thing_to_remove, text_to_replace)
              with open(host_path, "r+") as file:
                file.write(changes)
                file.close()
        print(changes)
    temp -= 1

#start timer button
StartTimer = tk.Button(root,text="Start Timer",font=("Times", 20),bd='5',command=submit)
StartTimer.place(x=180, y=325)

root.mainloop()
