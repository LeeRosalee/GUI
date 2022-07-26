from tkinter import *
from tkinter import ttk
GUI=Tk()
GUI.geometry('500x300')
GUI.title('โปรเเกรม BMI')

FONT1=('Angsana New',20)
FONT2=('Angsana New',15)

#ช่องกรอกข้อมูล(weight)
L=ttk.Label(GUI,text='Please insert your weight in unit(kg.)',font=FONT1)
L.pack()
w_weight=StringVar()
c1=ttk.Entry(GUI,textvariable=w_weight,font=FONT1)
c1.pack()

#ช่องกรอกข้อมูล(weight)
L=ttk.Label(GUI,text='Please insert your height in unit(cm.)',font=FONT1)
L.pack()
h_height=StringVar()
c2=ttk.Entry(GUI,textvariable=h_height,font=FONT1)
c2.pack()


def Calc(event=None):
    weight = int(w_weight.get())
    height = int(h_height.get())
    height = height/100
   
    BMI = weight/(height*height)
    if  BMI <=18.5:
        print('Under weight')
    elif BMI <=24.9:
        print('Normal weight')
    elif BMI <=29.9:
        print('Overweight')
    elif BMI <=34.9:
        print('Obesity class 1')      
    elif BMI <= 39.9:
        print('Obesity class 2') 
    else:
        print('Obesity class 3') 
    v_result.set('Your BMI:{:.2f}'.format(BMI))


B1=ttk.Button(GUI,text='Calculate',command=Calc)
B1.pack(ipadx=15,ipady=10,pady=10)

c2.bind('<Return>',Calc)

#ผลลัพท์จากการคํานวน####
v_result=StringVar()
v_result.set('<<<Your weight condition>>>')
R1=ttk.Label(GUI,textvariable=v_result,font=FONT1)
R1.pack()



GUI.mainloop()