from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=3bd6319b914854a79d11041b0944a871").json()
    w1_label.config(text=data["weather"][0]["main"])
    wd_label1.config(text=data["weather"][0]["description"])
    wt_label1.config(text=str(data["main"]["temp"]-273.15))
    wp_label1.config(text=data["main"]["pressure"])

win = Tk()
win.title("DreamFly Tech")
win.config(bg="sky blue")
win.geometry("550x550")

name_label = Label(win, text="WeatherCast", font=("Time new Roman", 35, "bold"))
name_label.place(x=25, y=50, height=50, width=500)

city_name = StringVar()
list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh",
    "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya",
    "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
    "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli",
    "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi", "Puducherry"
]
com = ttk.Combobox(win, text="WeatherCast", values=list_name, font=("Time new Roman", 17, "bold"), textvariable=city_name)
com.place(x=50, y=120, height=35, width=450)

done_button = Button(win, text="Done", font=("Time new Roman", 25, "bold"), command=data_get)
done_button.place(y=190, height=43, width=100, x=200)

w_label = Label(win, text="Weather Climate", font=("Time new Roman", 14))
w_label.place(x=25, y=260, height=40, width=200)

w1_label = Label(win, text="", font=("Time new Roman", 14))
w1_label.place(x=240, y=260, height=40, width=260)

wd_label = Label(win, text="Weather Description", font=("Time new Roman", 14))
wd_label.place(x=25, y=320, height=40, width=200)

wd_label1 = Label(win, text="", font=("Time new Roman", 14))
wd_label1.place(x=240, y=320, height=40, width=260)

wt_label = Label(win, text="Temperature", font=("Time new Roman", 14))
wt_label.place(x=25, y=380, height=40, width=200)

wt_label1 = Label(win, text="", font=("Time new Roman", 14))
wt_label1.place(x=240, y=380, height=40, width=260)

wp_label=Label(win,text="Pressure", font=("Time new Roman",14))
wp_label.place(x=25,y=440,height=40, width=200)

wp_label1=Label(win,text="", font=("Time new Roman",14))
wp_label1.place(x=240,y=440,height=40, width=260)


win.mainloop()
