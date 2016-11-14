# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def quadratic_results(request):
    mes_a=''
    mes_b=''
    mes_c=''
    a_int=False
    b_int=False
    c_int=False
    a=request.GET.get('a')
    b=request.GET.get('b')
    c=request.GET.get('c')
    if ((a.isdigit()==True) or ((len(a)>1) and (a[0]=='-') and (a[1:].isdigit())==True)):
        a_int=True
    if ((b.isdigit()==True) or ((len(b)>1) and (b[0]=='-') and (b[1:].isdigit())==True)):
        b_int=True
    if ((c.isdigit()==True) or ((len(c)>1) and (c[0]=='-') and (c[1:].isdigit())==True)):
        c_int=True

    if (a == '0') or (a =='') or (a_int==False) or (b=="") or (b_int==False) or (c=="") or (c_int==False):
        ch=1
        if (a!='') and (a_int==False):
            mes_a="коэффициент не целое число"
        if (b!='') and (b_int==False):
            mes_b="коэффициент не целое число"
        if (c!='') and (c_int==False):
            mes_c="коэффициент не целое число"
             

        return render(request, "quadratic/results.html", {"a": a, "b": b, "c": c, "mes_a": mes_a,"mes_b": mes_b,"mes_c": mes_c, "ch":ch})
    else:
        ch=0
        d=int(b)**2 - 4*int(a)*int(c)
        if d<0:
            return render(request, "quadratic/results.html", {"a": a, "b": b, "c": c, "discr": d,"ch":ch})
        else:
            x1=(-int(b)+d**(1/2))/2*int(a)
            x2=(-int(b)-d**(1/2))/2*int(a)
        return render(request, "quadratic/results.html", {"a": a, "b": b, "c": c, "discr": d,"x1": x1, "x2": x2, "ch":ch})

