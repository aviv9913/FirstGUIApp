import tkinter as tk
import requests
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 700
FONT = ['Ariel', 14]


def format_responce(weather):
    try:
        country = weather['sys']['country']
        city = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        final_str = 'Country: %s \nCity: %s \nConditions: %s\nTemperature (%cC): %s' \
                    % (country, city, description, 186, temp)

    except:
        final_str = "There was a problam retriving that information"

    return final_str


def get_weather(city):
    weather_key = "d48757ba1349fd31bd85ccf3cfa46076"
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_responce(weather)
    if weather['cod'] == 200:
        icon_name = weather['weather'][0]['icon']
        open_image(icon_name)


def open_image(icon):
    size = int(lower_frame.winfo_height()*0.3)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0, 0, anchor='nw', image=img)
    weather_icon.image = img


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="#80c1ff", bd=8)
frame.place(anchor='n', relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1)

entry = tk.Entry(frame, font=FONT)
entry.place(relwidth=0.67, relheight=1)

button = tk.Button(frame, text="Get Weather", font=FONT, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg="#80c1ff", bd=8)
lower_frame.place(anchor='n', relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6)

label = tk.Label(lower_frame, bg='white', font=FONT, anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)


root.mainloop()
