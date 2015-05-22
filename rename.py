import os

def rename_files():
    for i in os.listdir("/home/sglukhov/ph"):
        os.chdir("/home/sglukhov/ph")

        print i
        os.rename(i,i.translate(None,"0123456789"))
        print i

rename_files()
