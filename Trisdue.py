from tkinter import *
import random
class table:
     def __init__(self,root):
          self.var,self.user,self.cpu,self.go,self.play=StringVar(),0,0,True,True
          self.root=root
          self.set()
          self.canvas()
     def set(self):
          command=0
          ag=Button(self.root,text='Restart',font='Arial 14',width=9,command=lambda command=command: self.delete())
          ag.place(x=10,y=415)
          X=Radiobutton(self.root,text='X',variable=self.var,value='X',font='Arial 14')
          X.place(x=180,y=415)
          O=Radiobutton(self.root,text='O',variable=self.var,value='O',font='Arial 14')
          O.place(x=250,y=415)
     def canvas(self):
          self.table=Canvas(self.root,width=400,height=390,highlightbackground="black",highlightthickness=7)
          self.button()
          self.line()
          self.table.pack()
     def line(self):
          self.table.create_line(133,0,133,400,width=5)
          self.table.create_line(266,0,266,400,width=5)
          self.table.create_line(0,133,400,133,width=5)
          self.table.create_line(0,266,400,266,width=5)
     def button(self):
          self.user_choice,self.cpu_choice,self.blist=[],[],[]
          pos,counter=[16,25],0
          for i in range(3):
               for q in range(3):
                    self.x=Button(self.table,text=' ',bd=3,font='Arial 30 bold',
                                  width=4,height=1,borderwidth=0,command=lambda counter=counter: self.position(counter))
                    self.x.place(x=pos[0],y=pos[1])
                    self.blist.append(self.x)
                    counter +=1
                    pos[0]+=135
               pos[0],pos[1]=16,pos[1]+133
     def position(self,p):
          self.choicebut()
          if self.play==True:
               if p not in self.cpu_choice:
                    self.user_choice.append(p)
                    self.blist[p].config(text=self.user)
                    self.ai()
     def choicebut(self):
          if self.go== True:
               self.user=(self.var.get())
               if self.user=='X':
                    self.cpu='O'
               else:
                    self.cpu='X'
               self.go=False
     def ai(self):
          self.can=True
          self.defense,self.attack,self.notfound=[],[],0
          function=[self.row,self.column,self.diagonal]
          random.shuffle(function)
          for i in function:
               i()
          self.position2()
     def row(self):
          pos,self.result,counter,self.empty=[0,3,6],[],0,0
          for q in range(3):
               self.result=[]
               for u in range(3):
                    k=pos[q]+u
                    self.control(k)
               self.call_cpumove()
     def column(self):
          add,self.empty=[0,3,6],0
          for q in range(3):
               self.result=[]
               for u in range(3):
                    k=q+add[u]
                    self.control(k)
               self.call_cpumove()
     def diagonal(self):
          add,self.empty,k=[4,2],0,-4
          for q in range(2):
               self.result=[]
               for u in range(3):
                    k+=add[q]
                    self.control(k)
               self.call_cpumove()
               k=0
     def control(self,k):
          if k in self.user_choice:
               self.result.append(3)
          else:
               if k in self.cpu_choice:
                    self.result.append(5)
               else:
                    self.empty=k
                    self.result.append(1)
     def call_cpumove(self):
          if len(self.user_choice)==5:
               self.finish('Equal')
               self.can=False
          if self.result[0]*self.result[1]*self.result[2]==9:
               self.defense.append(self.empty)
          if self.result[0]*self.result[1]*self.result[2]==3:
               self.notfound=self.empty
          if self.result[0]*self.result[1]*self.result[2]==25:
               self.attack.append(self.empty)
          if self.result[0]*self.result[1]*self.result[2]==27:
               self.finish('You win')
               self.can=False
     def position2(self):
          if self.can==True:
               if len(self.attack)!=0:
                    self.cpu_move(random.choice(self.attack))
                    self.finish('Cpu win')
               elif len(self.defense)!=0:
                    self.cpu_move(random.choice(self.defense))
               else:
                    self.cpu_move(self.notfound)
     def cpu_move(self,t):
          self.cpu_choice.append(t)
          self.blist[t].config(text=self.cpu)
          self.can=False
     def finish(self,t):
          self.play=False
          self.whowin=Label(self.root,text=t,font='Arial 12')
          self.whowin.place(x=320,y=415)
     def delete(self):
          self.whowin.destroy()
          self.table.destroy()
          self.go=True
          self.play=True
          self.canvas()
def main():
     root=Tk()
     root.title('Tris')
     root.geometry('400x460')
     table(root)
     root.mainloop()
main()
