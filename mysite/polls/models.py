import datetime

from django.db import models
from django.utils import timezone #to reference python's standard datetime module



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self): #editing the question model, add string method to question (and choice below)
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text #this is impt as it is for our convenience when dealing with interactive prompt, but also
        # because objects' representations are used throughtout Django's automatically-generated admin


#from django.db import models

# Create your models here.

#class Question(models.Model):
#    question_text = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')

#    class Choice(models.Model):
#        question = models.ForeignKey(Question, on_delete=models.CASCADE)
#        choice_text = models.CharField(max_length=200)
#        votes = models.IntegerField(default=0)


# Models are represented by a class that subclasses django.db.models.Model
# each model has a number of class variables,
# each represents a database field in the model

# relationship is defined, using ForeginKey
# Tells Django each Choice is related to a single QUestion. 

# Activating models

# Django can create database schema (CREATE TABLE statements) for this app
# Create a Python database-access API for accessing Question and Choice objects
# tell our project that the polls app is installed. 



#Tutorial pt 2

# run the command: py manage.py makemigrations polls

# Telling Django that we have made some changes to the models
# Django will store the changes as a migration

#migrations are how Django stores changes to your model
#Files on disk
#can read the migration for the new model 
#in file polls/migration/0001_initial.py

#designed to be human-editable in case you want to tweak something

#command that will run the migrations and manage DATABASE SCHEMA automatically,
#thats called migrate

#now we see what SQL the migration would run

# sqlmigrate command takes migration names and return their SQL

#<insert output in command prompt>
# the exact output will vary depending ont he databse you are using
#Table names are automatically generaet dby combining the names of the app (poll)
#and the lowercase name of the model 
#Primary keys IDs are added automatically
# By convention, Django appends "_id" to the foreign key field name
# The foreign key relationship is made explicit by a Foreign Key constraint. 
# Deferrable: means telling PostgreSQL to not enforce the foreign key
