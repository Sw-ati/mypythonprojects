from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init() #creating instance of engine class

voice = engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)


#get_close_matches(word,possibilities,n,cutoff)
  
#-----------------------------------Functionality Part-----------------------------------------------------

#for search button
def search():
    data = json.load(open('data.json'))
    #print(data)
    enterword = enterwordEntry.get()
    #print(enterword)
    enterword.lower()
    if enterword in data:
        meaning = data[enterword]
        #print(meaning)
        #textArea.insert(END,meaning)
        textArea.delete(1.0,END)
        for item in meaning:
            textArea.insert(END, u'\u2022' + item + '\n\n')
    elif len(get_close_matches(enterword,data.keys()))>0:
        close_match = get_close_matches(enterword,data.keys())[0]
        res = messagebox.askyesno('Confirm','Did you mean '+close_match+' instead ?')
        #print(close_match)
        #print(res)
        if res == True:
            enterwordEntry.delete(0,END)
            enterwordEntry.insert(END,close_match)
            
            meaning = data[close_match]
            
            textArea.delete(1.0,END)
            
            for item in meaning:
                textArea.insert(END,u'\u2022' +item + '\n\n')
        else:
            messagebox.showerror('Error',"The word doesn't exist, Please double check it")
            enterwordEntry.delete(0,END)     
            textArea.delete(1.0,END)

    else:
        messagebox.showinfo('Information',"The word doesn't exits") 
        enterwordEntry.delete(0,END)     
        textArea.delete(1.0,END)


#for exit button
def exit():
    res = messagebox.askyesno('Confirm','Do you want to exit?')
    if res==True:
        root.destroy()
        
    else:
        pass
        
    #root.quit()
        
#for clear button
def clearall():
    enterwordEntry.delete(0,END)
    textArea.delete(1.0,END)   
        

#entry field word to audio
def wordAudio():
    engine.say(enterwordEntry.get())
    engine.runAndWait()
    
#meaning text area audio
def meaningAudio():
    engine.say(textArea.get(1.0,END))
    engine.runAndWait()
    






#----------------------------------------GUI PART------------------------------------------------------
root = Tk()
root.geometry('1000x626+500+150')
root.title('Talking Dictionary')
root.resizable(False,False)

#bg Image 
bgImage = PhotoImage(file='bg1.png')
bglabel = Label(root,image=bgImage)
bglabel.place(x=0,y=0)

#enter word label
enterwordLabel = Label(root,text='Enter Word',font=('castellar',29,'bold'),fg='maroon',bg='whitesmoke')
enterwordLabel.place(x=630,y=40)

#enterwordEntry
enterwordEntry = Entry(root,font=('arial',25,'bold'),fg='maroon',justify=CENTER,bd=6,relief=GROOVE,insertbackground='maroon')
enterwordEntry.place(x=600,y=100)

#searchImage button
searchImage = PhotoImage(file='search.png')
searchButton = Button(root,image=searchImage,bd=0,bg='whitesmoke',
                      fg='whitesmoke',cursor='hand2',command=search)
searchButton.place(x=690,y=170)

#micImage button
micImage = PhotoImage(file='mic3.png')
micButton = Button(root,image=micImage,bd=0,bg='whitesmoke',
                   fg='whitesmoke',cursor='hand2',command=wordAudio)
micButton.place(x=790,y=170)


#meaning label
meaningLabel = Label(root,text='Meaning',font=('castellar',35,'bold'),fg='maroon',bg='whitesmoke')
meaningLabel.place(x=420,y=240)

#meaningTextArea
textArea = Text(root,width=55,height=8,font=('arial',16,'bold'),fg='maroon',bg='whitesmoke',insertbackground='maroon',bd=6,relief=GROOVE)
textArea.place(x=230,y=305)

#audioImage
audioImage = PhotoImage(file='mic3.png')
audioButton = Button(root,image=audioImage,bd=0,bg='whitesmoke',
                     fg='whitesmoke',cursor='hand2',command=meaningAudio)
audioButton.place(x=390,y=540)

#clear all Image
clearImage = PhotoImage(file='clear2.png')
clearButton = Button(root,image=clearImage,bd=0,bg='whitesmoke',
                     fg='whitesmoke',cursor='hand2',command=clearall)
clearButton.place(x=490,y=540)

#exit  Image
exitImage = PhotoImage(file='exit1.png')
exitButton = Button(root,image=exitImage,bd=0,bg='whitesmoke',
                    fg='whitesmoke',cursor='hand2',command=exit)
exitButton.place(x=590,y=540)

#enter function invokes search button
def enter_function(event):
    searchButton.invoke()

#binding enter button on keyboard
root.bind('<Return>',enter_function)

root.mainloop()