from django.http import HttpResponse
from django.shortcuts import render
import datetime
from myapp.models import Fibonaccis 

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
		store = Fibonaccis(fib_result=result, exe_time=exe_time)
		store.save()
	return render(request, 'fibonacci.html', {"result":result, "num":num, "exe_time":exe_time})

#compute nth Fibonacci number in O(log(n))
def fibonacci(n):
    if n < 0:
        return "Incorrect input"
    if n == 0:
        return 0

    if n == 1:
        return 1

    def matmul(M1, M2):
        a11 = M1[0][0]*M2[0][0] + M1[0][1]*M2[1][0]
        a12 = M1[0][0]*M2[0][1] + M1[0][1]*M2[1][1]
        a21 = M1[1][0]*M2[0][0] + M1[1][1]*M2[1][0]
        a22 = M1[1][0]*M2[0][1] + M1[1][1]*M2[1][1]
        return [[a11, a12], [a21, a22]]

    def matPower(mat, p):
        if p == 1:
            return mat

        m2 = matPower(mat, p//2)
        if p % 2 == 0:
            return matmul(m2, m2)
        else:
            return matmul(matmul(m2, m2),mat)

    Q = [[1,1],[1,0]]

    q_final = matPower(Q, n-1)
    return q_final[0][0]

#bellow is the previous code
    # a = 0
    # b = 1
    # if n < 0:
    #     return "Incorrect input"
    # elif n == 0:
    #     return a
    # elif n == 1:
    #     return b
    # else:
    #     for i in range(2, n + 1):
    #         c = a + b
    #         a = b
    #         b = c
    #     return b