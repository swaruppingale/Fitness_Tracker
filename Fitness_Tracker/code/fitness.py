import mysql.connector
import hashlib

con=mysql.connector.connect(host="localhost",user="root",password="root",database="computerproject")

print("----------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                             FITACTIVE APP                                                                    ")
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print("                                                                                                                                              ")
print("                                                                                                                                              ")
print("-----------------------------------------------------------------LOGIN------------------------------------------------------------------------")
name=input("enter your name:\n")
age=float(input("enter your age:"))
def signup():
    email = input("Enter email address: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.txt", "w") as f:
             f.write(email + "\n")
             f.write(hash1)
        f.close()
        print("You have registered successfully!")
    else:
        print("Password is not same as above! \n")
def login():
    email = input("Enter email: ")
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and auth_hash == stored_pwd:
         print("Logged in Successfully!")
    else:
        print("Login failed! \n")
while 1:
                 
    print("1.Signup")
    print("2.Login")
    print("3.Proceed further wuth the app")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")
print("---------------------------------------------------------------------WELCOME----------------------------------------------------------------------")
print("Welcome to FITACTIVE app.\nWhat would you like to know?")
print("1.BMI \n2.Nutrition \n3.Fitness/Exercises")

choice=int(input("Enter your choice="))
if (choice==1):
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                                   BMI                                                                        ")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("Kindly enter the following details.")
    h=float(input("Enter your height:"))
    height=h/3.288
    weight=float(input("Enter your weight(in kg):"))

    BMI=float(weight/(height**2))
    print(name,"Your BMI is",round(BMI))

    if age in range(5,19):
        if BMI<12:
            print(name,"is severely malnourished. Please refer to proper diet.")
        elif BMI>12 and BMI<15:
            print(name,"is moderately malnourished. Please refer to proper diet.")
        elif BMI>15 and BMI<18:
             print(name,"is normal. Keep up the good work.")
        elif BMI>18 and BMI<20:
             print(name,"is overweight. Please refer to proper diet.")
        else:
            print(name,"is obese. Please refer to proper diet.")

    elif age>=19:
        if BMI<18.4:
            print(name,"is severely malnourished. Please refer to proper diet.")
        elif BMI in range(18.4,24.9):
            print(name,"is Normal. Please refer to proper diet.")
        elif BMI in range(25.0,39.9):
            print(name,"is Overweight. Little changes will help you to be normal. Refer to our diet plans.")
        elif BMI>=40:
            print(name,"is Obese. Please refer to a proper diet. ")
        else:
            print(name,"is obese. Please refer to a proper diet.")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                        THANKYOU FOR USING FITACTIVE                                                          ")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")

elif(choice==2):
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                               NUTRITION                                                                      ")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("Kindly enter the following details.")
    h=float(input("Enter your height(in feet):"))
    height=h/3.288
    weight=float(input("Enter your weight(in kg):"))
    choice=int(input("What would you like to know?\n1.protein\n2.vitamin\n3.calories"))
    BMI=weight/(height**2)
    print(name," your BMI is -",round(BMI))
    n1=2
    n2=3
    n3=4
    if choice==1:
      if BMI>1 and BMI<=15:
        cur=con.cursor()
        cur.execute("select * from nutrition where bmi1=1")
        data1=cur.fetchone()[n1]
        print("Suggested foods for protein intake- ",data1)
      elif BMI>=16 and BMI<=20:
        cur=con.cursor()
        cur.execute("select * from nutrition where bmi1=16")
        data1=cur.fetchone()[n1]
        print("Suggested foods for protein intake- ",data1)
      elif BMI>=21 and BMI<=30:
        cur=con.cursor()
        cur.execute("select * from nutrition where bmi1=21")
        data1=cur.fetchone()[n1]
        print("Suggested foods for protein intake- ",data1)
      elif BMI>=31 and BMI<=40:
        cur=con.cursor()
        cur.execute("select * from nutrition where bmi1=31")
        data1=cur.fetchone()[n1]
        print("Suggested foods for protein intake- ",data1)
    elif choice==2:
      if BMI>1 and BMI<=15:
        cur=con.cursor()
        cur.execute("select * from nutrition where bmi1=1")
        data1=cur.fetchone()[n2]
        print("Suggested vitamins- ",data1)
      elif BMI>=16 and BMI<=20:
        cur=con.cursor()
        cur.execute("select * from nutrition where bmi1=16")
        data1=cur.fetchone()[n2]
        print("Suggested vitamins- ",data1)
      elif BMI>=21 and BMI<=30:
        cur=con.cursor()
        cur.execute("select * from nutrition where bmi1=21")
        data1=cur.fetchone()[n2]
        print("Suggested vitamins- ",data1)
      elif BMI>=31 and BMI<=40:
        cur=con.cursor()
        cur.execute("select * from nutrition where bmi1=31")
        data1=cur.fetchone()[n2]
        print("Suggested vitamins- ",data1)
    elif choice==3:
      if BMI>1 and BMI<=15:
        cur=con.cursor()
        cur.execute("select * from nutrition where bmi1=1")
        data1=cur.fetchone()[n3]
        print("Suggested daily calorie intake- ",data1)
      elif BMI>=16 and BMI<=20:
        cur=con.cursor()
        cur.execute("select * from nutrition where bmi1=16")
        data1=cur.fetchone()[n3]
        print("Suggested daily calorie intake- ",data1)
      elif BMI>=21 and BMI<=30:
        cur=con.cursor()
        cur.execute("select * from nutrition where bmi1=21")
        data1=cur.fetchone()[n3]
        print("Suggested daily calorie intake- ",data1)
      elif BMI>=31 and BMI<=40:
        cur=con.cursor()
        cur.execute("select * from nutrition where bmi1=31")
        data1=cur.fetchone()[n3]
        print("Suggested daily calorie intake- ",data1)
    else:
        print("Wrong choice");
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("                                                         THANKYOU FOR USING FITACTIVE                                                         ")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")


elif(choice==3):
 print("----------------------------------------------------------------------------------------------------------------------------------------------")
 print("                                                               EXERCISE                                                                       ")
 print("----------------------------------------------------------------------------------------------------------------------------------------------")
 print("Kindly enter the following details.")
 day=int(input("Enter the number of day:"))
 number=int(input("Enter the number for the type of exercise you would like to do:\n 1:-warm up \n 2:-calisthenics \n 3:-cool down\n"))

 if age in range(11,20):
    if(day==1):
        cur=con.cursor()
        cur.execute("select * from teenagers")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==2):
        cur=con.cursor()
        cur.execute("select * from teenagers where days=2")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==3):
        cur=con.cursor()
        cur.execute("select * from teenagers where days=3")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==4):
        cur=con.cursor()
        cur.execute("select * from teenagers where days=4")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("exercises are:", data)
    elif(day==5):
        cur=con.cursor()
        cur.execute("select * from teenagers where days=5")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==6):
        cur=con.cursor()
        cur.execute("select * from teenagers where days=6")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==7):
        cur=con.cursor()
        cur.execute("select * from teenagers where days=7")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==8):
        cur=con.cursor()
        cur.execute("select * from teenagers where days=8")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==9):
        cur=con.cursor()
        cur.execute("select * from teenagers where days=9")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==10):
        cur=con.cursor()
        cur.execute("select * from teenagers where days=10")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==11):
        cur=con.cursor()
        cur.execute("select * from teenagers where days=11")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==12):
        cur=con.cursor()
        cur.execute("select * from teenagers where days=12")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==13):
        cur=con.cursor()
        cur.execute("select * from teenagers where days=13")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==14):
        cur=con.cursor()
        cur.execute("select * from teenagers where days=14")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    else:
     print("wrong choice")


 elif age in range(20,31):
    if(day==1):
        cur=con.cursor()
        cur.execute("select * from young_adults")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==2):
        cur=con.cursor()
        cur.execute("select * from young_adults where days=2")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==3):
        cur=con.cursor()
        cur.execute("select * from young_adults where days=3")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==4):
        cur=con.cursor()
        cur.execute("select * from young_adults where days=4")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==5):
        cur=con.cursor()
        cur.execute("select * from young_adults where days=5")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==6):
        cur=con.cursor()
        cur.execute("select * from young_adults where days=6")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==7):
        cur=con.cursor()
        cur.execute("select * from young_adults where days=7")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==8):
        cur=con.cursor()
        cur.execute("select * from young_adults where days=8")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==9):
        cur=con.cursor()
        cur.execute("select * from young_adults where days=9")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==10):
        cur=con.cursor()
        cur.execute("select * from young_adults where days=10")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==11):
        cur=con.cursor()
        cur.execute("select * from young_adults where days=11")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==12):
        cur=con.cursor()
        cur.execute("select * from young_adults where days=12")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==13):
        cur=con.cursor()
        cur.execute("select * from young_adults where days=13")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    elif(day==14):
        cur=con.cursor()
        cur.execute("select * from young_adults where days=14")
        data=cur.fetchone()[number]
        print("Let's start working out",name)
        print("Exercises are:", data)
    else:
     print("wrong choice")

 elif age in range(30,71):
    if(day==1):
        cur=con.cursor()
        cur.execute("select * from middleageadults")
        data=cur.fetchone()[number]
        print("You can do it!Let's go",name)
        print("Exercises are:", data)
    elif(day==2):
        cur=con.cursor()
        cur.execute("select * from from middleageadults where days=2")
        data=cur.fetchone()[number]
        print("You can do it!Let's go",name)
        print("Exercises are:", data)
    elif(day==3):
        cur=con.cursor()
        cur.execute("select * from middleageadults where days=3")
        data=cur.fetchone()[number]
        print("You can do it!Let's go",name)
        print("Exercises are:", data)
    elif(day==4):
        cur=con.cursor()
        cur.execute("select * from middleageadults where days=4")
        data=cur.fetchone()[number]
        print("You can do it!Let's go",name)
        print("Exercises are:", data)
    elif(day==5):
        cur=con.cursor()
        cur.execute("select * from middleageadults where days=5")
        data=cur.fetchone()[number]
        print("You can do it!Let's go",name)
        print("Exercises are:", data)
    elif(day==6):
        cur=con.cursor()
        cur.execute("select * from middleageadults where days=6")
        data=cur.fetchone()[number]
        print("You can do it!Let's go",name)
        print("Exercises are:", data)
    elif(day==7):
        cur=con.cursor()
        cur.execute("select * from middleageadults where days=7")
        data=cur.fetchone()[number]
        print("You can do it!Let's go",name)
        print("Exercises are:", data)
    elif(day==8):
        cur=con.cursor()
        cur.execute("select * from middleageadults where days=8")
        data=cur.fetchone()[number]
        print("You can do it!Let's go",name)
        print("Exercises are:", data)
    elif(day==9):
        cur=con.cursor()
        cur.execute("select * from middleageadults where days=9")
        data=cur.fetchone()[number]
        print("You can do it!Let's go",name)
        print("Exercises are:", data)
    elif(day==10):
        cur=con.cursor()
        cur.execute("select * from middleageadults where days=10")
        data=cur.fetchone()[number]
        print("You can do it!Let's go",name)
        print("Exercises are:", data)
    elif(day==11):
        cur=con.cursor()
        cur.execute("select * from middleageadults where days=11")
        data=cur.fetchone()[number]
        print("You can do it!Let's go",name)
        print("Exercises are:", data)
    elif(day==12):
        cur=con.cursor()
        cur.execute("select * from middleageadults where days=12")
        data=cur.fetchone()[number]
        print("You can do it!Let's go",name)
        print("Exercises are:", data)
    elif(day==13):
        cur=con.cursor()
        cur.execute("select * from middleageadults where days=13")
        data=cur.fetchone()[number]
        print("You can do it!Let's go",name)
        print("Exercises are:", data)
    elif(day==14):
        cur=con.cursor()
        cur.execute("select * from middleageadults where days=14")
        data=cur.fetchone()[number]
        print("You can do it!Let's go",name)
        print("Exercises are:", data)
    else:
     print("wrong choice")
 print("----------------------------------------------------------------------------------------------------------------------------------------------")
 print("                                                     THANKYOU FOR USING FITACTIVE                                                             ")
 print("----------------------------------------------------------------------------------------------------------------------------------------------")
else:
    print("Wrong choice, please try again")

