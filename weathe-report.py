from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
from PIL import Image, ImageTk
import requests
import pytz

root=Tk()
root.title("weatherReport")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
 try:  
    city=textfield.get()
    
    geolocator= Nominatim(user_agent="geopiExercise")
    Location= geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=Location.longitude, lat=Location.latitude)
    #print(result)
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")
    
    #weather
    
    api="https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=aa9e280969a34b796e0a558b8e061711"
    
    json_data  = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    
    t.config(text=(temp,"°"))
    c.config(text=(condition, "|", "LIKE", temp, "°"))
    
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)
 except Exception as e:
     messagebox.showerror("Weather App", "Invalid Entry!!") 
    
    

 
#Search box

Search_image=PhotoImage(file="./searchbar2.png")
myimage=Label(image=Search_image)
myimage.place(x=-3,y=-430)

textfield=Entry(root,justify="center", width=17, font=("georgia", 15, "bold"), bg="#ffffff", border=0, fg="black")
textfield.place(x=50, y=40)
textfield.focus()

#search_icon=PhotoImage(file="./find.png")
original_image = Image.open("./find.png")  # Load the image
resized_image = original_image.resize((30, 30))  # Resize to 50x50 pixels
search_icon = ImageTk.PhotoImage(resized_image)

myimage_icon=Button(image=search_icon, borderwidth=0, cursor="hand2", command=getWeather)
myimage_icon.place(x=350, y=40)

#logo
original_image = Image.open("./logo1.png")  # Load the image
resized_image = original_image.resize((300, 200))  # Resize to 50x50 pixels
logo_image = ImageTk.PhotoImage(resized_image)

#logo_image=PhotoImage(file="logo1.png")
logo=Label(image=logo_image)
logo.place(x=500,y=20)

#Bottom Box

Frame_image=PhotoImage(file="./box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=0,side=BOTTOM)


#time

name=Label(root, font=("georgia", 10, "bold"))
name.place(x=30,y=100)
clock=Label(root, font=("georgia", 15))
clock.place(x=30,y=130)



#label

label1=Label(root, text="WIND", font=("georgia", 12, "bold"), fg="white", bg="#5080ff")
label1.place(x=190,y=270)

label2=Label(root, text="HUMIDITY", font=("georgia", 12, "bold"), fg="white", bg="#5080ff")
label2.place(x=280,y=270)

label3=Label(root, text="DESCRIPTION", font=("georgia", 12, "bold"), fg="white", bg="#5080ff")
label3.place(x=420,y=270)

label4=Label(root, text="PRESSURE", font=("georgia", 12, "bold"), fg="white", bg="#5080ff")
label4.place(x=595,y=270)

t=Label(font=("georgia", 30, "bold"), fg="#ee666d")
t.place(x=400,y=110)
c=Label(font=("georgia", 8, "bold"))
c.place(x=400,y=200)

w=Label(text="...", font=("georgia", 15, "bold"), bg="#4374f6")
w.place(x=200,y=320)

h=Label(text="...", font=("georgia", 15, "bold"), bg="#4374f6")
h.place(x=310,y=320)

d=Label(text="...", font=("georgia", 15, "bold"), bg="#4374f6")
d.place(x=450,y=320)

p=Label(text="...", font=("georgia", 15, "bold"), bg="#4374f6")
p.place(x=620,y=320)



root.mainloop()
