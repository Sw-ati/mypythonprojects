from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import openpyxl
import os


#enter data function 
def enter_data():
    accepted = accecpt_var.get()
    if accepted=="Accepted":
        #userInfo
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        if firstname and lastname:
            titlename = title_combo_box.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            
            #Course Info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()
            
            print("----------User's Info Are Displayed Below!----------")
            print("First Name: {} \nLast Name: {} \nTitle: {} \nAge: {} \nNationality: {}"
                .format(firstname,lastname,titlename,age,nationality))
            print("----------Courses Info Are Displayed Below!----------")
            print("Completed Courses: {} \nSemesters: {}"
                .format(numcourses,numsemesters))
            print("Registration Status: ",registration_status)
            print("----------------------------------------------------------")
        else:
            messagebox.showwarning("Error","First name and Last name are required!")
         
        #Working with data entry in excel workbook   
        filepath = "C:\\Users\\SWATI RAJ\\Desktop\\python resume projects\\Data Entry GUI\\data.xlsx"
    
        if not os.path.exists(filepath):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            heading = ["First Name","Last Name","Title","Age"
                   ,"Nationality","# Courses","# Semesters", "Registraton Status"]
            sheet.append(heading)
            workbook.save(filepath)
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        sheet.append([firstname,lastname,titlename,age,nationality,
                      numcourses,numsemesters,registration_status])
        workbook.save(filepath)

    else:
        messagebox.showwarning("Error","Not Accepted the terms & Conditions!")  

    



window =Tk()
window.title("Data Entry Form")
window.resizable(False,False)
window.config(bg="RoyalBlue1")


frame = Frame(window,bg="RoyalBlue1")
frame.pack()


#Saving User Info
user_info_frame = LabelFrame(frame,text="User Information:",bg="RoyalBlue1",bd=0,font=("Helvetica","20"),fg="#fff")
user_info_frame.grid(row=0,column=0,padx=20, pady=10,sticky="w")

#first name label
first_name_label = Label(user_info_frame,text="First Name",bd=0,font=("Helvetica","18"),bg="RoyalBlue1",fg="#fff")
first_name_label.grid(row=0,column=0)
#last name label
last_name_label = Label(user_info_frame, text="Last Name",bd=0,font=("Helvetica","18"),bg="RoyalBlue1",fg="#fff")
last_name_label.grid(row=0,column=1)


#first name entry
first_name_entry = Entry(user_info_frame,bg="#fff",fg="#000",bd=0,insertbackground="#000",font=("Helvetica","13"))
first_name_entry.grid(row=1,column=0)
#last name entry
last_name_entry = Entry(user_info_frame,bg="#fff",fg="#000",bd=0,insertbackground="#000",font=("Helvetica","13"))
last_name_entry.grid(row=1,column=1)

#title label
title = Label(user_info_frame,text="Title",bd=0,font=("Helvetica","18"),bg="RoyalBlue1",fg="#fff")
title.grid(row=0,column=2)
#title ComboBox
title_combo_box = ttk.Combobox(user_info_frame,values = ["Mr.","Mrs.","Ms.","Dr."],background="#fff",foreground="#000",font=("Helvetica","13"))
title_combo_box.grid(row=1,column=2)

# age_label
age_label = Label(user_info_frame,text="Age",bd=0,font=("Helvetica","18"),bg="RoyalBlue1",fg="#fff")
age_label.grid(row=2,column=0)
# age spinbox
age_spinbox = Spinbox(user_info_frame, from_=18, to=100,bg="#fff",fg="#000",bd=0,font=("Helvetica","13"))
age_spinbox.grid(row=3,column=0)

#nationality label
nationality_label = Label(user_info_frame,text="Nationality",bd=0,font=("Helvetica","18"),bg="RoyalBlue1",fg="#fff")
nationality_label.grid(row=2,column=1)
#nationality Combobox
nationality_combobox = ttk.Combobox(user_info_frame,values=["Afghan","Albanian","Algerian","American","India"],font=("Helvetica","13"))
nationality_combobox.grid(row=3,column=1)

#for loop for grid widgets for spacing for user frame
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
# saving Course info Frame 2
courses_frame = LabelFrame(frame,text="Courses Information:",bg="RoyalBlue1",fg="#fff",bd=0,font=("Helvetica","20"))
courses_frame.grid(row=1,column=0,sticky="news",padx=20,pady=10)
 
#registered_label
registered_label = Label(courses_frame,text="# Registration Status",bd=0,font=("Helvetica","18"),bg="RoyalBlue1",fg="#fff")
registered_label.grid(row=0,column=0)

# registered_checkbox
reg_status_var = StringVar(value="Not Registered")
registered_check = Checkbutton(courses_frame,text="Currently Registered",font=("Helvetica","18"),
                               fg="#000",bg="RoyalBlue1",
                               activebackground="RoyalBlue1",
                               activeforeground="#000",variable=reg_status_var,
                               onvalue="Registered",offvalue="Not Registered")
registered_check.grid(row=1,column=0)

#numcoursesLabel
numcourses_label = Label(courses_frame,text="# Completed Courses",bd=0,font=("Helvetica","18"),bg="RoyalBlue1",fg="#fff")
numcourses_label.grid(row=0,column=1)
#numcourses Spinbox
numcourses_spinbox = Spinbox(courses_frame,from_=0, to="infinity",bg="#fff",fg="#000",bd=0,insertbackground="#000",font=("Helvetica","13"))
numcourses_spinbox.grid(row=1,column=1)


#numsemesters Label
numsemesters_label = Label(courses_frame,text="# Semesters",bd=0,font=("Helvetica","18"),bg="RoyalBlue1",fg="#fff")
numsemesters_label.grid(row=0,column=2)
#numsemesters Spinbox
numsemesters_spinbox = Spinbox(courses_frame,from_=0, to="infinity",bg="#fff",fg="#000",bd=0,insertbackground="#000",font=("Helvetica","13"))
numsemesters_spinbox.grid(row=1,column=2)

#for loop for grid widgets for spacing for courses frame
for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
#terms frame 3
terms_frame = LabelFrame(frame,text="Terms & Conditions:",bg="RoyalBlue1",fg="#fff",bd=0,font=("Helvetica","20"))
terms_frame.grid(row=2,column=0,sticky="news",padx=20,pady=10)

#terms check button
accecpt_var = StringVar(value="Not Accepted")
terms_check = Checkbutton(terms_frame,text="I Accept the Terms & Conditions",font=("Helvetica","18"),bg="RoyalBlue1",fg="#000"
                          ,activebackground="RoyalBlue1",
                          activeforeground="#000",variable=accecpt_var,
                          onvalue="Accepted",offvalue="Not Accepted")
terms_check.grid(row=0,column=0)

#enter data button
button = Button(frame, text="Enter Data",bg="#000",fg="#fff",bd=0,
                font=("Helvetica","16"),activebackground='#000',command=enter_data)
button.grid(row=3,column=0,sticky="news",padx=20,pady=10)
    
    
window.mainloop()