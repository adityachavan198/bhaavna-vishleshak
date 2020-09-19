from tkinter import *
from dbn_neuralnet import *
from ResourceBasedSentimentClassification import *
import tkinter.messagebox

def addNumbers():
    myText.set("Calculating")
    tkinter.messagebox.showinfo("Alert Message", "This may take time")
    # res = test_with_unigram_tf_dbn()[0]
    # res = sentiment("मैं इस उत्पाद से बहुत खुश हूँ  यह आराम दायक और सुन्दर है  यह खरीदने लायक है ")
    res = sentiment(str(e1.get()))
    myText.set(res)
 
master = Tk()
myText=StringVar()
Label(master, text="First").grid(row=0, sticky=W)
# Label(master, text="Second").grid(row=1, sticky=W)
Label(master, text="Result:").grid(row=3, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
 
e1 = Entry(master)
# e2 = Entry(master)
 
e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
 
b = Button(master, text="Calculate", command=addNumbers)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
 
mainloop()