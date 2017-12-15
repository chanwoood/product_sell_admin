from tkinter import *  
from tkinter.messagebox import *  
import pymssql

class InputFrame(Frame): # 录入类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.itemNum = StringVar()  
        self.itemName = StringVar()  
        self.size = StringVar()  
        self.price = StringVar()  
        self.sum_ = StringVar()  
        self.createPage()  
  
    def createPage(self):  
        Label(self).grid(row=0, stick=W, pady=10)  
        Label(self, text = '产品编号: ').grid(row=1, stick=W, pady=10)  
        Entry(self, textvariable=self.itemNum).grid(row=1, column=1, stick=E)  
        Label(self, text = '名称:').grid(row=2, stick=W, pady=10)  
        Entry(self, textvariable=self.itemName).grid(row=2, column=1, stick=E)  
        Label(self, text = '规格:').grid(row=3, stick=W, pady=10)  
        Entry(self, textvariable=self.size).grid(row=3, column=1, stick=E)  
        Label(self, text = '单价:').grid(row=4, stick=W, pady=10)  
        Entry(self, textvariable=self.price).grid(row=4, column=1, stick=E)  
        Label(self, text = '库存数量:').grid(row=5, stick=W, pady=10)  
        Entry(self, textvariable=self.sum_).grid(row=5, column=1, stick=E)
        Button(self, text='录入', command=self.add).grid(row=6, column=1, stick=E, pady=10)  


    def add(self):
        conn = pymssql.connect(host="127.0.0.1:1433",user="root",password="2519",database="product_sell_admin")
        cur = conn.cursor() 

        itemNum = self.itemNum.get()
        itemName = self.itemName.get()
        size = self.size.get()
        price = self.price.get()
        sum_ = self.sum_.get()
        try:
            cur.execute('insert into 产品 values(%s, %s, %s, %s, %s)', (itemNum, itemName, size, price, sum_))
        except Exception:
            showinfo(title='错误', message='更新数据出错！') 
        else:
            showinfo(title='成功', message='该条记录已成功录入！')

        finally:
            conn.commit()
            cur.close() 



  
class QueryFrame(Frame): # 查询类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.kw = StringVar()  
        self.createPage()  
  
    def createPage(self):  
        Label(self).grid(row=0, stick=W, pady=10)  
        Label(self, text = '产品名称: ').grid(row=1, stick=W, pady=10)  
        Entry(self, textvariable=self.kw).grid(row=1, column=1, stick=E) 
        Button(self, text='查询', command=self.check).grid(row=1, column=3, stick=E, pady=10) 
        Label(self).grid(row=2, stick=W, pady=10)  

    def check(self):
        kw = self.kw.get()
        conn = pymssql.connect(host="127.0.0.1:1433",user="root",password="2519",database="product_sell_admin")
        cur = conn.cursor()

        cur.execute('select 名称 from 产品')
        if (kw, ) in cur.fetchall():
            cur.execute("select * from 产品 where 名称=%s", kw)
            text = Text(self, width=21, height=6)
            text.grid(row=5, column=1) 
            result = cur.fetchall()
            text.insert(1.0, '产品编号：{}'.format(result[0][0]))
            text.insert(2.0, '\n产品名称：{}'.format(result[0][1]))
            text.insert(3.0, '\n规格：{}'.format(result[0][2]))
            text.insert(4.0, '\n单价：{}'.format(result[0][3]))
            text.insert(5.0, '\n库存数量：{}'.format(result[0][4]))

        else:
            showinfo(title='无记录', message='找不到该产品信息！') 

        conn.commit()
        cur.close()



  
class CountFrame(Frame): # 统计类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master  #定义内部变量root  
        self.sum_ = StringVar()
        self.createPage()  
  
    def createPage(self):  
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text = '库存数量低于').grid(row=1, stick=W, pady=10)  
        Entry(self, textvariable=self.sum_).grid(row=1, column=1, stick=E) 
        Button(self, text='统计', command=self.count).grid(row=1, column=3, stick=E, pady=10) 
        Label(self).grid(row=2, stick=W, pady=10)    

    def count(self):
        sum_ = self.sum_.get()
        conn = pymssql.connect(host="127.0.0.1:1433",user="root",password="2519",database="product_sell_admin")
        cur = conn.cursor()

        text = Text(self, width=21, height=6)
        text.grid(row=5, column=1)


        cur.execute("select 名称, 库存数量 from 产品 where 库存数量<%s", sum_)
        result = cur.fetchall()
        for i in result:
            text.insert(1.0, '{}：{}\n'.format(i[0], i[1]))

    

        conn.commit()
        cur.close()
  
  
class AboutFrame(Frame): # 关于类  
    def __init__(self, master=None):  
        Frame.__init__(self, master)  
        self.root = master #定义内部变量root  
        self.createPage()  
  
    def createPage(self):  
        Label(self, text='\n\n\n数据库课程设计\n\n产品销售管理系统\n\n使用 Python 开发', fg = 'red', 
            compound = 'center', font = ("Arial, 17")).pack()  

