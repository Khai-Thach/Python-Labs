import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()


    # your code to animate Irma here

    data = open('data/irma.csv', "r")
    text = data.readlines()
    
        
    for row in text[1:]:
        parts = row.strip().split(',')
        lon = float(parts[3])
        lat = float(parts[2])
        wind_speed = int(parts[4])

        if wind_speed >= 157:
            category = 5
            color = 'red'
        elif wind_speed >= 130:
            category = 4
            color = 'orange'
        elif wind_speed >= 111:
            category = 3
            color = 'yellow'
        elif wind_speed >= 96:
            category = 2
            color = 'green'
        elif wind_speed >= 74:
            category = 1
            color = 'blue'
        else:
            category = 0
            color = 'white'


        t.speed(0)
        t.goto(lon,lat)
        t.pendown()
        t.dot(5,color)
        if category > 0:
                t.write(str(category), font = ('Arial'))

        t.pensize(category*3)
        t.pencolor(color)
        t.goto(lon,lat)
    t.done()
              

if __name__ == "__main__":
    irma()


#open the file
#read each line using a for loop (except for the first line)
#break up the line using split function to break up the line on commas
#retrieve longitude and latitude
#make turtle GOTO lon(x) and lat(y) pair
#figure out the category of a storm based on wind speed & modify the turtle drawings
#put ^ before the goto
#figure out how to write the "number" of the category
