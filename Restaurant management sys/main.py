from tkinter import *
from tkinter import filedialog,messagebox
import ttkthemes
from tkinter import ttk
import random
import time

root  = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('breeze')
root.title('Restaurant Management System')
root.geometry('1188x643+350+30')
root.config(bg='#000')
root.resizable(False,False)
root.overrideredirect(True)


#Functionality part#############################################################################################
def  send():
    
    def send_msg():
        message = textArea.get(1.0,END)
        num = numberField.get()
        
    root2 = Toplevel()
    
    root2.title("SEND BILL")
    root2.config(bg='black')
    root2.geometry('485x620+50+50')
    
    logoImage = PhotoImage(file='sender.png')
    label = Label(root2,image=logoImage,bg='black')
    label.pack()
    
    numberlabel = Label(root2,text='Mobile Number',fg='white',bg='#000'
                        ,font=('Helvetica',18,'bold underline'))
    numberlabel.pack(pady=10)
    
    numberField = ttk.Entry(root2,width=54)
    numberField.pack()
    
    billLabel = Label(root2,text='Bill Details',fg='white',bg='#000'
                        ,font=('Helvetica',18,'bold underline'))
    billLabel.pack(pady=10)
    
    textArea = Text(root2,font=('Helvetica',14,'bold'),bd=3,
                    width=48,height=14)
    textArea.pack()
    
    sendButton = ttk.Button(root2,text='SEND',command=send_msg)
    sendButton.pack(pady=10)
    
    textArea.insert(END,'RECEIPT REF: \t'+'  '+billnum+'  '+' \t\t\t'+'('+date+')\n')
    textArea.insert(END,'********************************************************************\n')
    textArea.insert(END,'ITEMS:\t\tCOST OF ITEMS (Rs/-)\n')
    textArea.insert(END,'********************************************************************\n')
    #ifs for foods items
    if e1.get()!='0':
        textArea.insert(END,f'- Roti:\t\t\t{int(e1.get())*10} Rs/-\n\n')
    if e2.get()!='0':
        textArea.insert(END,f'- Daal:\t\t\t{int(e2.get())*60} Rs/-\n\n')
    if e3.get()!='0':
        textArea.insert(END,f'- Fish:\t\t\t{int(e3.get())*100} Rs/-\n\n')
    if e4.get()!='0':
        textArea.insert(END,f'- Sabji:\t\t\t{int(e4.get())*50} Rs/-\n\n')
    if e5.get()!='0':
        textArea.insert(END,f'- Kebab:\t\t\t{int(e5.get())*40} Rs/-\n\n')
    if e6.get()!='0':
        textArea.insert(END,f'- Chawal:\t\t\t{int(e6.get())*30} Rs/-\n\n')
    if e7.get()!='0':
        textArea.insert(END,f'- Paneer:\t\t\t{int(e7.get())*120} Rs/-\n\n')
    if e8.get()!='0':
        textArea.insert(END,f'- Naan:\t\t\t{int(e8.get())*100} Rs/-\n\n')
    if e9.get()!='0':
        textArea.insert(END,f'- Chole:\t\t\t{int(e9.get())*100} Rs/-\n\n')
    if e10.get()!='0':
        textArea.insert(END,f'- Rajma:\t\t\t{int(e10.get())*120} Rs/-\n\n')
    
    #ifs for drink items  
    if e11.get()!='0':
        textArea.insert(END,f'- Chai:\t\t\t{int(e11.get())*10} Rs/-\n\n')
    if e12.get()!='0':
        textArea.insert(END,f'- Coffee:\t\t\t{int(e12.get())*60} Rs/-\n\n')
    if e13.get()!='0':
        textArea.insert(END,f'- Pepsi:\t\t\t{int(e13.get())*100} Rs/-\n\n')
    if e14.get()!='0':
        textArea.insert(END,f'- Limka:\t\t\t{int(e14.get())*50} Rs/-\n\n')
    if e15.get()!='0':
        textArea.insert(END,f'- Faluda:\t\t\t{int(e15.get())*40} Rs/-\n\n')
    if e16.get()!='0':
        textArea.insert(END,f'- Soda:\t\t\t{int(e16.get())*30} Rs/-\n\n')
    if e17.get()!='0':
        textArea.insert(END,f'- Lassi:\t\t\t{int(e17.get())*120} Rs/-\n\n')
    if e18.get()!='0':
        textArea.insert(END,f'- Shikanji:\t\t\t{int(e18.get())*100} Rs/-\n\n')
    if e19.get()!='0':
        textArea.insert(END,f'- Frooti:\t\t\t{int(e19.get())*100} Rs/-\n\n')
    if e20.get()!='0':
        textArea.insert(END,f'- Mocha:\t\t\t{int(e20.get())*120} Rs/-\n\n')
        
     #ifs for snack items  
    if e21.get()!='0':
        textArea.insert(END,f'- Chips:\t\t\t{int(e21.get())*10} Rs/-\n\n')
    if e22.get()!='0':
        textArea.insert(END,f'- Samosa:\t\t\t{int(e22.get())*60} Rs/-\n\n')
    if e23.get()!='0':
        textArea.insert(END,f'- Chilli Potato:\t\t\t{int(e23.get())*100} Rs/-\n\n')
    if e24.get()!='0':
        textArea.insert(END,f'- Namkeen:\t\t\t{int(e24.get())*50} Rs/-\n\n')
    if e25.get()!='0':
        textArea.insert(END,f'- Biscuit:\t\t\t{int(e25.get())*40} Rs/-\n\n')
    if e26.get()!='0':
        textArea.insert(END,f'- Poha:\t\t\t{int(e26.get())*30} Rs/-\n\n')
    if e27.get()!='0':
        textArea.insert(END,f'- Idli:\t\t\t{int(e27.get())*120} Rs/-\n\n')
    if e28.get()!='0':
        textArea.insert(END,f'- Peanuts:\t\t\t{int(e28.get())*100} Rs/-\n\n')
    if e29.get()!='0':
        textArea.insert(END,f'- Sandwich:\t\t\t{int(e29.get())*100} Rs/-\n\n')
    if e30.get()!='0':
        textArea.insert(END,f'- Chowmin:\t\t\t{int(e30.get())*120} Rs/-\n\n')
    textArea.insert(END,'********************************************************************\n')
    if e31.get()!='0':
        textArea.insert(END,f'COST OF FOOD:\t\t\t{priceofFood} Rs/-\n\n')
    if e32.get()!='0':
        textArea.insert(END,f'COST OF DRINKS:\t\t\t{priceofDrinks} Rs/-\n\n')
    if e33.get()!='0':
        textArea.insert(END,f'COST OF SNACKS:\t\t\t{priceofSnacks} Rs/-\n\n')
    textArea.insert(END,'********************************************************************\n')
    textArea.insert(END,f'SUB TOTAL:\t\t\t{subtotalofitems} Rs/-\n\n')
    textArea.insert(END,f'SERVICE TAX:\t\t\t50 Rs/-\n\n')
    textArea.insert(END,'********************************************************************\n')
    textArea.insert(END,f'TOTAL COST:\t\t\t{totalCost} Rs/-\n\n')
    textArea.insert(END,'********************************************************************\n')
    
    root2.mainloop()

def reset():
    textReceipt.delete(1.0,END)
    


def save():
    url = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    
    bill_data = textReceipt.get(1.0,END)
    url.write(bill_data)
    url.close()
    messagebox.showinfo('Information','Your Bill is saved Succesfully!!')


def receipt():
    global billnum,date
    textReceipt.delete(1.0,END)
    x = random.randint(100,10000)
    billnum = 'BILL NO:  '+str(x)
    date = time.strftime('%d/%m/%Y')
    textReceipt.insert(END,'RECEIPT REF:- \t\t\t'+billnum+'   '+' \t\t\t'+'('+date+')\n')
    textReceipt.insert(END,'***********************************************************************************************\n')
    textReceipt.insert(END,'ITEMS:\t\t\tCOST OF ITEMS (Rs/-)\n')
    textReceipt.insert(END,'***********************************************************************************************\n')
    #ifs for foods items
    if e1.get()!='0':
        textReceipt.insert(END,f'- Roti:\t\t\t{int(e1.get())*10} Rs/-\n\n')
    if e2.get()!='0':
        textReceipt.insert(END,f'- Daal:\t\t\t{int(e2.get())*60} Rs/-\n\n')
    if e3.get()!='0':
        textReceipt.insert(END,f'- Fish:\t\t\t{int(e3.get())*100} Rs/-\n\n')
    if e4.get()!='0':
        textReceipt.insert(END,f'- Sabji:\t\t\t{int(e4.get())*50} Rs/-\n\n')
    if e5.get()!='0':
        textReceipt.insert(END,f'- Kebab:\t\t\t{int(e5.get())*40} Rs/-\n\n')
    if e6.get()!='0':
        textReceipt.insert(END,f'- Chawal:\t\t\t{int(e6.get())*30} Rs/-\n\n')
    if e7.get()!='0':
        textReceipt.insert(END,f'- Paneer:\t\t\t{int(e7.get())*120} Rs/-\n\n')
    if e8.get()!='0':
        textReceipt.insert(END,f'- Naan:\t\t\t{int(e8.get())*100} Rs/-\n\n')
    if e9.get()!='0':
        textReceipt.insert(END,f'- Chole:\t\t\t{int(e9.get())*100} Rs/-\n\n')
    if e10.get()!='0':
        textReceipt.insert(END,f'- Rajma:\t\t\t{int(e10.get())*120} Rs/-\n\n')
    
    #ifs for drink items  
    if e11.get()!='0':
        textReceipt.insert(END,f'- Chai:\t\t\t{int(e11.get())*10} Rs/-\n\n')
    if e12.get()!='0':
        textReceipt.insert(END,f'- Coffee:\t\t\t{int(e12.get())*60} Rs/-\n\n')
    if e13.get()!='0':
        textReceipt.insert(END,f'- Pepsi:\t\t\t{int(e13.get())*100} Rs/-\n\n')
    if e14.get()!='0':
        textReceipt.insert(END,f'- Limka:\t\t\t{int(e14.get())*50} Rs/-\n\n')
    if e15.get()!='0':
        textReceipt.insert(END,f'- Faluda:\t\t\t{int(e15.get())*40} Rs/-\n\n')
    if e16.get()!='0':
        textReceipt.insert(END,f'- Soda:\t\t\t{int(e16.get())*30} Rs/-\n\n')
    if e17.get()!='0':
        textReceipt.insert(END,f'- Lassi:\t\t\t{int(e17.get())*120} Rs/-\n\n')
    if e18.get()!='0':
        textReceipt.insert(END,f'- Shikanji:\t\t\t{int(e18.get())*100} Rs/-\n\n')
    if e19.get()!='0':
        textReceipt.insert(END,f'- Frooti:\t\t\t{int(e19.get())*100} Rs/-\n\n')
    if e20.get()!='0':
        textReceipt.insert(END,f'- Mocha:\t\t\t{int(e20.get())*120} Rs/-\n\n')
        
     #ifs for snack items  
    if e21.get()!='0':
        textReceipt.insert(END,f'- Chips:\t\t\t{int(e21.get())*10} Rs/-\n\n')
    if e22.get()!='0':
        textReceipt.insert(END,f'- Samosa:\t\t\t{int(e22.get())*60} Rs/-\n\n')
    if e23.get()!='0':
        textReceipt.insert(END,f'- Chilli Potato:\t\t\t{int(e23.get())*100} Rs/-\n\n')
    if e24.get()!='0':
        textReceipt.insert(END,f'- Namkeen:\t\t\t{int(e24.get())*50} Rs/-\n\n')
    if e25.get()!='0':
        textReceipt.insert(END,f'- Biscuit:\t\t\t{int(e25.get())*40} Rs/-\n\n')
    if e26.get()!='0':
        textReceipt.insert(END,f'- Poha:\t\t\t{int(e26.get())*30} Rs/-\n\n')
    if e27.get()!='0':
        textReceipt.insert(END,f'- Idli:\t\t\t{int(e27.get())*120} Rs/-\n\n')
    if e28.get()!='0':
        textReceipt.insert(END,f'- Peanuts:\t\t\t{int(e28.get())*100} Rs/-\n\n')
    if e29.get()!='0':
        textReceipt.insert(END,f'- Sandwich:\t\t\t{int(e29.get())*100} Rs/-\n\n')
    if e30.get()!='0':
        textReceipt.insert(END,f'- Chowmin:\t\t\t{int(e30.get())*120} Rs/-\n\n')
    textReceipt.insert(END,'************************************************************************************************\n')
    
    if e31.get()!='0':
        textReceipt.insert(END,f'COST OF FOOD:\t\t\t{priceofFood} Rs/-\n\n')
    if e32.get()!='0':
        textReceipt.insert(END,f'COST OF DRINKS:\t\t\t{priceofDrinks} Rs/-\n\n')
    if e33.get()!='0':
        textReceipt.insert(END,f'COST OF SNACKS:\t\t\t{priceofSnacks} Rs/-\n\n')

    textReceipt.insert(END,'************************************************************************************************\n')
    textReceipt.insert(END,f'SUB TOTAL:\t\t\t{subtotalofitems} Rs/-\n\n')
    textReceipt.insert(END,f'SERVICE TAX:\t\t\t50 Rs/-\n\n')
    textReceipt.insert(END,'************************************************************************************************\n')
    textReceipt.insert(END,f'TOTAL COST:\t\t\t{totalCost} Rs/-\n\n')
    textReceipt.insert(END,'************************************************************************************************\n')



def totalcost():
    global priceofFood,priceofDrinks,priceofSnacks,subtotalofitems,totalCost
    
    item1 = int(e1.get())
    item2 = int(e2.get())
    item3 = int(e3.get())
    item4 = int(e4.get())
    item5 = int(e5.get())
    item6 = int(e6.get())
    item7 = int(e7.get())
    item8 = int(e8.get())
    item9 = int(e9.get())
    item10 = int(e10.get())
    
    item11 = int(e11.get())
    item12 = int(e12.get())
    item13 = int(e13.get())
    item14 = int(e14.get())
    item15 = int(e15.get())
    item16 = int(e16.get())
    item17 = int(e17.get())
    item18 = int(e18.get())
    item19 = int(e19.get())
    item20 = int(e20.get())
    
    item21 = int(e21.get())
    item22 = int(e22.get())
    item23 = int(e23.get())
    item24 = int(e24.get())
    item25 = int(e25.get())
    item26 = int(e26.get())
    item27 = int(e27.get())
    item28 = int(e28.get())
    item29 = int(e29.get())
    item30 = int(e30.get())
    
    priceofFood = (item1*10)+(item2*60)+(item3*100)+(item4*50)+(item5*40)+(item6*30)+(item7*120)+(item8*100)+(item9*100)+(item10*120)

    priceofDrinks = (item11*10)+(item12*60)+(item13*100)+(item14*50)+(item15*40)+(item16*30)+(item17*120)+(item18*100)+(item19*100)+(item20*120)
    
    priceofSnacks = (item21*10)+(item22*60)+(item23*100)+(item24*50)+(item25*40)+(item26*30)+(item27*120)+(item28*100)+(item29*100)+(item30*120)
    
    e31.set(str(priceofFood)+ ' Rs/-')
    e32.set(str(priceofDrinks)+ ' Rs/-')
    e33.set(str(priceofSnacks)+ ' Rs/-')
    
    subtotalofitems = priceofFood+priceofDrinks+priceofSnacks
    e34.set(str(subtotalofitems)+' Rs/-')
    
    e35.set('50 Rs/-')
    
    totalCost = subtotalofitems+50
    e36.set(str(totalCost)+' Rs/-')
    
#FOR FOOD#
def roti():
    if var1.get()==1:
        text1.config(state=NORMAL)
        text1.delete(0,END)
        text1.focus()
    elif var1.get()==0:
        text1.config(state=DISABLED)
        e1.set('0')  
def daal():
    if var2.get()==1:
        text2.config(state=NORMAL)
        text2.delete(0,END)
        text2.focus()
    elif var2.get()==0:
        text2.config(state=DISABLED)
        e2.set('0')  
def fish():
    if var3.get()==1:
        text3.config(state=NORMAL)
        text3.delete(0,END)
        text3.focus()
    elif var3.get()==0:
        text3.config(state=DISABLED)
        e3.set('0')  
def sabji():
    if var4.get()==1:
        text4.config(state=NORMAL)
        text4.delete(0,END)
        text4.focus()
    elif var4.get()==0:
        text4.config(state=DISABLED)
        e4.set('0')  
def kebab():
    if var5.get()==1:
        text5.config(state=NORMAL)
        text5.delete(0,END)
        text5.focus()
    elif var5.get()==0:
        text5.config(state=DISABLED)
        e5.set('0')  
def chawal():
    if var6.get()==1:
        text6.config(state=NORMAL)
        text6.delete(0,END)
        text6.focus()
    elif var6.get()==0:
        text6.config(state=DISABLED)
        e6.set('0')  
def paneer():
    if var7.get()==1:
        text7.config(state=NORMAL)
        text7.delete(0,END)
        text7.focus()
    elif var7.get()==0:
        text7.config(state=DISABLED)
        e7.set('0')  
def naan():
    if var8.get()==1:
        text8.config(state=NORMAL)
        text8.delete(0,END)
        text8.focus()
    elif var8.get()==0:
        text8.config(state=DISABLED)
        e8.set('0')  
def chole():
    if var9.get()==1:
        text9.config(state=NORMAL)
        text9.delete(0,END)
        text9.focus()
    elif var9.get()==0:
        text9.config(state=DISABLED)
        e9.set('0')  
def rajma():
    if var10.get()==1:
        text10.config(state=NORMAL)
        text10.delete(0,END)
        text10.focus()
    elif var10.get()==0:
        text10.config(state=DISABLED)
        e10.set('0')  


#FOR DRINKS#
def chai():
    if var11.get()==1:
        text11.config(state=NORMAL)
        text11.delete(0,END)
        text11.focus()
    elif var11.get()==0:
        text11.config(state=DISABLED)
        e11.set('0')  
def coffee():
    if var12.get()==1:
        text12.config(state=NORMAL)
        text12.delete(0,END)
        text12.focus()
    elif var12.get()==0:
        text12.config(state=DISABLED)
        e12.set('0')  
def pepsi():
    if var13.get()==1:
        text13.config(state=NORMAL)
        text13.delete(0,END)
        text13.focus()
    elif var13.get()==0:
        text13.config(state=DISABLED)
        e13.set('0')  
def limka():
    if var14.get()==1:
        text14.config(state=NORMAL)
        text14.delete(0,END)
        text14.focus()
    elif var14.get()==0:
        text14.config(state=DISABLED)
        e14.set('0')  
def faluda():
    if var15.get()==1:
        text15.config(state=NORMAL)
        text15.delete(0,END)
        text15.focus()
    elif var15.get()==0:
        text15.config(state=DISABLED)
        e15.set('0')  
def soda():
    if var16.get()==1:
        text16.config(state=NORMAL)
        text16.delete(0,END)
        text16.focus()
    elif var16.get()==0:
        text16.config(state=DISABLED)
        e16.set('0')  
def lassi():
    if var17.get()==1:
        text17.config(state=NORMAL)
        text17.delete(0,END)
        text17.focus()
    elif var17.get()==0:
        text17.config(state=DISABLED)
        e17.set('0')  
def shikanji():
    if var18.get()==1:
        text18.config(state=NORMAL)
        text18.delete(0,END)
        text18.focus()
    elif var18.get()==0:
        text18.config(state=DISABLED)
        e18.set('0')  
def frooti():
    if var19.get()==1:
        text19.config(state=NORMAL)
        text19.delete(0,END)
        text19.focus()
    elif var19.get()==0:
        text19.config(state=DISABLED)
        e19.set('0')  
def mocha():
    if var20.get()==1:
        text20.config(state=NORMAL)
        text20.delete(0,END)
        text20.focus()
    elif var20.get()==0:
        text20.config(state=DISABLED)
        e20.set('0')  

#FOR SNACKS#
def chips():
    if var21.get()==1:
        text21.config(state=NORMAL)
        text21.delete(0,END)
        text21.focus()
    elif var21.get()==0:
        text21.config(state=DISABLED)
        e21.set('0')  
def samosa():
    if var22.get()==1:
        text22.config(state=NORMAL)
        text22.delete(0,END)
        text22.focus()
    elif var22.get()==0:
        text22.config(state=DISABLED)
        e22.set('0')  
def chillipot():
    if var23.get()==1:
        text23.config(state=NORMAL)
        text23.delete(0,END)
        text23.focus()
    elif var23.get()==0:
        text23.config(state=DISABLED)
        e23.set('0')  
def namkeen():
    if var24.get()==1:
        text24.config(state=NORMAL)
        text24.delete(0,END)
        text24.focus()
    elif var24.get()==0:
        text24.config(state=DISABLED)
        e24.set('0')  
def biscit():
    if var25.get()==1:
        text25.config(state=NORMAL)
        text25.delete(0,END)
        text25.focus()
    elif var25.get()==0:
        text25.config(state=DISABLED)
        e25.set('0')  
def poha():
    if var26.get()==1:
        text26.config(state=NORMAL)
        text26.delete(0,END)
        text26.focus()
    elif var26.get()==0:
        text26.config(state=DISABLED)
        e26.set('0')  
def idli():
    if var27.get()==1:
        text27.config(state=NORMAL)
        text27.delete(0,END)
        text27.focus()
    elif var27.get()==0:
        text27.config(state=DISABLED)
        e27.set('0')  
def peanuts():
    if var28.get()==1:
        text28.config(state=NORMAL)
        text28.delete(0,END)
        text28.focus()
    elif var28.get()==0:
        text28.config(state=DISABLED)
        e28.set('0')  
def sandwich():
    if var29.get()==1:
        text29.config(state=NORMAL)
        text29.delete(0,END)
        text29.focus()
    elif var29.get()==0:
        text29.config(state=DISABLED)
        e29.set('0')  
def chomin():
    if var30.get()==1:
        text30.config(state=NORMAL)
        text30.delete(0,END)
        text30.focus()
    elif var30.get()==0:
        text30.config(state=DISABLED)
        e30.set('0')  


#Top Frame for title-----------------------------------------------------
topFrame = Frame(root,bd=10,relief=RIDGE,bg='#3DAEE9')
topFrame.pack(side=TOP)

bottomFrame = Frame(root,bd=1,relief=FLAT,bg='#EFF0F1')
bottomFrame.pack(side=BOTTOM)

#,font=('Helvetica',14,'bold')
exitButton = Button(bottomFrame,text='EXIT APPLICATION',width=52
,font=('Helvetica',10,'bold'),bd=7,bg='#EFF0F1',
fg='#000',command=root.destroy,activebackground='#EFF0F1',
activeforeground='#000')
exitButton.pack()


#000
#Title Label#
labelTitle = Label(topFrame,text='Restaurant Management System',font=('Verdana',34,'bold'),
                   fg='#EFF0F1',bg='#000',width=36,bd=9)
labelTitle.grid(row=0,column=0)

#Frames###############################################################

#Menu Frame-------------------------------------------------------------
menuFrame = Frame(root,bd=10,relief=RIDGE,bg='#000')
menuFrame.pack(side=LEFT)


#Cost Frame-------------------------------------------------------------
costFrame = Frame(menuFrame,bd=4,relief=RIDGE,bg='#EFF0F1')
costFrame.pack(side=BOTTOM)

#food labelFrame1
foodFrame = LabelFrame(menuFrame,text='Food',font=('Helvetica',23,'bold'),
                       bd=10,relief=RIDGE,bg='#EFF0F1',fg='#000')
foodFrame.pack(side=LEFT)

#drinks labelFrame2
drinksFrame = LabelFrame(menuFrame,text='Drinks',font=('Helvetica',23,'bold'),
                         bd=10,relief=RIDGE,bg='#EFF0F1',fg='#000')
drinksFrame.pack(side=LEFT)

#snacks labelFrame3
snacksFrame = LabelFrame(menuFrame,text='Snacks',font=('Helvetica',23,'bold')
                         ,bd=10,relief=RIDGE,bg='#EFF0F1',fg='#000')
snacksFrame.pack(side=LEFT)

#Right frame---------------------------------------------------------
rightFrame = Frame(root,bd=15,relief=RIDGE)
rightFrame.pack(side=RIGHT)

#calc frame1
calcFrame = Frame(rightFrame,bd=1,relief=RIDGE)
calcFrame.pack()

#reciept frame2
recieptFrame = Frame(rightFrame,bd=4,relief=RIDGE)
recieptFrame.pack()

#button frame2
buttonFrame = Frame(rightFrame,bd=7,relief=GROOVE,bg='#000')
buttonFrame.pack()


#Variables
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()

e1 = StringVar()
e2 = StringVar()
e3 = StringVar()
e4 = StringVar()
e5 = StringVar()
e6 = StringVar()
e7 = StringVar()
e8 = StringVar()
e9 = StringVar()
e10 = StringVar()

e1.set('0')
e2.set('0')
e3.set('0')
e4.set('0')
e5.set('0')
e6.set('0')
e7.set('0')
e8.set('0')
e9.set('0')
e10.set('0')

#------FOOD
roti = ttk.Checkbutton(foodFrame,text='Roti',onvalue=1,offvalue=0,
                       variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)

daal = ttk.Checkbutton(foodFrame,text='Daal',onvalue=1,offvalue=0,variable=var2,command=daal)
daal.grid(row=1,column=0,sticky=W)

fish = ttk.Checkbutton(foodFrame,text='Fish',onvalue=1,offvalue=0,
                       variable=var3,command=fish)
fish.grid(row=2,column=0,sticky=W)

sabji = ttk.Checkbutton(foodFrame,text='Sabji',onvalue=1,offvalue=0,
                        variable=var4,command=sabji)
sabji.grid(row=3,column=0,sticky=W)

kebab = ttk.Checkbutton(foodFrame,text='Kebab',onvalue=1,offvalue=0,
                        variable=var5,command=kebab)
kebab.grid(row=4,column=0,sticky=W)

chawal = ttk.Checkbutton(foodFrame,text='Chawal',onvalue=1,offvalue=0,
                         variable=var6,command=chawal)
chawal.grid(row=5,column=0,sticky=W)

paneer = ttk.Checkbutton(foodFrame,text='Paneer',onvalue=1,offvalue=0,
                         variable=var7,command=paneer)
paneer.grid(row=6,column=0,sticky=W)

naan = ttk.Checkbutton(foodFrame,text='Naan',onvalue=1,offvalue=0,
                       variable=var8,command=naan)
naan.grid(row=7,column=0,sticky=W)

chole = ttk.Checkbutton(foodFrame,text='Chole',onvalue=1,offvalue=0,
                        variable=var9,command=chole)
chole.grid(row=8,column=0,sticky=W)

rajma = ttk.Checkbutton(foodFrame,text='Rajma',onvalue=1,offvalue=0,
                        variable=var10,command=rajma)
rajma.grid(row=9,column=0,sticky=W)

#Entry fields for food items

text1 = ttk.Entry(foodFrame,width=10,state=DISABLED,textvariable=e1)
text1.grid(row=0,column=1)

text2 = ttk.Entry(foodFrame,width=10,state=DISABLED,textvariable=e2)
text2.grid(row=1,column=1)

text3 = ttk.Entry(foodFrame,width=10,state=DISABLED,textvariable=e3)
text3.grid(row=2,column=1)

text4 = ttk.Entry(foodFrame,width=10,state=DISABLED,textvariable=e4)
text4.grid(row=3,column=1)

text5 = ttk.Entry(foodFrame,width=10,state=DISABLED,textvariable=e5)
text5.grid(row=4,column=1)

text6 = ttk.Entry(foodFrame,width=10,state=DISABLED,textvariable=e6)
text6.grid(row=5,column=1)

text7 = ttk.Entry(foodFrame,width=10,state=DISABLED,textvariable=e7)
text7.grid(row=6,column=1)

text8 = ttk.Entry(foodFrame,width=10,state=DISABLED,textvariable=e8)
text8.grid(row=7,column=1)

text9 = ttk.Entry(foodFrame,width=10,state=DISABLED,textvariable=e9)
text9.grid(row=8,column=1)

text10 = ttk.Entry(foodFrame,width=10,state=DISABLED,textvariable=e10)
text10.grid(row=9,column=1)

#VARIABLES
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()

e11 = StringVar()
e12 = StringVar()
e13 = StringVar()
e14 = StringVar()
e15 = StringVar()
e16 = StringVar()
e17 = StringVar()
e18 = StringVar()
e19 = StringVar()
e20 = StringVar()

e11.set('0')
e12.set('0')
e13.set('0')
e14.set('0')
e15.set('0')
e16.set('0')
e17.set('0')
e18.set('0')
e19.set('0')
e20.set('0')

#------DRINKS
chai = ttk.Checkbutton(drinksFrame,text='Chai',onvalue=1,offvalue=0,variable=var11,command=chai)
chai.grid(row=0,column=0,sticky=W)

coffee = ttk.Checkbutton(drinksFrame,text='Coffee',onvalue=1,offvalue=0,variable=var12,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

pepsi = ttk.Checkbutton(drinksFrame,text='Pepsi',onvalue=1,offvalue=0,variable=var13,command=pepsi)
pepsi.grid(row=2,column=0,sticky=W)

limka = ttk.Checkbutton(drinksFrame,text='Limka',onvalue=1,offvalue=0,variable=var14,command=limka)
limka.grid(row=3,column=0,sticky=W)

faluda = ttk.Checkbutton(drinksFrame,text='Faluda',onvalue=1,offvalue=0,variable=var15,command=faluda)
faluda.grid(row=4,column=0,sticky=W)

soda = ttk.Checkbutton(drinksFrame,text='Soda',onvalue=1,offvalue=0,variable=var16,command=soda)
soda.grid(row=5,column=0,sticky=W)

lassi = ttk.Checkbutton(drinksFrame,text='Lassi',onvalue=1,offvalue=0,variable=var17,command=lassi)
lassi.grid(row=6,column=0,sticky=W)

shikanji= ttk.Checkbutton(drinksFrame,text='Shikanji',onvalue=1,offvalue=0,variable=var18,command=shikanji)
shikanji.grid(row=7,column=0,sticky=W)

frooti = ttk.Checkbutton(drinksFrame,text='Frooti',onvalue=1,offvalue=0,variable=var19,command=frooti)
frooti.grid(row=8,column=0,sticky=W)

mocha = ttk.Checkbutton(drinksFrame,text='Mocha',onvalue=1,offvalue=0,variable=var20,command=mocha)
mocha.grid(row=9,column=0,sticky=W)

#Entry fields for drink items

text11 = ttk.Entry(drinksFrame,width=10,state=DISABLED,textvariable=e11)
text11.grid(row=0,column=1)

text12 = ttk.Entry(drinksFrame,width=10,state=DISABLED,textvariable=e12)
text12.grid(row=1,column=1)

text13 = ttk.Entry(drinksFrame,width=10,state=DISABLED,textvariable=e13)
text13.grid(row=2,column=1)

text14 = ttk.Entry(drinksFrame,width=10,state=DISABLED,textvariable=e14)
text14.grid(row=3,column=1)

text15 = ttk.Entry(drinksFrame,width=10,state=DISABLED,textvariable=e15)
text15.grid(row=4,column=1)

text16 = ttk.Entry(drinksFrame,width=10,state=DISABLED,textvariable=e16)
text16.grid(row=5,column=1)

text17 = ttk.Entry(drinksFrame,width=10,state=DISABLED,textvariable=e17)
text17.grid(row=6,column=1)

text18 = ttk.Entry(drinksFrame,width=10,state=DISABLED,textvariable=e18)
text18.grid(row=7,column=1)

text19 = ttk.Entry(drinksFrame,width=10,state=DISABLED,textvariable=e19)
text19.grid(row=8,column=1)

text20 = ttk.Entry(drinksFrame,width=10,state=DISABLED,textvariable=e20)
text20.grid(row=9,column=1)

#VARIABLES
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = IntVar()
var30 = IntVar()

e21 = StringVar()
e22 = StringVar()
e23 = StringVar()
e24 = StringVar()
e25 = StringVar()
e26 = StringVar()
e27 = StringVar()
e28 = StringVar()
e29 = StringVar()
e30 = StringVar()

e21.set('0')
e22.set('0')
e23.set('0')
e24.set('0')
e25.set('0')
e26.set('0')
e27.set('0')
e28.set('0')
e29.set('0')
e30.set('0')

#------SNACKS
chips = ttk.Checkbutton(snacksFrame,text='Chips',onvalue=1,offvalue=0,variable=var21,command=chips)
chips.grid(row=0,column=0,sticky=W)

samosa = ttk.Checkbutton(snacksFrame,text='Samosa',onvalue=1,offvalue=0,variable=var22,command=samosa)
samosa.grid(row=1,column=0,sticky=W)

chillipot = ttk.Checkbutton(snacksFrame,text='Chilli Potato',onvalue=1,offvalue=0,variable=var23,command=chillipot)
chillipot.grid(row=2,column=0,sticky=W)

namkeen = ttk.Checkbutton(snacksFrame,text='Namkeen',onvalue=1,offvalue=0,variable=var24,command=namkeen)
namkeen.grid(row=3,column=0,sticky=W)

biscit = ttk.Checkbutton(snacksFrame,text='Biscuit',onvalue=1,offvalue=0,variable=var25,command=biscit)
biscit.grid(row=4,column=0,sticky=W)

poha = ttk.Checkbutton(snacksFrame,text='Poha',onvalue=1,offvalue=0,variable=var26,command=poha)
poha.grid(row=5,column=0,sticky=W)

idli = ttk.Checkbutton(snacksFrame,text='Idli',onvalue=1,offvalue=0,variable=var27,command=idli)
idli.grid(row=6,column=0,sticky=W)

peanuts= ttk.Checkbutton(snacksFrame,text='Peanuts',onvalue=1,offvalue=0,variable=var28,command=peanuts)
peanuts.grid(row=7,column=0,sticky=W)

sandwich = ttk.Checkbutton(snacksFrame,text='Sandwich',onvalue=1,offvalue=0,variable=var29,command=sandwich)
sandwich.grid(row=8,column=0,sticky=W)

chomin = ttk.Checkbutton(snacksFrame,text='Chowmin',onvalue=1,offvalue=0,variable=var30,command=chomin)
chomin.grid(row=9,column=0,sticky=W)

#Entry fields for Snack items

text21 = ttk.Entry(snacksFrame,width=10,state=DISABLED,textvariable=e21)
text21.grid(row=0,column=1)

text22 = ttk.Entry(snacksFrame,width=10,state=DISABLED,textvariable=e22)
text22.grid(row=1,column=1)

text23 = ttk.Entry(snacksFrame,width=10,state=DISABLED,textvariable=e23)
text23.grid(row=2,column=1)

text24 = ttk.Entry(snacksFrame,width=10,state=DISABLED,textvariable=e24)
text24.grid(row=3,column=1)

text25 = ttk.Entry(snacksFrame,width=10,state=DISABLED,textvariable=e25)
text25.grid(row=4,column=1)

text26 = ttk.Entry(snacksFrame,width=10,state=DISABLED,textvariable=e26)
text26.grid(row=5,column=1)

text27 = ttk.Entry(snacksFrame,width=10,state=DISABLED,textvariable=e27)
text27.grid(row=6,column=1)

text28 = ttk.Entry(snacksFrame,width=10,state=DISABLED,textvariable=e28)
text28.grid(row=7,column=1)

text29 = ttk.Entry(snacksFrame,width=10,state=DISABLED,textvariable=e29)
text29.grid(row=8,column=1)

text30 = ttk.Entry(snacksFrame,width=10,state=DISABLED,textvariable=e30)
text30.grid(row=9,column=1)

#variables
e31 = StringVar()
e32 = StringVar()
e33 = StringVar()
e34 = StringVar()
e35 = StringVar()
e36 = StringVar()


e31.set('0')
e32.set('0')
e33.set('0')
e34.set('0')
e35.set('0')
e36.set('0')


#-4----------Cost4labels & Entry fields----------------------##EFF0F1#000
labelCostofFood = Label(costFrame,text='Cost of Food:',bg='#EFF0F1',fg='#000',
                        font=('Helvetica',12,'bold'))
labelCostofFood.grid(row=0,column=0,padx=1,sticky=W,pady=5)
#1
textcostoffood = ttk.Entry(costFrame,width=21,state=NORMAL,textvariable=e31)
textcostoffood.grid(row=0,column=1,padx=1,pady=5)
#-----
labelCostofdrinks = Label(costFrame,text='Cost of Drinks:',bg='#EFF0F1',fg='#000',font=('Helvetica',12,'bold'))
labelCostofdrinks.grid(row=1,column=0,padx=1,sticky=W,pady=5)
#2
textcostofdrinks = ttk.Entry(costFrame,width=21,state=NORMAL,textvariable=e32)
textcostofdrinks.grid(row=1,column=1,padx=1,pady=5)
#-----
labelCostofsnacks = Label(costFrame,text='Cost of Snacks:',bg='#EFF0F1',fg='#000',font=('Helvetica',12,'bold'))
labelCostofsnacks.grid(row=2,column=0,padx=1,sticky=W,pady=5)
#3
textcostofsnacks = ttk.Entry(costFrame,width=21,state=NORMAL,textvariable=e33)
textcostofsnacks.grid(row=2,column=1,padx=1,pady=5)
#-----
labelsubtotal = Label(costFrame,text='Sub Total:',bg='#EFF0F1',fg='#000',font=('Helvetica',12,'bold'))
labelsubtotal.grid(row=0,column=2,padx=1,sticky=W,pady=5)
#4
textsubtotal = ttk.Entry(costFrame,width=21,state=NORMAL,textvariable=e34)
textsubtotal.grid(row=0,column=3,padx=1,pady=5)
#-----
labelservicetax = Label(costFrame,text='Service Tax:',bg='#EFF0F1',fg='#000',font=('Helvetica',12,'bold'))
labelservicetax.grid(row=1,column=2,padx=1,sticky=W,pady=5)
#5
textservicetax = ttk.Entry(costFrame,width=21,state=NORMAL,textvariable=e35)
textservicetax.grid(row=1,column=3,padx=1,pady=5)
#-----
labeltotalcost = Label(costFrame,text='Total Cost:',bg='#EFF0F1',fg='#000',font=('Helvetica',12,'bold'))
labeltotalcost.grid(row=2,column=2,padx=1,sticky=W,pady=5)
#6
texttotalcost = ttk.Entry(costFrame,width=21,state=NORMAL,textvariable=e36)
texttotalcost.grid(row=2,column=3,padx=1,pady=5)


#Buttons--------------------------IN BUTTON FRAME-----------------------------------------------------------------
buttonTotal = Button(buttonFrame,text='TOTAL',font=('Helvetica',9,'bold')
                 ,bd=4,width=14,fg='#EFF0F1',bg='#000',command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt = Button(buttonFrame,text='RECEIPT',font=('Helvetica',9,'bold')
                 ,bd=4,width=14,fg='#EFF0F1',bg='#000',command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave = Button(buttonFrame,text='SAVE',font=('Helvetica',9,'bold')
                 ,bd=4,width=14,fg='#EFF0F1',bg='#000',command=save)
buttonSave.grid(row=0,column=2)

buttonSend = Button(buttonFrame,text='SEND',font=('Helvetica',9,'bold')
                 ,bd=4,width=14,fg='#EFF0F1',bg='#000',command=send)
buttonSend.grid(row=0,column=3)

buttonReset = Button(buttonFrame,text='RESET',font=('Helvetica',9,'bold')
                 ,bd=4,width=14,fg='#EFF0F1',bg='#000',command=reset)
buttonReset.grid(row=0,column=4)

#TEXT AREA FOR RECEIPT-------------------------------------------------
textReceipt = Text(recieptFrame,bd=3,font=('Helvetica',12,'bold'),
                   width=64,height=13)
textReceipt.grid(row=0,column=0)


#Calc functions------------------------------------------------------------------------------------------------------------------------------------------------------
operator =''
def buttonClick(numbers):
    global operator
    operator = operator + numbers
    calcField.delete(0,END)
    calcField.insert(END,operator)
    
def clear():
    global operator
    operator = ''
    calcField.delete(0,END)
    
def ans():
    global operator
    result = str(eval(operator))
    calcField.delete(0,END)
    calcField.insert(0,result)
    operator = ''

#variable
#calctxt = StringVar()
#calctxt.set('0')
#CALCULATOR-----------------------------------------------------------------
calcField = ttk.Entry(calcFrame,width=80)
calcField.grid(row=0,column=0,columnspan=4)

#calc buttons row 1
button7 = Button(calcFrame,text='7',font=('Helvetica',12,'bold')
                 ,bd=4,width=13,fg='#EFF0F1',bg='#000',
                 command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8 = Button(calcFrame,text='8',font=('Helvetica',12,'bold'),bd=4,width=13,
                 fg='#EFF0F1',bg='#000',command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9 = Button(calcFrame,text='9',font=('Helvetica',12,'bold'),bd=4,
                 width=13,fg='#EFF0F1',bg='#000'
                 ,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonplus = Button(calcFrame,text='+',font=('Helvetica',12,'bold'),
                    bd=4,width=13,fg='#EFF0F1',bg='#000'
                    ,command=lambda:buttonClick('+'))
buttonplus.grid(row=1,column=3)

#calc buttons row 2
button4 = Button(calcFrame,text='4',font=('Helvetica',13,'bold')
                 ,bd=4,width=13,fg='#EFF0F1',bg='#000',
                 command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5 = Button(calcFrame,text='5',font=('Helvetica',13,'bold'),bd=4,
                 width=13,bg='#EFF0F1',fg='#000',
                 activebackground='#EFF0F1',
                 activeforeground='#000',command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6 = Button(calcFrame,text='6',font=('Helvetica',13,'bold'),bd=4
                 ,width=13,bg='#EFF0F1',fg='#000',
                 activebackground='#EFF0F1',
                 activeforeground='#000',command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonminus = Button(calcFrame,text='-',font=('Helvetica',13,'bold'),bd=4,width=13,
                     fg='#EFF0F1',bg='#000',command=lambda:buttonClick('-'))
buttonminus.grid(row=2,column=3)

#calc buttons row 3
button1 = Button(calcFrame,text='1',font=('Helvetica',13,'bold')
                 ,bd=4,width=13,fg='#EFF0F1',bg='#000'
                 ,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2 = Button(calcFrame,text='2',font=('Helvetica',13,'bold'),bd=4,width=13,
                 bg='#EFF0F1',fg='#000',activebackground='#EFF0F1',
                 activeforeground='#000',command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3 = Button(calcFrame,text='3',font=('Helvetica',13,'bold'),bd=4,width=13,
                 bg='#EFF0F1',fg='#000',activebackground='#EFF0F1',
                 activeforeground='#000',command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonmul = Button(calcFrame,text='*',font=('Helvetica',13,'bold'),
                   bd=4,width=13,fg='#EFF0F1',bg='#000',
                   command=lambda:buttonClick('*'))
buttonmul.grid(row=3,column=3)

#calc buttons row 4
buttonAns = Button(calcFrame,text='Ans',font=('Helvetica',13,'bold')
                 ,bd=4,width=13,fg='#EFF0F1',bg='#000',command=ans)
buttonAns.grid(row=4,column=0)

buttonClear = Button(calcFrame,text='Clear',font=('Helvetica',13,'bold'),bd=4,
                     width=13,fg='#EFF0F1',bg='#000',command=clear)
buttonClear.grid(row=4,column=1)

button0 = Button(calcFrame,text='0',font=('Helvetica',13,'bold'),bd=4,width=13,fg='#EFF0F1',bg='#000'
                 ,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv = Button(calcFrame,text='/',font=('Helvetica',13,'bold'),bd=4,width=13,fg='#EFF0F1',bg='#000'
                   ,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.mainloop()