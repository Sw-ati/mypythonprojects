from tkinter import *
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime



def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name = first_name_entry.get()+last_name_entry.get()
    phone = phone_entry.get()
    subtotal = sum(item[3] for item in invoice_list)
    salestax = 0.1
    total =  subtotal*(1-salestax)
    
    doc.render({"name":name,
                "phone":phone,
                "invoice_list": invoice_list,
                "subtotal":subtotal,
                "salestax":str(salestax*100)+"%",
                "total":total})
    
    doc_name = 'new_invoice' + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)
    
    
#function for new invoice button
def new_invoice():
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    phone_entry.delete(0,END)
    clear_item()
    tree.delete(*tree.get_children())
    
    invoice_list.clear()
   
#function for clearing items
def clear_item():
    qty_spinbox.delete(0, END)
    qty_spinbox.insert(0,"1")
    desc_entry.delete(0, END)
    price_spinbox.delete(0, END)
    price_spinbox.insert(0,"0.0")
 
invoice_list = [] 
#function for add item button
def add_item():
    qty = int(qty_spinbox.get())
    desc = desc_entry.get()
    price = float(price_spinbox.get())
    line_total = qty*price
    invoice_item = [qty, desc, price, line_total]
    tree.insert('',0,values=invoice_item)
    clear_item()
    
    invoice_list.append(invoice_item)

#Tkinter_Window_application
window = Tk()
window.title("Invoice Generator Form")
#window.geometry("900x900+300+200")
window.config(bg="cyan4")
window.resizable(False,False)

frame = Frame(window)
frame.config(bg='cyan4')
frame.pack(padx=20,pady=10)

#Labels Row 0
first_name_label =Label(frame, text="First Name", font=("Helvetica",'16'), bd=0,background='cyan4',foreground='#fff')
first_name_label.grid(row=0,column=0)

last_name_label = Label(frame,text="Last Name", font=("Helvetica",'16'), bd=0,background='cyan4',foreground='#fff')
last_name_label.grid(row=0,column=1)

phone_label = Label(frame,text="Phone",  font=("Helvetica",'16'), bd=0,background='cyan4',foreground='#fff')
phone_label.grid(row=0,column=2)

#Entry Fields Row 1
first_name_entry = Entry(frame, border=0,background='cyan4',insertbackground='#fff',fg='#fff',font=("Helvetica",'13'))
first_name_entry.grid(row=1,column=0)
Frame(frame,width=180,height=2,bg='#fff').grid(row=2,column=0) #frame1 row 2

last_name_entry = Entry(frame,border=0,background='cyan4',insertbackground='#fff',fg='#fff',font=("Helvetica",'13'))
last_name_entry.grid(row=1,column=1)
Frame(frame,width=180,height=2,bg='#fff').grid(row=2,column=1) #frame2 row 2

phone_entry = Entry(frame, border=0,background='cyan4',insertbackground='#fff',fg='#fff',font=("Helvetica",'13'))
phone_entry.grid(row=1,column=2)
Frame(frame,width=180,height=2,bg='#fff').grid(row=2,column=2) #frame3 row 2

#Labels Row 4
qty_label = Label(frame,text="Qty",  font=("Helvetica",'16'), bd=0,background='cyan4',foreground='#fff')
qty_label.grid(row=4,column=0)

desc_label = Label(frame,text="Description",  font=("Helvetica",'16'), bd=0,background='cyan4',foreground='#fff')
desc_label.grid(row=4,column=1)

price_label = Label(frame,text="Unit Price",  font=("Helvetica",'16'), bd=0,background='cyan4',foreground='#fff')
price_label.grid(row=4,column=2)


#Entry and Spinbox Fields Row 5
qty_spinbox = Spinbox(frame, from_=1, to=100, border=0,insertbackground='cyan4',fg='cyan4',
                      bg='#fff',font=("Helvetica",'13'))
qty_spinbox.grid(row=5,column=0)
#Frame(frame,width=175,height=2,bg='#fff').grid(row=6,column=0) #frame1 row 6

desc_entry = Entry(frame,border=0, background='cyan4',insertbackground='#fff', fg='#fff',font=("Helvetica",'13'))
desc_entry.grid(row=5,column=1)
Frame(frame,width=180,height=2,bg='#fff').grid(row=6,column=1) #frame2 row 6

price_spinbox = Spinbox(frame,from_=0.0, to=500, increment=0.5,border=0, bg='#fff',insertbackground='cyan4',fg='cyan4',font=("Helvetica",'13'))
price_spinbox.grid(row=5,column=2)
#Frame(frame,width=175,height=2,bg='#fff').grid(row=6,column=2) #frame3 row 6



#Add Item Button
add_item_button = Button(frame, text="Add Items", command=add_item, bg='#fff',bd=0, fg='cyan4',font=("Helvetica",'16'),
                         activeforeground='#fff',activebackground='cyan4')
add_item_button.grid(row=7, column=0,columnspan=3, sticky="e",padx=20, pady=10)


# tree view the table we are adding in gui
#tuple used for columns
columns = ('qty', 'desc', 'price', 'total')
"""style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders"""

tree = ttk.Treeview(frame, columns=columns, show="headings") #style="mystyle.TreeView")


tree.heading('qty', text='Qty')
tree.heading('desc', text='Description')
tree.heading('price', text='Unit Price')
tree.heading('total', text='Total')
tree.grid(row=8, column=0, columnspan=3, padx=20, pady= 10)


#last two buttons
save_invoice_button = Button(frame, text='Generate Invoice', bg='#fff',bd=0, fg='cyan4',font=("Helvetica",'16'),
                             activeforeground='#fff',activebackground='cyan4',command=generate_invoice)
save_invoice_button.grid(row=9, column=0, columnspan=3, sticky="w",padx=20, pady=5)

new_invoice_button = Button(frame, text='Create New Invoice', command=new_invoice,
                             bg='#fff',bd=0, fg='cyan4',font=("Helvetica",'16'),activeforeground='#fff',activebackground='cyan4')
new_invoice_button.grid(row=9, column=0, columnspan=3, sticky="e",padx=20, pady=5)


window.mainloop()