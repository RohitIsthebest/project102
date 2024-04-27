import os
import shutil

from_dir = "C:/Users/This PC/Downloads"
to_dir = "C:/Users/This PC/Documents"

list_of_files = os.listdir(from_dir)

for i in list_of_files:
    name,ext = os.path.splitext(i)

    if ext == "":
        continue
    if ext in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir +'/' + i
        path2 = to_dir + '/' + "Document Files"
        path3 = to_dir + '/' + "Document Files" + '/' + i
        if os.path.exists(path2):
            print("moving to destination")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("creating new folder at desitnation")
            
            shutil.move(path1,path3)
            