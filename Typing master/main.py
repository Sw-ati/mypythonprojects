from tkinter import *
import random
import ttkthemes
from tkinter import ttk
from time import sleep
import threading
#if you want to execute multiple functions at same
# time then use concept of threading



#Functions------------------------------------------------------------
#command for exit button

def exit():
    root.destroy()

#command for start button
t = 0
totaltime = 60
wrongwords = 0
elaspedtimeinminutes = 0
def start_timer():
    global t
    startbutton.config(state=DISABLED)
    
    textArea.config(state=NORMAL)
    textArea.focus()
    
    #for elasped time and remaining time
    for t in range(1,61):
        elasped_time_label_value.config(text=t)
        remaining_time = totaltime-t
        remaining_time_label_text.config(text=remaining_time)
        sleep(1)
        root.update()

    textArea.config(state=DISABLED)
    resetbutton.config(state=NORMAL)

#to count total words
def count():
    global wrongwords
    global elaspedtimeinminutes
    while t!=totaltime:
        entered_paragraph = textArea.get(1.0,END).split()
        total_words = len(entered_paragraph)
         
    total_words_label_value.config(text=total_words)   
    
    para_words_list = label_paragraph['text'].split()
    
    #to count wrong words
    for pair in list(zip(para_words_list,entered_paragraph)):
        if pair[0]!=pair[1]:
            wrongwords+=1
    
    wrong_words_label_value.config(text=wrongwords)
    
    #for calc WPM
    elaspedtimeinminutes = t/60
    wpm = (total_words - wrongwords)/elaspedtimeinminutes
    wpm_count_label.config(text=wpm)
        
    #For Accuracy
    grossWPM = total_words/elaspedtimeinminutes
    accuracy = wpm/grossWPM*100
    accuracy = round(accuracy)
    accuracy_label_value.config(text=str(accuracy)+'%')
   
#command called in start button    
def start():
    #thread 1
    t1 = threading.Thread(target=start_timer)    
    t1.start()
    
    #thread 2
    t2 = threading.Thread(target=count)    
    t2.start()
    
        
#reset button
def reset():
    global t
    t=0
    global elaspedtimeinminutes
    elaspedtimeinminutes = 0
    startbutton.config(state=NORMAL)
    resetbutton.config(state=DISABLED)
    textArea.config(state=NORMAL)
    textArea.delete(1.0,END)
    textArea.config(state=DISABLED)
    
    elasped_time_label_value.config(text='0')
    remaining_time_label_text.config(text='60')
    accuracy_label_value.config(text='0')
    wpm_count_label.config(text='0')
    total_words_label_value.config(text='0')
    wrong_words_label_value.config(text='0')
    





################################-----------GUI PART-----------#########################
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('breeze')
root.geometry('940x775+400+110')
root.configure(bg='#fff')
root.resizable(False,False)
root.overrideredirect(True)


#Mainnframe-------------------------------------------------------------
mainframe = Frame(root,bg='white')
mainframe.grid()

#title frame------------------------------------------------------------
titleframe = Frame(mainframe,bg='black')
titleframe.grid()

titlelabel = Label(titleframe,text="TYPING MASTER",font=('Helvetica',23,'bold'),bg='#2596be',
                   fg='white',width=50,relief=RAISED,bd=2)
titlelabel.grid(pady=5)


#paragraph frame------------------------------------------------------
paragraph_frame = Frame(mainframe,bg='white')
paragraph_frame.grid(row=1,column=0,padx=5)

paragraph_list = ['India and UAE have built a strong connection over time, and it includes things like their shared history, culture, and economy. As they both deal with the challenges of today’s world, their partnership has gotten stronger and brought new chances for them to work together.',
                  'In the quest for economic growth, countries have long relied on natural resources, which has led to environmental degradation and climate change. Green growth, however, offers an alternative approach that seeks to balance economic growth with environmental sustainability. ',
                  'Adventure tourism is a type of tourism that involves activities that are challenging and often require physical hard work. It goes beyond traditional sightseeing or relaxation, focusing on providing thrilling and adventurous experiences to participants. It includes activities such as trekking, mountaineering, white water rafting, paragliding, scuba diving, and wildlife safaris. ',
                  '3D printing, also known as additive manufacturing, is the process of creating three-dimensional objects from a digital file. It involves building the object layer by layer using materials such as plastics, metals, and ceramics. ',
                  'There are so many real-life examples where one person made a difference. For example, Hungarian physician and scientist, Ignaz Semmelweis invented the concept of handwashing in the year 1847 to prevent the spread of diseases.',
                  'Medical tourism is the practice of travelling to another country to receive medical treatment. This can be done for a variety of reasons, including cost, access to specialized care, or a desire to receive care in a more relaxed environment.',
                  'In today’s fast-changing world, we face complex problems like poverty, inequality, climate change, and environmental degradation. To tackle these challenges and make a better future for everyone, the international community came together to work on a plan called the Sustainable Development Goals (SDGs). ']
random.shuffle(paragraph_list)


label_paragraph = Label(paragraph_frame,text=paragraph_list[0],wraplength=912,justify=CENTER,font=('arial',14,'bold'),bg='white')
label_paragraph.grid(row=0,column=0,padx=10)


#text area frame------------------------------------------------------
textAreaFrame = Frame(mainframe,bg='white')
textAreaFrame.grid(row=2,column=0,padx=5)

textArea = Text(textAreaFrame,font=('arial',12,'bold'),width=100,height=8,bd=4,relief=SUNKEN,wrap=WORD,
                insertbackground='#2596be',fg='#2596be',state=DISABLED)
textArea.grid(pady=8)

#Output Frame---------------------------------------------------------
frame_output  = Frame(mainframe,bg='white')
frame_output.grid(row=3,column=0,padx=3)

#elasped time label
elasped_time_label = Label(frame_output,text='Elasped Time:',font=('Tahoma',12,'bold'),fg='violet red',bg='white')
elasped_time_label.grid(row=0,column=0,padx=5)
#elasped time value
elasped_time_label_value = Label(frame_output,text='0',font=('Tahoma',12,'bold'),fg='black',bg='white')
elasped_time_label_value.grid(row=0,column=1,padx=5)

#reamining time label
remaining_time_label = Label(frame_output,text='Remaining Time:',font=('Tahoma',12,'bold'),fg='violet red',bg='white')
remaining_time_label.grid(row=0,column=2,padx=5)
#remaining time value
remaining_time_label_text = Label(frame_output,text='60',font=('Tahoma',12,'bold'),fg='black',bg='white')
remaining_time_label_text.grid(row=0,column=3,padx=5)

#wpm label
wpm_label = Label(frame_output,text='WPM:',font=('Tahoma',12,'bold'),fg='violet red',bg='white')
wpm_label.grid(row=0,column=4,padx=5)
#wpm label value
wpm_count_label = Label(frame_output,text='0',font=('Tahoma',12,'bold'),fg='black',bg='white')
wpm_count_label.grid(row=0,column=5,padx=5)

#accuracy label
accuracy_label = Label(frame_output,text='Accuracy:',font=('Tahoma',12,'bold'),fg='violet red',bg='white')
accuracy_label.grid(row=0,column=6,padx=5)
#accuracy label value
accuracy_label_value = Label(frame_output,text='0',font=('Tahoma',12,'bold'),fg='black',bg='white')
accuracy_label_value.grid(row=0,column=7,padx=5)

#total words label
total_words_label = Label(frame_output,text='Total Words:',font=('Tahoma',12,'bold'),fg='violet red',bg='white')
total_words_label.grid(row=0,column=8,padx=5)
#total words label value
total_words_label_value = Label(frame_output,text='0',font=('Tahoma',12,'bold'),fg='black',bg='white')
total_words_label_value.grid(row=0,column=9,padx=5)

#total words label
wrong_words_label = Label(frame_output,text='Wrong Words:',font=('Tahoma',12,'bold'),fg='violet red',bg='white')
wrong_words_label.grid(row=0,column=10,padx=5)
#total words label value
wrong_words_label_value = Label(frame_output,text='0',font=('Tahoma',12,'bold'),fg='black',bg='white')
wrong_words_label_value.grid(row=0,column=11,padx=5)

#buttons_frame--------------------------------------------------------
buttons_frame = Frame(mainframe,bg='white')
buttons_frame.grid(row=4,column=0)
#buttons

#startbutton
startbutton = ttk.Button(buttons_frame,text='START',command=start)
startbutton.grid(row=0,column=0,padx=20,pady=15)

#resetbutton
resetbutton = ttk.Button(buttons_frame,text='RESET',
                         state=DISABLED,command=reset)
resetbutton.grid(row=0,column=1,padx=20,pady=15)

#Exit button
Exitbutton = ttk.Button(buttons_frame,text='EXIT',command=exit)
Exitbutton.grid(row=0,column=2,padx=20,pady=15)

#Keyboard Frame-------------------------------------------------------
keyboard_frame = Frame(mainframe,bg='black')
keyboard_frame.grid(row=5,column=0)

#--------------frame 1  inside keyboard frame for keys 1 to 0-----------------
frame1to0 = Frame(keyboard_frame,bg='black')
frame1to0.grid(row=0,column=0)

#list1to0 = ['1','2','3','4','5','6','7','8','9','0']
label1 = Label(frame1to0,text='1',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)
label2 = Label(frame1to0,text='2',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)
label3 = Label(frame1to0,text='3',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
label4 = Label(frame1to0,text='4',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
label5 = Label(frame1to0,text='5',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
label6 = Label(frame1to0,text='6',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
label7 = Label(frame1to0,text='7',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
label8 = Label(frame1to0,text='8',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)

label9 = Label(frame1to0,text='9',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)

label10 = Label(frame1to0,text='0',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)
label1.grid(row=0,column=1,padx=5,pady=3)
label2.grid(row=0,column=2,padx=5,pady=3)
label3.grid(row=0,column=3,padx=5,pady=3)
label4.grid(row=0,column=4,padx=5,pady=3)
label5.grid(row=0,column=5,padx=5,pady=3)
label6.grid(row=0,column=6,padx=5,pady=3)
label7.grid(row=0,column=7,padx=5,pady=3)
label8.grid(row=0,column=8,padx=5,pady=3)
label9.grid(row=0,column=9,padx=5,pady=3)
label10.grid(row=0,column=10,padx=5,pady=3)





#--------------frame 2  i10ide keyboard frame for keys q to p-----------------
frameqtop = Frame(keyboard_frame,bg='black')
frameqtop.grid(row=1,column=0)


#listqtop = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
labelq = Label(frameqtop,text='Q',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)
labelw = Label(frameqtop,text='W',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)
labele = Label(frameqtop,text='E',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labelr = Label(frameqtop,text='R',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labelt = Label(frameqtop,text='T',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labely = Label(frameqtop,text='Y',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labelu = Label(frameqtop,text='U',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labeli = Label(frameqtop,text='I',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)

labelo = Label(frameqtop,text='O',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)

labelp = Label(frameqtop,text='P',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)
labelq.grid(row=0,column=1,padx=5,pady=3)
labelw.grid(row=0,column=2,padx=5,pady=3)
labele.grid(row=0,column=3,padx=5,pady=3)
labelr.grid(row=0,column=4,padx=5,pady=3)
labelt.grid(row=0,column=5,padx=5,pady=3)
labely.grid(row=0,column=6,padx=5,pady=3)
labelu.grid(row=0,column=7,padx=5,pady=3)
labeli.grid(row=0,column=8,padx=5,pady=3)
labelo.grid(row=0,column=9,padx=5,pady=3)
labelp.grid(row=0,column=10,padx=5,pady=3)


#--------------frame 3 inside keyboard frame for keys a to l-----------------
frameatol = Frame(keyboard_frame,bg='black')
frameatol.grid(row=2,column=0)

#listatol = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
labela = Label(frameatol,text='A',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)
labels = Label(frameatol,text='S',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)
labeld = Label(frameatol,text='D',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labelf = Label(frameatol,text='F',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labelg = Label(frameatol,text='G',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labelh = Label(frameatol,text='H',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labelj = Label(frameatol,text='J',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labelk = Label(frameatol,text='K',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)
labell = Label(frameatol,text='L',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)

labela.grid(row=0,column=1,padx=5,pady=3)
labels.grid(row=0,column=2,padx=5,pady=3)
labeld.grid(row=0,column=3,padx=5,pady=3)
labelf.grid(row=0,column=4,padx=5,pady=3)
labelg.grid(row=0,column=5,padx=5,pady=3)
labelh.grid(row=0,column=6,padx=5,pady=3)
labelj.grid(row=0,column=7,padx=5,pady=3)
labelk.grid(row=0,column=8,padx=5,pady=3)
labell.grid(row=0,column=9,padx=5,pady=3)


#--------------frame 4 inside keyboard frame for keys z to m-----------------
frameztom = Frame(keyboard_frame,bg='black')
frameztom.grid(row=3,column=0)

#listztom = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
labelz = Label(frameztom,text='Z',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)
labelx = Label(frameztom,text='X',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=5,height=2,
                bd=5,relief=RAISED)
labelc = Label(frameztom,text='C',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labelv = Label(frameztom,text='V',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labelb = Label(frameztom,text='B',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labeln = Label(frameztom,text='N',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labelm = Label(frameztom,text='M',bg='#2596be',fg='#fff',
              font=('arial',12,'bold'),width=5,height=2,
              bd=5,relief=RAISED)
labelz.grid(row=0,column=1,padx=5,pady=3)
labelx.grid(row=0,column=2,padx=5,pady=3)
labelc.grid(row=0,column=3,padx=5,pady=3)
labelv.grid(row=0,column=4,padx=5,pady=3)
labelb.grid(row=0,column=5,padx=5,pady=3)
labeln.grid(row=0,column=6,padx=5,pady=3)
labelm.grid(row=0,column=7,padx=5,pady=3)



#--------------frame 5 inside keyboard frame for Space Key-----------------
frameSpace = Frame(keyboard_frame,bg='black')
frameSpace.grid(row=4,column=0)

label_space_key = Label(frameSpace,text='SPACE',bg='#2596be',fg='#fff',
                font=('arial',12,'bold'),width=35,height=2,
                bd=5,relief=RAISED)
label_space_key.grid(row=0,column=0,padx=5,pady=3)

space_label = [label_space_key]

label_numbers = [label1,label2,label3,label4,label5,label6,label7,label8,label9,label10]

label_alphabets = [labela, labelb, labelc, labeld, labele, labelf, labelg, labelh, labeli, labelj, labelk, labell, 
 labelm, labeln, labelo, labelp, labelq, labels, labelr, labelt, labelu, labelv, labelw, labelx, labely, labelz]

binding_numbers = ['1','2','3','4','5','6','7','8','9','0']

binding_capital_alphabets = ['A','B' ,'C','D', 'E', 'F', 'G', 'H','I','J','K', 'L','M',
            'N','O', 'P','Q','S' , 'R', 'T', 'U', 'V', 'W', 'X', 'Y','Z']

binding_small_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                           'n', 'o', 'p', 'q', 's', 'r', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def changeBG(widget):
    widget.config(bg='violet red')
    widget.after(100,lambda:widget.config(bg='#2596be'))
    
for n in range(len(binding_numbers)):
    root.bind(binding_numbers[n],lambda event,label=label_numbers[n]:changeBG(label))
    
for n2 in range(len(binding_capital_alphabets)):
    root.bind(binding_capital_alphabets[n2],lambda event,label=label_alphabets[n2]:changeBG(label))

for n3 in range(len(binding_small_alphabets)):
    root.bind(binding_small_alphabets[n3],lambda event,label=label_alphabets[n3]:changeBG(label))

root.bind('<space>',lambda event:changeBG(space_label[0]))
root.mainloop()