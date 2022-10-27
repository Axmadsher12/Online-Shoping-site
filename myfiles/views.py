from django.shortcuts import render,redirect
from django.http import HttpResponse,request
from django.forms import inlineformset_factory
from myfiles.models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,User
from .forms import UserCreateFormShop
from django.db.models import Q
from django.forms import *

# Create your views here.
def about(b):
    if b.method == "POST":
        Mail = b.POST.get('Mail')
        Time = b.POST.get('Time')
        email(Mail=Mail, Time=Time).save()
    chegirma = Discounts_mobile.objects.all()
    Meet = MeetOurTeam.objects.all()
    return render(b, 'about.html',{'ch':chegirma,'Meet':Meet})


def codes(c):
    if c.method == "POST":
        Mail = c.POST.get('Mail')
        Time = c.POST.get('Time')
        email(Mail=Mail, Time=Time).save()
    chegirma = Discounts_mobile.objects.all()
    return render(c, 'codes.html',{'ch':chegirma})


def faq(f):
    if f.method == "POST":
        Mail = f.POST.get('Mail')
        Time = f.POST.get('Time')
        email(Mail=Mail, Time=Time).save()
    chegirma = Discounts_mobile.objects.all()
    return render(f, 'faq.html',{'ch':chegirma})


def icons(i):
    if i.method == "POST":
        Mail = i.POST.get('Mail')
        Time = i.POST.get('Time')
        email(Mail=Mail, Time=Time).save()
    chegirma = Discounts_mobile.objects.all()
    return render(i, 'icons.html', {'ch':chegirma})

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import random as rd

@login_required(login_url='index')
def index(h):
    form = UserCreateFormShop()
    if 'Mail' in h.POST:
        Mail = h.POST.get('Mail')
        Time = h.POST.get('Time')
        email(Mail=Mail, Time=Time).save()

    elif 'sign in' in h.POST:
        username = h.POST.get('username')
        password = h.POST.get('password')
        user1 = authenticate(h,username=username,password=password)
        if user1 is not None:
            login(h,user1)
            return redirect('index')
        else:
            messages.info(h,'Username OR Password is incorrect')

    elif h.method == 'POST':
        form = UserCreateFormShop(h.POST)
        print('post')
        if form.is_valid():
            print('is_valid')
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(h, 'Account was created for' + user)
            return redirect('index')



    'Type All Get'
    brend = TopBrent.objects.all()

    ty_m1 = type_mobile.objects.get(Name='Mobile Phone')
    m1 = mobile.objects.filter(Type=ty_m1).order_by('?')[0:3]

    ta_a = type_appliance.objects.get(Name='Mp3 Player')
    app_audio = appliance.objects.filter(Type=ta_a).order_by('?')[0:3]

    ta_l = type_computer.objects.get(Name='Laptop')
    com = computer.objects.filter(Type=ta_l).order_by('?')[0:3]

    app_hou = type_appliance.objects.get(Name='Appliances Household')
    app_Household = appliance.objects.filter(Type=app_hou).order_by('?')[0:3]

    app_kit = type_appliance.objects.get(Name='Appliances Kitchen')
    app_Kitchen = appliance.objects.filter(Type=app_kit).order_by('?')[0:3]

    "<-- New_products -->"
    "<-- 1 Mobiles -->"
    tm_t = type_mobile.objects.get(Name='Tablet')
    New_t = mobile.objects.filter(Type=tm_t.id)
    if New_t:
        New_t = mobile.objects.filter(Type=tm_t.id).order_by('-Time')[0]
    else:
        New_t = 'T'
    tm_s = type_mobile.objects.get(Name='Smart Watch')
    New_s = mobile.objects.filter(Type=tm_s.id)
    if New_s:
        New_s = mobile.objects.filter(Type=tm_s.id).order_by('-Time')[0]
        print("New_s = mobile.objects.filter(Type=tm_s.id).order_by('-Time')[0]")
    else:
        New_s = 'W'
    tm_m = type_mobile.objects.get(Name='Mobile Phone')
    New_m = mobile.objects.filter(Type=tm_m.id)
    if New_m:
        New_m = mobile.objects.filter(Type=tm_m.id).order_by('-Time')[0]
        print("New_m = mobile.objects.filter(Type=tm_m.id).order_by('-Time')[0]")
    else:
        New_m = 'M'
    "<-- 2 Compyuter -->"
    tm_c = type_computer.objects.get(Name='Laptop')
    New_l = computer.objects.filter(Type=tm_c.id)
    if New_l:
        New_l = computer.objects.filter(Type=tm_c.id).order_by('-Time')[0]
        print("New_l = computer.objects.all().order_by('-Time')[0]")
    else:
        New_l ='L'
    "<-- 3 Appliances -->"
    ta_h = type_appliance.objects.get(Name='Appliances Household')
    New_h = appliance.objects.filter(Type=ta_h.id)
    if New_h:
        New_h = appliance.objects.filter(Type=ta_h.id).order_by('-Time')[0]
        print("New_h = appliance.objects.filter(Type=ta_h.id).order_by('-Time')[0]")
    else:
        New_h = 'H'
    ta_k = type_appliance.objects.get(Name='Appliances Kitchen')
    New_k = appliance.objects.filter(Type=ta_k.id)
    if New_k:
        New_k = appliance.objects.filter(Type=ta_k.id).order_by('-Time')[0]
        print("New_k = appliance.objects.filter(Type=ta_k.id).order_by('-Time')[0]")
    else:
        New_k = 'K'
    ta_c = type_appliance.objects.get(Name='Camera')
    New_c = appliance.objects.filter(Type=ta_c.id)
    if New_c:
        New_c = appliance.objects.filter(Type=ta_c.id).order_by('-Time')[0]
        print("New_c = appliance.objects.filter(Type=ta_c.id).order_by('-Time')[0]")
    else:
        New_c = 'C'
    ta_m = type_appliance.objects.get(Name='Mp3 Player')
    New_p = appliance.objects.filter(Type=ta_m.id)
    if New_p:
        New_p = appliance.objects.filter(Type=ta_m.id).order_by('-Time')[0]
        print("New_p = appliance.objects.filter(Type=ta_m.id).order_by('-Time')[0]")
    else:
        New_p = 'P'
    chegirma = Discounts_mobile.objects.all()
    comment1 = comment.objects.all()
    return render(h, 'indexs.html', {'tb': brend,'ms1':m1,'app1':app_audio,'com':com,'apph':app_Household,'appk':app_Kitchen,
                                    't':New_t,'m':New_m,'w':New_s,
                                    'l':New_l,
                                    'h':New_h,'k':New_k,'c':New_c,'p':New_p,
                                    'ch':chegirma,'comment':comment1,'form1':form})


def mail(m):
    if 'Your_Name' in m.POST:
        Your_name = m.POST.get('Your_Name')
        Your_email = m.POST.get('Your_Email')
        Telephone_no = m.POST.get('Telephone_No')
        Send_message = m.POST.get('Message')
        Time = m.POST.get('Time')
        Contact(Your_name=Your_name,Your_email=Your_email,Telephone_no=Telephone_no,Send_message=Send_message,Time=Time).save()

    elif m.method == "POST":
        Mail = m.POST.get('Mail')
        Time = m.POST.get('Time')
        email(Mail=Mail, Time=Time).save()
    chegirma = Discounts_mobile.objects.all()
    con = Contact.objects.all()
    return render(m, 'mail.html',{'ch':chegirma,'con':con})

#  pro ---------- ---------- ----------
def pro_all(p,allf,allf2):
    if p.method == "POST":
        Mail = p.POST.get('Mail')
        Time = p.POST.get('Time')
        email(Mail=Mail, Time=Time).save()
        'Filter----------------------------------------------|'
    elif allf != '':
        chegirma = Discounts_mobile.objects.all().order_by('-id')[0:1]
        if allf2 == 'New':
            maxsulot = mobile.objects.all().order_by('-Time')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html', {'Max': maxsulot,'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,'allt':allf})
        elif allf2 == 'Rating':
            maxsulot = mobile.objects.all().order_by('-Rating')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html', {'Max': maxsulot,'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,'allt':allf})
        elif allf2 == 'low to high':
            maxsulot = mobile.objects.all().order_by('New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html', {'Max': maxsulot,'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,'allt':allf})
        elif allf2 == 'high to low':
            maxsulot = mobile.objects.all().order_by('-New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html', {'Max': maxsulot,'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,'allt':allf})
        elif allf2 == 'select_item_all':
            if 'select_item_all' in p.POST:
                sort = p.POST.get('select_item_all')
                if sort == "Default":
                    maxsulot = mobile.objects.all().order_by('Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Default'
                    return render(p, 'products.html', {'Max': maxsulot,'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,'select': selects,'allt':allf})
                elif sort == "Rating":
                    maxsulot = mobile.objects.all().order_by('-Rating')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Rating'
                    return render(p, 'products.html', {'Max': maxsulot,'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,'select': selects,'allt':allf})
                elif sort == "Newness":
                    maxsulot = mobile.objects.all().order_by('-Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Newness'
                    return render(p, 'products.html', {'Max': maxsulot,'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,'select': selects,'allt':allf})
                elif sort == "low to high":
                    maxsulot = mobile.objects.all().order_by('New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'low to high'
                    return render(p, 'products.html', {'Max': maxsulot,'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,'select': selects,'allt':allf})
                elif sort == "-high to low":
                    maxsulot = mobile.objects.all().order_by('-New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = '-high to low'
                    return render(p, 'products.html', {'Max': maxsulot,'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,'select': selects,'allt':allf})
                else:
                    maxsulot = mobile.objects.all().order_by('?')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'allt': allf})
        else:
            maxsulot = mobile.objects.all().order_by('?')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html', {'Max': maxsulot,'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,'allt':allf})

    elif allf == 'Mobile Phone':
        chegirma = Discounts_mobile.objects.all().order_by('-id')[0:1]
        ty_m = type_mobile.objects.get(Name=allf)
        if allf2 == 'New':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Time')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'Rating':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Rating')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'low to high':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'high to low':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'select_item_mob':
            if 'select_item_mob' in p.POST:
                sort = p.POST.get('select_item_mob')
                if sort == "Default":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Default'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Rating":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Rating')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Rating'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Newness":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Newness'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "low to high":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'low to high'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "-high to low":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = '-high to low'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                else:
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('?')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'allt': allf})
        else:
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('?')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                           'ch': chegirma, 'allt': allf})

    elif allf == 'Tablet':
        chegirma = Discounts_mobile.objects.all().order_by('-id')[0:1]
        ty_m = type_mobile.objects.get(Name=allf)
        if allf2 == 'New':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Time')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'Rating':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Rating')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'low to high':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'high to low':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'select_item_tab':
            if 'select_item_tab' in p.POST:
                sort = p.POST.get('select_item_tab')
                if sort == "Default":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Default'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Rating":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Rating')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Rating'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Newness":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Newness'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "low to high":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'low to high'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "-high to low":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = '-high to low'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                else:
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('?')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'allt': allf})
        else:
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('?')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                           'ch': chegirma, 'allt': allf})

    elif allf == 'Smart Watch':
        chegirma = Discounts_mobile.objects.all().order_by('-id')[0:1]
        ty_m = type_mobile.objects.get(Name=allf)
        if allf2 == 'New':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Time')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'Rating':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Rating')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'low to high':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'high to low':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'select_item_sma':
            if 'select_item_sma' in p.POST:
                sort = p.POST.get('select_item_sma')
                if sort == "Default":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Default'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Rating":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Rating')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Rating'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Newness":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Newness'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "low to high":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'low to high'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "-high to low":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = '-high to low'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                else:
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('?')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'allt': allf})
        else:
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('?')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                           'ch': chegirma, 'allt': allf})
# end pro ---------- ---------- ----------

#  pro ---------- ---------- ----------
def pro1_all(p, allf, allf2):
    if p.method == "POST":
        Mail = p.POST.get('Mail')
        Time = p.POST.get('Time')
        email(Mail=Mail, Time=Time).save()
        'Filter----------------------------------------------|'

    elif allf != '':
        chegirma = Discounts_mobile.objects.all().order_by('-id')[0:1]
        if allf2 == 'New':
            maxsulot = computer.objects.all().order_by('-Time')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'Rating':
            maxsulot = computer.objects.all().order_by('-Rating')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'low to high':
            maxsulot = computer.objects.all().order_by('New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'high to low':
            maxsulot = computer.objects.all().order_by('-New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'select_item_all':
            if 'select_item_all' in p.POST:
                sort = p.POST.get('select_item_all')
                if sort == "Default":
                    maxsulot = computer.objects.all().order_by('Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Default'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Rating":
                    maxsulot = computer.objects.all().order_by('-Rating')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Rating'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Newness":
                    maxsulot = computer.objects.all().order_by('-Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Newness'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "low to high":
                    maxsulot = computer.objects.all().order_by('New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'low to high'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "-high to low":
                    maxsulot = computer.objects.all().order_by('-New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = '-high to low'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                else:
                    maxsulot = computer.objects.all().order_by('?')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                                   'allt': allf})
        else:
            maxsulot = computer.objects.all().order_by('?')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})

    elif allf == 'Laptop':
        chegirma = Discounts_mobile.objects.all().order_by('-id')[0:1]
        ty_m = type_mobile.objects.get(Name=allf)
        if allf2 == 'New':
            maxsulot = computer.objects.filter(Type=ty_m).order_by('-Time')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'Rating':
            maxsulot = computer.objects.filter(Type=ty_m).order_by('-Rating')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'low to high':
            maxsulot = computer.objects.filter(Type=ty_m).order_by('New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'high to low':
            maxsulot = computer.objects.filter(Type=ty_m).order_by('-New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'select_item_lap':
            if 'select_item_lap' in p.POST:
                sort = p.POST.get('select_item_lap')
                if sort == "Default":
                    maxsulot = computer.objects.filter(Type=ty_m).order_by('Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Default'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Rating":
                    maxsulot = computer.objects.filter(Type=ty_m).order_by('-Rating')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Rating'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Newness":
                    maxsulot = computer.objects.filter(Type=ty_m).order_by('-Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Newness'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "low to high":
                    maxsulot = computer.objects.filter(Type=ty_m).order_by('New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'low to high'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "-high to low":
                    maxsulot = computer.objects.filter(Type=ty_m).order_by('-New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = '-high to low'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                else:
                    maxsulot = computer.objects.filter(Type=ty_m).order_by('?')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'allt': allf})
        else:
            maxsulot = computer.objects.filter(Type=ty_m).order_by('?')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                           'ch': chegirma, 'allt': allf})

    elif allf == 'Personal Computer':
        chegirma = Discounts_mobile.objects.all().order_by('-id')[0:1]
        ty_m = type_mobile.objects.get(Name=allf)
        if allf2 == 'New':
            maxsulot = computer.objects.filter(Type=ty_m).order_by('-Time')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'Rating':
            maxsulot = computer.objects.filter(Type=ty_m).order_by('-Rating')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'low to high':
            maxsulot = computer.objects.filter(Type=ty_m).order_by('New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'high to low':
            maxsulot = computer.objects.filter(Type=ty_m).order_by('-New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'select_item_per':
            if 'select_item_per' in p.POST:
                sort = p.POST.get('select_item_per')
                if sort == "Default":
                    maxsulot = computer.objects.filter(Type=ty_m).order_by('Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Default'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Rating":
                    maxsulot = computer.objects.filter(Type=ty_m).order_by('-Rating')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Rating'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Newness":
                    maxsulot = computer.objects.filter(Type=ty_m).order_by('-Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Newness'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "low to high":
                    maxsulot = computer.objects.filter(Type=ty_m).order_by('New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'low to high'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "-high to low":
                    maxsulot = computer.objects.filter(Type=ty_m).order_by('-New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = '-high to low'
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                else:
                    maxsulot = computer.objects.filter(Type=ty_m).order_by('?')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    return render(p, 'products1.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'allt': allf})
        else:
            maxsulot = computer.objects.filter(Type=ty_m).order_by('?')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products1.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                           'ch': chegirma, 'allt': allf})
# end pro1 ---------- ---------- ----------

#  pro2 ---------- ---------- ----------
def pro2_all(p, allf, allf2):
    if p.method == "POST":
        Mail = p.POST.get('Mail')
        Time = p.POST.get('Time')
        email(Mail=Mail, Time=Time).save()
        'Filter----------------------------------------------|'

    elif allf != '':
        chegirma = Discounts_mobile.objects.all().order_by('-id')[0:1]
        if allf2 == 'New':
            maxsulot = mobile.objects.all().order_by('-Time')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'Rating':
            maxsulot = mobile.objects.all().order_by('-Rating')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'low to high':
            maxsulot = mobile.objects.all().order_by('New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'high to low':
            maxsulot = mobile.objects.all().order_by('-New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'select_item_all':
            if 'select_item' in p.POST:
                sort = p.POST.get('select_item')
                if sort == "Default":
                    maxsulot = mobile.objects.all().order_by('Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Default'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Rating":
                    maxsulot = mobile.objects.all().order_by('-Rating')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Rating'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Newness":
                    maxsulot = mobile.objects.all().order_by('-Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Newness'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "low to high":
                    maxsulot = mobile.objects.all().order_by('New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'low to high'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "-high to low":
                    maxsulot = mobile.objects.all().order_by('-New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = '-high to low'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                else:
                    maxsulot = mobile.objects.all().order_by('?')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                                   'allt': allf})
        else:
            maxsulot = mobile.objects.all().order_by('?')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})

    elif allf == 'Camera':
        chegirma = Discounts_mobile.objects.all().order_by('-id')[0:1]
        ty_m = type_mobile.objects.get(Name=allf)
        if allf2 == 'New':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Time')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'Rating':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Rating')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'low to high':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'high to low':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'select_item_mob':
            if 'select_item_mob' in p.POST:
                sort = p.POST.get('select_item')
                if sort == "Default":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Default'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Rating":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Rating')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Rating'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Newness":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Newness'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "low to high":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'low to high'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "-high to low":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = '-high to low'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                else:
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('?')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'allt': allf})
        else:
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('?')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                           'ch': chegirma, 'allt': allf})

    elif allf == 'Mp3 Player':
        chegirma = Discounts_mobile.objects.all().order_by('-id')[0:1]
        ty_m = type_mobile.objects.get(Name=allf)
        if allf2 == 'New':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Time')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'Rating':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Rating')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'low to high':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'high to low':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'select_item_tab':
            if 'select_item_tab' in p.POST:
                sort = p.POST.get('select_item')
                if sort == "Default":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Default'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Rating":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Rating')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Rating'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Newness":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Newness'
                    return render(p, 'products.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "low to high":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'low to high'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "-high to low":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = '-high to low'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                else:
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('?')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'allt': allf})
        else:
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('?')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                           'ch': chegirma, 'allt': allf})

    elif allf == 'Appliance Kitchen':
        chegirma = Discounts_mobile.objects.all().order_by('-id')[0:1]
        ty_m = type_mobile.objects.get(Name=allf)
        if allf2 == 'New':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Time')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'Rating':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Rating')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'low to high':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'high to low':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'select_item_sma':
            if 'select_item_sma' in p.POST:
                sort = p.POST.get('select_item')
                if sort == "Default":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Default'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Rating":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Rating')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Rating'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Newness":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Newness'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "low to high":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'low to high'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "-high to low":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = '-high to low'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                else:
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('?')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    return render(p, 'products22.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'allt': allf})
        else:
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('?')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products22.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                           'ch': chegirma, 'allt': allf})

    elif allf == 'Appliance Household':
        chegirma = Discounts_mobile.objects.all().order_by('-id')[0:1]
        ty_m = type_mobile.objects.get(Name=allf)
        if allf2 == 'New':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Time')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'Rating':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Rating')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'low to high':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'high to low':
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('-New_price')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products2.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,
                           'allt': allf})
        elif allf2 == 'select_item_sma':
            if 'select_item_sma' in p.POST:
                sort = p.POST.get('select_item')
                if sort == "Default":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Default'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Rating":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Rating')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Rating'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "Newness":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-Time')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'Newness'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "low to high":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = 'low to high'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                elif sort == "-high to low":
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('-New_price')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    selects = '-high to low'
                    return render(p, 'products2.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'select': selects, 'allt': allf})
                else:
                    maxsulot = mobile.objects.filter(Type=ty_m).order_by('?')
                    maxsulot1 = mobile.objects.all().order_by('?')
                    maxsulot2 = appliance.objects.all().order_by('?')
                    maxsulot3 = computer.objects.all().order_by('?')
                    return render(p, 'products22.html',
                                  {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                                   'ch': chegirma, 'allt': allf})
        else:
            maxsulot = mobile.objects.filter(Type=ty_m).order_by('?')
            maxsulot1 = mobile.objects.all().order_by('?')
            maxsulot2 = appliance.objects.all().order_by('?')
            maxsulot3 = computer.objects.all().order_by('?')
            return render(p, 'products22.html',
                          {'Max': maxsulot, 'Max1': maxsulot1, 'Max2': maxsulot2, 'Max3': maxsulot3,
                           'ch': chegirma, 'allt': allf})
# end pro ---------- ---------- ----------

def single1(s):
    if 'Review' in s.POST:
        Name = s.POST.get('Name')
        Mail = s.POST.get('Mail2')
        Telephone_no = s.POST.get('Telephone')
        Add_You_Review = s.POST.get('Review')
        Time = s.POST.get('Time')
        comment(Name=Name, Mail=Mail, Telephone_no=Telephone_no, Add_Yuor_Review=Add_You_Review, Time=Time).save()

    elif s.method == "POST":
        Mail = s.POST.get('Mail')
        Time = s.POST.get('Time')
        email(Mail=Mail, Time=Time).save()

    maxsulot = mobile.objects.all().order_by('?')
    maxsulot2 = appliance.objects.all().order_by('?')
    maxsulot3 = computer.objects.all().order_by('?')
    chegirma = Discounts_mobile.objects.all()
    com = comment.objects.all()
    y = 0
    for st in com:
        y += 1
    y=y
    return render(s, 'single.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma,'com':com,'y':y})

'single---------------------------------------------------------------------------'


def single_mobile(s, id):
    if 'Review' in s.POST:
        Name = s.POST.get('Name')
        Mail = s.POST.get('Mail2')
        Telephone_no = s.POST.get('Telephone')
        Add_You_Review = s.POST.get('Review')
        Time = s.POST.get('Time')
        comment(Name=Name, Mail=Mail, Telephone_no=Telephone_no, Add_Yuor_Review=Add_You_Review, Time=Time).save()

    elif s.method == "POST":
        Mail = s.POST.get('Mail')
        Time = s.POST.get('Time')
        email(Mail=Mail, Time=Time).save()

    css = mobile.objects.get(id=id)
    rams = ram_mobile.objects.all()
    maxsulot = mobile.objects.all().order_by('?')
    maxsulot2 = appliance.objects.all().order_by('?')
    maxsulot3 = computer.objects.all().order_by('?')
    chegirma = Discounts_mobile.objects.all()
    com = comment.objects.all()
    y = 0
    for st in com:
        y += 1
    a = y
    return render(s, 'single.html',{'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3,'css': css, 'ra': rams, 'ch': chegirma,'com':com,'y':a})


def single_compyuter(s, id):
    if 'Review' in s.POST:
        Name = s.POST.get('Name')
        Mail = s.POST.get('Mail2')
        Telephone_no = s.POST.get('Telephone')
        Add_You_Review = s.POST.get('Review')
        Time = s.POST.get('Time')
        comment(Name=Name, Mail=Mail, Telephone_no=Telephone_no, Add_Yuor_Review=Add_You_Review, Time=Time).save()

    elif s.method == "POST":
        Mail = s.POST.get('Mail')
        Time = s.POST.get('Time')
        email(Mail=Mail, Time=Time).save()

    css = computer.objects.get(id=id)
    rams = ram_compyuter.objects.all()
    corei = core_i.objects.all()
    gens = gen.objects.all()
    maxsulot = mobile.objects.all().order_by('?')
    maxsulot2 = appliance.objects.all().order_by('?')
    maxsulot3 = computer.objects.all().order_by('?')
    chegirma = Discounts_mobile.objects.all()
    com = comment.objects.all()
    y = 0
    for st in com:
        y = y + 1
    return render(s, 'single.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3,'css': css, 'ch': chegirma, 'ra': rams, 'co': corei, 'gen': gens,'com':com,'y':y})


def single_appliance(s, id):
    if 'Review' in s.POST:
        Name = s.POST.get('Name')
        Mail = s.POST.get('Mail2')
        Telephone_no = s.POST.get('Telephone')
        Add_You_Review = s.POST.get('Review')
        Time = s.POST.get('Time')
        comment(Name=Name, Mail=Mail, Telephone_no=Telephone_no, Add_Yuor_Review=Add_You_Review, Time=Time).save()


    elif s.method == "POST":
        Mail = s.POST.get('Mail')
        Time = s.POST.get('Time')
        email(Mail=Mail, Time=Time).save()

    css = appliance.objects.get(id=id)
    maxsulot = mobile.objects.all().order_by('?')
    maxsulot2 = appliance.objects.all().order_by('?')
    maxsulot3 = computer.objects.all().order_by('?')
    chegirma = Discounts_mobile.objects.all()
    com = comment.objects.all()
    y = 0
    for st in com:
        y = y + 1
    return render(s, 'single.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3,'css': css, 'ch': chegirma,'com':com,'y':y})


'color--prices---------------------------------------------------------------------'

"""
MyModel.objects.filter(field__gte=5)  # field ≥ 5
MyModel.objects.filter(field__lte=5)  # field ≤ 5
"""

'p'
def mobils(r,allf,rang):
    chegirma = Discounts_mobile.objects.all()
    if rang == 'Red' or rang == 'Brown' or rang == 'Yellow' or rang == 'Violet' or rang == 'Orange' or rang == 'Blue':
        col = color.objects.get(Name=rang)
        colors = mobile.objects.filter(Color=col.id).order_by('?')
        colors1 = mobile.objects.all().order_by('?')
        colors2 = appliance.objects.all().order_by('?')
        colors3 = computer.objects.all().order_by('?')
        return render(r,'products.html', {'Max': colors,'Max1': colors1,'Max2': colors2, 'Max3': colors3, 'ch': chegirma})
    else:
        if rang == 'yk':
            prices = mobile.objects.filter(field__gt=100).order_by('?')
            prices1 = mobile.objects.all().order_by('?')
            prices2 = appliance.objects.all().order_by('?')
            prices3 = computer.objects.all().order_by('?')
            return render(r,'products.html', {'Max': prices,'Max1':prices1,'Max2': prices2, 'Max3': prices3, 'ch': chegirma})
        elif rang == 'yb':
            prices = mobile.objects.filter(field__gt=100, field__lt=500).order_by('?')
            prices1 = mobile.objects.all().order_by('?')
            prices2 = appliance.objects.all().order_by('?')
            prices3 = computer.objects.all().order_by('?')
            return render(r, 'products.html', {'Max': prices,'Max1':prices1,'Max2': prices2, 'Max3': prices3, 'ch': chegirma})
        elif rang == 'mom':
            prices = mobile.objects.filter(field__gt=1000, field__lt=10000).order_by('?')
            prices1 = mobile.objects.all().order_by('?')
            prices2 = appliance.objects.all().order_by('?')
            prices3 = computer.objects.all().order_by('?')
            return render(r, 'products.html', {'Max': prices,'Max1':prices1,'Max2': prices2, 'Max3': prices3, 'ch': chegirma})
        elif rang == 'omym':
            prices = mobile.objects.filter(field__gt=10000, field__lt=20000).order_by('?')
            prices1 = mobile.objects.all().order_by('?')
            prices2 = appliance.objects.all().order_by('?')
            prices3 = computer.objects.all().order_by('?')
            return render(r, 'products.html', {'Max': prices,'Max1':prices1,'Max2': prices2, 'Max3': prices3, 'ch': chegirma})
        elif rang == 'ymk':
            prices = mobile.objects.filter(field__lt=20000).order_by('?')
            prices1 = mobile.objects.all().order_by('?')
            prices2 = appliance.objects.all().order_by('?')
            prices3 = computer.objects.all().order_by('?')
            return render(r, 'products.html', {'Max': prices,'Max1':prices1,'Max2': prices2, 'Max3': prices3, 'ch': chegirma})
        else:
            prices = mobile.objects.all().order_by('?')
            prices2 = appliance.objects.all().order_by('?')
            prices3 = computer.objects.all().order_by('?')
            return render(r, 'products.html', {'Max': prices,'Max1':prices1,'Max2': prices2, 'Max3': prices3, 'ch': chegirma})

'p1'
def Computer(r, rang1):
    chegirma = Discounts_mobile.objects.all()
    if rang1 == 'Red' or rang1 == 'Brown' or rang1 == 'Yellow' or rang1 == 'Violet' or rang1 == 'Orange' or rang1 == 'Blue':
        col = color.objects.get(Name=rang1)
        colors = mobile.objects.all()
        colors2 = appliance.objects.all()
        colors3 = computer.objects.filter(Color=col.id)
        return render(r, 'products1.html', {'Max': colors, 'Max2': colors2, 'Max3': colors3, 'ch': chegirma})
    else:
        prices = mobile.objects.all()
        prices2 = appliance.objects.all()
        prices3 = computer.objects.filter(New_price=rang1)
        return render(r, 'products1.html', {'Max': prices, 'Max2': prices2, 'Max3': prices3, 'ch': chegirma})

'p2'
def appliances(r, rang2):
    chegirma = Discounts_mobile.objects.all()
    if rang2 == 'Red' or rang2 == 'Brown' or rang2 == 'Yellow' or rang2 == 'Violet' or rang2 == 'Orange' or rang2 == 'Blue':
        col = color.objects.get(Name=rang2)
        colors = mobile.objects.all()
        colors2 = appliance.objects.filter(Color=col.id)
        colors3 = computer.objects.all()
        return render(r, 'products2.html', {'Max': colors, 'Max2': colors2, 'Max3': colors3, 'ch': chegirma})
    else:
        prices = mobile.objects.all()
        prices2 = appliance.objects.filter(New_price=rang2)
        prices3 = computer.objects.all()
        return render(r, 'products2.html', {'Max': prices, 'Max2': prices2, 'Max3': prices3, 'ch': chegirma})
