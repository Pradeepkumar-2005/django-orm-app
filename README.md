# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![image](https://github.com/jabezs2005/django-orm-app/assets/147473463/4624c801-d2f9-4474-ae14-726068645b53)
## DESIGN STEPS:
### STEP 1:
Make new folder and give it a name and fork the folder from repository.

### STEP 2:
Now inside this folder create a folder called "django-orm-app" 

### STEP 3:
Now navigate to dataproject folder.

### STEP 4:
Now create a app called myapp

### STEP 5:
Now apply all migrations 

### STEP 6:
now write the necessary code for models.py and admin.py

### STEP 7:
Now create a superuser with global user.name and global user.email and mail.id as admin@example.com and a password.

#### STEP 8:
Now run the server and naviagte the admin page 

### STEP 9:
Now add 10 employees id.

## PROGRAM

Include your code here
### models.py
 write the following  code  in models.py
 ```
from django.db import models
from django.contrib import admin
# Create your models here.
class Student (models.Model):
    referencenumber=models.CharField(max_length=20,help_text="reference number")
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
class StudentAdmin(admin.ModelAdmin):
    list_display=('referencenumber','name','age','email')
class Employee (models.Model):
   emp_id=models.CharField(primary_key=True,max_length=4,help_text='Employee ID')
    ename=models.CharField(max_length=50)
    post=models.CharField(max_length=20)
    salary=models.IntegerField()
class EmployeeAdmin(admin.ModelAdmin):
    list_display=('emp_id','ename','post','salary')
```
write the following code in admin.py
```
from django.contrib import admin
from .models import Student,StudentAdmin,Employee,EmployeeAdmin
# Register your models here.
admin.site.register(Student,StudentAdmin)
admin.site.register(Employee,EmployeeAdmin)
```
### OUTPUT:
## Server Output:
![django server output](https://github.com/jabezs2005/django-orm-app/assets/147473463/f672e449-02bc-4834-97d2-7c0201621150)
### RESULT :
Django ORM web application have been created succesfully.
