from tkinter import*
from tkinter import messagebox
from PIL import ImageTk, Image
from pictures import*
import pygame
from pygame.locals import *
from pygame import mixer
pygame.init()
mixer.init()
mixer.music.load('Bg.mp3')

class App:
	def __init__(self,root):
		self.root = root
		self.root.geometry("1080x2129+0+0")
		self.root.overrideredirect(True)
		self.root.config(bg="gray")
		
		with open('mus_state.txt', 'r') as fo:
			#fo.write("true")
			if fo.read() == "true":
				self.mus_state = True
			else:
				self.mus_state = False
		
		if self.mus_state == True:
			mixer.music.play()
		
		self.bg_img = ImageTk.PhotoImage(listpic["bg"])
		self.puz_bg_img = ImageTk.PhotoImage(listpic["puz_bg"])
		self.play_img = ImageTk.PhotoImage(listpic["play"])
		self.level_img = ImageTk.PhotoImage(listpic["level"])
		self.setting_img = ImageTk.PhotoImage(listpic["setting"])
		self.muson_img = ImageTk.PhotoImage(listpic["muson"])
		self.musoff_img = ImageTk.PhotoImage(listpic["musoff"])
		self.board_img = ImageTk.PhotoImage(listpic["board"])
		self.back_img = ImageTk.PhotoImage(listpic["back"])
		self.home_img = ImageTk.PhotoImage(listpic["home"])
		self.hint_img = ImageTk.PhotoImage(listpic["hint"])
		self.puz1_img = ImageTk.PhotoImage(listpic["puz1"])
		self.next_img = ImageTk.PhotoImage(listpic["next"])
		
		self.level1 = ImageTk.PhotoImage(listpic["level1"])
		self.level2 = ImageTk.PhotoImage(listpic["level2"])
		self.level3 = ImageTk.PhotoImage(listpic["level3"])
		self.level4 = ImageTk.PhotoImage(listpic["level4"])
		self.level5 = ImageTk.PhotoImage(listpic["level5"])
		self.level6 = ImageTk.PhotoImage(listpic["level6"])
		self.level7 = ImageTk.PhotoImage(listpic["level7"])
		self.level8 = ImageTk.PhotoImage(listpic["level8"])
		self.level9 = ImageTk.PhotoImage(listpic["level9"])
		self.level10 = ImageTk.PhotoImage(listpic["level10"])
		
		
	def main(self):
		self.backg=Label(self.root,image=self.bg_img)
		self.backg.place(x=20,y=5)
		
		self.playbtn = Button(self.root,bd=0,image= self.play_img,bg="#ADF0F6",command=self.play_fun)
		self.playbtn.place(x=400,y=1000,width=370,height=130)
		
		self.levelbtn = Button(self.root,bd=0,image=self.level_img,bg="#ADF0F6",command=self.levels_fun)
		self.levelbtn.place(x=530,y=1200,width=100,height=100)
		
		self.settingbtn = Button(self.root,bd=0,image=self.setting_img,bg="#ADF0F6")
		self.settingbtn.place(x=330,y=1200,width=100,height=100)
		
		self.musicbtn = Button(self.root,bd=0,image=self.muson_img,bg="#ADF0F6", command = self.music_fun)
		self.musicbtn.place(x=730,y=1200,width=100,height=100)
		
		with open('mus_state.txt', 'r') as fo:
			#fo.write("true")
			if fo.read() == "true":
				self.mus_state = True
				self.musicbtn.config(image=self.muson_img)
			else:
				self.mus_state = False
				self.musicbtn.config(image=self.musoff_img)
			
		#self.mus_state = True
		
		pass
		
	def music_fun(self):
		with open('mus_state.txt','r') as fo:
			if fo.read() == "true":
				self.mus_state = True
			else:
				self.mus_state = False
				
		if self.mus_state == True:
			mixer.music.pause()
			self.musicbtn.config(image=self.musoff_img)
			with open('mus_state.txt','w') as fo:
				fo.write("false")
		elif self.mus_state == False:
			mixer.music.play()
			self.musicbtn.config(image=self.muson_img)
			with open('mus_state.txt','w') as fo:
				fo.write("true")
				
	def play_fun(self):
		self.level1_fun()
		
	def levels_fun(self):
		self.board=Label(self.root,bg="#7AE6F3")
		self.board.place(x=150,y=600,width=800,height=1200)
		
		self.backbtn = Button(self.board,bd=0,image=self.back_img,bg="#7AE6F3",command=self.destroy_fun)
		self.backbtn.place(x=0,y=0)
		
		self.btn1 = Button(self.board,bd=0,image=self.level1,bg="#7AE6F3",command=self.level1_fun)
		self.btn2 = Button(self.board,bd=0,image=self.level2,bg="#7AE6F3",command=self.level2_fun)
		self.btn3 = Button(self.board,bd=0,image=self.level3,bg="#7AE6F3",command=self.level3_fun)
		self.btn4 = Button(self.board,bd=0,image=self.level4,bg="#7AE6F3",command=self.level4_fun)
		self.btn5 = Button(self.board,bd=0,image=self.level5,bg="#7AE6F3",command=self.level5_fun)
		self.btn6 = Button(self.board,bd=0,image=self.level6,bg="#7AE6F3",command=self.level6_fun)
		self.btn7 = Button(self.board,bd=0,image=self.level7,bg="#7AE6F3",command=self.level7_fun)
		self.btn8 = Button(self.board,bd=0,image=self.level8,bg="#7AE6F3",command=self.level8_fun)
		self.btn9 = Button(self.board,bd=0,image=self.level9,bg="#7AE6F3",command=self.level9_fun)
		self.btn10 = Button(self.board,bd=0,image=self.level10,bg="#7AE6F3",command=self.level10_fun)
		
		self.btn1.place(x=50,y=200,width=300)
		self.btn2.place(x=50,y=380,width=300)
		self.btn3.place(x=50,y=550,width=300)
		self.btn4.place(x=50,y=730,width=300)
		self.btn5.place(x=50,y=910,width=300)
		self.btn6.place(x=450,y=200,width=300)
		self.btn7.place(x=450,y=380,width=300)
		self.btn8.place(x=450,y=550,width=300)
		self.btn9.place(x=450,y=730,width=300)
		self.btn10.place(x=450,y=910,width=300)
		
		pass
		
	def destroylevel(self):
		self.bg.destroy()
		
	def hint_fun(self):
		pass
		
	def level1_fun(self):
		self.bg=Label(self.root,image=self.puz_bg_img,bg="white")
		self.bg.place(x=20,y=5)
		
		self.puz=Label(self.bg,image=self.puz1_img,bg="white")
		self.puz.place(x=150,y=650)
		
		self.ansbtn1 = Button(self.bg,text="5",font=("Arial",8,"bold"),bd=7,bg="gray70",command=self.wrgans_fun)
		self.ansbtn1.place(x=100,y=1400,width=100,height=100)
		
		self.ansbtn2 = Button(self.bg,text="2",font=("Arial",8,"bold"),bd=7,bg="gray70",command=self.crrans_fun)
		self.ansbtn2.place(x=350,y=1400,width=100,height=100)
		
		self.ansbtn3 = Button(self.bg,text="7",font=("Arial",8,"bold"),bd=7,bg="gray70",command=self.wrgans_fun)
		self.ansbtn3.place(x=600,y=1400,width=100,height=100)
		
		self.ansbtn4 = Button(self.bg,text="3",font=("Arial",8,"bold"),bd=7,bg="gray70",command=self.wrgans_fun)
		self.ansbtn4.place(x=850,y=1400,width=100,height=100)
		
		self.backbtn = Button(self.bg,bd=0,image=self.back_img,bg="#FFFDDF",command=self.main)
		self.backbtn.place(x=300,y=1750)
		
		self.nextbtn = Button(self.bg,bd=0,image=self.next_img,bg="#FFFDDF",command=self.level2_fun)
		
		self.homebtn = Button(self.bg,bd=0,image=self.home_img,bg="#FFFDDF",command=self.main)
		self.homebtn.place(x=500,y=1750)
		
		self.hintbtn = Button(self.bg,bd=0,image=self.hint_img,bg="#FFFDDF",command=self.hint_fun)
		self.hintbtn.place(x=700,y=1750)
		pass
	def level2_fun(self):
		self.bg=Label(self.root,image=self.puz_bg_img,bg="white")
		self.bg.place(x=20,y=5)
		
		self.backbtn = Button(self.bg,bd=0,image=self.back_img,bg="#FFFDDF",command=self.level1_fun)
		self.backbtn.place(x=300,y=1750)
		
		self.homebtn = Button(self.bg,bd=0,image=self.home_img,bg="#FFFDDF",command=self.main)
		self.homebtn.place(x=500,y=1750)
		
		self.hintbtn = Button(self.bg,bd=0,image=self.hint_img,bg="#FFFDDF",command=self.hint_fun)
		self.hintbtn.place(x=700,y=1750)
		pass
	def level3_fun(self):
		self.bg=Label(self.root,image=self.puz_bg_img,bg="white")
		self.bg.place(x=20,y=5)
		
		self.backbtn = Button(self.bg,bd=0,image=self.back_img,bg="#FFFDDF",command=self.level2_fun)
		self.backbtn.place(x=300,y=1750)
		
		self.homebtn = Button(self.bg,bd=0,image=self.home_img,bg="#FFFDDF",command=self.main)
		self.homebtn.place(x=500,y=1750)
		
		self.hintbtn = Button(self.bg,bd=0,image=self.hint_img,bg="#FFFDDF",command=self.hint_fun)
		self.hintbtn.place(x=700,y=1750)
		pass
	def level4_fun(self):
		self.bg=Label(self.root,image=self.puz_bg_img,bg="white")
		self.bg.place(x=20,y=5)
		
		self.backbtn = Button(self.bg,bd=0,image=self.back_img,bg="#FFFDDF",command=self.level3_fun)
		self.backbtn.place(x=300,y=1750)
		
		self.homebtn = Button(self.bg,bd=0,image=self.home_img,bg="#FFFDDF",command=self.main)
		self.homebtn.place(x=500,y=1750)
		
		self.hintbtn = Button(self.bg,bd=0,image=self.hint_img,bg="#FFFDDF",command=self.hint_fun)
		self.hintbtn.place(x=700,y=1750)
		pass
	def level5_fun(self):
		self.bg=Label(self.root,image=self.puz_bg_img,bg="white")
		self.bg.place(x=20,y=5)
		
		self.backbtn = Button(self.bg,bd=0,image=self.back_img,bg="#FFFDDF",command=self.level4_fun)
		self.backbtn.place(x=300,y=1750)
		
		self.homebtn = Button(self.bg,bd=0,image=self.home_img,bg="#FFFDDF",command=self.main)
		self.homebtn.place(x=500,y=1750)
		
		self.hintbtn = Button(self.bg,bd=0,image=self.hint_img,bg="#FFFDDF",command=self.hint_fun)
		self.hintbtn.place(x=700,y=1750)
		pass
	def level6_fun(self):
		self.bg=Label(self.root,image=self.puz_bg_img,bg="white")
		self.bg.place(x=20,y=5)
		
		self.backbtn = Button(self.bg,bd=0,image=self.back_img,bg="#FFFDDF",command=self.level5_fun)
		self.backbtn.place(x=300,y=1750)
		
		self.homebtn = Button(self.bg,bd=0,image=self.home_img,bg="#FFFDDF",command=self.main)
		self.homebtn.place(x=500,y=1750)
		
		self.hintbtn = Button(self.bg,bd=0,image=self.hint_img,bg="#FFFDDF",command=self.hint_fun)
		self.hintbtn.place(x=700,y=1750)
		pass
	def level7_fun(self):
		self.bg=Label(self.root,image=self.puz_bg_img,bg="white")
		self.bg.place(x=20,y=5)
		
		self.backbtn = Button(self.bg,bd=0,image=self.back_img,bg="#FFFDDF",command=self.level6_fun)
		self.backbtn.place(x=300,y=1750)
		
		self.homebtn = Button(self.bg,bd=0,image=self.home_img,bg="#FFFDDF",command=self.main)
		self.homebtn.place(x=500,y=1750)
		
		self.hintbtn = Button(self.bg,bd=0,image=self.hint_img,bg="#FFFDDF",command=self.hint_fun)
		self.hintbtn.place(x=700,y=1750)
		pass
	def level8_fun(self):
		self.bg=Label(self.root,image=self.puz_bg_img,bg="white")
		self.bg.place(x=20,y=5)
		
		self.backbtn = Button(self.bg,bd=0,image=self.back_img,bg="#FFFDDF",command=self.level7_fun)
		self.backbtn.place(x=300,y=1750)
		
		self.homebtn = Button(self.bg,bd=0,image=self.home_img,bg="#FFFDDF",command=self.main)
		self.homebtn.place(x=500,y=1750)
		
		self.hintbtn = Button(self.bg,bd=0,image=self.hint_img,bg="#FFFDDF",command=self.hint_fun)
		self.hintbtn.place(x=700,y=1750)
		pass
	def level9_fun(self):
		self.bg=Label(self.root,image=self.puz_bg_img,bg="white")
		self.bg.place(x=20,y=5)
		
		self.backbtn = Button(self.bg,bd=0,image=self.back_img,bg="#FFFDDF",command=self.level8_fun)
		self.backbtn.place(x=300,y=1750)
		
		self.homebtn = Button(self.bg,bd=0,image=self.home_img,bg="#FFFDDF",command=self.main)
		self.homebtn.place(x=500,y=1750)
		
		self.hintbtn = Button(self.bg,bd=0,image=self.hint_img,bg="#FFFDDF",command=self.hint_fun)
		self.hintbtn.place(x=700,y=1750)
		pass
	def level10_fun(self):
		self.bg=Label(self.root,image=self.puz_bg_img,bg="white")
		self.bg.place(x=20,y=5)
		
		self.backbtn = Button(self.bg,bd=0,image=self.back_img,bg="#FFFDDF",command=self.level9_fun)
		self.backbtn.place(x=300,y=1750)
		
		self.homebtn = Button(self.bg,bd=0,image=self.home_img,bg="#FFFDDF",command=self.main)
		self.homebtn.place(x=500,y=1750)
		
		self.hintbtn = Button(self.bg,bd=0,image=self.hint_img,bg="#FFFDDF",command=self.hint_fun)
		self.hintbtn.place(x=700,y=1750)
		pass
		
	def destroy_fun(self):
		self.board.destroy()
		
	def crrans_fun(self):
		messagebox.showinfo("well done","Your ANSWER is right")
		self.nextbtn.place(x=500,y=1600)
		
	def wrgans_fun(self):
		messagebox.showinfo("Try again","Your ANSWER is wrong")
		self.nextbtn["state"]=DISABLED
		pass
		
	def setting_fun(self):
		pass
		
	def back_fun(self):
		pass

root = Tk()
obj = App(root)
obj.main()
root.mainloop()