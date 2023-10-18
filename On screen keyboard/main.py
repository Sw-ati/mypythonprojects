from tkinter import *
from tkinter import ttk
import ttkthemes

def select(value):
    if value=='Space':
        textArea.insert(INSERT,' ')
        
    elif value=='↲ Enter':
        textArea.insert(INSERT,'\n')
        
    elif value=='Tab ↦':
        textArea.insert(INSERT,'\t')
        
    elif value=='Del ↳':
        textArea.delete(1.0,END)
        
    elif value=='← Backs':
        i = textArea.get(1.0,END)
        newText = i[:-2]
        textArea.delete(1.0,END)
        textArea.insert(INSERT,newText)
      
    elif value=='Shift ↑':
       left_shift_buttons = ['~','!','@','$','%','%','^','&','*','(',')','-','=','← Backs','Del ↳',
           'Tab ↦','q','w','e','r','t','y','u','i','o','p',']','7','8','9',
           'Caps ⇧','a','s','d','f','g','h','j','k','l',';','↲ Enter','4','5','6',
           'Shift ↑','z','x','c','v','b','n','m','<','>','?','↑ Shift','1','2','3',
           'Space']
       varRow = 2
       varCol = 0
       for button in left_shift_buttons:
           command = lambda x=button: select(x)
           if button != 'Space':
               ttk.Button(root,text=button,width=9,command=command).grid(row=varRow,column=varCol)
               varCol+=1
               if varCol>14:
                    varCol = 0
                    varRow+=1
               else:
                    ttk.Button(root,text=button,width=60).grid(row=6,column=0,columnspan=15)
    
    elif value=='↑ Shift':
       right_shift_buttons = ['~','1','2','3','4','5','6','7','8','9','0','-','=','← Backs','Del ↳',
           'Tab ↦','q','w','e','r','t','y','u','i','o','p','[','7','8','9',
           'Caps ⇧','a','s','d','f','g','h','j','k','l',';','↲ Enter','4','5','6',
           'Shift ↑','z','x','c','v','b','n','m',',','.','/','↑ Shift','1','2','3',
           'Space']
       varRow = 2
       varCol = 0
       for button in right_shift_buttons:
           command = lambda x=button: select(x)
           if button != 'Space':
               ttk.Button(root,text=button,width=9,command=command).grid(row=varRow,column=varCol)
               varCol+=1
               if varCol>14:
                    varCol = 0
                    varRow+=1
               else:
                    ttk.Button(root,text=button,width=60).grid(row=6,column=0,columnspan=15)
    
    elif value=='Caps ⇩':
       caps_buttons = ['~','1','2','3','4','5','6','7','8','9','0','-','=','← Backs','Del ↳',
           'Tab ↦','Q','W','E','R','T','Y','U','I','O','P','[','7','8','9',
           'CAPS ⇧','A','S','D','F','G','H','J','K','L',';','↲ Enter','4','5','6',
           'Shift ↑','Z','X','C','V','B','N','M',',','.','/','↑ Shift','1','2','3',
           'Space']
       varRow = 2
       varCol = 0
       for button in caps_buttons:
           command = lambda x=button: select(x)
           if button != 'Space':
               ttk.Button(root,text=button,width=9,command=command).grid(row=varRow,column=varCol)
               varCol+=1
               if varCol>14:
                    varCol = 0
                    varRow+=1
               else:
                    ttk.Button(root,text=button,width=60).grid(row=6,column=0,columnspan=15)
                    
    elif value=='CAPS ⇧':
       CAPS_buttons = ['~','1','2','3','4','5','6','7','8','9','0','-','=','← Backs','Del ↳',
           'Tab ↦','q','w','e','r','t','y','u','i','o','p','[','7','8','9',
           'Caps ⇩','a','s','d','f','g','h','j','k','l',';','↲ Enter','4','5','6',
           'Shift ↑','z','x','c','v','b','n','m',',','.','/','↑ Shift','1','2','3',
           'Space']
       varRow = 2
       varCol = 0
       for button in CAPS_buttons:
           command = lambda x=button: select(x)
           if button != 'Space':
               ttk.Button(root,text=button,width=9,command=command).grid(row=varRow,column=varCol)
               varCol+=1
               if varCol>14:
                    varCol = 0
                    varRow+=1
               else:
                    ttk.Button(root,text=button,width=60).grid(row=6,column=0,columnspan=15)

    else:
        textArea.insert(INSERT,value)

        
    textArea.focus_set()
    

root = ttkthemes.ThemedTk()
root.get_themes()

root.set_theme('radiance')

root.title('On Screen Keyboard')
root.resizable(False,False)


#title label
titleLabel = Label(root,text='On Screen Keyboard',font=('arial',25,'bold'))
titleLabel.grid(row=0,column=0,columnspan=15)

#text area 
textArea = Text(root,font=('arial',20,'bold'),height=10,width=100,bd=8,relief=GROOVE,insertbackground='grey')
textArea.grid(row=1,column=0,columnspan=15)


varRow = 2
varCol = 0
#buttons
buttons = ['~','1','2','3','4','5','6','7','8','9','0','-','=','← Backs','Del ↳',
           'Tab ↦','q','w','e','r','t','y','u','i','o','p','[','7','8','9',
           'Caps ⇩','a','s','d','f','g','h','j','k','l',';','↲ Enter','4','5','6',
           'Shift ↑','z','x','c','v','b','n','m',',','.','/','↑ Shift','1','2','3',
           'Space']

for button in buttons:
    command = lambda x=button: select(x)
    if button != 'Space':
        ttk.Button(root,text=button,width=9,command=command).grid(row=varRow,column=varCol)
        varCol+=1
        if varCol>14:
            varCol = 0
            varRow+=1
    else:
        ttk.Button(root,text=button,width=60).grid(row=6,column=0,columnspan=15)












root.mainloop()