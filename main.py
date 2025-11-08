#!/bin/python3

import json
import turtle
import urllib.request
import time

def main(user_lon, user_lat):
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    location = result['iss_position']
    lat = float(location['latitude'])
    lon = float(location['longitude'])
    print('The current location of the ISS is:')
    print('latitude: ', lat)
    print('longitude: ', lon)

    screen = turtle.Screen()
    screen.setup(720,360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic('map.gif')

    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)
    iss.penup()
    iss.goto(lon,lat)


    location = turtle.Turtle()
    location.penup()
    location.color("red")
    location.goto(user_lon, user_lat)
    location.dot(5)
    location.hideturtle()

    # ISS Pass predictions are now turned off temporarily by Open-Notify

    # url = "http://api.open-notify.org/iss-pass.json"
    # url = url + "?lat=" + str(user_lat) + "&lon=" + str(user_lon)
    # response = urllib.request.urlopen(url)
    # result = json.loads(response.read())
    # # print(result)

    # over = result["response"][0]["risetime"]
    # # print(over)

    # style = ("noteworthy", 4, 'bold')
    # location.write("My House" + time.ctime(over), font = style, align = 'center')

    turtle.mainloop()

if __name__ == "__main__":
    # User's latitude and longitude
    # Example: My Home, Abu Dhabi, UAE
    user_lat = 24.4539
    user_lon = 54.3773
    main(user_lon, user_lat)