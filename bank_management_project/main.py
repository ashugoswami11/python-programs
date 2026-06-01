import json 
import random
import string
import re
from pathlib import Path


class Bank:
    database = "data.json" 
    data = []
    
    try:
        if Path(database).exists():
            with open(database) as fs: 
                data = json.loads(fs.read())   
        else:
            print("file doesn't exists")  
    except Exception as err:
        print(f"error occured : {err}")
      
    @classmethod  
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k =3)
        num = random.choices(string.digits, k = 3)
        spchar = random.choices("!@#$%^&*", k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        id = "".join(id)
        
        exists = [i for i in cls.data if i["Account_NO."] == id]
        if len(exists) == 0:
            return id
        else:
            print("duplicate account number created !!!")
    
        
    def create_account(self):
        
        # email verification
        while True:
            email = input("tell your email: ")
            pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

            
            if re.match(pattern, email):
                exits = [i for i in Bank.data if i['email'] == email]
                if len(exits)>0:
                    print("this email is already registerd !!!")
                else:
                    break
            else:
                print("invalid email format please try again ")
            
    
    
        info = {
            "name" : input("tell your name :"),
            "age" : int(input("tell your age :")),
            "email" : email,
            "pin"  : int(input("please enter a new pin only 4 digits :")),
            "Account_NO." : Bank.__accountgenerate(),
            "balance" : 0
        }
        
        
        if info['age']< 18 or len(str(info['pin'])) != 4 or type(info['pin']) != int:
                print("sorry you can't create account because of either under age or wrong pin type")
        else:
            print("your account has been created successfully ")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your account number")
            
            Bank.data.append(info)
            Bank.__update()
    
    
  
    def deposit_money(self):
        acnum = input("please tell your account number ")         
        pin = int(input("please tell you pin "))
        
        userdata = [i for i in Bank.data if i['Account_NO.'] == acnum and i['pin'] == pin]
        userdata = userdata[0]
        if len(userdata) == 0:
            print("sorry no data found")
            return
            
        else:
            amount = int(input("how much amount you want to deposit "))
            if amount <= 0:
                print("invalid amount")
            else:
                userdata['balance'] += amount
                print("\nAmount deposit successfully ")
                Bank.__update()
     
                
      
    def withdraw_money(self):
        acnum = input("please tell your account number ")         
        pin = int(input("please tell you pin "))
        
        userdata = [i for i in Bank.data if i['Account_NO.'] == acnum and i['pin'] == pin]
        userdata = userdata[0]
        if len(userdata) == 0:
            print("sorry no data found")
            return
            
        else:
            print(f"\nyour account balance is : {userdata['balance']}")
            amount = int(input("how much amount you want to withdraw : "))
            if amount <= 0 or amount > userdata['balance']:
                print("\ninvalid amount or you are trying to withdraw more than balance")
            else:
                userdata['balance'] -= amount
                print(f"\nyour remaining balance is : {userdata['balance']}")
                Bank.__update()                  
      
      
    def show_details(self):
        acnum = input("please tell your account number ")         
        pin = int(input("please tell you pin "))   
        print("\n")
        
        userdata = [i for i in Bank.data if i['Account_NO.'] == acnum and i['pin'] == pin]
        userdata = userdata[0]
    
        if len(userdata) == 0:
            print("sorry no data found")
            return
                
        else:
            print("your details are :---- \n")
            for i in userdata:
                print(f"your {i} :  {userdata[i]}")
    
    
    def update_details(self):
        acnum = input("please tell your account number ")         
        pin = int(input("please tell you pin "))   
        print("\n")
        
        userdata = [i for i in Bank.data if i['Account_NO.'] == acnum and i['pin'] == pin]
        userdata = userdata[0]
        
        if len(userdata) == 0:
            print("sorry no data found")
            return
        
        else:
            print("you cannot change the age, account number, balance")
            print("fill the details for change or press enter for no change")
    
            newdata = {
                "name" : input("please fill new name here : "),
                "email" : input("enter your new email here : "),
                "pin" : input("fill your new pin : ")   
            }
            
            if newdata["name"] == "":
                newdata["name"] = userdata['name']
            if newdata["email"] == "":
                newdata["email"] = userdata['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata['pin']
                    
            newdata['age']   =  userdata['age']   
            newdata['Account_NO.']  =  userdata['Account_NO.']     
            newdata['balance']  =  userdata['balance'] 
                    
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[i]:
                    continue
                else:
                    userdata[i] = newdata[i]
        
            Bank.__update()
            print("\ndetails updated successfully ")
      
      
    def user_delete(self):
        acnum = input("please tell your account number ")         
        pin = int(input("please tell you pin "))   
        print("\n")
        
        userdata = [i for i in Bank.data if i['Account_NO.'] == acnum and i['pin'] == pin]
        userdata = userdata[0]
        
        if len(userdata) == 0:
            print("sorry no data found")
            return
        else:
            check = input("press 'y' if you actually want to delete your acccount and 'n' if won't ")
            
            if check == 'n' or check == 'N':
                print("no account deleted")
            else:
                index = Bank.data.index(userdata)
                Bank.data.pop(index)
                print("your account deleted successfully ! ")
                Bank.__update()
            
            
            
user = Bank()
print("Press 1 to create an Account")
print("Press 2 to Deposit Money")
print("press 3 to Withdraw Money") 
print("press 4 to Check Details")
print("press 5 to Update Details")
print("press 6 to Delete or Closure of Account")

check = int(input("please give us your response between 1 to 6 : "))

if check  == 1:
    user.create_account()
    
elif check == 2:
    user.deposit_money()
    
elif check == 3:
    user.withdraw_money()
    
elif check == 4:
    user.show_details()
    
elif check == 5:
    user.update_details()
    
elif check == 6:
    user.user_delete()
    
else:
    print("invalid choice")