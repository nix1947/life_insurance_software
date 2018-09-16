'''
This model contains all the abstract models, that used in core application. 
Database schema aren't created from this schema
'''

from django.db import models

class Person(models.Model):
    '''
    Person abstract class having basic person attributes
    ''' 

    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    

    class Meta:
        abstract =  