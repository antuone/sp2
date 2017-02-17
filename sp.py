from tkinter import ttk
from tkinter import *
import os
import threading


walk = os.walk('/mnt/ftp')
root = walk.__next__()
DIRS = {}

for dir in root[1]:
    DIRS[dir] = []
    sds = walk.__next__()
    for sd in sds[1]:
         DIRS[dir].append(sd)
         walk.__next__()

def EntryR_Change(event):
    ListBoxR.delete(0, ListBoxR.size()-1)
    text = EntryR.get()
    for r in DIRS:
        if text in r:
            ListBoxR.insert(END, r)

def ListBoxRClick(event):
    ListBoxP.delete(0, ListBoxP.size()-1)
    sds = DIRS[ListBoxR.get(ListBoxR.curselection()[0])]
    for sd in sds:
        ListBoxP.insert(END, sd)

def Button1Click(event):
    if Button1['state'] == 'disabled':
        return

    r = ListBoxR.get(ListBoxR.curselection()[0])
    p = ListBoxP.get(ListBoxP.curselection()[0])
    n = ListBoxZV.get(ListBoxZV.curselection()[0])
    
    Button1['state'] = 'disabled'
    Button1['text'] = 'Фотографии перемещаются на сервер'
    progressbar.start()
    threading.Thread(target=rocket, args=(r, p, n, Var1.get())).start()
    
def rocket(r, p, n, v):
    os.system("/etc/udev/rules.d/sp/sp.sh %s %s %s %s" % (r,p,n,v))
    progressbar.stop()
    Button1['text'] = 'Фотографии перемещены'
    # Button1['state'] = 'normal'

window = Tk()
window.title('Обнаружено USB устройство')
# window.bind('<Destroy>', Exit)

Label1=Label(window, text='Для поиска рейса введите название и нажмите Enter', font='arial 18')
Label1.pack()

EntryR=Entry(window, width=50, font='Arial 18',)
EntryR.pack()
EntryR.bind("<KeyRelease>", EntryR_Change)

Label2=Label(window, text='Выберите Рейс:', font='arial 18')
Label2.pack()

ListBoxR = Listbox(window, width=50, font='Arial 18', exportselection=0)
ListBoxR.pack()
ListBoxR.bind('<ButtonRelease-1>', ListBoxRClick)

Label4=Label(window, text='Выберите Партию:', font='arial 18')
Label4.pack()

ListBoxP = Listbox(window, width=50, font='Arial 18', exportselection=0)
ListBoxP.pack()

Label5=Label(window, text='Направление', font='arial 18')
Label5.pack()

ListBoxZV = Listbox(window, width=50, height=2, font='Arial 18', exportselection=0)
ListBoxZV.pack()
ListBoxZV.insert(END, "Загрузка")
ListBoxZV.insert(END, "Выгрузка")

Var1=IntVar()
СheckBox1=Checkbutton(window, text='Удалить фотографии после отправки', variable=Var1, onvalue=1, offvalue=0, font='arial 20')
СheckBox1.pack()


Button1=Button(window, text='Отправить фотографии',width=25, font='arial 20')
Button1.pack()
Button1.bind('<ButtonRelease-1>', Button1Click)

progressbar = ttk.Progressbar(window, orient='horizontal', length=700, mode='indeterminate')
progressbar.pack()


window.mainloop()
