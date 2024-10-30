from django.db import models

# Create your models here.
class login_table(models.Model):
    username=models.CharField(max_length=80)
    password=models.CharField(max_length=80)
    type=models.CharField(max_length=80)



class user_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=80)
    lastname=models.CharField(max_length=80)
    gender=models.CharField(max_length=80)
    age=models.IntegerField()
    place=models.CharField(max_length=80)
    post=models.CharField(max_length=80)
    pin=models.IntegerField()
    email=models.CharField(max_length=80)
    phone=models.BigIntegerField()



class feedback_table(models.Model):
    USER=models.ForeignKey(user_table,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=80)
    rating=models.CharField(max_length=80)
    date=models.DateField()


class complaint_table(models.Model):
    USER = models.ForeignKey(user_table, on_delete=models.CASCADE)
    complaints=models.CharField(max_length=80)
    reply = models.CharField(max_length=10)
    date=models.DateField()

