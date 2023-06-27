from tkinter import *
from tkinter import ttk
from parsing import *

root = Tk()
root.title('OLX parsing')
root.geometry('700x150')
root.wm_attributes('-alpha', 2) 

root.resizable(width=False, height=False)

frame1 = Frame(root, bg = 'sky blue')
frame1.place(relwidth=1, relheight=1)

title = Label(frame1, text='Ноутбуки.', bg='plum1', font='Arial 20')
title.pack()
title1 = Label(frame1, text='\/ Топ-3 интересных ноутбуков на Olx можно посмотреть здесь\/', bg='plum1', font='Arial 15')
title1.pack()
def click():
    window = Toplevel()
    window.title("OLX product")
    window1 = Frame(window, bg='sky blue')
    window.geometry('600x3000')
    window.resizable(width=False, height=False)
    window1.place(relwidth=1, relheight=1)
    window_title = Label(window1, text='Первое место:', bg='plum1', font='Arial 13')
    window_title.grid(row=1, column=0, padx=10, pady=10)
    Olx_label1 = Label(window1, text="название:", font=("Arial", 12))
    Olx_label1.grid(row=3, column=0, padx=10, pady=10)
    Olx_label2 = Label(window1, text="цена:", font=("Arial", 12))
    Olx_label2.grid(row=4, column=0, padx=10, pady=10)
    Olx_label3 = Label(window1, text="описание:", font=("Arial", 12))
    Olx_label3.grid(row=5, column=0, padx=10, pady=10)


    window_title = Label(window1, text='Второе место:', bg='plum1', font='Arial 13')
    window_title.grid(row=7, column=0, padx=10, pady=10)
    Olx_label5 = Label(window1, text="название:", font=("Arial", 12))
    Olx_label5.grid(row=8, column=0, padx=10, pady=10)
    Olx_label6 = Label(window1, text="цена:", font=("Arial", 12))
    Olx_label6.grid(row=9, column=0, padx=10, pady=10)
    Olx_label7 = Label(window1, text="описание:", font=("Arial", 12))
    Olx_label7.grid(row=10, column=0, padx=10, pady=10)



    window_title = Label(window1, text='Третье место:', bg='plum1', font='Arial 13')
    window_title.grid(row=12, column=0, padx=10, pady=10)
    Olx_label9 = Label(window1, text="название", font=("Arial", 12))
    Olx_label9.grid(row=13, column=0, padx=10, pady=10)
    Olx_label10 = Label(window1, text="цена:", font=("Arial", 12))
    Olx_label10.grid(row=14, column=0, padx=10, pady=10)
    Olx_label11 = Label(window1, text="описание:", font=("Arial", 12))
    Olx_label11.grid(row=15, column=0, padx=10, pady=10)


    def get_data():
       
        asus1 = get_olx_data1(ASUS)
        asus2 = get_olx_data2(ASUS)
        asus3 = get_olx_data3(ASUS)
        acer1 = get_olx_data1(ACER)
        acer2 = get_olx_data2(ACER)
        acer3 = get_olx_data3(ACER)
        lenovo1 = get_olx_data1(LENOVO)
        lenovo2 = get_olx_data2(LENOVO)
        lenovo3 = get_olx_data3(LENOVO)
     

        All_data = [asus1, asus2, asus3, acer1, acer2, acer3, lenovo1, lenovo2, lenovo3]
        return All_data
            

    def add_values(ALL_DATA):
        global asus_value1, asus_value2, asus_value3, acer_value1, acer_value2, acer_value3, lenovo_value1, lenovo_value2, lenovo_value3

        asus_value1 = Label(window1, text=f'{ALL_DATA[0][0]}.', bg="yellow", font=('Arial', 12))
        asus_value1.grid(row=8, column=1, padx=10, pady=10)
        asus_value2 = Label(window1, text=f'{ALL_DATA[1][0]}.', font=('Arial', 12))
        asus_value2.grid(row=9, column=1, padx=10, pady=10)
        asus_value3 = Label(window1, text=f'{ALL_DATA[2][0]}.', font=('Arial', 9))
        asus_value3.grid(row=10, column=1, padx=10, pady=10)
        acer_value1 = Label(window1, text=f'{ALL_DATA[3][0]}.', bg="yellow", font=('Arial', 12))
        acer_value1.grid(row=3, column=1, padx=10, pady=10)
        acer_value2 = Label(window1, text=f'{ALL_DATA[4][0]}.', font=('Arial', 12))
        acer_value2.grid(row=4, column=1, padx=10, pady=10)
        acer_value3 = Label(window1, text=f'{ALL_DATA[5][0]}.', font=('Arial', 9))
        acer_value3.grid(row=5, column=1, padx=10, pady=10)  
        lenovo_value1 = Label(window1, text=f'{ALL_DATA[6][0]}.', bg="yellow", font=('Arial', 12))
        lenovo_value1.grid(row=13, column=1, padx=10, pady=10)  
        lenovo_value2 = Label(window1, text=f'{ALL_DATA[7][0]}.', font=('Arial', 12))
        lenovo_value2.grid(row=14, column=1, padx=10, pady=10)  
        lenovo_value3 = Label(window1, text=f'{ALL_DATA[8][0]}.', font=('Arial', 9))
        lenovo_value3.grid(row=15, column=1, padx=10, pady=10)  


            
    add_values(get_data())
    def Label_destroy():
        asus_value1.destroy()
        asus_value2.destroy()
        asus_value3.destroy()
        acer_value1.destroy()
        acer_value2.destroy()
        acer_value3.destroy()
        lenovo_value1.destroy()
        lenovo_value2.destroy()
        lenovo_value3.destroy()

    def refresh():
        ALL_DATA = get_data()
        Label_destroy()
        add_values(ALL_DATA=ALL_DATA)


button = ttk.Button( text="        НАЖМИ НА МЕНЯ ЧТОБЫ ПЕРЕЙТИ ДАЛЬШЕ       ",command=click)
button.pack(anchor=CENTER, expand=1 )

if __name__ =="__main__":
    
    root.mainloop()


