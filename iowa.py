from tkinter import *
from PIL import ImageTk,Image

root=Tk()
bg=PhotoImage(file='Photos/92ccba192b614b9faeeffe6841ab5c6d.png')
Settingbglabel=Label(root,image=bg).place(x=0,y=0)
test1=Label()
class Songs:
    def __init__(self,directory):
        self.directory=directory
        self.image=PhotoImage(file=directory)
def img_515():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    global test1
    test1.place_forget()
    button1=Button(root,text="515",state=DISABLED)
    button1.place(x=0,y=0)
    button2=Button(root,text="People=shit",command=peopleshit)
    button2.place(x=0,y=50)
    button3=Button(root,text="Disasterpiece",command=disaster)
    button3.place(x=0,y=100)
    button4=Button(root,text="My Plague",command=myplague)
    button4.place(x=0,y=150)
    button5=Button(root,text="Everything Ends",command=everything_ends)
    button5.place(x=0,y=200)
    button6=Button(root,text="Heretic Anthem",command=heretic_anthem)
    button6.place(x=0,y=250)
    button7=Button(root,text="Gently",command=gently)
    button7.place(x=0,y=300)
    button8=Button(root,text="Left Behind",command=left_behind)
    button8.place(x=0,y=350)
    button9=Button(root,text="The Shape",command=the_shape)
    button9.place(x=0,y=400)
    button10=Button(root,text="I Am Hated",command=i_am_hated)
    button10.place(x=0,y=450)
    button11=Button(root,text="Skin Ticket",command=skin_ticket)
    button11.place(x=0,y=500)
    button12=Button(root,text="New Abortion",command=new_abortion)
    button12.place(x=0,y=550)
    button13=Button(root,text="Metabolic",command=metabolic)
    button13.place(x=0,y=600)
    button14=Button(root,text="IOWA",command=iowa_song)
    button14.place(x=0,y=650)

    test1=Label(image=firstphoto)
    test1.place(x=100,y=50)

    
def peopleshit():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    global test1
    test1.place_forget()
    button1=Button(root,text="515",command=img_515)
    button1.place(x=0,y=0)
    
    button2=Button(root,text="People=shit",state=DISABLED)
    button2.place(x=0,y=50)
    button3=Button(root,text="Disasterpiece",command=disaster)
    button3.place(x=0,y=100)
    button4=Button(root,text="My Plague",command=myplague)
    button4.place(x=0,y=150)
    button5=Button(root,text="Everything Ends",command=everything_ends)
    button5.place(x=0,y=200)
    button6=Button(root,text="Heretic Anthem",command=heretic_anthem)
    button6.place(x=0,y=250)
    button7=Button(root,text="Gently",command=gently)
    button7.place(x=0,y=300)
    button8=Button(root,text="Left Behind",command=left_behind)
    button8.place(x=0,y=350)
    button9=Button(root,text="The Shape",command=the_shape)
    button9.place(x=0,y=400)
    button10=Button(root,text="I Am Hated",command=i_am_hated)
    button10.place(x=0,y=450)
    button11=Button(root,text="Skin Ticket",command=skin_ticket)
    button11.place(x=0,y=500)
    button12=Button(root,text="New Abortion",command=new_abortion)
    button12.place(x=0,y=550)
    button13=Button(root,text="Metabolic",command=metabolic)
    button13.place(x=0,y=600)
    button14=Button(root,text="IOWA",command=iowa_song)
    button14.place(x=0,y=650)

    test1=Label(image=secondphoto)
    test1.place(x=100,y=50)
def disaster():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    global test1
    test1.place_forget()
    button1=Button(root,text="515",command=img_515)
    button1.place(x=0,y=0)
    
    button2=Button(root,text="People=shit",command=peopleshit)
    button2.place(x=0,y=50)
    button3=Button(root,text="Disasterpiece",state=DISABLED)
    button3.place(x=0,y=100)
    button4=Button(root,text="My Plague",command=myplague)
    button4.place(x=0,y=150)
    button5=Button(root,text="Everything Ends",command=everything_ends)
    button5.place(x=0,y=200)
    button6=Button(root,text="Heretic Anthem",command=heretic_anthem)
    button6.place(x=0,y=250)
    button7=Button(root,text="Gently",command=gently)
    button7.place(x=0,y=300)
    button8=Button(root,text="Left Behind",command=left_behind)
    button8.place(x=0,y=350)
    button9=Button(root,text="The Shape",command=the_shape)
    button9.place(x=0,y=400)
    button10=Button(root,text="I Am Hated",command=i_am_hated)
    button10.place(x=0,y=450)
    button11=Button(root,text="Skin Ticket",command=skin_ticket)
    button11.place(x=0,y=500)
    button12=Button(root,text="New Abortion",command=new_abortion)
    button12.place(x=0,y=550)
    button13=Button(root,text="Metabolic",command=metabolic)
    button13.place(x=0,y=600)
    button14=Button(root,text="IOWA",command=iowa_song)
    button14.place(x=0,y=650)

    test1=Label(image=thirdphoto)
    test1.place(x=100,y=50)
    
def myplague():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    global test1
    test1.place_forget()
    button1=Button(root,text="515",command=img_515)
    button1.place(x=0,y=0)
    
    button2=Button(root,text="People=shit",command=peopleshit)
    button2.place(x=0,y=50)
    button3=Button(root,text="Disasterpiece",command=disaster)
    button3.place(x=0,y=100)
    button4=Button(root,text="My Plague",state=DISABLED)
    button4.place(x=0,y=150)
    button5=Button(root,text="Everything Ends",command=everything_ends)
    button5.place(x=0,y=200)
    button6=Button(root,text="Heretic Anthem",command=heretic_anthem)
    button6.place(x=0,y=250)
    button7=Button(root,text="Gently",command=gently)
    button7.place(x=0,y=300)
    button8=Button(root,text="Left Behind",command=left_behind)
    button8.place(x=0,y=350)
    button9=Button(root,text="The Shape",command=the_shape)
    button9.place(x=0,y=400)
    button10=Button(root,text="I Am Hated",command=i_am_hated)
    button10.place(x=0,y=450)
    button11=Button(root,text="Skin Ticket",command=skin_ticket)
    button11.place(x=0,y=500)
    button12=Button(root,text="New Abortion",command=new_abortion)
    button12.place(x=0,y=550)
    button13=Button(root,text="Metabolic",command=metabolic)
    button13.place(x=0,y=600)
    button14=Button(root,text="IOWA",command=iowa_song)
    button14.place(x=0,y=650)

    test1=Label(image=fourthphoto)
    test1.place(x=100,y=50)

def everything_ends():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    global test1
    test1.place_forget()
    button1=Button(root,text="515",command=img_515)
    button1.place(x=0,y=0)
    
    button2=Button(root,text="People=shit",command=peopleshit)
    button2.place(x=0,y=50)
    button3=Button(root,text="Disasterpiece",command=disaster)
    button3.place(x=0,y=100)
    button4=Button(root,text="My Plague",command=myplague)
    button4.place(x=0,y=150)
    button5=Button(root,text="Everything Ends",state=DISABLED)
    button5.place(x=0,y=200)
    button6=Button(root,text="Heretic Anthem",command=heretic_anthem)
    button6.place(x=0,y=250)
    button7=Button(root,text="Gently",command=gently)
    button7.place(x=0,y=300)
    button8=Button(root,text="Left Behind",command=left_behind)
    button8.place(x=0,y=350)
    button9=Button(root,text="The Shape",command=the_shape)
    button9.place(x=0,y=400)
    button10=Button(root,text="I Am Hated",command=i_am_hated)
    button10.place(x=0,y=450)
    button11=Button(root,text="Skin Ticket",command=skin_ticket)
    button11.place(x=0,y=500)
    button12=Button(root,text="New Abortion",command=new_abortion)
    button12.place(x=0,y=550)
    button13=Button(root,text="Metabolic",command=metabolic)
    button13.place(x=0,y=600)
    button14=Button(root,text="IOWA",command=iowa_song)
    button14.place(x=0,y=650)

    test1=Label(image=fifthphoto)
    test1.place(x=100,y=50)
    
def heretic_anthem():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    global test1
    test1.place_forget()
    button1=Button(root,text="515",command=img_515)
    button1.place(x=0,y=0)
    button2=Button(root,text="People=shit",command=peopleshit)
    button2.place(x=0,y=50)
    button3=Button(root,text="Disasterpiece",command=disaster)
    button3.place(x=0,y=100)
    button4=Button(root,text="My Plague",command=myplague)
    button4.place(x=0,y=150)
    button5=Button(root,text="Everything Ends",command=everything_ends)
    button5.place(x=0,y=200)
    button6=Button(root,text="Heretic Anthem",state=DISABLED)
    button6.place(x=0,y=250)
    button7=Button(root,text="Gently",command=gently)
    button7.place(x=0,y=300)
    button8=Button(root,text="Left Behind",command=left_behind)
    button8.place(x=0,y=350)
    button9=Button(root,text="The Shape",command=the_shape)
    button9.place(x=0,y=400)
    button10=Button(root,text="I Am Hated",command=i_am_hated)
    button10.place(x=0,y=450)
    button11=Button(root,text="Skin Ticket",command=skin_ticket)
    button11.place(x=0,y=500)
    button12=Button(root,text="New Abortion",command=new_abortion)
    button12.place(x=0,y=550)
    button13=Button(root,text="Metabolic",command=metabolic)
    button13.place(x=0,y=600)
    button14=Button(root,text="IOWA",command=iowa_song)
    button14.place(x=0,y=650)

    test1=Label(image=sixthphoto)
    test1.place(x=100,y=50)

def gently():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    global test1
    test1.place_forget()
    button1=Button(root,text="515",command=img_515)
    button1.place(x=0,y=0)
    button2=Button(root,text="People=shit",command=peopleshit)
    button2.place(x=0,y=50)
    button3=Button(root,text="Disasterpiece",command=disaster)
    button3.place(x=0,y=100)
    button4=Button(root,text="My Plague",command=myplague)
    button4.place(x=0,y=150)
    button5=Button(root,text="Everything Ends",command=everything_ends)
    button5.place(x=0,y=200)
    button6=Button(root,text="Heretic Anthem",command=heretic_anthem)
    button6.place(x=0,y=250)
    button7=Button(root,text="Gently",state=DISABLED)
    button7.place(x=0,y=300)
    button8=Button(root,text="Left Behind",command=left_behind)
    button8.place(x=0,y=350)
    button9=Button(root,text="The Shape",command=the_shape)
    button9.place(x=0,y=400)
    button10=Button(root,text="I Am Hated",command=i_am_hated)
    button10.place(x=0,y=450)
    button11=Button(root,text="Skin Ticket",command=skin_ticket)
    button11.place(x=0,y=500)
    button12=Button(root,text="New Abortion",command=new_abortion)
    button12.place(x=0,y=550)
    button13=Button(root,text="Metabolic",command=metabolic)
    button13.place(x=0,y=600)
    button14=Button(root,text="IOWA",command=iowa_song)
    button14.place(x=0,y=650)

    test1=Label(image=seventhphoto)
    test1.place(x=100,y=50)

def left_behind():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    global test1
    test1.place_forget()
    button1=Button(root,text="515",command=img_515)
    button1.place(x=0,y=0)
    button2=Button(root,text="People=shit",command=peopleshit)
    button2.place(x=0,y=50)
    button3=Button(root,text="Disasterpiece",command=disaster)
    button3.place(x=0,y=100)
    button4=Button(root,text="My Plague",command=myplague)
    button4.place(x=0,y=150)
    button5=Button(root,text="Everything Ends",command=everything_ends)
    button5.place(x=0,y=200)
    button6=Button(root,text="Heretic Anthem",command=heretic_anthem)
    button6.place(x=0,y=250)
    button7=Button(root,text="Gently",command=gently)
    button7.place(x=0,y=300)
    button8=Button(root,text="Left Behind",state=DISABLED)
    button8.place(x=0,y=350)
    button9=Button(root,text="The Shape",command=the_shape)
    button9.place(x=0,y=400)
    button10=Button(root,text="I Am Hated",command=i_am_hated)
    button10.place(x=0,y=450)
    button11=Button(root,text="Skin Ticket",command=skin_ticket)
    button11.place(x=0,y=500)
    button12=Button(root,text="New Abortion",command=new_abortion)
    button12.place(x=0,y=550)
    button13=Button(root,text="Metabolic",command=metabolic)
    button13.place(x=0,y=600)
    button14=Button(root,text="IOWA",command=iowa_song)
    button14.place(x=0,y=650)

    test1=Label(image=eighthphoto)
    test1.place(x=100,y=50)
    
def the_shape():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    global test1
    test1.place_forget()
    button1=Button(root,text="515",command=img_515)
    button1.place(x=0,y=0)
    button2=Button(root,text="People=shit",command=peopleshit)
    button2.place(x=0,y=50)
    button3=Button(root,text="Disasterpiece",command=disaster)
    button3.place(x=0,y=100)
    button4=Button(root,text="My Plague",command=myplague)
    button4.place(x=0,y=150)
    button5=Button(root,text="Everything Ends",command=everything_ends)
    button5.place(x=0,y=200)
    button6=Button(root,text="Heretic Anthem",command=heretic_anthem)
    button6.place(x=0,y=250)
    button7=Button(root,text="Gently",command=gently)
    button7.place(x=0,y=300)
    button8=Button(root,text="Left Behind",command=left_behind)
    button8.place(x=0,y=350)
    button9=Button(root,text="The Shape",state=DISABLED)
    button9.place(x=0,y=400)
    button10=Button(root,text="I Am Hated",command=i_am_hated)
    button10.place(x=0,y=450)
    button11=Button(root,text="Skin Ticket",command=skin_ticket)
    button11.place(x=0,y=500)
    button12=Button(root,text="New Abortion",command=new_abortion)
    button12.place(x=0,y=550)
    button13=Button(root,text="Metabolic",command=metabolic)
    button13.place(x=0,y=600)
    button14=Button(root,text="IOWA",command=iowa_song)
    button14.place(x=0,y=650)

    test1=Label(image=ninthphoto)
    test1.place(x=100,y=50)
def i_am_hated():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    global test1
    test1.place_forget()
    button1=Button(root,text="515",command=img_515)
    button1.place(x=0,y=0)
    button2=Button(root,text="People=shit",command=peopleshit)
    button2.place(x=0,y=50)
    button3=Button(root,text="Disasterpiece",command=disaster)
    button3.place(x=0,y=100)
    button4=Button(root,text="My Plague",command=myplague)
    button4.place(x=0,y=150)
    button5=Button(root,text="Everything Ends",command=everything_ends)
    button5.place(x=0,y=200)
    button6=Button(root,text="Heretic Anthem",command=heretic_anthem)
    button6.place(x=0,y=250)
    button7=Button(root,text="Gently",command=gently)
    button7.place(x=0,y=300)
    button8=Button(root,text="Left Behind",command=left_behind)
    button8.place(x=0,y=350)
    button9=Button(root,text="The Shape",command=the_shape)
    button9.place(x=0,y=400)
    button10=Button(root,text="I Am Hated",state=DISABLED)
    button10.place(x=0,y=450)
    button11=Button(root,text="Skin Ticket",command=skin_ticket)
    button11.place(x=0,y=500)
    button12=Button(root,text="New Abortion",command=new_abortion)
    button12.place(x=0,y=550)
    button13=Button(root,text="Metabolic",command=metabolic)
    button13.place(x=0,y=600)
    button14=Button(root,text="IOWA",command=iowa_song)
    button14.place(x=0,y=650)
    test1=Label(image=tenthphoto)
    test1.place(x=100,y=50)
def skin_ticket():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    global test1
    test1.place_forget()
    button1=Button(root,text="515",command=img_515)
    button1.place(x=0,y=0)
    button2=Button(root,text="People=shit",command=peopleshit)
    button2.place(x=0,y=50)
    button3=Button(root,text="Disasterpiece",command=disaster)
    button3.place(x=0,y=100)
    button4=Button(root,text="My Plague",command=myplague)
    button4.place(x=0,y=150)
    button5=Button(root,text="Everything Ends",command=everything_ends)
    button5.place(x=0,y=200)
    button6=Button(root,text="Heretic Anthem",command=heretic_anthem)
    button6.place(x=0,y=250)
    button7=Button(root,text="Gently",command=gently)
    button7.place(x=0,y=300)
    button8=Button(root,text="Left Behind",command=left_behind)
    button8.place(x=0,y=350)
    button9=Button(root,text="The Shape",command=the_shape)
    button9.place(x=0,y=400)
    button10=Button(root,text="I Am Hated",command=i_am_hated)
    button10.place(x=0,y=450)
    button11=Button(root,text="Skin Ticket",state=DISABLED)
    button11.place(x=0,y=500)
    button12=Button(root,text="New Abortion",command=new_abortion)
    button12.place(x=0,y=550)
    button13=Button(root,text="Metabolic",command=metabolic)
    button13.place(x=0,y=600)
    button14=Button(root,text="IOWA",command=iowa_song)
    button14.place(x=0,y=650)


    test1=Label(image=eleventhphoto)
    test1.place(x=100,y=50)
def new_abortion():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    global test1
    test1.place_forget()
    button1=Button(root,text="515",command=img_515)
    button1.place(x=0,y=0)
    button2=Button(root,text="People=shit",command=peopleshit)
    button2.place(x=0,y=50)
    button3=Button(root,text="Disasterpiece",command=disaster)
    button3.place(x=0,y=100)
    button4=Button(root,text="My Plague",command=myplague)
    button4.place(x=0,y=150)
    button5=Button(root,text="Everything Ends",command=everything_ends)
    button5.place(x=0,y=200)
    button6=Button(root,text="Heretic Anthem",command=heretic_anthem)
    button6.place(x=0,y=250)
    button7=Button(root,text="Gently",command=gently)
    button7.place(x=0,y=300)
    button8=Button(root,text="Left Behind",command=left_behind)
    button8.place(x=0,y=350)
    button9=Button(root,text="The Shape",command=the_shape)
    button9.place(x=0,y=400)
    button10=Button(root,text="I Am Hated",command=i_am_hated)
    button10.place(x=0,y=450)
    button11=Button(root,text="Skin Ticket",command=skin_ticket)
    button11.place(x=0,y=500)
    button12=Button(root,text="New Abortion",state=DISABLED)
    button12.place(x=0,y=550)
    button13=Button(root,text="Metabolic",command=metabolic)
    button13.place(x=0,y=600)
    button14=Button(root,text="IOWA",command=iowa_song)
    button14.place(x=0,y=650)

    test1=Label(image=twelfthphoto)
    test1.place(x=100,y=50)
def metabolic():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    global test1
    test1.place_forget()
    button1=Button(root,text="515",command=img_515)
    button1.place(x=0,y=0)
    button2=Button(root,text="People=shit",command=peopleshit)
    button2.place(x=0,y=50)
    button3=Button(root,text="Disasterpiece",command=disaster)
    button3.place(x=0,y=100)
    button4=Button(root,text="My Plague",command=myplague)
    button4.place(x=0,y=150)
    button5=Button(root,text="Everything Ends",command=everything_ends)
    button5.place(x=0,y=200)
    button6=Button(root,text="Heretic Anthem",command=heretic_anthem)
    button6.place(x=0,y=250)
    button7=Button(root,text="Gently",command=gently)
    button7.place(x=0,y=300)
    button8=Button(root,text="Left Behind",command=left_behind)
    button8.place(x=0,y=350)
    button9=Button(root,text="The Shape",command=the_shape)
    button9.place(x=0,y=400)
    button10=Button(root,text="I Am Hated",command=i_am_hated)
    button10.place(x=0,y=450)
    button11=Button(root,text="Skin Ticket",command=skin_ticket)
    button11.place(x=0,y=500)
    button12=Button(root,text="New Abortion",command=new_abortion)
    button12.place(x=0,y=550)
    button13=Button(root,text="Metabolic",state=DISABLED)
    button13.place(x=0,y=600)
    button14=Button(root,text="IOWA",command=iowa_song)
    button14.place(x=0,y=650)

    test1=Label(image=thirteenthphoto)
    test1.place(x=100,y=50)
def iowa_song():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    global button10
    global button11
    global button12
    global button13
    global button14
    global test1
    test1.place_forget()
    button1=Button(root,text="515",command=img_515)
    button1.place(x=0,y=0)
    button2=Button(root,text="People=shit",command=peopleshit)
    button2.place(x=0,y=50)
    button3=Button(root,text="Disasterpiece",command=disaster)
    button3.place(x=0,y=100)
    button4=Button(root,text="My Plague",command=myplague)
    button4.place(x=0,y=150)
    button5=Button(root,text="Everything Ends",command=everything_ends)
    button5.place(x=0,y=200)
    button6=Button(root,text="Heretic Anthem",command=heretic_anthem)
    button6.place(x=0,y=250)
    button7=Button(root,text="Gently",command=gently)
    button7.place(x=0,y=300)
    button8=Button(root,text="Left Behind",command=left_behind)
    button8.place(x=0,y=350)
    button9=Button(root,text="The Shape",command=the_shape)
    button9.place(x=0,y=400)
    button10=Button(root,text="I Am Hated",command=i_am_hated)
    button10.place(x=0,y=450)
    button11=Button(root,text="Skin Ticket",command=skin_ticket)
    button11.place(x=0,y=500)
    button12=Button(root,text="New Abortion",command=new_abortion)
    button12.place(x=0,y=550)
    button13=Button(root,text="Metabolic",command=metabolic)
    button13.place(x=0,y=600)
    button14=Button(root,text="IOWA",state=DISABLED)
    button14.place(x=0,y=650)

    test1=Label(image=fourteenthphoto)
    test1.place(x=100,y=50)
    
besyuzonbes=Songs('Photos/mqdefault.png')
peopleequalsshit=Songs('Photos/people.png')
disasterpiece=Songs('Photos/Download.png')
plague=Songs('Photos/myplague.png')
everything=Songs('Photos/E.png')
heretic=Songs('Photos/hqdefault.png')
gent=Songs('Photos/gently.png')
left=Songs('Photos/leftbehind.png')
shape=Songs('Photos/TheShape.png')
hated=Songs('Photos/hated.png')
skinticket=Songs('Photos/skinticket.png')
abortion=Songs('Photos/NewAbortion.png')
meta=Songs('Photos/metabolic.png')
iowasong=Songs('Photos/iowa.png')
root.title("IOWA")
root.iconbitmap('Photos/Slipknot.ico')
root.geometry("800x800")
root.resizable(0,0)
list=Label(root,text="IOWA Album list: ",fg="firebrick",font="Arial 20 bold",bg="#CCD6E0")
credit=Label(root,text="Made by Umut",bg="#CCD6E0")



credit.place(x=700,y=700)
list.place(x=500)
firstphoto=besyuzonbes.image
secondphoto=peopleequalsshit.image
thirdphoto=disasterpiece.image
fourthphoto=plague.image
fifthphoto=everything.image
sixthphoto=heretic.image
seventhphoto=gent.image
eighthphoto=left.image
ninthphoto=shape.image
tenthphoto=hated.image
eleventhphoto=skinticket.image
twelfthphoto=abortion.image
thirteenthphoto=meta.image
fourteenthphoto=iowasong.image


button1=Button(root,text="515",command=img_515)
button1.place(x=0,y=0)
button2=Button(root,text="People=shit",command=peopleshit)
button2.place(x=0,y=50)
button3=Button(root,text="Disasterpiece",command=disaster)
button3.place(x=0,y=100)
button4=Button(root,text="My Plague",command=myplague)
button4.place(x=0,y=150)
button5=Button(root,text="Everything Ends",command=everything_ends)
button5.place(x=0,y=200)
button6=Button(root,text="Heretic Anthem",command=heretic_anthem)
button6.place(x=0,y=250)
button7=Button(root,text="Gently",command=gently)
button7.place(x=0,y=300)
button8=Button(root,text="Left Behind",command=left_behind)
button8.place(x=0,y=350)
button9=Button(root,text="The Shape",command=the_shape)
button9.place(x=0,y=400)
button10=Button(root,text="I Am Hated",command=i_am_hated)
button10.place(x=0,y=450)
button11=Button(root,text="Skin Ticket",command=skin_ticket)
button11.place(x=0,y=500)
button12=Button(root,text="New Abortion",command=new_abortion)
button12.place(x=0,y=550)
button13=Button(root,text="Metabolic",command=metabolic)
button13.place(x=0,y=600)
button14=Button(root,text="IOWA",command=iowa_song)
button14.place(x=0,y=650)



















root.mainloop()
