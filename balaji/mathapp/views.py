from django.shortcuts import render

def power(request):
    context={}
    context['Power'] = "0"
    context['i'] = "0"
    context['r'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        I = request.POST.get('Intensity','0')
        R = request.POST.get('Resistence','0')
        print('request=',request)
        print('Intensity=',I)
        print('Resistence=',R)
        Power = int(I) * int(I) * int(R)
        context['Power'] = Power
        context['i'] = I
        context['r'] = R
        print('Power=',Power)
    return render(request,'mathapp/power.html',context)