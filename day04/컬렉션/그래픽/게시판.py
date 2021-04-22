#게시판 화면 만들기
#항목/입력번호/ / 제목// 내용// 작성자
#버튼 : 글쓰기완료
from tkinter import *
from tkinter import messagebox
def summit():
    number2=number_entry.get()
    title2=title_entry.get()
    cont2=cont_entry.get()
    writer2=writer_entry.get()
    print(number2, title2, cont2, writer2)
    w2=Tk()
    w2.geometry('300x300')
    l = Label(w2, text=number2 , font=('돋움', 30))
    l.pack()
    l2 = Label(w2, text=title2, font=('돋움', 30))
    l2.pack()
    l3 = Label(w2, text=cont2, font=('돋움', 30))
    l3.pack()
    l4 = Label(w2, text=writer2, font=('돋움', 30))
    l4.pack()
    #messagebox.showinfo(number2, title2, cont2, writer2)
    w2.mainloop()

w= Tk()
w.geometry("500x500")
number = Label(w, text="번호 ", font=('돋움', 30), bg='white', fg='blue')#번호 글자
number.pack()
number_entry=Entry(w, font=('돋움', 30), bg='pink', fg='black')#번호 입력
number_entry.pack()
title=Label(w, text='제목', font=('돋움', 30), bg='white', fg='blue') #제목글자
title.pack()
title_entry=Entry(w, font=('돋움', 30), bg='pink', fg='black')#제목입력
title_entry.pack()
cont = Label(w, text="내용 ", font=('돋움', 30), bg='white', fg='blue')#내용 글자
cont.pack()
cont_entry=Entry(w, font=('돋움', 30), bg='pink', fg='black')#내용 입력
cont_entry.pack()
writer = Label(w, text="작성자 ", font=('돋움', 30), bg='white', fg='blue')#작성자 글자
writer.pack()
writer_entry=Entry(w, font=('돋움', 30), bg='pink', fg='black')#작성자 입력
writer_entry.pack()

b=Button(w, text='글쓰기 완료', font=('돋움',30), bg='white', fg='green', command=summit) #버튼
b.pack()

w.mainloop()
