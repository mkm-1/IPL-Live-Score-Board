import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import requests
import urllib.request
from urllib import *
import sports
import bs4
from bs4 import BeautifulSoup as BS
import requests
import sys


link='https://www.cricbuzz.com/live-cricket-scores/30505/mi-vs-rcb-48th-match-indian-premier-league-2020'
res = requests.get(link)
soup = bs4.BeautifulSoup(res.text,'html.parser')
global S
details =soup.select('.cb-col .cb-col-100 .cb-col-scores')
for i in details:
      k=str(i.getText().strip())
S=k.replace(",","\n")
h=S.replace("     ","")
p=S.replace(")","\n")






class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, LiveScore, PageTwo, PageThree, Login):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
     
           
   

    
        


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#2F9599')
        self.controller = controller

        self.controller.title("IPL SCOREBOARD")
        self.controller.iconphoto(False,tk.PhotoImage(file='C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\cricket.png'))
        self.controller.geometry("700x500")
        headingLabel1=tk.Label(self,text="IPL SCOREBOARD",
                               font=('verdana',45,'bold'),
                               foreground='white',
                               background='#2F9599')
        headingLabel1.pack()

        #self.controller.bg=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\ipl1.png")
       # self.bg_image=Label(self,image=self.controller.bg).place(x=0,y=0)
        self.controller.b1=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\btn1.png")
        
        self.btn1=Button(self,image=self.controller.b1,bd = 0,bg='#2F9599',activebackground='#2F9599',command=lambda: controller.show_frame("LiveScore")).place(x=280,y=90) 
        self.controller.b2=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\btn2.png")
        self.btn2=Button(self,image=self.controller.b2,bd = 0,bg='#2F9599',activebackground='#2F9599',command=lambda: controller.show_frame("PageTwo")).place(x=245,y=145)
        self.controller.b3=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\btn3.png")
        self.btn3=Button(self,image=self.controller.b3,bd = 0,bg='#2F9599',activebackground='#2F9599',command=lambda: controller.show_frame("PageThree")).place(x=245,y=200)
        self.controller.b4=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\btn4.png")
        self.btn4=Button(self,image=self.controller.b4,bd = 0,bg='#2F9599',activebackground='#2F9599',command=lambda: controller.show_frame("Login")).place(x=285,y=255)
        self.controller.b5=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\btn5.png")
        self.btn5=Button(self,image=self.controller.b5,bd = 0,bg='#2F9599',activebackground='#2F9599').place()
        self.controller.o=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\quit.png")
        self.bt9=Button(self,image=self.controller.o,bd = 0,bg='#2F9599',activebackground='#2F9599',command=self.controller.destroy).place(x=295,y=310) 
        
       


class LiveScore(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#2F9599')
        self.controller = controller
        headingLabel1=tk.Label(self,text="IPL SCOREBOARD",
                               font=('verdana',45,'bold'),
                               foreground='white',
                               background='#2F9599')
        headingLabel1.pack()


        
       # T=Text(self).place(x=100,y=200,height=100,width=400)
        #self.b1 = Button(self, text="DISPLAY SCORE", bg="blue", fg="white", command=lambda: controller.score).place(x=120, y=450, height=80, width=250)
        #self.b2 = Button(self, text="CLEAR SCORE", bg="blue", fg="white", command=lambda: controller.clear).place(x=420, y=450, height=80, width=250)
    

        frame = LabelFrame(self,bg="white",borderwidth=0,relief=SUNKEN,height="100",width="500",text=p,font=('verdana',15,'bold'),padx=100,pady=100).place(x=100,y=100)
        self.controller.b6=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\btn6.png")
        self.btn6=Button(self,image=self.controller.b6,bd = 0,bg='#2F9599',activebackground='#2F9599',command=lambda: controller.show_frame("StartPage")).place(x=400,y=400)
        self.controller.u=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\quit.png")
        self.bt0=Button(self,image=self.controller.u,bd = 0,bg='#2F9599',activebackground='#2F9599',command=self.controller.destroy).place(x=100,y=400) 

        

	
      
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#582eb3')
        self.controller = controller
        headingLabel1=tk.Label(self,text="RECENT",
                               font=('verdana',45,'bold'),
                               foreground='white',
                               background='#582eb3')
        headingLabel1.pack()
        self.controller.p1=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\s1.png")
        self.t1=Button(self,image=self.controller.p1,bd = 0,bg='#2F9599',activebackground='#2F9599').place(x=120,y=90) 
        self.controller.p2=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\s2.png")
        self.t2=Button(self,image=self.controller.p2,bd = 0,bg='#2F9599',activebackground='#2F9599').place(x=120,y=180)
        self.controller.p3=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\s3.png")
        self.t3=Button(self,image=self.controller.p3,bd = 0,bg='#2F9599',activebackground='#2F9599').place(x=120,y=270)
        self.controller.p4=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\s4.png")
        self.t4=Button(self,image=self.controller.p4,bd = 0,bg='#2F9599',activebackground='#2F9599').place(x=120,y=360)
        self.controller.b7=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\btn6.png")
        self.btnn6=Button(self,image=self.controller.b7,bd = 0,bg='#582eb3',activebackground='#582eb3',command=lambda: controller.show_frame("StartPage")).place(x=600,y=450)
        self.controller.g=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\quit.png")
        self.b9=Button(self,image=self.controller.g,bd = 0,bg='#582eb3',activebackground='#582eb3',command=self.controller.destroy).place(x=200,y=450) 

        
        

class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#582eb3')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Upcoming",
                               font=('verdana',45,'bold'),
                               foreground='white',
                               background='#582eb3')
        headingLabel1.pack()
        self.controller.a1=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\u1.png")
        self.c1=Button(self,image=self.controller.a1,bd = 0,bg='#2F9599',activebackground='#2F9599').place(x=120,y=90) 
        self.controller.a2=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\u2.png")
        self.c2=Button(self,image=self.controller.a2,bd = 0,bg='#2F9599',activebackground='#2F9599').place(x=120,y=180)
        self.controller.a3=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\u3.png")
        self.c3=Button(self,image=self.controller.a3,bd = 0,bg='#2F9599',activebackground='#2F9599').place(x=120,y=270)
        self.controller.a4=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\u4.png")
        self.c4=Button(self,image=self.controller.a4,bd = 0,bg='#2F9599',activebackground='#2F9599').place(x=120,y=360)
        self.controller.h=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\btn6.png")
        self.bt7=Button(self,image=self.controller.h,bd = 0,bg='#582eb3',activebackground='#582eb3',command=lambda: controller.show_frame("StartPage")).place(x=600,y=450)
        self.controller.z=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\quit.png")
        self.bt8=Button(self,image=self.controller.z,bd = 0,bg='#582eb3',activebackground='#582eb3',command=self.controller.destroy).place(x=200,y=450) 
        

                
class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#582eb3')
        self.controller = controller
        headingLabel1=tk.Label(self,text="Login",
                               font=('verdana',45,'bold'),
                               foreground='white',
                               background='#582eb3')
        headingLabel1.pack()
        label1=Label(self,text="Username :",font=('arial',15,'bold'), background='#582eb3').place(x=130,y=150)
        self.e1=Entry(self).place(x=300,y=160)
        label2=Label(self,text="Password :",font=('arial',15,'bold'), background='#582eb3').place(x=130,y=200)
        self.e2=Entry(self, show="*").place(x=300,y=210)
        self.controller.q=PhotoImage(file="C:\\Users\\krishna\\OneDrive\\Pictures\\ipl score board\\btn4.png")
        self.c=Button(self,image=self.controller.q,bd = 0,bg='#582eb3',activebackground='#582eb3',command=lambda: controller.show_frame("LiveScore")).place(x=285,y=255)

      


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
