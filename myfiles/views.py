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

    brend = TopBrents.objects.all()
    return render(h, 'index.html', {'tb': brend})


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
    maxsulot2 = appliances.objects.all()
    maxsulot3 = computer.objects.all()
    chegirma = Discounts_mobiles.objects.all()
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
    maxsulot2 = appliances.objects.all()
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
    maxsulot2 = appliances.objects.all()
    maxsulot3 = computer.objects.all()
    chegirma = Discounts_appliance.objects.all()
    return render(p, 'products2.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma})


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
    return render(s, 'single.html')


'single---------------------------------------------------------------------------'


def single_mobile(s, id):
    css = mobile.objects.get(id=id)
    rams = ram_mobile.objects.all()
    return render(s, 'single.html', {'css': css, 'ra': rams})


def single_compyuter(s, id):
    css = computer.objects.get(id=id)
    rams = ram_compyuter.objects.all()
    corei = core_i.objects.all()
    gens = gen.objects.all()
    return render(s, 'single.html', {'css': css, 'ra': rams, 'co': corei, 'gen': gens})


def single_appliance(s, id):
    css = appliance.objects.get(id=id)
    return render(s, 'single.html', {'css': css})


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

