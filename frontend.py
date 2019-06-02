from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    e5.delete(0,END)
    e5.insert(END,selected_tuple[5])
    e6.delete(0,END)
    e6.insert(END,selected_tuple[6])
    e7.delete(0,END)
    e7.insert(END,selected_tuple[7])
    e8.delete(0,END)
    e8.insert(END,selected_tuple[8])
    e9.delete(0,END)
    e9.insert(END,selected_tuple[9])
    e10.delete(0,END)
    e10.insert(END,selected_tuple[10])
    e11.delete(0,END)
    e11.insert(END,selected_tuple[11])
    e12.delete(0,END)
    e12.insert(END,selected_tuple[12])
    e13.delete(0,END)
    e13.insert(END,selected_tuple[13])




def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get(), des_text.get(), certi_text.get(), logo_link.get(), orgname_text.get(), orgadd_text.get(), start_text.get(), min_text.get(), max_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get(),des_text.get(),certi_text.get(),logo_link.get(),orgname_text.get(),orgadd_text.get(),start_text.get(),min_text.get(),max_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get(), des_text.get(), certi_text.get(),logo_link.get(),orgname_text.get(),orgadd_text.get(),start_text.get(),min_text.get(),max_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get(), des_text.get(), certi_text.get(),logo_link.get(),orgname_text.get(),orgadd_text.get(),start_text.get(),min_text.get(),max_text.get())

window=Tk()

window.wm_title("Admin")

l1=Label(window,text="Programme Name")
l1.grid(row=0,column=0)

l2=Label(window,text="Trainer")
l2.grid(row=0,column=2)

l3=Label(window,text="No. of Semesters")
l3.grid(row=1,column=0)

l4=Label(window,text="No. of Credits")
l4.grid(row=1,column=2)

l5=Label(window,text="Programme Description")
l5.grid(row=2,column=0)

l6=Label(window,text="Type of Certification")
l6.grid(row=2,column=2)

l7=Label(window,text="Logo Link")
l7.grid(row=3,column=0)

l8=Label(window,text="Name of Organisation")
l8.grid(row=3,column=2)

l9=Label(window,text="Address of Organisation")
l9.grid(row=4,column=0)

l10=Label(window,text="Start Date")
l10.grid(row=4,column=2)

l11=Label(window,text="Minimum Participation")
l11.grid(row=5,column=0)

l10=Label(window,text="Maximum Participation")
l10.grid(row=5,column=2)







title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

des_text=StringVar()
e5=Entry(window,textvariable=des_text)
e5.grid(row=2,column=1)

certi_text=StringVar()
e6=Entry(window,textvariable=certi_text)
e6.grid(row=2,column=3)

logo_link=StringVar()
e7=Entry(window,textvariable=logo_link)
e7.grid(row=3,column=1)


orgname_text=StringVar()
e8=Entry(window,textvariable=orgname_text)
e8.grid(row=3,column=3)

orgadd_text=StringVar()
e9=Entry(window,textvariable=orgadd_text)
e9.grid(row=4,column=1)

start_text=StringVar()
e10=Entry(window,textvariable=start_text)
e10.grid(row=4,column=3)

min_text=StringVar()
e11=Entry(window,textvariable=min_text)
e11.grid(row=5,column=1)

max_text=StringVar()
e12=Entry(window,textvariable=max_text)
e12.grid(row=5,column=3)



list1=Listbox(window, height=18,width=50)
list1.grid(row=7,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=7,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window,text="View all", width=18,command=view_command)
b1.grid(row=7,column=3)

b2=Button(window,text="Search entry", width=18,command=search_command)
b2.grid(row=8,column=3)

b3=Button(window,text="Add entry", width=18,command=add_command)
b3.grid(row=9,column=3)

b4=Button(window,text="Update selected", width=18,command=update_command)
b4.grid(row=10,column=3)

b5=Button(window,text="Delete selected", width=18,command=delete_command)
b5.grid(row=11,column=3)

b6=Button(window,text="Close", width=18,command=window.destroy)
b6.grid(row=12,column=3)

window.mainloop()
