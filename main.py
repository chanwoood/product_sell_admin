from tkinter import *  
from tkinter.messagebox import *  
from MainPage import *  
import pymssql

conn = pymssql.connect(host="127.0.0.1:1433",user="root",password="xxxx",database="product_sell_admin")
cur = conn.cursor() 
  
class LoginPage(object):  
    def __init__(self, master=None):  
        self.root = master #定义内部变量root  
        self.root.geometry('%dx%d' % (300, 180)) #设置窗口大小  
        self.username = StringVar()  
        self.password = StringVar()  
        self.createPage()  
  
    def createPage(self):  
        self.page = Frame(self.root) #创建Frame  
        self.page.pack()  
        Label(self.page).grid(row=0, stick=W)  
        Label(self.page, text = '账户: ').grid(row=1, stick=W, pady=10)  
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)  
        Label(self.page, text = '密码: ').grid(row=2, stick=W, pady=10)  
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)  
        Button(self.page, text='登陆', command=self.login).grid(row=3, stick=W, pady=10)  
        Button(self.page, text='注册', command=self.register).grid(row=3, column=1, stick=E)  

    def login(self):  
        user = self.username.get()  
        psw = self.password.get()  
        cur.execute('select * from 用户')
        if (user, psw) in cur.fetchall():
            self.page.destroy()  
            MainPage(self.root)
        else:
            showinfo(title = '错误', message="用户名或密码有误！")
         

    def register(self):
        user = self.username.get()  
        psw = self.password.get()
        cur.execute('select 用户名 from 用户')
        if (user,) in cur.fetchall() :
            showinfo(title='错误', message='该用户已注册！请输入其他用户名') 
        else: 
            showinfo(title = '成功', message="注册成功！已以{}身份登入".format(user))
            self.page.destroy()  
            MainPage(self.root)
            cur.execute('insert into 用户 values(%s, %s)', (user, psw))

root = Tk()  
root.title('产品销售管理系统')  
LoginPage(root)  
root.mainloop() 

conn.commit()
cur.close()