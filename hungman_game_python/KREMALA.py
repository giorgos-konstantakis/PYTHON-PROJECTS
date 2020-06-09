from tkinter import *
from tkinter import messagebox
import random
from random import *

global word_to_be_guessed
global word

# Class of the texts and variables of the game
class labels:
    def _init_(self):
        self.word1=word1
        self.word2=word2
        self.Tries=Tries
        self.leksi=leksi
        self.word=word
        self.word_to_be_guessed=word_to_be_guessed
        self.tries=tries
        self.No_Of_Tries_Remaining=No_Of_Tries_Remaining

# Class of the winning texts
class win:
    def _init_(self):
        self.winning_text=winning_text
        self.winning_guide_text=winning_guide_text

# Class of the loss texts        
class lose:
    def _init_(self):
        self.loss=loss
        self.loss_guide_text=loss_guide_text
        
# The function which starting a new KREMALA game 
def start_new_game():
    # Reading the word_to_be_guessed by the file with the words to a string
    labels.word=""
    labels.word_to_be_guessed=""
    word_file=open(r" The path where you have saved this words.txt file ( where the program should also be saved )","r")
    N=randint(0,9)
    for i, line in enumerate(word_file):
        if i==N and i!=0:
            labels.word_to_be_guessed=word_file.readline()
            break
        elif i==N and N==0:
            N=N+1
            continue
        else:
            continue
    word_file.close()
    for z in range(0,len(labels.word_to_be_guessed)-1):
        labels.word=labels.word+"-"
    labels.No_Of_Tries_Remaining=2*len(labels.word)
    labels.tries=str(labels.No_Of_Tries_Remaining)
    labels.leksi=Label(kremala,text=labels.word,bg="white",fg="DodgerBlue4",font=('Calibri','40'))
    labels.leksi.grid(row=1,column=0,columnspan=13)
    labels.Tries=Label(kremala,text="No Of Tries Remaining"+labels.tries,bg="DodgerBlue4",fg="white",font=('Calibri','20'))
    labels.Tries.grid(row=2,column=0,columnspan=3)


# The function of the game
def game(letter):
    c=0
    labels.Tries.destroy()
    labels.leksi.destroy()
    labels.word1=list(labels.word)
    labels.word2=list(labels.word_to_be_guessed)
    if not labels.word_to_be_guessed:
        return 0
    else:
        for j in range(0,len(labels.word2)-1):
            if letter == labels.word2[j]:
                labels.word1[j]=letter
                c=c+1
        if c==0:
            labels.No_Of_Tries_Remaining=labels.No_Of_Tries_Remaining-1
        def conv(s):
            st=""
            return (st.join(s))
        labels.word=conv(labels.word1)    
        labels.tries=str(labels.No_Of_Tries_Remaining)
        labels.leksi=Label(kremala,text=labels.word,bg="white",fg="DodgerBlue4",font=('Calibri','40'))
        labels.leksi.grid(row=1,column=0,columnspan=13)
        labels.Tries=Label(kremala,text="No Of Tries Remaining"+labels.tries,bg="DodgerBlue4",fg="white",font=('Calibri','20'))
        labels.Tries.grid(row=2,column=0,columnspan=3)
        if labels.word1==labels.word2[:-1]:
            labels.Tries.destroy()
            labels.leksi.destroy()
            win.winning_text=Label(kremala,text="SYGXARHTHRIA KERDISATE",bg="DeepSkyBlue4",fg="white",font=('Calibri','40'))
            win.winning_text.grid(row=1,column=0,columnspan=13)
            win.winning_guide_text=Label(kremala,text='''Pieste FINISH CURRENT GAME
                gia na termatisete to paixnidi ''',bg="DodgerBlue4",fg="white",font=('Calibri','20'))
            win.winning_guide_text.grid(row=2,column=0,columnspan=5)
        if labels.No_Of_Tries_Remaining<=0:
            labels.Tries.destroy()
            labels.leksi.destroy()
            lose.loss=Label(kremala,text="DYSTYXWS XASATE",bg="DeepSkyBlue4",fg="white",font=('Calibri','40'))
            lose.loss.grid(row=1,column=0,columnspan=13)
            lose.loss_guide_text=Label(kremala,text='''Pieste FINISH CURRENT GAME
                gia na termatisete to paixnidi''',bg="DodgerBlue4",fg="white",font=('Calibri','20'))
            lose.loss_guide_text.grid(row=2,column=0,columnspan=5)
        print(labels.word1)
        print(labels.word2)

                
# The function which finishes the current game
def end_current_game():
    #labels.Tries.destroy()
    #labels.leksi.destroy()
    win.winning_text.destroy()
    win.winning_guide_text.destroy()
    lose.loss.destroy()
    lose.loss_guide_text.destroy()
    labels.word=""
    labels.word_to_be_guessed=""
    labels.word1=[]
    labels.word2=[]
    labels.No_Of_Tries_Remaining=0
    labels.tries=0
    

# Define our tkinter window
kremala = Tk()

# Define the title of our program
kremala.title("KREMALA")

# Define the background color of the window
kremala.configure(background="dodger blue")

# Creating the text with the instructions of game
odhgies=Label(kremala,text='''Edw paizoume to paixnidi KREMALA. Epilegete apo to programma tuxaia mia leksh , kai eseis prepei na thn
mantepsete. Oi sunolikes prospatheis pou diathetete einai ises me to sunolo twn grammatwn ths lekshs epi 2.
Pieste START NEW GAME gia na ksekinisete ena paixnidi, h FINISH CURRENT GAME gia na to termathsete. GOOD LUCK''',bg="DodgerBlue4",fg="white",font=('Calibri','15') )
odhgies.grid(row=0,column=0,columnspan=13)


# Buttons
button_A=Button(kremala,text="a",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("a"))
button_B=Button(kremala,text="b",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("b"))
button_C=Button(kremala,text="c",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("c"))
button_D=Button(kremala,text="d",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("d"))
button_E=Button(kremala,text="e",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("e"))
button_F=Button(kremala,text="f",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("f"))
button_G=Button(kremala,text="g",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("g"))
button_H=Button(kremala,text="h",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("h"))
button_I=Button(kremala,text="i",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("i"))
button_J=Button(kremala,text="j",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("j"))
button_K=Button(kremala,text="k",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("k"))
button_L=Button(kremala,text="l",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("l"))
button_M=Button(kremala,text="m",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("m"))
button_N=Button(kremala,text="n",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("n"))
button_O=Button(kremala,text="o",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("o"))
button_P=Button(kremala,text="p",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("p"))
button_Q=Button(kremala,text="q",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("q"))
button_R=Button(kremala,text="r",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("r"))
button_S=Button(kremala,text="s",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("s"))
button_T=Button(kremala,text="t",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("t"))
button_U=Button(kremala,text="u",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("u"))
button_V=Button(kremala,text="v",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("v"))
button_W=Button(kremala,text="w",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("w"))
button_X=Button(kremala,text="x",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("x"))
button_Y=Button(kremala,text="y",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("y"))
button_Z=Button(kremala,text="z",width=10,padx=10,pady=10,bg="DeepSkyBlue4",fg="white",command=lambda:game("z"))
button_END_GAME=Button(kremala,text="FINISH CURRENT GAME",width=144,padx=130,pady=10,
                       bg="DeepSkyBlue4",fg="white",command=end_current_game)
button_START_GAME=Button(kremala,text="START NEW GAME",width=144,padx=130,pady=10,
                         bg="DeepSkyBlue4",fg="white",command=start_new_game)

# Buttons' grids ( their positions in the screen , which is organized as a table  )
button_A.grid(row=5,column=0)
button_B.grid(row=5,column=1)
button_C.grid(row=5,column=2)
button_D.grid(row=5,column=3)
button_E.grid(row=5,column=4)
button_F.grid(row=5,column=5)
button_G.grid(row=5,column=6)
button_H.grid(row=5,column=7)
button_I.grid(row=5,column=8)
button_J.grid(row=5,column=9)
button_K.grid(row=5,column=10)
button_L.grid(row=5,column=11)
button_M.grid(row=5,column=12)
button_N.grid(row=6,column=0)
button_O.grid(row=6,column=1)
button_P.grid(row=6,column=2)
button_Q.grid(row=6,column=3)
button_R.grid(row=6,column=4)
button_S.grid(row=6,column=5)
button_T.grid(row=6,column=6)
button_U.grid(row=6,column=7)
button_V.grid(row=6,column=8)
button_W.grid(row=6,column=9)
button_X.grid(row=6,column=10)
button_Y.grid(row=6,column=11)
button_Z.grid(row=6,column=12)
button_END_GAME.grid(row=7,column=0,columnspan=13)
button_START_GAME.grid(row=8,column=0,columnspan=13)


kremala.mainloop()











