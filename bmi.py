from tkinter import *

window=Tk()
window.title("BMI Calculator")
window.geometry('380x400')
window.configure(bg='lightcyan')

def calculateBMI():
    weight=int(weightEntry.get())
    height=int(heightEntry.get())/100
    bmi=weight/(height*height)
    bmi=round(bmi, 1)
    name=username.get()
    resultLabel.destroy()
    msg=''
    if bmi<18.5:
        msg='You are underweighted'
    
    elif bmi>18.5 and bmi<=24.9:
        msg='You are in the normal range'

    elif bmi>25 and bmi<=29.9:
        msg='You are overweighted'

    elif bmi>30:
        msg='You are obese'
    
    else:
        msg='Something went wrong'
    
    outputmsg=Label(resultFrame, text=name+', your BMI is '+str(bmi)+' and '+msg, bg='lightcyan', font=('Calibri', 12), width=42)
    outputmsg.place(x=20, y=40)
    outputmsg.pack()

appLabel=Label(window, text='BMI Calculator', fg='black', bg='lightcyan', font=('Calibri', 20), bd=5)
appLabel.place(x=50, y=20)

nameLabel=Label(window, text='Your Name', fg='black', bg='lightcyan', font=('Calibri', 12), bd=1)
nameLabel.place(x=20, y=90)

username=Entry(window, text='', bd=2, width=22)
username.place(x=150, y=92)

heightLabel=Label(window, text='Your Height (cm)', fg='black', bg='lightcyan', font=('Calibri', 12), bd=1)
heightLabel.place(x=20, y=140)

heightEntry=Entry(window, text='', bd=2, width=22)
heightEntry.place(x=150, y=142)

weightLabel=Label(window, text='Your Weight (kg)', fg='black', bg='lightcyan', font=('Calibri', 12), bd=1)
weightLabel.place(x=20, y=185)

weightEntry=Entry(window, text='', bd=2, width=22)
weightEntry.place(x=150, y=187)

calculateButton=Button(window, text='Calculate', fg='black', bg='cyan', bd=4, command=calculateBMI)
calculateButton.place(x=20, y=250)

resultFrame=LabelFrame(window, text='Result', fg='black', bg='lightcyan', font=('Calibri', 12))
resultFrame.pack(padx=20, pady=20)
resultFrame.place(x=20, y=300)

resultLabel=Label(resultFrame, text='', bg='lightcyan', font=('Calibri', 12), width=33)
resultLabel.place(x=20, y=20)
resultLabel.pack()

window.mainloop()