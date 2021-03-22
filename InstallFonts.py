import shutil
import os
inputPath = r"D:\Cinema\剪辑素材\540个电影级调色LUTS预设包@资源实验室\540个电影级调色LUTS预设包@资源实验室"
outputPath = r"D:\Cinema\剪辑素材\cube"#目标文件位置Font
sourceFiles = []


def search (path,sourceFiles):
    items = os.listdir(path)
    for item in items:
        subpath = os.path.join(path,item)
        if os.path.isdir(subpath):#是个文件夹
            print("[dir]"+subpath)
            search(subpath,sourceFiles)
        elif subpath.split('.')[-1]=="cube":
            print("[target]" + subpath)
            sourceFiles.append(subpath)
        else:
            #print("[non-target]"+subpath)
            pass


print("开始扫描")
search(inputPath,sourceFiles)
print("共有"+str(len(sourceFiles))+"文件，现在开始安装")
for file in sourceFiles:
    if not os.path.exists(outputPath):
        os.mkdir(outputPath)
    shutil.copy(file,outputPath)
    print("完成"+file+"文件安装")
