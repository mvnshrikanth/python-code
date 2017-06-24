import os
import re

def rename_files():
    file_list = os.listdir(r"C:\Users\mvnsh\Documents\Work\Python\prank")
    saved_path = os.getcwd()
    print("Current Working Directory is "+ saved_path)
    os.chdir(r"C:\Users\mvnsh\Documents\Work\Python\prank")

    for file_name in file_list:
        os.rename(file_name,re.sub('[0-9]','',file_name))

    os.chdir(saved_path)

rename_files()
