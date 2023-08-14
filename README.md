![Screenshot](https://github.com/egidijus78/egidijus78/blob/main/img/tkinter%20logo1.jpg)











<h2 align="center"> Calculator project </h2>

![Screenshot](https://raw.githubusercontent.com/egidijus78/egidijus78/main/img/calculator81497.ico)

<h4> This is my first step trying to program in Python. The project was conceived as learning and testing the possibilities of tkinter package as part of Python and its functionality. The idea of this project was to create a transparent graphic calculator, unfortunately tkinter does not provide the ability to make function keys transparent, it's not meant for that. So I had to compromise, I made the calculator screen frame and background transparent and functional parts with a permanent color.</h4> 


![Screenshot](https://github.com/egidijus78/egidijus78/blob/main/img/calculator%20permanent0.jpg)






















<h4> I tried what else can be added to this calculator, I added a combobox with the ability to change background color and added eleven colors. 

![Screenshot](https://github.com/egidijus78/egidijus78/blob/main/img/combobox3.jpg)















<h4> I have added a digital clock with date, day of the week, month.</h4>

![Screenshot](https://github.com/egidijus78/egidijus78/blob/main/img/clock%20date%20temperature.jpg)









<h4> I also added the weather forecast for now in my city Vilnius. Unfortunately the screen of the calculator and window itself ar not able to place extensive information about the weather and other parameters. </h4>

![Screenshot](https://github.com/egidijus78/egidijus78/blob/main/img/openweathermap.jpg)


















<h4> I also added a window at the bottom of the window with the ability to enter text as notes. </h4>

![Screenshot](https://github.com/egidijus78/egidijus78/blob/main/img/calculatoryellow.jpg)






















<h3> Comprehensive description of the program: </h3>




<h4>  <!--- Import the tkinter package for working with the Tk library ---> </h4>
<h4>  <!--- Import the Pmw tool for creating widgets and megawidgets ---> </h4>
     # Import a module for working with time
     # Import a module for working with requests
import tkinter
from tkinter import *
import Pmw
import time
import requests

     # Create a main window
window = Tk()

    # Remove the title bar of the window
    # window.overrideredirect(True)

    # Create the window title, set the format of the window layout parameters,
    # width x height + placement on the screen in the x coordinate axis (from the upper left corner to the right)
    # + on the y coordinate axis (from the upper left corner down)
window.title("Calculator")
window.geometry("{}x{}+{}+{}".format(264, 560, 600, 250))
window.columnconfigure(index = 1, weight = 0)
window.rowconfigure(index = 1, weight = 0)

  <!--- # Changing the window size --->
window.resizable(width = False, height = False)
   # change the window icon
window.iconbitmap("calculator81497.ico")

   # set the background color
window.configure(bg = "#4A7A8C")
   # an additional attribute is transparency. The color code is suitable for the transparency effect
window.wm_attributes("-transparentcolor","#4A7A8C")
   # display window font, width, background transparent color, text color, frame size in millimeters, relief   


   # positioning method grid, argument indicating how many columns the element should occupy 
display = Entry(window, font = ("Fixedsys", 12), width = 32, bg = "#4A7A8C", fg = "#171717", bd = "0.4m", relief = RAISED, cursor = "draft_large")
   # outer-margin argument inner-margin argument element-align direction
display.grid(row = 0, rowspan = 1, column = 0, columnspan = 5, padx = 0, pady = 35, ipadx = 0 ,ipady = 15, sticky = N)
display.columnconfigure(index = 0, weight = 1)
display.rowconfigure(index = 0, weight = 1)

   # create a list of buttons, in this way, instead of 18 lines (for each button, one line gives a significantly shorter code
buttonText = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    "0", ".", "=", "/",
    "", "OFF", "C", ""]

    
   # call the buttons function, with the condition if, elif, elif, else
def click(key):
        if key == "=":
                result = eval(display.get())
                display.delete(0, END)
                display.insert(END, result)
        elif key == "C":
                display.delete(0, END)
        elif key == "OFF":
            window.destroy()
        else:
                display.insert(END, key)



   # set the first row index, column index of the buttons
rowIndex = 1
colIndex = 0

   # call the function, set the width, height, color, relief of the buttons, change the cursor, enter the argument command
   # button column indexes condition, button row indexes condition (if there are more than 3 columns, then move to a new row)
for button_Text in buttonText:
        def process(t = button_Text):
                click(t)

        Button(window, text = button_Text, width = 8, height = 3, bg = "#FA8072",
               fg = "#171717", bd = "0.4m", relief = RAISED, cursor = "draft_large",
               command = process).grid(row = rowIndex, column = colIndex)

        colIndex += 1
        if colIndex > 3:
                rowIndex += 1
                colIndex = 0
   
   
   # background color change scrollbar(combobox)
def changeColor(col):
    window1.configure(background = col)

   # scrollbar list of selectable colors
colors = ("#4a7a8c", "Aqua", "Aquamarine", "Bisque", "Black",
          "DodgerBlue", "Indigo", "MediumSeaGreen", "Navy",
          "Tomato", "Yellow")

   # scrollbar window launch, scrollbar color, layout direction
   # scrollbar title, scrollbar dropdown width
   # setting the selectioncommand argument
   # scrollbar first row index
   # argument indicating how many columns the element should occupy
   # scrollbar outer margin argument, inner margin argument
window1 = Pmw.initialise()
combo = Pmw.ComboBox(window1, labelpos = N,
                     label_text = "change background color :",
                     scrolledlist_items = colors,
                     listheight = 150,
                     selectioncommand = changeColor,
                     )
combo.grid(row = 6, rowspan = 1, column = 0,columnspan = 5, padx = 1, pady = 1, ipadx = 0, ipady = 0, sticky = N)


   # run a function that outputs the current time and formats it into a string, I set the time display format
   # delete the clock window title text
   # call the gettime function every second (time delay of 1000 milliseconds) to get the current time
delay of 1000 milliseconds), kad gauti esamą laiką
def gettime():
    timestring = time.strftime("%H:%M:%S \n %A \n %d %B")
    lb.configure(text = timestring)
    window.after(1000, gettime)


   # create a note window inside the calculator screen,
   # set its background color, symbol color, frame size in millimeters, font, size, relief
   # determine its layout according to the row and column indices, how many rows and columns the element should occupy,
   # outer margins, inner margins, element alignment direction
lb = tkinter.Label(window, text = "", bg = "Salmon", fg = "#171717", bd = "0.4m",
                   font = ("Courier", 7), relief = GROOVE, cursor = "draft_large")

lb.grid(row = 0, rowspan = 1, column = 3, columnspan = 1, padx = 0,
        pady = 0, ipadx = 0, ipady = 0, sticky = W)

   # start the clock rendering
gettime()


   # indicate the city
city = "Vilnius"
   # making a request
url = "https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347"
   # send a request to the server and get an immediate response
weather_data = requests.get(url).json()
   # getting temperature data
   # output the values to the screen
temperature = round(weather_data["main"]["temp"])
temperature_feels = round(weather_data["main"]["feels_like"])
print("Now weather", city, str(temperature), "°C")
print("Temperature feels", str(temperature_feels), "°C")

   # run a function that outputs the current air temperature
   # call the gettemperature function every second to get the current air temperature
def gettemperature():
    lb2.configure(text=temperature)
    window.after(1000, gettemperature)


   # create a note window inside the calculator screen,
   # set its background color, symbol color, frame size in millimeters, font, size, relief
   # determine its layout according to the row and column indices, how many rows and columns the element should occupy,
   # outer margins, inner margins, element alignment direction
lb2 = tkinter.Label(window, text = "\n", bg = "Salmon", fg = "#171717", bd = "0.4m",
                   font = ("Courier", 9), relief = GROOVE, cursor = "draft_large")

lb2.grid(row = 0, rowspan = 1, column = 2, columnspan = 1, padx = 1,
        pady = 1, ipadx = 5, ipady = 10, sticky = E)
gettemperature()

lb3 = tkinter.Label(window, text = "c", bg = "Salmon", fg = "#171717", bd = "0.3m",
                   font = ("Courier", 7), relief = GROOVE, cursor = "draft_large")

lb3.grid(row = 0, rowspan = 1, column = 2, columnspan = 1, padx = 0,
        pady = 0, ipadx = 0, ipady = 0, sticky = E)


  # created a second screen at the bottom of the application, set its color, character color, frame size, relief
  # determined its layout according to the row and column indices, how many rows and columns the element should occupy,
  # outer margins, inner margins, element alignment direction
display2 = Text(window, font = ("Fixedsys", 12), height = 1, width = 31, bg = "#fff", fg = "#171717", bd = "0.4m",
                relief = SUNKEN, cursor = "draft_large")

  # transparent text window is not functional, Tkinter is not designed for this
# display2 = Text(window, font = ("Fixedsys", 12), height = 1, width = 31, bg = "#4A7A8C", fg = "#171717", bd = "0.4m",
#                 relief = RAISED, cursor = "draft_large")
display2.grid(row = 12, rowspan = 5,column = 0, columnspan = 8, padx = 0, pady = 0,
        ipadx = 0, ipady = 12, sticky = S)

display2.columnconfigure(index = 0, weight = 1)
display2.rowconfigure(index = 0, weight = 1)

  
  # calling an infinite loop of rendering the program window with the help of the mainloop function
window.mainloop() </h4>


























