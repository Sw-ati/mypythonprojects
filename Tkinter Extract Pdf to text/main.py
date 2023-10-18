import tkinter, PyPDF2
from tkinter import *
from tkinter import filedialog


#openFile Command in button open file
def openFile():
    filename = filedialog.askopenfilename(title='Open PDF file',
                                          initialdir='c:\\Users\\SWATI RAJ\\Desktop\\python resume projects\\Tkinter Extract Pdf to text',
                                          filetypes=[('PDF files','*.pdf')])
    print(filename)
    
    filename_label.configure(text=filename)
    
    outputfile_text.delete("1.0",tkinter.END)
   
    reader = PyPDF2.PdfReader(filename)
    for i in range(reader.numPages):
        current_text = reader.getPage(i).extractText()
        outputfile_text.insert(tkinter.END, current_text)
        #print(current_text)
    
    
    
    


root = tkinter.Tk()
root.title("PDF Text Extractor")

#widgets used
filename_label = Label(root, text="No File Selected")
outputfile_text = Text(root)
openfile_button = Button(root,text="Open PDF File",command=openFile)

#their place in root window
filename_label.pack()
outputfile_text.pack()
openfile_button.pack()

root.mainloop()