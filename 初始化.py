import easygui as eg
import sys
import random
import pandas
import pickle
import warnings
import contextlib

w = pandas.DataFrame(columns=["工号","姓名","性别","年龄","工作","学历","月薪","电话号码","家庭住址"])
f = open("txt.txt", "wb")  # 以写的方式打开txt.txt文档，并用f来实例化这个文档
pickle.dump(w, f)  # 将people这个Dataframe数据结构存入txt.txt文档中
f.close()

