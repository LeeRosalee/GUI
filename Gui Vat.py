from http.client import FORBIDDEN
from itertools import product
from tkinter import *
from tkinter import ttk
GUI=Tk()
GUI.geometry('500x450')
GUI.title('โปรเเกรมคํานวน Vat')

# FONT 
FONT1 = ('Angsana New',20)




####### ช่องกรอกข้อมูล(Name of product) #######
L=ttk.Label(GUI,text='ชื่อสินค้า',font=FONT1).pack()#ข้อความเเสดง
v_product=StringVar() # ตัวเเปลสําหรับเก็บชื่อสินค้าตอนพิมพ์
E1 = ttk.Entry(GUI,textvariable=v_product,font=FONT1)
E1.pack()#ข้อความเเสดง

####### ช่องกรอกข้อมูล(price of product) #######
L=ttk.Label(GUI,text='ราคาสินค้า',font=FONT1).pack()#ข้อความเเสดง
v_price=StringVar()  # ตัวเเปลสําหรับเก็บราคาตอนพิมพ์
E2 = ttk.Entry(GUI,textvariable=v_price,font=FONT1)
E2.pack()#ข้อความเเสดง

####### ช่องกรอกข้อมูล(Quantity of product) #######
L=ttk.Label(GUI,text='จํานวน(ชิ้น/กก)',font=FONT1).pack()#ข้อความเเสดง
v_quantity=StringVar() # ตัวเเปลสําหรับเก็บจํานวนตอนพิมพ์
E3 = ttk.Entry(GUI,textvariable=v_quantity,font=FONT1)
E3.pack()#ข้อความเเสดง

####### Radio เลือกประเภท VAT ########
F1 = Frame(GUI)
F1.pack(pady=10)

v_radio = StringVar()
R1=ttk.Radiobutton(F1,text='ราคารวม VAT เเล้ว',variable=v_radio,value='ic')
R1.grid(row=0,column=0)

R1.invoke()  #เลือกเป็นค่าเริ่มต้น

R2=ttk.Radiobutton(F1,text='ราคา + VAT 7%',variable=v_radio,value='av')
R2.grid(row=0,column=1)

R3=ttk.Radiobutton(F1,text='ราคาไม่รวม VAT ',variable=v_radio,value='nic')
R3.grid(row=0,column=2)


####### ปุ่มกดเพื่อคํานวน######
def Calc(event=None):  # event=None เพื่อให้ทั้งสองฟังชั่น(Enter + Button)ทํางานได้
    # print('RADIO:',v_radio.get())
   # print(type(int(v_price.get())))
    product = v_product.get()
    price = int(v_price.get())
    quantity = int(v_quantity.get())
    total = price*quantity
    
    if v_radio.get()=='ic':
        vat7=total*(7/107)
        nettotal = total*(100/107)
        #print(' ราคาก่อน vat:{:.2f} (vat7%: {:.2f})'.format(nettotal,vat7))
        v_result.set('สินค้า:{} จํานวน {} (ชิ้น/กก) รวมเป็นเงิน {} บาท ({}/ชิ้น)\nราคาสินค้า:{:.2f}.- VAT7%:{:.2f}.-)'.format(product,quantity,total,price,nettotal,vat7))

    elif v_radio.get()=='av':
        vat7 = (total*(7/100))
        nettotal=total
        sumtotal=total+vat7
        v_result.set('สินค้า:{} จํานวน {} (ชิ้น/กก) รวมเป็นเงิน {:.2f} บาท ({}/ชิ้น)\nราคาสินค้า:{:.2f}.- VAT7%:{:.2f}.-)'.format(product,quantity,sumtotal,price+(vat7/quantity),nettotal,vat7))

    else:
        v_result.set('สินค้า:{} {} (ชิ้น/กก) รวมเป็นเงิน {} บาท ({}/ชิ้น)\n'.format(product,quantity,total,price))

B1 = ttk.Button(GUI,text='Calculate',command=Calc)
B1.pack(ipadx=20,ipady=10,pady=10)

E3.bind('<Return>',Calc) #ฟังชั่นกด Enter

########ผลลัพท์จากการคํานวน####
v_result=StringVar()
v_result.set('<<<ผลลัพท์โชว์จุดนี้>>>') #โชว์ข้อมูลเริ่มต้น
R1=ttk.Label(GUI,textvariable=v_result,font=FONT1)
R1.pack()







GUI.mainloop()