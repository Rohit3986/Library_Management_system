from pyexpat import model
from django.db import models
from datetime import datetime

class bookrecords(models.Model):
    book_id=models.AutoField(primary_key=True, serialize=True)
    book_title=models.CharField(max_length=30)
    book_type=models.CharField(max_length=30)
    author_name=models.CharField(max_length=30)
    recent_transaction_date=models.CharField(max_length=30)
    
    