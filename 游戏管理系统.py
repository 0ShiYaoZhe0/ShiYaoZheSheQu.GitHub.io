# 导入模块
import time as TM
import tkinter as TIT


def initialization():
    root = TIT.Tk()
    root.geometry("600x400+374+182")
    root.title("电脑游戏管理系统")
    ## 更改左上角窗口的的icon图标,加载C语言中文网logo标
    #root.iconbitmap('ico.ico')
    judgeLabel = TIT.Label(root, text="您是否是第一次使用？", font=("微软雅黑", 18))
    judgeLabel.grid()  # 定位
    # 添加点击按钮
    judgeBottonYes = TIT.Button(root, text="是(yse)", font=("微软雅黑", 18), fg="green")
    judgeBottonYes.grid(row=1, column=1)
    judgeBottonYes = TIT.Button(root, text="不是(no)", font=("微软雅黑", 18), fg="red")
    judgeBottonYes.grid(row=1, column=2)
    judgeBottonYes = TIT.Button(root, text="退出", font=("微软雅黑", 18), fg="blue",command=root.quit)
    judgeBottonYes.grid(row=2, column=1)
    root.mainloop()


# def judge():

initialization()
