from django.db import models

# Create your models here.
class Fibonaccis(models.Model):
	result = models.CharField(max_length = 1024)
	exe_time = models.CharField(max_length = 200)

	class Meta:
		db_table = "fibonaccis"