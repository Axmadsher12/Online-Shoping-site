from django.shortcuts import render
from myfiles.models import *
from django.db.models import Q


# Create your views here.
def about(b):
    if b.method == "POST":
        Mail = b.POST.get('Mail')
        Time = b.POST.get('Time')
        email(Mail=Mail, Time=Time).save()
    return render(b, 'about.html')


def codes(c):
    if c.method == "POST":
        Mail = c.POST.get('Mail')
        Time = c.POST.get('Time')
        email(Mail=Mail, Time=Time).save()
    return render(c, 'codes.html')


def faq(f):
    if f.method == "POST":
        Mail = f.POST.get('Mail')
        Time = f.POST.get('Time')
        email(Mail=Mail, Time=Time).save()
    return render(f, 'faq.html')


def icons(i):
    if i.method == "POST":
        Mail = i.POST.get('Mail')
        Time = i.POST.get('Time')
        email(Mail=Mail, Time=Time).save()
    return render(i, 'icons.html')


def index(h):
    if 'Mail3' in h.POST:
        EmailAddress = h.POST.get('Mail3')
        Password = h.POST.get('Password3')
        Time = h.POST.get('Time')
        signin(EmailAddress=EmailAddress, Password=Password, Time=Time).save()

    elif 'Name' in h.POST:
        Name = h.POST.get('Name')
        EmailAddress = h.POST.get('Mail2')
        Password = h.POST.get('Password1')
        ConfirmPassword = h.POST.get('Password2')
        Time = h.POST.get('Time')
        signup(Name=Name, EmailAddress=EmailAddress, Password=Password, ConfirmPassword=ConfirmPassword,
               Time=Time).save()

    elif h.method == "POST":
        Mail = h.POST.get('Mail')
        Time = h.POST.get('Time')
        email(Mail=Mail, Time=Time).save()

    brend = TopBrent.objects.all()
    m = mobile.objects.all()
    ta_a = type_appliance.objects.get(Name='Mp3 Player')
    app_audio = appliance.objects.filter(Type=ta_a.id).order_by('-id')
    ta_c = type_appliance.objects.get(Name='Camera')
    app_camera = appliance.objects.filter(Type=ta_c.id).order_by('-id')
    com = computer.objects.all().order_by('-id')
    app_hou = type_appliance.objects.get(Name='Appliances Household')
    app_Household = appliance.objects.filter(Type=app_hou.id).order_by('-id')
    app_kit = type_appliance.objects.get(Name='Appliances Kitchen')
    app_Kitchen = appliance.objects.filter(Type=app_kit.id).order_by('-id')
    "<-- New_products -->"
    "<-- 1 Mobiles -->"
    tm_t = type_mobile.objects.get(Name='Tablet')
    New_t = mobile.objects.filter(Type=tm_t.id)
    if New_t:
        New_t = mobile.objects.filter(Type=tm_t.id).order_by('-Time')[0]
    else:
        New_t = 1
    tm_s = type_mobile.objects.get(Name='Smart Watch')
    New_s = mobile.objects.filter(Type=tm_s.id)
    if New_s:
        New_s = mobile.objects.filter(Type=tm_s.id).order_by('-Time')[0]
    else:
        New_s = 1
    tm_m = type_mobile.objects.get(Name='Mobile Phone')
    New_m = mobile.objects.filter(Type=tm_m.id)
    if New_m:
        New_m = mobile.objects.filter(Type=tm_m.id).order_by('-Time')[0]
    else:
        New_m = 1
    "<-- 2 Compyuter -->"
    New_l = computer.objects.all()
    if New_l:
        New_l = computer.objects.all().order_by('-Time')[0]
    else:
        New_l = 1
    "<-- 3 Appliances -->"
    ta_h = type_appliance.objects.get(Name='Appliances Household')
    New_h = appliance.objects.filter(Type=ta_h.id)
    if New_h:
        New_h = appliance.objects.filter(Type=ta_h.id).order_by('-Time')[0]
    else:
        New_h = 1
    ta_k = type_appliance.objects.get(Name='Appliances Kitchen')
    New_k = appliance.objects.filter(Type=ta_k.id)
    if New_k:
        New_k = appliance.objects.filter(Type=ta_k.id).order_by('-Time')[0]
    else:
        New_k = 1
    ta_c = type_appliance.objects.get(Name='Camera')
    New_c = appliance.objects.filter(Type=ta_c.id)
    if New_c:
        New_c = appliance.objects.filter(Type=ta_c.id).order_by('-Time')[0]
    else:
        New_c = 1
    ta_m = type_appliance.objects.get(Name='Mp3 Player')
    New_p = appliance.objects.filter(Type=ta_m.id)
    if New_p:
        New_p = appliance.objects.filter(Type=ta_m.id).order_by('-Time')[0]
    else:
        New_p = 1
    return render(h, 'index.html', {'tb': brend,'ms':m,'app1':app_audio,'app2':app_camera,'com':com,'apph':app_Household,'appk':app_Kitchen,
                                    't':New_t,'m':New_m,'w':New_s,
                                    'l':New_l,
                                    'h':New_h,'k':New_k,'c':New_c,'p':New_p})


def mail(m):
    if m.method == "POST":
        Mail = m.POST.get('Mail')
        Time = m.POST.get('Time')
        email(Mail=Mail, Time=Time).save()
    return render(m, 'mail.html')


def pro(p):
    if 'Mail3' in p.POST:
        EmailAddress = p.POST.get('Mail3')
        Password = p.POST.get('Password3')
        Time = p.POST.get('Time')
        signin(EmailAddress=EmailAddress, Password=Password, Time=Time).save()

    elif 'Name' in p.POST:
        Name = p.POST.get('Name')
        EmailAddress = p.POST.get('Mail2')
        Password = p.POST.get('Password1')
        ConfirmPassword = p.POST.get('Password2')
        Time = p.POST.get('Time')
        signup(Name=Name, EmailAddress=EmailAddress, Password=Password, ConfirmPassword=ConfirmPassword,
               Time=Time).save()

    elif p.method == "POST":
        Mail = p.POST.get('Mail')
        Time = p.POST.get('Time')
        email(Mail=Mail, Time=Time).save()

    maxsulot = mobile.objects.all()
    maxsulot2 = appliance.objects.all()
    maxsulot3 = computer.objects.all()
    chegirma = Discounts_mobile.objects.all()
    return render(p, 'products.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma})


def pro1(p):
    if 'Mail3' in p.POST:
        EmailAddress = p.POST.get('Mail3')
        Password = p.POST.get('Password3')
        Time = p.POST.get('Time')
        signin(EmailAddress=EmailAddress, Password=Password, Time=Time).save()

    elif 'Name' in p.POST:
        Name = p.POST.get('Name')
        EmailAddress = p.POST.get('Mail2')
        Password = p.POST.get('Password1')
        ConfirmPassword = p.POST.get('Password2')
        Time = p.POST.get('Time')
        signup(Name=Name, EmailAddress=EmailAddress, Password=Password, ConfirmPassword=ConfirmPassword,
               Time=Time).save()

    elif p.method == "POST":
        Mail = p.POST.get('Mail')
        Time = p.POST.get('Time')
        email(Mail=Mail, Time=Time).save()

    maxsulot = mobile.objects.all()
    maxsulot2 = appliance.objects.all()
    maxsulot3 = computer.objects.all()
    chegirma = Discounts_compyuter.objects.all()
    return render(p, 'products1.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma})


def pro2(p):
    if 'Mail3' in p.POST:
        EmailAddress = p.POST.get('Mail3')
        Password = p.POST.get('Password3')
        Time = p.POST.get('Time')
        signin(EmailAddress=EmailAddress, Password=Password, Time=Time).save()

    elif 'Name' in p.POST:
        Name = p.POST.get('Name')
        EmailAddress = p.POST.get('Mail2')
        Password = p.POST.get('Password1')
        ConfirmPassword = p.POST.get('Password2')
        Time = p.POST.get('Time')
        signup(Name=Name, EmailAddress=EmailAddress, Password=Password, ConfirmPassword=ConfirmPassword,
               Time=Time).save()

    elif p.method == "POST":
        Mail = p.POST.get('Mail')
        Time = p.POST.get('Time')
        email(Mail=Mail, Time=Time).save()

    maxsulot = mobile.objects.all()
    maxsulot2 = appliance.objects.all()
    maxsulot3 = computer.objects.all()
    chegirma = Discounts_appliance.objects.all()
    return render(p, 'products2.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma})


def single1(s):
    if 'Review' in s.POST:
        Name = s.POST.get('Name')
        Mail = s.POST.get('Mail2')
        Telephone_no = s.POST.get('Telephone')
        Image = s.POST.get('')
        Add_You_Review = s.POST.get('Review')
        Time = s.POST.get('Time')
        comment(Name=Name, Mail=Mail, Telephone_no=Telephone_no, Image=Image, Add_Yuor_Review=Add_You_Review, Time=Time).save()

    elif 'Mail3' in s.POST:
        EmailAddress = s.POST.get('Mail3')
        Password = s.POST.get('Password3')
        Time = s.POST.get('Time')
        signin(EmailAddress=EmailAddress, Password=Password, Time=Time).save()

    elif 'Name2' in p.POST:
        Name = s.POST.get('Name2')
        EmailAddress = s.POST.get('Mail4')
        Password = s.POST.get('Password1')
        ConfirmPassword = s.POST.get('Password2')
        Time = s.POST.get('Time')
        signup(Name=Name, EmailAddress=EmailAddress, Password=Password, ConfirmPassword=ConfirmPassword,Time=Time).save()


    elif s.method == "POST":
        Mail = s.POST.get('Mail')
        Time = s.POST.get('Time')
        email(Mail=Mail, Time=Time).save()

    com = comment.objects.all()
    maxsulot = mobile.objects.all()
    maxsulot2 = appliance.objects.all()
    maxsulot3 = computer.objects.all()
    return render(s, 'single.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3, 'com':com})

'single---------------------------------------------------------------------------'


def single_mobile(s, id):
    css = mobile.objects.get(id=id)
    rams = ram_mobile.objects.all()
    com = comment.objects.all()
    return render(s, 'single.html', {'css': css, 'ra': rams,'com':com})


def single_compyuter(s, id):
    css = computer.objects.get(id=id)
    rams = ram_compyuter.objects.all()
    corei = core_i.objects.all()
    gens = gen.objects.all()
    com = comment.objects.all()
    return render(s, 'single.html', {'css': css, 'ra': rams, 'co': corei, 'gen': gens,'com':com})


def single_appliance(s, id):
    css = appliance.objects.get(id=id)
    com = comment.objects.all()
    return render(s, 'single.html', {'css': css,'com':com})


'color-----------------------------------------------------------------------------'

'p'
def color_mobils(r, rang):
    chegirma = Discounts_compyuter.objects.all()
    col = color.objects.get(Name=rang)
    colors = mobile.objects.filter(Color=col.id)
    return render(r, 'products.html', {'Max': colors,'ch':chegirma})

'p1'
def color_Computer(r, rang1):
    chegirma = Discounts_compyuter.objects.all()
    col = color.objects.get(Name=rang1)
    colors = computer.objects.filter(Color=col.id)
    return render(r, 'products1.html', {'Max': colors,'ch':chegirma})


'price-------------------------------------------------------------------------------'

'p'
def price_mobils(p, price):
    chegirma = Discounts_compyuter.objects.all()
    prices = mobile.objects.filter(New_price=price)
    return render(p, 'products.html', {'Max': prices,'ch':chegirma})

'p1'
def price_compyuter(p, price1):
    chegirma = Discounts_compyuter.objects.all()
    prices = computer.objects.filter(New_price=price1)
    return render(p, 'products1.html', {'Max': prices,'ch':chegirma})

