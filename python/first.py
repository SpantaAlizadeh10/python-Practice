# comment
'''comment'''
"""comment"""


  # variable : int - float -str -bool
x= 1402
score =19.5
name = "ali"
isDone = True
print(score,type(score)),
print(name,type(name)),
print(isDone,type(isDone)),


#int برای تغییر استرینگ به اینت

birtHDAY=input("enter your name:")
birtHDAY=int(birtHDAY),
print(type (birtHDAY)),


age =2023-int(birtHDAY)
print(age)

#operator + - * / %(باقی مانده)  //(قسمت صحیح تقسم) **(توان)
print(55*52),


#Arithmentic operator  تغییر دهنده
x=10,
x=x+20,
print(x),
x=25,
x+=6,

#operator precedence اولویت ها
# ** * / % + - =
x=10+3*8,
print(x),


#comparison operator
# >= > < <= == !=(مخالف)

n1 = 10
n2 =30
print(n1> n2),

#logicl operators
# and or not

age= 30,
#(هردو عبارت باید درست باشد)
print(age > 20 and age < 40),
#(یکی عبارت باید درست باشد)
print(age > 20 or age < 40),





  #string
first_name = "sarvin",
score=30,
print(f"hello {first_name} youe score {str(score)}")
print("hello"+first_name+"your score"+str(score)),

course="hello world"
print(course.upper())
print(course.lower())
print(course.capitalize())

print(len(course))

print(course.find("o"))

print(course.replace("hello","salam"))
course = (course.replace("hello","salam"))
print(course)

course="hello world"
print(course.startswith("he"))
print(course.endswith("am"))

print(course.split(","))


#حروف الفبا چون فضای خالی دارد در نتیجه فالص هست.

print(course.isalpha())
#فقط عدد
print(course.isnumeric())


#list

student_name=["sara","nima","shadi"]
student_name=list(("sara","nima","shadi"))
print(student_name,type(student_name))
print(student_name[0]),
print(student_name[-1]),

student_name[1]= "sama",
print(student_name),

print(student_name[1:3]), #شماره یک و دو را بر میگرداند

nums = [1,2,3,4.,5,]
nums.append(6) #اضافه کردن عدد به اخر ارایه
print(nums),

nums.insert(3,55) #یعنی من میخوام به ایندکس سه عدد55 اضافه بشود
nums.remove(1) #با این دستور میگوید محتوای که عدد یک دارد را حذف کن

nums.pop(0) #با این دستور میگوید محتوای که جایگاه یک دارد را حذف کن

nums.reverse() #ارایه را برعکس میکند
nums.sort() # از بزرگ تر به کوچک تر مرتب میکند

print(2 in nums) # جستجو میکند ایا عدد دو در نام وجود دارد یا خیر

print(len(nums)) # میگوید چند تا ایتم دارد

nums.clear() #تمام محتوای لیست حذف می شود


#Tuple لیستی که مقدارش غیر قابل تغیر است

course =("ali","zahra")
print(course,type(course)),
print(course[1]),
course[1]="sama"  #خطا میده چون نمیشه مقدارشو عوض کرد
del course  #   برای حذف توپل و دیگه متغیری به اسم course  را نمیشناسد
print(len(course)),



#set ترتیبی ندارد و ایتم تکراری قبول نمی کند

course={"ali","ahs","ddam"}
print(course,type(course)),
course.add("bita")
print(course),

course.remove("css"),
course.clear(),

#dictionary دیتای های که از بکند میاد ما در دیکشنری ذخیره میکنیم

student= {
    "firs_name": "ali",
     "last_name": "amani",
      "age": 20,
      "isDone": True,
}
student2 = dict(first_name = "jadi", last_name= "sadi")
print(student,type(student))
 #با هردوی اینها می شود به مقدار داخل دیکشنری دستری پیدا کرد
print(student["age"])
print(student.get("age")),
student["phone"]="224-98-789-12" # برای اضافه کردن
print(student)

print(student.keys()) # برای فهمیدن key های دیکشنری


print(student.items()) # کلا همه را داخل یک پرانز می اورد

person = student.copy(), #برای کپی کردن دیتا های یک چیر یه یک چیز دیگر
person["city"]= "tehran" #اضافه کردن ویژگی
del(person["city"]) #برای حذف کردن ویژگی
person.pop("age") # حذف ویژگی

print(len(student)), # چند ایتم دارد
student.clear() # empty
  

people = [
    {"name":"sarvin","class":"html"},
      {"name":"ali","reza":"css"},
]
print(people[0]["name"]),


#function  فقط زمانی که فراخوانی شده باشد اجرا مشود

def sayHello(name):
    print("hello")
    x=name
    print("hello" + x)


#محمدوه فانکش تمام شد
sayHello("ali")    

def sayHello(name="ali"):
    print("hello")
    x=name
    print("hello" + x)


#محمدوه فانکش تمام شد
sayHello()  

def getSum(x,y):
    total =x+y
    return total,
result=getSum(10,5),
print(result),
 
#lambda function تعریف فانکش های یک سطری
#این دو خط یکی هستن
getSum = lambda p1,p2:p1+p2
def getSum (p1,p2):
    return p1+p2,

print(getSum(1,5)),


#condition

x=35
y=50

# ==, !=(نامساوی), > ,>= ,< ,<=

if x>y:
    print("x is greater than y")

elif x==30:
    print(f"{x} is equal to 30")
elif x==y:
    print(f"{x} is equal to y")
else:
    print(f"x is greater than y")    
print("done")

#nested if if های تو در تو
x=40
y=30

if x>y:
    if x==40:
        print("x > y and x =30")

#logical operator عملگر های منطقی

# and , or , not

if x > 30 and y == 30 :
    print("x > 30 and y =30")   

if x > 30 or y == 30 :
    print("x > 30 or y =30")  

if not (x > 30):
    print("x is not greater than 30"),   

#membership (in, not in) برای اینکه چیزی داخلش هست یا نیست   

num=[1,2,3,4,5,]
x=4
#in
if x in num:
    print("x is in num")       

if x not in num:
    print("x is not in num")  


    #identity operator (is,not is)  برای اینکه چیزی برابر هست یانه

x=3
y=3
if x is y:
    print("x is y")
if x is not y :
    print("x is not y")   


#loop

student = ["sara","dara","jan"]
#break    
for items in student:
    if items == "dara":
        break
    print(f"current student : {items}") # این دستور به تعدا ارایه تکرا مبی شود

    #continue
for items in student:
    if items == "dara": # دارا را چاپ نمیکند 
        continue
    print(f"current student : {items}") # این دستور به تعدا ارایه تکرا مبی شود    

#range
    
for i in range(10):
    print(i) #از صفر تا نه شروع میکند

for i in range(len(student)):
    print(student[i]) #
  

#while
    
count = 0 
while count < 10 :
    print(f"count is {count}")
    count+=2,    


#module
#core modules

import datetime

today = datetime.datetime.today()
print(today),


from datetime import datetime

today = datetime.today()
print(today),

#external module  در تریمنال چاپ میشه

# from CamelCase()
# print(c.hump("ali style camel case")) # تمام کاراکتر ای اول را با حرف بزرگ می نویسید

#custom module 

import validate

from validate import validate_email
email = "sdfsdf@gmail.com"

print(validate_email)

# create class

class User:
    def __init__(self, name, email,birtHDAY):
        self.email=email
        self.birtHDAY=birtHDAY
        self.name=name

    def greetin(self):
        return f"your name is {self.name}"   

    def get_age(self):
        return f"y2022- self.birthDay"     


newUser = User("sarvin","addf#gamil.com", 1998)
print(type(newUser)),  
print(newUser.greetin())
print(newUser.get_age())   


class students (User):
    def __init__(self, name, email,birtHDAY):
        self.email=email
        self.birtHDAY=birtHDAY
        self.name=name
        self.score = 0

    def set_score(self,score):
        self.score=score

    def set_score(self):
        return self.score    


sara = students("sara","jsdhsg@gmail.com",1998)  
sara.set_score(10)    





#file
newfile= open("new.txt","w") # crate new file in file فرمت w نوشته های قبلی را پاک و نوشته جدید جایگزین میکند

print(f"name : {newfile.name}is closed : {newfile.closed},mode : {newfile.mode}")
newfile.write("first msg")
newfile.write("second msg")
newfile.close()

newfile= open("new.txt","a") # نوشته های قبلی را به نوشته های جدید اضافه میکند a 

print(f"name : {newfile.name}is closed : {newfile.closed},mode : {newfile.mode}")
newfile.write("first msg")
newfile.write("second msg")
newfile.close()



newfile= open("new.txt","r") #  کاراکتر برای خواندن 


text = newfile.read(5)
print(text),

#json

import json
samplejson = '{"name":"ali","last_name":"asadi"}'
User = json.loads(samplejson)

print(User)
print(sum["name"])



user2 = {'name':'sara',"last_name":"amami"}
user2tojson = json.dumps(user2)

print(user2tojson)






