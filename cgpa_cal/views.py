from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def Calculate(request):
    var1=int(request.GET['num1'])
    var2=int(request.GET['num2'])
    var3=int(request.GET['num3'])
    var4=int(request.GET['num4'])
    var5=int(request.GET['num5'])
    var6=int(request.GET['num6'])
    var7=int(request.GET['num7'])
    var8=int(request.GET['num8']) 
       
    total=(var1*4 +var2*3+var3*3+var4*3+var5*3+var6*3+(var7*3)/2+(var8*3)/2)/22

    return render(request,'result.html',{"result":total})

         

