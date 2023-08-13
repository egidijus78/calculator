# Importuoju paketą tkinter skirtą darbui su biblioteka Tk
# importuoju instrumentą Pmw skirtą widgets ir megawidgets sukūrimui
# importuoju modulį darbui su laiku time
# importuoju modulį darbui su užklausomis
import tkinter
from tkinter import *
import Pmw
import time
import requests

# Sukuriu langą window
window = Tk()

# Panaikinu lango title bar
# window.overrideredirect(True)


# Sukuriu lango antraštę, nustatau lango išdėstymo parametrų formatą,
# plotis x aukštis + išdėstymas ekrane x koordinačių ašyje(nuo viršutinio kairio kampo į dešinę)
#  + y koordinačių ašyje(nuo viršutinio kairio kampo žemyn)
window.title("Calculator")
window.geometry("{}x{}+{}+{}".format(264, 560, 600, 250))
window.columnconfigure(index = 1, weight = 0)
window.rowconfigure(index = 1, weight = 0)

# Lango dydžio pakeitimas
window.resizable(width = False, height = False)
# Pakeičiu lango ikoną
window.iconbitmap("calculator81497.ico")


# Nustatau background spalvą
window.configure(bg = "#4A7A8C")
# Papildomas atributas - permatomumas, Spalvos kodas tinkamas permatomumo efektui
window.wm_attributes("-transparentcolor","#4A7A8C")


# Ekrano lango šriftas, plotis, background permatoma spalva, teksto spalva, rėmelio dydis milimetrais, reljefas
display = Entry(window, font = ("Fixedsys", 12), width = 32,
                bg = "#4A7A8C", fg = "#171717", bd = "0.4m", relief = RAISED, cursor = "draft_large")
# Pozicionavimo metodas grid, argumentas rodantis kiek stulpelių turi užimti elementas
# išorinės paraštės argumentas, vidinės paraštės argumentas, elemento išlyginimo kryptis
display.grid(row = 0, rowspan = 1, column = 0, columnspan = 5, padx = 0,
             pady = 35, ipadx = 0 ,ipady = 15, sticky = N)
display.columnconfigure(index = 0, weight = 1)
display.rowconfigure(index = 0, weight = 1)


# Sukuriu mygtukų listą, tokiu būdu vietoje 18 eilučių(kiekvienam mygtukui po eilutę gaunasi žymiai trumpesnis kodas
buttonText = [
    "1", "2", "3", "+",
    "4", "5", "6", "-",
    "7", "8", "9", "*",
    "0", ".", "=", "/",
    "", "OFF", "C", ""]


# Iškviečiu mygtukų funkciją, su sąlyga jeigu, jeigukitaip, jeigukitaip, kitaip
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


# Nustatau mygtukų pirmos eilutės indeksą, stulpelio indeksą
rowIndex = 1
colIndex = 0


# Iškviečiu funkciją, nustatau mygtukų plotį, aukštį, spalvą, reljefą, pakeičiu kursorių, įvedu argumentą command
# mygtukų stulpelių indeksų sąlygą, mygtukų eilučių indeksų sąlygą(jei stulpelių daugiau nei 3 tuomet perkelti į naują eilutę)
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



# Background spalvos pakeitimo scrollbar
def changeColor(col):
    window1.configure(background = col)

# Scrollbar pasirenkamų spalvų sąrašas
colors = ("#4a7a8c", "Aqua", "Aquamarine", "Bisque", "Black",
          "DodgerBlue", "Indigo", "MediumSeaGreen", "Navy",
          "Tomato", "Yellow")


# Scrollbar lango paleidimas, scrollbar spalva, išdėstymo kryptis
# Scrollbar antraštė, scrollbar išskleidžiamos dalies plotis
# argumento selectioncommand nustatymas
# Scrollbar pirmos eilutės indeksas
# argumentas rodantis kiek stulpelių turi užimti elementas
# Scrollbar išorinės paraštės argumentas, vidinės paraštės argumentas
window1 = Pmw.initialise()
combo = Pmw.ComboBox(window1, labelpos = N,
                     label_text = "change background color :",
                     scrolledlist_items = colors,
                     listheight = 150,
                     selectioncommand = changeColor,
                     )
combo.grid(row = 6, rowspan = 1, column = 0,columnspan = 5, padx = 1, pady = 1, ipadx = 0, ipady = 0, sticky = N)


# Paleidžiu funkciją kuri išveda esamą laiką ir formatuoja jį į stringą, nustatau laiko atvaizdavimo formatą
# panaikinu laikrodžio lango antraštės tekstą
# iškviečiu gettime funkciją kas sekundę(time delay of 1000 milliseconds), kad gauti esamą laiką
def gettime():
    timestring = time.strftime("%H:%M:%S \n %A \n %d %B")
    lb.configure(text = timestring)
    window.after(1000, gettime)


# Sukuriu užrašo langą viduje kalkuliatoriaus ekrano,
# nustatau jo background spalvą, simbolių spalvą, rėmelio dydį milimetrais, fontą, dydį, reljefą
# nustatau jo išdėstymą pagal eilučių, stulpelių  ideksus, kiek eilučių, stulpelių turi užimti elementas,
# išorinės paraštes, vidines paraštes, elemento išlyginimo kryptį
lb = tkinter.Label(window, text = "", bg = "Salmon", fg = "#171717", bd = "0.4m",
                   font = ("Courier", 7), relief = GROOVE, cursor = "draft_large")

lb.grid(row = 0, rowspan = 1, column = 3, columnspan = 1, padx = 0,
        pady = 0, ipadx = 0, ipady = 0, sticky = W)

# Paleidžiu laikrodžio atvaizdavimą
gettime()

# Nurodau miestą
city = 'Vilnius'
# Formuoju užklausą
url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
# Siunčiu užklausą į serverį ir iškart gaunu atsakymą
weather_data = requests.get(url).json()
# gaunu duomenis apie temperatūrą
# išvedu reikšmes į ekraną
temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
print('Now weather', city, str(temperature), '°C')
print('Temperature feels', str(temperature_feels), '°C')

# Paleidžiu funkciją kuri išveda esamą oro temperatūrą
# iškviečiu gettemperature funkciją kas sekundę kad gauti esamą oro temperatūrą
def gettemperature():
    lb2.configure(text=temperature)
    window.after(1000, gettemperature)


# Sukuriu užrašo langą viduje kalkuliatoriaus ekrano,
# nustatau jo background spalvą, simbolių spalvą, rėmelio dydį milimetrais, fontą, dydį, reljefą
# nustatau jo išdėstymą pagal eilučių, stulpelių  ideksus, kiek eilučių, stulpelių turi užimti elementas,
# išorinės paraštes, vidines paraštes, elemento išlyginimo kryptį
lb2 = tkinter.Label(window, text = "\n", bg = "Salmon", fg = "#171717", bd = "0.4m",
                   font = ("Courier", 9), relief = GROOVE, cursor = "draft_large")

lb2.grid(row = 0, rowspan = 1, column = 2, columnspan = 1, padx = 1,
        pady = 1, ipadx = 5, ipady = 10, sticky = E)
gettemperature()

lb3 = tkinter.Label(window, text = "c", bg = "Salmon", fg = "#171717", bd = "0.3m",
                   font = ("Courier", 7), relief = GROOVE, cursor = "draft_large")

lb3.grid(row = 0, rowspan = 1, column = 2, columnspan = 1, padx = 0,
        pady = 0, ipadx = 0, ipady = 0, sticky = E)


# Sukūriau antrą ekraną programos apačioje, nustačiau jo spalvą, simbolių spalvą, rėmelio dydį, reljefą
# nustačiau jo išdėstymą pagal eilučių, stulpelių  ideksus, kiek eilučių, stulpelių turi užimti elementas,
# # išorinės paraštes, vidines paraštes, elemento išlyginimo kryptį
display2 = Text(window, font = ("Fixedsys", 12), height = 1, width = 31, bg = "#fff", fg = "#171717", bd = "0.4m",
                relief = SUNKEN, cursor = "draft_large")
# Nespalvotas teksto langas nėra funkcionalus, Tkinter nėra pritaikytas tam
# display2 = Text(window, font = ("Fixedsys", 12), height = 1, width = 31, bg = "#4A7A8C", fg = "#171717", bd = "0.4m",
#                 relief = RAISED, cursor = "draft_large")
display2.grid(row = 12, rowspan = 5,column = 0, columnspan = 8, padx = 0, pady = 0,
        ipadx = 0, ipady = 12, sticky = S)

display2.columnconfigure(index = 0, weight = 1)
display2.rowconfigure(index = 0, weight = 1)

# Programos lango atvaizdavimo begalinio ciklo iškvietimas su funkcijos mainloop pagalba
window.mainloop()
