from tkinter import *
import random
class table:
     def __init__(self,root):
          self.root=root
          self.user_choice,self.cpu_choice,self.blist=[],[],[]
          self.canvas()    
     def canvas(self):
          self.table=Canvas(self.root,width=400,height=400)
          self.button()
          self.line()
          self.table.pack()
     def line(self):
          self.table.create_line(133,0,133,400,width=5)
          self.table.create_line(266,0,266,400,width=5)
          self.table.create_line(0,133,400,133,width=5)
          self.table.create_line(0,266,400,266,width=5)
     def button(self):
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
          self.user_choice.append(p)
          self.blist[p].config(text='X')
          self.ai()
     def ai(self):
          self.can=True
          function=[self.row,self.column,self.diagonal]
          random.shuffle(function)
          for i in function:
               i()
          self.notfound()
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
     def notfound(self):
          if self.can==True:
               loop=True
               while loop==True:
                    t=random.randint(0,8)
                    if t not in self.user_choice and t not in self.cpu_choice:
                         loop=False
                         self.cpu_move(t)
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
          if self.result[0]*self.result[1]*self.result[2]==27:
               print('Player Win')
          if self.result[0]*self.result[1]*self.result[2]==125:
               print('Cpu    Win')
          if self.result[0]*self.result[1]*self.result[2]==9:
               if self.can==True:
                    self.cpu_move(self.empty)
          if self.result[0]*self.result[1]*self.result[2]==25:
               if self.can==True:
                    self.cpu_move(self.empty)
     def cpu_move(self,t):
          self.cpu_choice.append(t)
          self.blist[t].config(text='O')
          self.can=False
def main():
     root=Tk()
     root.title('Tris')
     root.geometry('400x400')
     table(root)
     root.mainloop()
main()
