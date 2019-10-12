from django.db import models

# Create your models here.
class Fibonaccis(models.Model):
	fib_result = models.TextField(max_length = 65535)
	exe_time = models.CharField(max_length = 200)

	class Meta:
		db_table = "fib_table"