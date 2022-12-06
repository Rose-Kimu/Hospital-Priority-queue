from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

window = Tk()

my_canvas = Canvas(window, width = 1000, height=700  )
my_canvas.pack()

#hospital image
icon1=PhotoImage(file="C:/Users/user/Desktop/queue/hospital2.png")
image1 = Label(window,image=icon1)
image1.place( x=900,y=200,height=300,width=300)

icon2=PhotoImage(file="C:/Users/user/Desktop/queue/person1.png")
image2 = Label(window,image=icon2)
image2.place( x=1000,y=400,height=150,width=150)

#patients
photo=PhotoImage(file="C:/Users/user/Desktop/queue/person2.png")

class myList:
    def __init__(self):
        self.storage = []
        self.size = 0

    def isEmpty(self):
        return len(self.storage) ==0

    def addPatient(self,item):
        self.storage.append(item)
        self.size += 1
        self.sortList(self.storage)

    def sortList(self,list):
        n = len(self.storage)
        for pass_num in range(n-1,0,-1):
            for i in range(pass_num): 
                if list[i] > list[i+1]:
                    list[i],list[i+1]=list[i+1],list[i]

    def removePatient(self,item):
        for i in range(len(self.storage)-1):
            if self.storage[i] ==item:
                print(f"found and removing {item}")
                self.storage.pop(i)#reduces capacity
        last_index=len(self.storage)-1
        if self.storage[last_index] ==item:
            print(f"found and removing {item}")
            self.storage.pop(last_index)
                #self.storage[self.size+1]=0

    def replace(self,item,newitem):# new item=new key,old value
        if self.size==0:
            raise Exception("Queue is empty")
        for i in range(len(self.storage)):
            if self.storage[i] ==item:
                print(f"found {item}")
                self.storage.pop(i)#reduces capacity
                self.storage.append(newitem)
                self.sortList(self.storage)

    def Queuesize(self):
        return len(self.storage)

    def peekQueue(self):
        return self.storage[0]

    def pollQueue(self):
        first_item = self.storage[0]
        self.removePatient(first_item)
        return first_item

# HELPER FUNCTIONS
def size_of_queue():
    if (m.Queuesize()>0):
        messagebox.showinfo("Status",f"SIZE = {m.Queuesize()}")
    else:
        messagebox.showinfo("Error","SIZE=0")


def is_queue_empty():
    if (m.Queuesize()==0):
        messagebox.showinfo("Status","TRUE")
    else:
        messagebox.showinfo("Status","FALSE")


def peek():
    if(m.Queuesize()>0):
        messagebox.showinfo("Status", f" TOP= {m.peekQueue()}")
    else:
        messagebox.showerror("Error", "Queue is Empty")



def poll_queue():
    if (m.Queuesize()==0):
        messagebox.error("Error","Cannot poll from an empty queue")
    else:
        messagebox.showinfo("Status",f"Removed={m.peekQueue()}")
        
        # my_canvas.delete("all")
        m.pollQueue()
        print(m.storage)
        my_canvas.delete("all")
        
        inter = 120
        starting = 200
        s = m.Queuesize()
        p = 0
        while p < s:
            my_canvas.create_image((starting + (inter * p)), 490, image=photo, anchor='center')
            p += 1
        print(m.storage)

     


def admitbutton():
    txt=Entry(window,width=15, borderwidth=2)#add
    txt.place(x=280,y=93)
    add = Button(my_canvas, text="Add",fg="white", bg='chocolate', height=1, width=4, command= lambda: admit_patient(txt) )
    add.place(x=280,y=93)

def admit_patient(txt):
    if (m.Queuesize() == 5):
        messagebox.showerror("Error", "Queue is already full")
    else:
        res = txt.get()
        txt.delete(0,END)
        y=res.split(',')
        changed = int(y[0])   
        y.pop(0)
        y.insert(0,changed)
        m.addPatient(y)
        # DRAWING
        inter = 120
        starting = 200
        s = m.Queuesize()
        p = 0
        while p < s:
            my_canvas.create_image((starting + (inter * p)), 490, image=photo, anchor='center')
            p += 1
        print(m.storage)

def removebutton():
    txt2=Entry(window,width=15, borderwidth=2)#remove
    txt2.place(x=280,y=215)
    remove = Button(my_canvas, text="Remove",fg="white", bg='chocolate', height=1, width=6, command= lambda: remove_patient(txt2) )
    remove.place(x=280,y=215)
  

def remove_patient(txt2):
    if (m.Queuesize()==0):
        messagebox.showinfo("Error","Cannot remove from an empty queue")
    removed = txt2.get()
    txt2.delete(0,END)
    z = removed.split(',')
    new_int = int(z[0])
    z.pop(0)
    z.insert(0, new_int)
    m.removePatient(z)
    # DRAWING
    my_canvas.delete("all")
    inter = 120
    starting = 200
    s = m.Queuesize()
    p = 0
    while p < s:
        my_canvas.create_image((starting + (inter * p)), 490, image=photo, anchor='center')
        p += 1
    print(m.storage)

def prioritybutton():
    txt3=Entry(window,width=15, borderwidth=2)#old value
    txt3.place(x=280,y=335)

    txt4=Entry(window,width=15, borderwidth=2)#new value
    txt4.place(x=400,y=335)

    replace = Button(my_canvas, text="Replace",fg="white", bg='chocolate', height=1, width=6, command= lambda: change_priority(txt3,txt4) )
    replace.place(x=400,y=335)
  


def change_priority(txt3,txt4):
    #get data
    old_data = txt3.get()
    txt3.delete(0,END)
    a=old_data.split(',')
    old_data_int =int(a[0])
    a.pop(0)
    a.insert(0,old_data_int)
    #change with new_data
    new_data = txt4.get()
    txt4.delete(0,END)
    b = new_data.split(',')
    new_data_int= int(b[0])
    b.pop(0)
    b.insert(0, new_data_int)
    m.replace(a,b)
    print(m.storage)

def valuebutton():
    txt5=Entry(window,width=15, borderwidth=2)#old value
    txt5.place(x=280,y=375)

    txt6=Entry(window,width=15, borderwidth=2)#new value
    txt6.place(x=400,y=375)

    replace = Button(my_canvas, text="Replace",fg="white", bg='chocolate', height=1, width=6, command= lambda: change_value(txt5,txt6) )
    replace.place(x=400,y=375)


def change_value(txt5,txt6):
    #get data
    old_val = txt5.get()
    txt5.delete(0,END)
    c=old_val.split(',')
    old_val_int =int(c[0])
    c.pop(0)
    c.insert(0,old_val_int)
    #change with new_data
    new_val = txt6.get()
    txt6.delete(0,END)
    d = new_val.split(',')
    new_val_int= int(d[0])
    d.pop(0)
    d.insert(0, new_val_int)
    m.replace(c,d)
    print(m.storage)



admit = Button(my_canvas, text="Admit",fg="white", bg='chocolate', height=1, width=10, command=admitbutton)
admit.place(x=0, y=90)

peek = Button(my_canvas, text="Peek",fg="white", bg='chocolate', height=1, width=10, command=peek )
peek.place(x=0, y=130)

poll = Button(my_canvas, text="Poll", fg="white", bg='chocolate', height=1, width=10, command=poll_queue)
poll.place(x=0, y=170)

remove = Button(my_canvas, text="Remove",fg="white", bg='chocolate', height=1, width=10,command=removebutton )
remove.place(x=0, y=210)  

size = Button(my_canvas, text="Size", fg="white", bg='chocolate', height=1, width=10, command=size_of_queue)
size.place(x=0, y=250)

isEmpty = Button(my_canvas, text="isEmpty",fg="white", bg='chocolate', height=1, width=10, command=is_queue_empty)
isEmpty.place(x=0, y=290)

RepPriority = Button(my_canvas, text="RepPriority",fg="white", bg='chocolate', height=1, width=10, command= prioritybutton)
RepPriority.place(x=0, y=330)

RepValue = Button(my_canvas, text="RepValue", fg="white", bg='chocolate', height=1, width=10, command=valuebutton)
RepValue.place(x=0, y=370)


m = myList()



window.mainloop()