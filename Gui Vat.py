from http.client import FORBIDDEN
from itertools import product
from tkinter import *
from tkinter import ttk
GUI=Tk()
GUI.geometry('500x400')
GUI.title('โปรเเกรมคํานวน Vat')

# FONT 
FONT1 = ('Angsana New',20)




####### ช่องกรอกข้อมูล(Name of product) #######
L=ttk.Label(GUI,text='ชื่อสินค้า',font=FONT1).pack()
v_product=StringVar() # ตัวเเปลสําหรับเก็บชื่อสินค้าตอนพิมพ์
E1 = ttk.Entry(GUI,textvariable=v_product,font=FONT1)
E1.pack()

####### ช่องกรอกข้อมูล(price of product) #######
L=ttk.Label(GUI,text='ราคาสินค้า',font=FONT1).pack()
v_price=StringVar()  # ตัวเเปลสําหรับเก็บราคาตอนพิมพ์
E2 = ttk.Entry(GUI,textvariable=v_price,font=FONT1)
E2.pack()

####### ช่องกรอกข้อมูล(Quantity of product) #######
L=ttk.Label(GUI,text='จํานวน',font=FONT1).pack()
v_quantity=StringVar() # ตัวเเปลสําหรับเก็บจํานวนตอนพิมพ์
E3 = ttk.Entry(GUI,textvariable=v_quantity,font=FONT1)
E3.pack()







####### ปุ่มกดเพื่อคํานวน######
def Calc(event=None):  # event=None เพื่อให้ทั้งสองฟังชั่น(Enter + Button)ทํางานได้
   # print(type(int(v_price.get())))
    product = v_product.get()
    price = int(v_price.get())
    quantity = int(v_quantity.get())
    total = price*quantity

    vat7=total*(7/107)
    nettotal = total*(100/107)
    print(' ราคาก่อน vat:{:.2f} (vat7%: {:.2f})'.format(nettotal,vat7))
    v_result.set('สินค้า:{} {} ชิ้น รวมเป็นเงิน {} บาท ({}/ชิ้น\nราคาสินค้า:{:.2f}.- VAT7%:{:.2f}.-)'.format(product,quantity,total,price,nettotal,vat7))




B1 = ttk.Button(GUI,text='Calculate',command=Calc)
B1.pack(ipadx=20,ipady=10,pady=10)

E3.bind('<Return>',Calc) #ฟังชั่นกด Enter

########ผลลัพท์จากการคํานวน####
v_result=StringVar()
v_result.set('<<<ผลลัพท์โชว์จุดนี้>>>') #โชว์ข้อมูลเริ่มต้น
R1=ttk.Label(GUI,textvariable=v_result,font=FONT1)
R1.pack()

GUI.mainloop()