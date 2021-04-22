
from tkinter import *
#import tkinter

#GUI/CLI
#함수 : 버튼을 눌렀을 때 로그인 기능을 처리해야 함.
# 특정 기능은 하나의 함수로 만들어줌.
# 버튼 = 눌렀을 때 처리하고자 하는 기능 하나 = 기능 하나 당 함수 하나.
# 함수를 만드는 것 =함수를 정의함. why? 기능을 프로그래머가 정의하기 때문에
def login():#ID,PW 입력/ 회원가입시 입력값과 비교
    id2= id_entry.get()
    print('입력한 id는', id2)
    #root/1234 원래의 값과 동일한지 판별하여 프린트
    pw2=pw_entry.get()
    print('입력한 pw는', pw2)
    if id2 == "root" and pw2 =="1234":
        messagebox.showinfo('로그인성공', '축하합니다')
        print('로그인성공')
        w2 = Tk()
        w2.geometry('300x300')
        l=Label(w2, text="로그인성공 축하합니다")
        l.pack()
        w2.mainloop()
    else:
        print('잘못된 정보입니다.')
#id


w = Tk()
w.geometry("500x250")

id = Label(w, text="ID입력: ", font=('궁서', 30))#id 글자 넣는 함
id.pack()
id_entry=Entry(w, font=('궁서', 30), bg='blue', fg='white')
id_entry.pack()

pw=Label(w, text="pw입력: ", font=('궁서', 30))
pw.pack()

#
pw_entry=Entry(w, font=('궁서', 30), bg='blue', fg='white')
pw_entry.pack()

b= Button(w, text='로그인 처리', font=('궁서', 30), bg='yellow', command=login)
b.pack()

w.mainloop()