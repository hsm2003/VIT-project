# -*- coding: utf-8 -*-
import tkinter as tk
import requests 
def format_response(weather):
    name= weather['name']
    desc= weather['weather'][0]['description']
    temp= weather['main']['temp']
    
    final_str= 'City:%s \n Conditions: %s \n Temperature( °c): %s' %(name,desc,temp) 
    
   
    return final_str
    
def knw_weather(city):
    wkey='971f0efa660e482a53c439a625dbbef7'
    link='https://api.openweathermap.org/data/2.5/weather'
    parameters = {'APPID': wkey, 'q':city, 'units':'Metric'}
    response = requests.get(link, params=parameters)
    weather=response.json()
    
    label['text']= format_response(weather)
root = tk.Tk()
root.title("Weather App")
canvas = tk.Canvas(root, height = 500, width = 600)
canvas.pack()


frame = tk.Frame(root,bg='#80ff80', bd = 2.5)
frame.place(relx=0.5, rely = 0.75, relwidth=0.75, relheight=0.1, anchor='n')

frame1 = tk.Frame(root,bg='#80ff80', bd = 2.5)
frame1.place(relx=0.5, rely = 0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame1, font= ('Maiandra GD', 20))
entry.place(relx= 0.1, relheight=1, relwidth= 0.8)

button = tk.Button(frame, text = "Show Weather Condition", font =40, command= lambda: knw_weather(entry.get()))
button.place(relx = 0.06, relheight= 1, relwidth= 0.90)

lf = tk.Frame(root,bg='#80ff80', bd = 10)
lf.place(relx= 0.5, rely = 0.20, relwidth= 0.75, relheight= 0.55, anchor= 'n')

label=tk.Label(lf, font= ('Maiandra GD', 20))
label.place(relwidth= 1, relheight= 1)

root.mainloop()    



