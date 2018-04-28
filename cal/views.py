# Create your views here.
from django.shortcuts import render
from .models import hotelcal
from django.db.models import Q
import random

def ind(request):
    queryset = hotelcal.objects.all()
    context={
        'q': queryset,
    }
    template_name="try.html"
    return render(request,template_name,context)



def quantitySingle(request, *args, **kwargs):
    mmonth = kwargs.get('mmonth')
    ddate = int(kwargs.get('ddate'))
    sord = kwargs.get('sord')
    quant = int(kwargs.get('quant'))

    queryset = hotelcal.objects.filter(
        Q(month__iexact=mmonth) &
        Q(date__iexact=ddate)
    )

    if queryset:
        a = queryset.first()
        if quant >=0 and quant <=5:
            if sord == "s":
                a.single = quant
                a.save()
            elif sord == "d":
                a.double = quant
                a.save()
            else:
                raise AttributeError("Use 's' for Single Rooms and 'd' for Double Rooms")
        else:
            raise AttributeError("Single Room can only be between Zero to Five")
    else:
        raise AttributeError("No such Date and Month is available in database")

    queryset = hotelcal.objects.all()
    context = {
        'q': queryset,
    }
    template_name = "try.html"
    return render(request, template_name, context)


def pricesingle(request,*args,**kwargs):
    mmonth = kwargs.get('mmonth')
    ddate = int(kwargs.get('ddate'))
    sord = kwargs.get('sord')
    price = int(kwargs.get('price'))

    queryset = hotelcal.objects.filter(
        Q(month__iexact=mmonth) &
        Q(date__iexact=ddate)
    )

    if queryset:
        a = queryset.first()
        if price >= 0:
            if sord == "s":
                a.single_price = price
                a.save()
            elif sord == "d":
                a.double_price = price
                a.save()
            else:
                raise AttributeError("Use 's' for Single Rooms and 'd' for Double Rooms")
        else:
            raise AttributeError("Price cannnot be Negative")
    else:
        raise AttributeError("No such Date and Month is available in database")

    queryset = hotelcal.objects.all()
    context = {
        'q': queryset,
    }
    template_name = "try.html"
    return render(request, template_name, context)


def bulk(request, *args, **kwargs):
    fromMonth = kwargs.get('fromMonth')
    toMonth = kwargs.get('toMonth')
    fromDate = int(kwargs.get('fromDate'))
    toDate = int(kwargs.get('toDate'))
    sord = kwargs.get('sord')
    price = int(kwargs.get('price'))
    quant = int(kwargs.get('quant'))
    condition = int(kwargs.get('condition'))
    listmonth=['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    prepredata = {
        'january': 1,
        'february': 2,
        'march': 3,
        'april': 4,
        'may': 5,
        'june': 6,
        'july': 7,
        'august': 8,
        'september': 9,
        'october': 10,
        'november': 11,
        'december': 12,
    }
    predata = {
        'january': 31,
        'february': 28,
        'march': 31,
        'april': 30,
        'may': 31,
        'june': 30,
        'july': 31,
        'august': 31,
        'september': 30,
        'october': 31,
        'november': 30,
        'december': 31,
    }
    conarray ={
        1: 'monday',
        2: 'tuesday',
        3: 'wednesday',
        4: 'thursday',
        5: 'friday',
        6: 'saturday',
        7: 'sunday',
        8: 'weakdays',
        9: 'weakends',
    }

    def justdo(x, j):
        queryset = hotelcal.objects.filter(
            Q(month__iexact=x) &
            Q(date__iexact=j)
        )
        a = queryset.first()
        if condition < 10 and condition > 0:
            if condition < 8 and a.day != conarray.get(condition):
                return
            elif condition == 9 and (a.day != 'sunday' and a.day != 'saturday'):
                return
            elif condition == 8 and (a.day == 'sunday' or a.day == 'saturday'):
                return

        if price >= 0:
            if sord == "s":
                a.single_price = price
                a.save()
            elif sord == "d":
                a.double_price = price
                a.save()
            else:
                raise AttributeError("Use 's' for Single Rooms and 'd' for Double Rooms")
        else:
            raise AttributeError("Price cannnot be Negative")

        if quant >= 0 and quant <= 5:
            if sord == "s":
                a.single = quant
                a.save()
            elif sord == "d":
                a.double = quant
                a.save()
            else:
                raise AttributeError("Use 's' for Single Rooms and 'd' for Double Rooms")
        else:
            raise AttributeError("Single Room can only be between Zero to Five")

    for i in range(prepredata.get(fromMonth), prepredata.get(toMonth)+1):
        if listmonth[i-1] == toMonth and toMonth != fromMonth:
            for j in range(1, toDate+1):
                justdo(toMonth, j)
        elif toMonth == fromMonth:
            for j in range(fromDate, toDate + 1):
                justdo(toMonth, j)
        elif listmonth[i-1] != toMonth and listmonth[i-1] != fromMonth:
            for j in range(1, predata.get(listmonth[i-1])+1):
                justdo(listmonth[i-1], j)
        elif listmonth[i-1]==fromMonth and listmonth != fromMonth:
            for j in range(fromDate, predata.get(listmonth[i-1])+1):
                justdo(listmonth[i-1], j)

    queryset = hotelcal.objects.all()
    context = {
        'q': queryset,
    }
    template_name = "try.html"
    return render(request, template_name, context)

# def stuffdata(request):
#     month = "september"
#     daystemp=['thursday', 'friday', 'saturday', 'sunday','monday', 'tuesday', 'wednesday']
#     j = 0
#     for i in range(1, 31):
#         date = i
#         single = random.randint(1, 5)
#         double = random.randint(1, 5)
#         single_price = random.randint(1500, 6500)
#         double_price = random.randint(2500, 8000)
#         day = daystemp[j]
#         j+=1
#         j=j%7
#         hotelcal.objects.create(month=month, date=date, single=single, double=double, single_price=single_price, double_price=double_price, day=day)