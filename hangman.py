from tkinter import *
import random
import time

words= open("words.txt", "r").readline().split()

def add():
    global f
    if nom.get() !='':
        f=1
    name=nom.get
    debut.destroy()
    
win =0
lose =0

def hang(c):
            line = C.create_line(320,200,200,200,fill = c,width=5)
            line = C.create_line(295,200,295,50,fill = c,width=5)
            line = C.create_line(150+65,50,263+35,50,fill = c,width=5)
            line = C.create_line(150+65,48,150+65,60,fill = c,width=5)

def stickman(c,x,y):
    line = C.create_oval(138+110+x,60+y,162+110+x,85+y,outline = c,width=3)
    line = C.create_line(150+110+x,85+y,150+110+x,130+y,fill = c,width=3)
    line = C.create_line(150+110+x,90+y,190+110+x,80+y,fill = c,width=3)
    line = C.create_line(150+110+x,90+y,110+110+x,80+y,fill = c,width=3)
    line = C.create_line(150+110+x,130+y,180+110+x,180+y,fill = c,width=3)
    line = C.create_line(150+110+x,130+y,120+110+x,180+y,fill = c,width=3)

def des():
    pendu.destroy()
    global tr
    tr=0
def check(c,x,y):
    global i
    global word2
    global win
    global lose
    global deja
    deja+=c
    Label(font=("",11,'bold'),text=deja).place(x=132,y=453)
    Button(text = c,bg = "black",fg='white',width=2).place(x = x, y = y)
    if c in word.upper():
        for j in range(len(word)):
            if word[j].upper()==c:
                word2= word2[:j] + c + word2[j+1:]
                Label(text=' '.join(word2),font=("consolas",15,'bold')).place(x=225,y=280)
            
        if '_' not in word2:
            win+=1
            Label(font=("consolas ",20,'bold italic'),text="WINNER ! ",fg="green2",bg='black').place(x=50,y=90)
            Label(text=f"Congra {nom.get()} the word was {word.upper()}").place(x=205,y=340)
            Label(text=f"statistiques : WIN {win}, LOSE {lose}").place(x=225,y=370)
            Button(width=13,text="Replay",bg='blue',fg='white',command =des).place(x=225,y=400)
            Button(width=13,text="Exit",bg='orange red',fg='black',command=pendu.destroy).place(x=400,y=470)

            y = 293
            for h in range(65,91):
                if ((h+1) % 6) == 0:
                    x=40
                    y+=27
                else:
                    x+=25
                Button(text = chr(h),bg = "black",fg='white',width=2).place(x = x, y = y)
            
            hang('black')
            stickman('black',-45,0)
            stickman('cyan',0,10)


    else:
        i+=1
        if i==1:
            line = C.create_line(320,200,200,200,fill = 'white',width=5)
        if i==2:
            line = C.create_line(295,200,295,50,fill = 'white',width=5)
        if i==3:
            line = C.create_line(150+65,50,263+35,50,fill = 'white',width=5)
            line = C.create_line(150+65,48,150+65,60,fill = 'white',width=5)
        if i==4:
            line = C.create_oval(138+65,60,162+65,85,outline = 'white',width=3)
        if i==5:
            line = C.create_line(150+65,85,150+65,130,fill = 'white',width=3)
        if i==6:
            line = C.create_line(150+65,90,190+65,80,fill = 'white',width=3)
        if i==7:
            line = C.create_line(150+65,90,110+65,80,fill = 'white',width=3)
        if i==8:
            line = C.create_line(150+65,130,180+65,180,fill = 'white',width=3)
        if i==9:
            lose+=1
            hang('white')
            stickman('black',-45,0)
            line = C.create_line(150+65,70,150+65,58,fill = 'white',width=2)
            line = C.create_oval(138+65,70,162+65,92,outline = 'red',width=3)
            line = C.create_line(150+65,93,150+65,130,fill = 'red',width=3)
            line = C.create_line(150+70,120,150+70,92,fill = 'red',width=3)
            line = C.create_line(150+60,120,150+60,92,fill = 'red',width=3)
            line = C.create_line(152+65,130,153+65,180,fill = 'red',width=3)
            line = C.create_line(148+65,130,147+65,180,fill = 'red',width=3)
            
            
            Label(font=("consolas ",20,'bold italic'),text="LOSER ! ",fg="red",bg='black').place(x=375,y=90)
            Label(text=f"bad luck {nom.get()} but the word was {word.upper()}").place(x=205,y=340)
            Label(text=f"statistiques : gagné {win}, perdu {lose}").place(x=225,y=370)
            Button(width=13,text="Replay",bg='blue',fg='white',command =des).place(x=225,y=400)
            Button(width=13,text="EXIT",bg='orange red',fg='black',command=pendu.destroy).place(x=400,y=470)
            y = 293
            for h in range(65,91):
                if ((h+1) % 6) == 0:
                    x=40
                    y+=27
                else:
                    x+=25
                Button(text = chr(h),bg = "black",fg='white',width=2).place(x = x, y = y)
f=0
while f==0 :
    debut=Tk()
    debut.geometry("250x90")
    debut.title("HANGMAN GAME")
    debut.resizable(False, False)
    nom = StringVar()
    Label(text="player name ",fg="blue").place(x=10,y=10)
    Entry( bd = 2,textvariable = nom).place(x = 110,y = 10)
    Button(text="PLAY",bg='green',fg='white',command=add,width=10).place(x=80,y=40)
    debut.mainloop()


tr=0
while tr==0:
    tr=1
    word=random.choice(words)
    i=0
    deja=""
    word2="_"*len(word)
    pendu=Tk()
    pendu.geometry("514x500")
    pendu.title("HANGMAN GAME")
    pendu.resizable(False, False)

    C=Canvas(width=510,height=250,bg = "black")
    C.place(x=0,y=0)

    Label(text=' '.join(list(word2)),font=("consolas",15,'bold')).place(x=225,y=280)
    Label(font=("arial ",15,'bold'),text="HANGMAN GAME",fg="gold",bg="black").place(x=180,y=5)
    Label(font=('consolas',10,'bold'),text="available :").place(x=40,y=297)
    Label(font=('consolas',10,'bold'),text="played :").place(x=40,y=455)
    Label(font=('consolas',17,'bold italic'),text=f"{nom.get().upper()}",fg="deep sky blue",bg="black",width=18).place(x=140,y=215)
    Label(font=('consolas',8,''),text="Player :",fg="deep sky blue",bg="black",width=20).place(x=200,y=203)


    Button(text = "A",command = lambda:check("A",40,320),bg = "white",width=2).place(x = 40, y = 320)
    Button(text = "B",command = lambda:check("B",65,320),bg = "white",width=2).place(x = 65, y = 320)
    Button(text = "C",command = lambda:check("C",90,320),bg = "white",width=2).place(x = 90, y = 320)
    Button(text = "D",command = lambda:check("D",115,320),bg = "white",width=2).place(x = 115, y = 320)
    Button(text = "E",command = lambda:check("E",140,320),bg = "white",width=2).place(x = 140, y = 320)
    Button(text = "F",command = lambda:check("F",165,320),bg = "white",width=2).place(x = 165, y = 320)
    Button(text = "G",command = lambda:check("G",40,347),bg = "white",width=2).place(x = 40, y = 347)
    Button(text = "H",command = lambda:check("H",65,347),bg = "white",width=2).place(x = 65, y = 347)
    Button(text = "I",command = lambda:check("I",90,347),bg = "white",width=2).place(x = 90, y = 347)
    Button(text = "J",command = lambda:check("J",115,347),bg = "white",width=2).place(x = 115, y = 347)
    Button(text = "K",command = lambda:check("K",140,347),bg = "white",width=2).place(x = 140, y = 347)
    Button(text = "L",command = lambda:check("L",165,347),bg = "white",width=2).place(x = 165, y = 347)
    Button(text = "M",command = lambda:check("M",40,374),bg = "white",width=2).place(x = 40, y = 374)
    Button(text = "N",command = lambda:check("N",65,374),bg = "white",width=2).place(x = 65, y = 374)
    Button(text = "O",command = lambda:check("O",90,374),bg = "white",width=2).place(x = 90, y = 374)
    Button(text = "P",command = lambda:check("P",115,374),bg = "white",width=2).place(x = 115, y = 374)
    Button(text = "Q",command = lambda:check("Q",140,374),bg = "white",width=2).place(x = 140, y = 374)
    Button(text = "R",command = lambda:check("R",165,374),bg = "white",width=2).place(x = 165, y = 374)
    Button(text = "S",command = lambda:check("S",40,401),bg = "white",width=2).place(x = 40, y = 401)
    Button(text = "T",command = lambda:check("T",65,401),bg = "white",width=2).place(x = 65, y = 401)
    Button(text = "U",command = lambda:check("U",90,401),bg = "white",width=2).place(x = 90, y = 401)
    Button(text = "V",command = lambda:check("V",115,401),bg = "white",width=2).place(x = 115, y = 401)
    Button(text = "W",command = lambda:check("W",140,401),bg = "white",width=2).place(x = 140, y = 401)
    Button(text = "X",command = lambda:check("X",165,401),bg = "white",width=2).place(x = 165, y = 401)
    Button(text = "Y",command = lambda:check("Y",40,428),bg = "white",width=2).place(x = 40, y = 428)
    Button(text = "Z",command = lambda:check("Z",65,428),bg = "white",width=2).place(x = 65, y = 428)

    pendu.mainloop()
































