import pandas as pd
import random
import xlrd
import numpy


def randomPick(length,columns):
    myset = set()
    for i in range(length):
        myset.add(random.randrange(0,columns-1))
    return myset


inputPath = "学生名单.xls" #输入文件路径
number = 6#学生个数
df = pd.read_excel(inputPath,sheet_name=0,header=1)
columns = df.shape[0]
set = randomPick(number,columns)
setlist = list(set)
print(df.iloc[setlist,0:3])#输出



