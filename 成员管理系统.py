import easygui as eg
import sys
import random
import pandas
import pickle
import warnings
import contextlib
warnings.filterwarnings("ignore")

f=open("txt.txt","rb")
w = pickle.load(f)
f.close()
i=0
while 1:
    try:                                          #忽视报错（头），
        q = eg.multpasswordbox("欢迎使用成员管理系统", "2000800304罗丽诗的成员管理系统", fields=('账户', '密码'))  #密码输入框
        if q[0]=="1"and q[1] == "1":              #检验账号密码是否正确
            try:                                  #忽视报错（头），（如果编译发生错误，直接跳到最后面的except）
                while 1:
                    c = eg.choicebox("功能选择","2000800304罗丽诗的成员管理系统",
                                     ["录入成员信息","显示成员信息","删除成员信息",
                                    "排序成员信息","查找成员信息", "修改成员信息","退出"])  #选择框


                    if str(c) == "录入成员信息":    #判断选择
                        t = "成员信息录入系统"
                        xuanxiang =["工号","姓名","性别","年龄","工作","学历","月薪","电话号码","家庭住址"]
                        xinxi = []
                        xinxi = eg.multenterbox("请填写成员信息",t,xuanxiang)                 #多项填写框，依次填写列表xuanxiang中的内容
                        d = {'工号': xinxi[0], '姓名': xinxi[1], '性别': xinxi[2],'年龄':xinxi[3],
                             '工作':xinxi[4],'学历':xinxi[5],
                             '月薪':xinxi[6],'电话号码':xinxi[7],'家庭住址':xinxi[8]}            #将所填写的新成员信息存入字典d中
                        w = pandas.DataFrame(w)
                        d = pandas.Series(d, name=xinxi[0])             #将字典d变成可供Dataframe数据结构识别的序列
                        w = w.append(d)                                #将字典d添加到w这个Dataframe数据结构中（Dataframe数据结构就是由若干个字典构成的）
                        f = open("txt.txt", "wb")                      #以写的方式打开txt.txt文档，并用f来实例化这个文档
                        pickle.dump(w, f)                               #将people这个Dataframe数据结构存入txt.txt文档中
                        f.close()                                       #保存并关闭文档


                    elif str(c)=="显示成员信息":
                        f=open("txt.txt","rb")                   #以读的方式打开txt.txt文档，并用f来实例化这个文档
                        w = pickle.load(f)                       #将文档中储存的数据结构存入w这个Dataframe数据结构中
                        f.close()                              #保存并关闭文档
                        w=pandas.DataFrame(w)                 #确保w为Dataframe数据结构，再赋值
                        w = w.values                            #转化为二维列表
                        string = "工号         姓名    性别  年龄  工作  学历   月薪    电话号码     家庭住址      \n"
                        for i in range(len(w)):                #遍历成员
                            for j in range(9):                 #遍历遍历成员信息
                                string = string+str(w[i][j])+"   "    #信息存入字符串中
                            string = string+"\n"               #将每个成员信息的最后加一个换行符换行（实现一成员占一行的显示效果）
                        eg.msgbox(string,"成员信息")            #提示框，将每个成员的信息打印在提示框上，按OK继续


                    elif str(c) == "删除成员信息":
                        while 1:
                            f=open("txt.txt","rb")
                            w = pickle.load(f)
                            f.close()
                            w = pandas.DataFrame(w)
                            w1 = w.values
                            chengyuan=[]                                    #创建一个空列表用于存放成员姓名
                            for i in range(len(w1)):
                                chengyuan.append(str(w1[i][1]))             #将w1[i][1]（所指的成员位置添加到chengyuan这个列表中
                            chengyuan.append("退出")                         #将"退出"这个字符串添加到末尾，用于用户的退出操作
                            c = eg.choicebox("请选择欲删除的成员","成员信息删除系统",chengyuan)  #选择框，
                            if c=="退出":break                                  #当c为”退出“，break（退出）
                            else:
                                w.drop(c, axis=0, inplace=True)           #将w这个Dataframe数据结构中删除名为c（所选的姓名）序列
                                f = open("txt.txt", "wb")
                                pickle.dump(w, f)
                                f.close()


                    elif str(c) == "排序成员信息":
                        f=open("txt.txt","rb")
                        w = pickle.load(f)
                        f.close()
                        w = pandas.DataFrame(w)
                        c = eg.choicebox("请选择排序方式","成员信息排序系统",["按工号排序","按年龄排序","按工资排序"])
                        if  c=="按工号排序":
                            w = w.sort_values(by="工号")
                        elif c=="按年龄排序":
                            w = w.sort_values(by="年龄")
                        elif c == "按工资排序":
                            w = w.sort_values(by="月薪")
                        eg.msgbox("排序成功！！", "排序成功！！")

                        f = open("txt.txt", "wb")
                        pickle.dump(w, f)
                        f.close()


                    elif str(c) == "查找成员信息":
                        f=open("txt.txt","rb")
                        w = pickle.load(f)
                        f.close()
                        w = pandas.DataFrame(w)
                        w1 = w.values
                        while 1:
                            ID = eg.enterbox("请输入成员工号进行查询：(输入r退出查找系统)","成员信息查找系统")
                            z=-1
                            if ID=='r':break
                            else:
                                for i in range(len(w1)):
                                    if w1[i][0] == ID:
                                        z=i
                                if z<0:
                                    eg.msgbox("未找到该成员信息，请重新输入","异常")
                                else:
                                    string = "工号         姓名    性别  年龄  工作  学历   月薪    电话号码     家庭住址      \n"
                                    for j in range(9):  # for循环
                                        string = string + str(w1[z][j]) + "   "  # 将各项成员信息存入string这个字符串中
                                    eg.msgbox(string,"已找到该成员信息")
                                    break


                    elif str(c) == "退出":
                        sys.exit()


                    elif str(c) == "修改成员信息":
                        xuanxiang = ["工号", "姓名", "性别", "年龄", "工作", "学历", "月薪", "电话号码", "家庭住址"]
                        f=open("txt.txt","rb")
                        w = pickle.load(f)
                        f.close()
                        w = pandas.DataFrame(w)
                        w1 = w.values
                        while 1:
                            ID = eg.enterbox("请输入需要修改的成员工号：(输入r退出查找系统)", "成员信息修改系统")
                            z = -1
                            if ID == 'r':
                              break
                            else:
                                for i in range(len(w1)):
                                    if w1[i][0] == ID:
                                      z = i
                                if z < 0:
                                     eg.msgbox("未找到该成员信息，请重新输入", "异常")
                                else:
                                      string = "工号         姓名    性别  年龄  工作  学历   月薪    电话号码     家庭住址      \n"
                                      for j in range(9):  # for循环
                                          string = string + str(w1[z][j]) + "   "    # 将各项成员信息存入string这个字符串中
                                      c = eg.choicebox(string+"\n请选择需要修改的信息","信息修改系统",xuanxiang)
                                      q = eg.enterbox("请输入新信息：(输入'r'退出查找系统)","信息修改系统")
                                      if q=='r':
                                          break
                                      else:
                                        w[c][z]=q
                                        eg.msgbox("修改成功！","修改成功！")
                                        f = open("txt.txt", "wb")
                                        pickle.dump(w, f)
                                        f.close()
                                        break
            except:           #忽视报错（尾），（如果编译发生错误，执行下列语句break）
                break
        else:
          eg.msgbox("账号或密码错误！", "账号或密码错误！")
    except:                   #忽视报错（尾），（如果编译发生错误，执行下列语句break）
        break
