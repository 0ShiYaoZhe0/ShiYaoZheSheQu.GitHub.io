# 导入模块
import time as TM
import tkinter as TIT
import tkinter.messagebox as TITMAB
root = TIT.Tk()

def Exit_program():#离开提醒
    i = TITMAB.askyesno("退出程序","是否关闭程序？")
    if i == True:
        root.quit()
    else:
        return

def sb_Not_finished():
    e = TITMAB.showwarning("摸鱼大王（0shiyaozhe0）","大哥大嫂对不起，没做完")
def Parent_management_interface():#家长程序
    root5 = TIT.Tk()
    root5.title("电脑游戏管理系统")
    root5.geometry("600x400+374+182")
    judgeBottonYes = TIT.Button(root5, text="时间限制", font=("微软雅黑", 18), fg="blue", command=sb_Not_finished)
    judgeBottonYes.grid(row=1, column=1)
    judgeBottonYes = TIT.Button(root5, text="游戏名单", font=("微软雅黑", 18), fg="blue", command=sb_Not_finished)
    judgeBottonYes.grid(row=1, column=2)
    judgeLabel = TIT.Label(root5, text="周一", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    judgeLabel = TIT.Label(root5, text="周二", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    judgeLabel = TIT.Label(root5, text="周三", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    judgeLabel = TIT.Label(root5, text="周四", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    judgeLabel = TIT.Label(root5, text="周五", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    judgeLabel = TIT.Label(root5, text="周六", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    judgeLabel = TIT.Label(root5, text="周日", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    judgeBottonYes = TIT.Button(root5, text="退出", font=("微软雅黑", 18), fg="red", command=Exit_program)
    judgeBottonYes.grid(row=9, column=1)
    root5.mainloop()


def Student_interface():#学生程序
    root5 = TIT.Tk()
    root5.title("电脑游戏管理系统")
    root5.geometry("600x400+374+182")
    judgeLabel = TIT.Label(root5, text="你好，正在开发中。。。。。。", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    judgeBottonYes = TIT.Button(root5, text="退出", font=("微软雅黑", 18), fg="red", command=Exit_program)
    judgeBottonYes.grid(row=5, column=1)
    root5.mainloop()

def Parent_registration():#家长注册
    root2 = TIT.Tk()
    fP = open("家长的密码和账户名（好好藏好，不要泄露.txt",mode='a')
    root2.title("电脑游戏管理系统")
    root2.geometry("600x400+374+182")
    judgeLabel = TIT.Label(root2, text="请输入您的账户名和密码（注册）", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    judgeLabel = TIT.Label(root2, text="账户名：", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    e = TIT.StringVar()
    e2 = TIT.StringVar()
    entry = TIT.Entry(root2, font=("微软雅黑", 18), textvariable=e)
    entry.grid()
    userName1 = e
    userName1s =userName1
    judgeLabel = TIT.Label(root2, text="密码：", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    e = TIT.StringVar()
    entry2 = TIT.Entry(root2, font=("微软雅黑", 18), textvariable=e)
    usermm = e2
    usermms = usermm
    #global user
    entry2.grid()
    judgeBottonOk = TIT.Button(root2, text="确定", font=("微软雅黑", 18), fg="green",command=Parent_management_interface)
    judgeBottonOk.grid(row=4, column=1)
    judgeBottonYes = TIT.Button(root2, text="退出", font=("微软雅黑", 18), fg="red", command=Exit_program)
    judgeBottonYes.grid(row=5, column=1)
    root2.mainloop()

def student_registration():#学生注册
    root4 = TIT.Tk()
    root4.title("电脑游戏管理系统")
    root4.geometry("600x400+374+182")
    judgeLabel = TIT.Label(root4, text="请输入您的账户名（注册）", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    judgeLabel = TIT.Label(root4, text="账户名：", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    #e = root4.StringVar()
    entry = TIT.Entry(root4, font=("微软雅黑", 18))
    entry.grid()
    #userName2 = e
    judgeBottonOk = TIT.Button(root4, text="确定", font=("微软雅黑", 18), fg="green",command=Student_interface)
    judgeBottonOk.grid(row=4, column=1)
    judgeBottonYes = TIT.Button(root4, text="退出", font=("微软雅黑", 18), fg="red", command=Exit_program)
    judgeBottonYes.grid(row=5, column=1)
    root4.mainloop()
def judgeYes_identity():#身份选择
    root3 = TIT.Tk()
    root3.title("电脑游戏管理系统")
    root3.geometry("600x400+374+182")
    judgeLabel = TIT.Label(root3, text="请选择身份", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    judgeBottonYes = TIT.Button(root3, text="学生", font=("微软雅黑", 18), fg="green",command=student_registration)
    judgeBottonYes.grid(row=1, column=1)
    judgeBottonYes = TIT.Button(root3, text="家长", font=("微软雅黑", 18), fg="yellow", command=Parent_registration)
    judgeBottonYes.grid(row=2, column=1)
    judgeBottonYes = TIT.Button(root3, text="退出", font=("微软雅黑", 18), fg="blue", command=Exit_program)
    judgeBottonYes.grid(row=3, column=1)
    root.mainloop()
    # 添加输入框


def initialization():#主程序

    root.geometry("600x400+374+182")
    root.title("电脑游戏管理系统")
    #root.iconbitmap('ico.ico')
    judgeLabel = TIT.Label(root, text="您是否是第一次使用？", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    # 添加点击按钮
    judgeBottonYes = TIT.Button(root, text="是(yse)", font=("微软雅黑", 18), fg="green", command=judgeYes_identity)
    judgeBottonYes.grid(row=1, column=1)
    judgeBottonYes = TIT.Button(root, text="不是(no)", font=("微软雅黑", 18), fg="red",command=sb_Not_finished)
    judgeBottonYes.grid(row=1, column=2)
    judgeBottonYes = TIT.Button(root, text="退出", font=("微软雅黑", 18), fg="blue",command=Exit_program)
    judgeBottonYes.grid(row=2, column=1)
    root.mainloop()

initialization()
