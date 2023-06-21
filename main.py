from tkinter import *
from tkinter import ttk
from parsing import *


root = Tk()
root.title('OLX парсинг')
# root.geometry('375x150')
root.wm_attributes('-alpha', 2)

# root.resizable(width=False, height=False)

frame1 = Frame(root, bg = 'sky blue')
frame1.place(relwidth=1, relheight=1)

title = Label(frame1, text='\/ \/ \/напишите ниже что вам нужно\/ \/ \/', bg='plum1')
title.pack()

loginInput = Entry(frame1, bg='gray', width=41)
loginInput.pack()

def click():
    window = Tk()
    window.title("OLX товар")
    # window.geometry("300x300")
    window = Frame(window, bg='sky blue')
    window.place(relwidth=1, relheight=1)
 
button = ttk.Button( text="нажми на меня чтобы перейти дальше",command=click)
button.pack(anchor=CENTER, expand=1)

def App():
    # dollar
    # dollar_label = Label(root, text="Курс доллара:", font=("Arial", 15))
    # dollar_label.grid(row=1, column=0, padx=10, pady=10)
    # # euro
    # euro_label = Label(root, text="Курс евро:", font=("Arial", 15))
    # euro_label.grid(row=2, column=0, padx=10, pady=10)
    # # ruble
    # ruble_label = Label(root, text="Курс рубля:", font=("Arial", 15))
    # ruble_label.grid(row=3, column=0, padx=10, pady=10)
    # # weather
    # weather_label1 = Label(root, text="температура:", font=("Arial", 15))
    # weather_label1.grid(row=4, column=0, padx=10, pady=5)
    # weather_label2 = Label(root, text="скорость ветра:", font=("Arial", 15))
    # weather_label2.grid(row=5, column=0, padx=10, pady=5)
    # weather_label3 = Label(root, text="влажность:", font=("Arial", 15))
    # weather_label3.grid(row=6, column=0, padx=10, pady=5)
    # weather_label4 = Label(root, text="вероятность осатков:", font=("Arial", 15))
    # weather_label4.grid(row=7, column=0, padx=10, pady=5)
    # #youtube
    # youtube_label = Label(root, text="подпищики:", font=("Arial", 15))
    # youtube_label.grid(row=8, column=0,padx=10, pady=10)

    def get_data():
        olx1 = get_olx_data1(OLX)

        All_data = [olx1]
        return All_data
    
    def add_values(ALL_DATA):
        global 



        olx_value = Label(root, text=f"{ALL_DATA[0][0]}", font=("Arial", 15))
        olx_value.grid(row=1, column=1, padx=10, pady=10)

   
    add_values(get_data())
    def Label_destroy():
        olx_value.destroy()

    def refresh():
        ALL_DATA = get_data()
        Label_destroy()
        add_values(ALL_DATA=ALL_DATA)

        
if __name__ =="__main__":
    
    App()
    root.mainloop()


