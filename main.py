#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys
from icon import img #引入生成的图标base64编码
import base64 #引入编码库

if sys.version_info[0] == 2:
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    from tkinter import *
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('VB登录界面')
        self.master.geometry('393x296')
        self.master.resizable(0,0)
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.TabStrip1 = Notebook(self.top)
        self.TabStrip1.place(relx=0.081, rely=0.135, relwidth=0.837, relheight=0.814)

        self.TabStrip1__Tab1 = Frame(self.TabStrip1)
        self.Command_登录Var = StringVar(value='登录')
        self.style.configure('TCommand_登录.TButton', font=('宋体',9))
        self.Command_登录 = Button(self.TabStrip1__Tab1, text='登录', textvariable=self.Command_登录Var, command=self.Command_登录_Cmd, style='TCommand_登录.TButton')
        self.Command_登录.setText = lambda x: self.Command_登录Var.set(x)
        self.Command_登录.text = lambda : self.Command_登录Var.get()
        self.Command_登录.place(relx=0.511, rely=0.75, relwidth=0.198, relheight=0.192)
        self.Command_注册Var = StringVar(value='注册')
        self.style.configure('TCommand_注册.TButton', font=('宋体',9))
        self.Command_注册 = Button(self.TabStrip1__Tab1, text='注册', textvariable=self.Command_注册Var, command=self.Command_注册_Cmd, style='TCommand_注册.TButton')
        self.Command_注册.setText = lambda x: self.Command_注册Var.set(x)
        self.Command_注册.text = lambda : self.Command_注册Var.get()
        self.Command_注册.place(relx=0.219, rely=0.75, relwidth=0.173, relheight=0.192)
        self.Text_密码Var = StringVar(value='')
        self.Text_密码 = Entry(self.TabStrip1__Tab1, textvariable=self.Text_密码Var, font=('宋体',9))
        self.Text_密码.setText = lambda x: self.Text_密码Var.set(x)
        self.Text_密码.text = lambda : self.Text_密码Var.get()
        self.Text_密码.place(relx=0.316, rely=0.45, relwidth=0.392, relheight=0.155)
        self.Text_用户名Var = StringVar(value='')
        self.Text_用户名 = Entry(self.TabStrip1__Tab1, textvariable=self.Text_用户名Var, font=('宋体',9))
        self.Text_用户名.setText = lambda x: self.Text_用户名Var.set(x)
        self.Text_用户名.text = lambda : self.Text_用户名Var.get()
        self.Text_用户名.place(relx=0.316, rely=0.188, relwidth=0.392, relheight=0.155)
        self.Label2Var = StringVar(value='密码')
        self.style.configure('TLabel2.TLabel', anchor='w', font=('宋体',9))
        self.Label2 = Label(self.TabStrip1__Tab1, text='密码', textvariable=self.Label2Var, style='TLabel2.TLabel')
        self.Label2.setText = lambda x: self.Label2Var.set(x)
        self.Label2.text = lambda : self.Label2Var.get()
        self.Label2.place(relx=0.122, rely=0.45, relwidth=0.1, relheight=0.155)
        self.Label1Var = StringVar(value='用户名')
        self.style.configure('TLabel1.TLabel', anchor='w', font=('宋体',9))
        self.Label1 = Label(self.TabStrip1__Tab1, text='用户名', textvariable=self.Label1Var, style='TLabel1.TLabel')
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(relx=0.097, rely=0.188, relwidth=0.149, relheight=0.155)
        self.TabStrip1.add(self.TabStrip1__Tab1, text='登录界面')

        self.TabStrip1__Tab2 = Frame(self.TabStrip1)
        self.Text_登录成功Font = Font(font=('宋体',9))
        self.Text_登录成功 = Text(self.TabStrip1__Tab2, font=self.Text_登录成功Font)
        self.Text_登录成功.place(relx=0.073, rely=0.113, relwidth=0.854, relheight=0.792)
        self.Text_登录成功.insert('1.0','管理员，欢迎您！\n您已经登录成功\n接下来可以进行增删查改操作啦！\n')
        self.TabStrip1.add(self.TabStrip1__Tab2, text='登录成功')
class Application_ui1(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('注册界面')
        self.master.geometry('456x339')
        self.master.resizable(0,0)
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.style.configure('TFrame1.TLabelframe', font=('宋体',9))
        self.style.configure('TFrame1.TLabelframe.Label', font=('宋体',9))
        self.Frame1 = LabelFrame(self.top, text='注册界面', style='TFrame1.TLabelframe')
        self.Frame1.place(relx=0.035, rely=0.047, relwidth=0.879, relheight=0.9)

        self.Command_忘记密码Var = StringVar(value='忘记密码')
        self.style.configure('TCommand_忘记密码.TButton', font=('宋体',9))
        self.Command_忘记密码 = Button(self.Frame1, text='忘记密码', textvariable=self.Command_忘记密码Var, command=self.Command_忘记密码_Cmd, style='TCommand_忘记密码.TButton')
        self.Command_忘记密码.setText = lambda x: self.Command_忘记密码Var.set(x)
        self.Command_忘记密码.text = lambda : self.Command_忘记密码Var.get()
        self.Command_忘记密码.place(relx=0.738, rely=0.367, relwidth=0.182, relheight=0.108)

        self.Command_提交注册Var = StringVar(value='提交注册')
        self.style.configure('TCommand_提交注册.TButton', font=('宋体',9))
        self.Command_提交注册 = Button(self.Frame1, text='提交注册', textvariable=self.Command_提交注册Var, command=self.Command_提交注册_Cmd, style='TCommand_提交注册.TButton')
        self.Command_提交注册.setText = lambda x: self.Command_提交注册Var.set(x)
        self.Command_提交注册.text = lambda : self.Command_提交注册Var.get()
        self.Command_提交注册.place(relx=0.738, rely=0.787, relwidth=0.182, relheight=0.108)

        self.Command_获取验证码Var = StringVar(value='获取验证码')
        self.style.configure('TCommand_获取验证码.TButton', font=('宋体',9))
        self.Command_获取验证码 = Button(self.Frame1, text='获取验证码', textvariable=self.Command_获取验证码Var, command=self.Command_获取验证码_Cmd, style='TCommand_获取验证码.TButton')
        self.Command_获取验证码.setText = lambda x: self.Command_获取验证码Var.set(x)
        self.Command_获取验证码.text = lambda : self.Command_获取验证码Var.get()
        self.Command_获取验证码.place(relx=0.738, rely=0.577, relwidth=0.182, relheight=0.108)

        self.Text_注册验证码Var = StringVar(value='')
        self.Text_注册验证码 = Entry(self.Frame1, textvariable=self.Text_注册验证码Var, font=('宋体',9))
        self.Text_注册验证码.setText = lambda x: self.Text_注册验证码Var.set(x)
        self.Text_注册验证码.text = lambda : self.Text_注册验证码Var.get()
        self.Text_注册验证码.place(relx=0.279, rely=0.787, relwidth=0.401, relheight=0.108)

        self.Text_注册手机号Var = StringVar(value='')
        self.Text_注册手机号 = Entry(self.Frame1, textvariable=self.Text_注册手机号Var, font=('宋体',9))
        self.Text_注册手机号.setText = lambda x: self.Text_注册手机号Var.set(x)
        self.Text_注册手机号.text = lambda : self.Text_注册手机号Var.get()
        self.Text_注册手机号.place(relx=0.279, rely=0.577, relwidth=0.401, relheight=0.108)

        self.Text_注册密码Var = StringVar(value='')
        self.Text_注册密码 = Entry(self.Frame1, textvariable=self.Text_注册密码Var, font=('宋体',9))
        self.Text_注册密码.setText = lambda x: self.Text_注册密码Var.set(x)
        self.Text_注册密码.text = lambda : self.Text_注册密码Var.get()
        self.Text_注册密码.place(relx=0.279, rely=0.367, relwidth=0.401, relheight=0.108)

        self.Text_注册账号Var = StringVar(value='')
        self.Text_注册账号 = Entry(self.Frame1, textvariable=self.Text_注册账号Var, font=('宋体',9))
        self.Text_注册账号.setText = lambda x: self.Text_注册账号Var.set(x)
        self.Text_注册账号.text = lambda : self.Text_注册账号Var.get()
        self.Text_注册账号.place(relx=0.279, rely=0.157, relwidth=0.401, relheight=0.108)

        self.Label5Var = StringVar(value='验证码')
        self.style.configure('TLabel5.TLabel', anchor='w', font=('宋体',9))
        self.Label5 = Label(self.Frame1, text='验证码', textvariable=self.Label5Var, style='TLabel5.TLabel')
        self.Label5.setText = lambda x: self.Label5Var.set(x)
        self.Label5.text = lambda : self.Label5Var.get()
        self.Label5.place(relx=0.08, rely=0.787, relwidth=0.122, relheight=0.082)

        self.Label4Var = StringVar(value='手机号')
        self.style.configure('TLabel4.TLabel', anchor='w', font=('宋体',9))
        self.Label4 = Label(self.Frame1, text='手机号', textvariable=self.Label4Var, style='TLabel4.TLabel')
        self.Label4.setText = lambda x: self.Label4Var.set(x)
        self.Label4.text = lambda : self.Label4Var.get()
        self.Label4.place(relx=0.08, rely=0.577, relwidth=0.162, relheight=0.108)

        self.Label3Var = StringVar(value='密码')
        self.style.configure('TLabel3.TLabel', anchor='w', font=('宋体',9))
        self.Label3 = Label(self.Frame1, text='密码', textvariable=self.Label3Var, style='TLabel3.TLabel')
        self.Label3.setText = lambda x: self.Label3Var.set(x)
        self.Label3.text = lambda : self.Label3Var.get()
        self.Label3.place(relx=0.08, rely=0.367, relwidth=0.142, relheight=0.108)

        self.Label2Var = StringVar(value='账号')
        self.style.configure('TLabel2.TLabel', anchor='w', font=('宋体',9))
        self.Label2 = Label(self.Frame1, text='账号', textvariable=self.Label2Var, style='TLabel2.TLabel')
        self.Label2.setText = lambda x: self.Label2Var.set(x)
        self.Label2.text = lambda : self.Label2Var.get()
        self.Label2.place(relx=0.08, rely=0.157, relwidth=0.142, relheight=0.108)

        self.Label1Var = StringVar(value='直接用学号注册，注册后登录账号就是学号')
        self.style.configure('TLabel1.TLabel', anchor='w', font=('宋体',9))
        self.Label1 = Label(self.Frame1, text='直接用学号注册，注册后登录账号就是学号', textvariable=self.Label1Var, style='TLabel1.TLabel')
        self.Label1.setText = lambda x: self.Label1Var.set(x)
        self.Label1.text = lambda : self.Label1Var.get()
        self.Label1.place(relx=0.18, rely=0.052, relwidth=0.681, relheight=0.056)
class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def Command_登录_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass
    def Command_注册_Cmd(self, event=None):
        # TODO, Please finish the function here!
        top1 = Toplevel(self)
        tmp = open("tmp.ico", "wb+")
        tmp.write(base64.b64decode(img))
        tmp.close()
        top1.iconbitmap('tmp.ico')
        os.remove("tmp.ico")  # 删掉临时文件
        Application1(top1)
        pass

class Application1(Application_ui1):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui1中。
    def __init__(self, master=None):
        Application_ui1.__init__(self, master)

    def Command_忘记密码_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def Command_提交注册_Cmd(self, event=None):
        #TODO, Please finish the function here!
        showinfo("信息","注册成功")
        self.top.destroy()
        pass

    def Command_获取验证码_Cmd(self, event=None):
        #TODO, Please finish the function here!
        showinfo("信息","验证码已发送至你的手机\n请注意查收")
        pass
if __name__ == "__main__":
    tmp = open("tmp.ico", "wb+")
    tmp.write(base64.b64decode(img))
    tmp.close()
    top = Tk()
    top.iconbitmap('tmp.ico')
    os.remove("tmp.ico")  # 删掉临时文件
    Application(top).mainloop()



