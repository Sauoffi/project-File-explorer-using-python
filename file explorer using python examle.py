import os, shutil
path = r"folder path"
a = os.listdir(path)
print(a)
folfers = ["csv files", "image files", "text files", "Excel files"]
try:
    for i in range(0,4):
        if not os.path.exists(path + 'folfers'):
            print(path + folfers[i])
            os.makedirs(path + folfers[i])

except:
    for x in a:
        if ".txt" in x and not os.path.exists(path + "text files/" + x):
            shutil.move(path + x, path + "text files/" + x)
        elif ".jpg" in x and not os.path.exists(path + "image files/" + x):
            shutil.move(path + x, path + "image files/" + x)
        elif ".xlsx" in x and not os.path.exists(path + "Excel files/" + x):
            shutil.move(path + x, path + "Excel files/" + x)
        else:
            print("This file type is not supported.")