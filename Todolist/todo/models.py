from ast import Delete
from django.db import models
from django.contrib.auth.models import User #this helps us to manage everything of the user
# Create your models here.

class task(models.Model):
    user =models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title=models.CharField(max_length=200 , null=True)#title
   
    complete =models.BooleanField(default=False) #this is a checkbox it is set to false because initially task should not complete 
    created =models.DateTimeField(auto_now_add=True) #the parameter passes automatically adds the time to task
    
    def __str__(self):
        return self.title #returns only the name of the title when an object is created
    
    
        
