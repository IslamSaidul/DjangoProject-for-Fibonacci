from django.http import HttpResponse
from django.shortcuts import render
import datetime

def index(request):
	return render(request, 'index.html')

def show(request):
	result=''
	exe_time=''
	num=''
	if request.method == "POST":
		start_time = datetime.datetime.now()
		number = request.POST['number']
		num = int(number)
		result = fibonacci(num)
		exe_time=datetime.datetime.now()-start_time
	return render(request, 'fibonacci.html', {"result":result, "num":num, "exe_time":exe_time})


def fibonacci(n):
		    a = 0
		    b = 1
		    if n < 0:
		        return "Incorrect input"
		    elif n == 0:
		        return a
		    elif n == 1:
		        return b
		    else:
		        for i in range(2, n + 1):
		            c = a + b
		            a = b
		            b = c
		        return b