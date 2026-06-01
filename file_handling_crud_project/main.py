from pathlib import Path
import os

def read_file_and_folder():
    path = Path('')  #here empty space means path of current folder in which we are right now
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f" {i+1} : {item} ")
    
    
def createfile():
    try:
        read_file_and_folder()  
        name = input("please tell your file name:-- ")
        p = Path(name)
        
        if not p.exists and p.is_file():
            with open(p, 'w') as fs:
                data = input("what you want to write in this file:- ")
                fs.write(data)    
                
            print(F"FILE CREATED SUCCESSFULLY")
        else:
            print("this file already exists")
        
    except Exception as err:
        print(f"An error occured {err}")
    
 
def readfile():
    try:
        read_file_and_folder()
        file_name = input("please write the name of file which you want to read")    
        p = Path(file_name)
        if p.exists() and p.is_file():
            with open(p) as fs:
                data = fs.read()
                print(data)
     
            print("file read successfully ")
        else:
            print("This File does not exists")        
    
    except Exception as err:
        print(f"An error occur {err}")
    

def updatefile():
    try:
        read_file_and_folder()
        name = input("tell which file you want to update :-- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 to change the name of your file :--"
                "press 2 to overwriting data of your file :--"
                "press 3 to append some content in your file :--")
            
            res = int(input("press num keys to choose :--"))
            
            if res == 1:
                name2 = input("tell me your new name of file :--")
                p2 = Path(name2)
                p.rename(p2)
                
            if res == 2:
                with open(p, 'w') as fs:
                    data = input("tell what you want to write but it will overwrite : ")
                    fs.write(data)
                    
            if res == 3:
                with open(p, 'a') as fs:
                    data = input("tell what you want append : ")
                    fs.write(" "+data)      
    except Exception as err:
        print(f"error occured : {err}")
 
 
def deletefile():
    try:
        read_file_and_folder()
        name = input("which file you want to delete :- ")
        p = Path(name)
        
        if p.exists() and p.is_file():
            os.remove(p)
            
            print("file remove successfully ")
            
        else:
            print("no such file exists ")
    except Exception as err:
        print(f"an error occured : {err}")  
        
        
        
print("press 1 to create a file")
print("press 2 to Read a file")
print("press 3 to Updating a file")
print("press 4 to Delete a file")

check = int(input("please tell your response:-- "))

if check == 1 :
    createfile()
    
if check == 2 :
    readfile()
    
if check == 3 :
    updatefile()
    
if check == 4 :
    deletefile()