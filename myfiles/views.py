from django.shortcuts import render,redirect
from myfiles.models import *
from django.db.models import Q


# Create your views here.
def about(b):
    if 'Mail3' in b.POST:
        EmailAddress = b.POST.get('Mail3')
        Password = b.POST.get('Password3')
        Time = b.POST.get('Time')
        signin(EmailAddress=EmailAddress, Password=Password, Time=Time).save()

    elif 'Name' in b.POST:
        Name = b.POST.get('Name')
        EmailAddress = b.POST.get('Mail2')
        Password = b.POST.get('Password1')
        ConfirmPassword = b.POST.get('Password2')
        Time = b.POST.get('Time')
        signup(Name=Name, EmailAddress=EmailAddress, Password=Password, ConfirmPassword=ConfirmPassword,Time=Time).save()

    elif b.method == "POST":
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

from django.contrib.auth.forms import UserCreationForm,UserChangeForm
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

    'Tab'
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
    chegirma = Discounts_mobile.objects.all()
    comment1 = comment.objects.all()

    if up1 == 'sign in ':
        form = forms.LoginForm()
        message = ''
        if request.method == 'POST':
            form = forms.LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                )
                if user is not None:
                    login(request, user)
                    return redirect('home')
            message = 'Login failed!'

    return render(h, 'index.html', {'tb': brend,'ms':m,'app1':app_audio,'app2':app_camera,'com':com,'apph':app_Household,'appk':app_Kitchen,
                                    't':New_t,'m':New_m,'w':New_s,
                                    'l':New_l,
                                    'h':New_h,'k':New_k,'c':New_c,'p':New_p,
                                    'ch':chegirma,'comment':comment1})


def mail(m):
    if 'Your_Name' in m.POST:
        Your_Name = m.POST.get('Your_Name')
        Your_email = m.POST.get('Your_Email')
        Telephone_no = m.POST.get('Telephone_No')
        Send_message = m.POST.get('Message')
        Time = m.POST.get('Time')
        Contact(Your_name=Your_Name,Your_email=Your_email,Telephone_no=Telephone_no,Send_message=Send_message,Time=Time).save()

    elif 'Mail3' in m.POST:
        EmailAddress = m.POST.get('Mail3')
        Password = m.POST.get('Password3')
        Time = m.POST.get('Time')
        signin(EmailAddress=EmailAddress, Password=Password, Time=Time).save()

    elif 'Name' in m.POST:
        Name = m.POST.get('Name')
        EmailAddress = m.POST.get('Mail2')
        Password = m.POST.get('Password1')
        ConfirmPassword = m.POST.get('Password2')
        Time = m.POST.get('Time')
        signup(Name=Name, EmailAddress=EmailAddress, Password=Password, ConfirmPassword=ConfirmPassword,Time=Time).save()

    elif m.method == "POST":
        Mail = m.POST.get('Mail')
        Time = m.POST.get('Time')
        email(Mail=Mail, Time=Time).save()
    chegirma = Discounts_mobile.objects.all()
    con = Contact.objects.all()
    return render(m, 'mail.html',{'ch':chegirma,'con':con})


def pro(p,allf):
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

        'Filter----------------------------------------------|'
    elif allf == 'Mobile Phone' or allf == 'Smart Watch' or allf == 'Tablet':
        tmf = type_mobile.objects.get(Name=allf)
        maxsulot = mobile.objects.filter(Type=tmf)
        maxsulot2 = appliance.objects.all()
        maxsulot3 = computer.objects.all()
        chegirma = Discounts_mobile.objects.all()
        return render(p, 'products.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma})
    else:
        maxsulot = mobile.objects.all()
        maxsulot2 = appliance.objects.all()
        maxsulot3 = computer.objects.all()
        chegirma = Discounts_mobile.objects.all()
        return render(p, 'products.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma})


def pro1(p,allf):
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

        'Filter----------------------------------------------|'
    elif allf == 'Laptop' or allf == 'Personal Computer':
        tmf = type_compyuter.objects.get(Name=allf)
        maxsulot = mobile.objects.all()
        maxsulot2 = appliance.objects.all()
        maxsulot3 = computer.objects.filter(Type=tmf)
        chegirma = Discounts_mobile.objects.all()
        return render(p, 'products1.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma})
    else:
        maxsulot = mobile.objects.all()
        maxsulot2 = appliance.objects.all()
        maxsulot3 = computer.objects.all()
        chegirma = Discounts_mobile.objects.all()
        return render(p, 'products1.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma})


def pro2(p,allf):
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

        'Filter----------------------------------------------|'
    elif allf == 'Appliances Kitchen' or allf == 'Appliances Household' or allf == 'Camera' or allf == 'Mp3 Player':
        tmf = type_appliance.objects.get(Name=allf)
        maxsulot = mobile.objects.all()
        maxsulot2 = appliance.objects.filter(Type=tmf)
        maxsulot3 = computer.objects.all()
        chegirma = Discounts_mobile.objects.all()
        return render(p, 'products2.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma})
    else:
        maxsulot = mobile.objects.all()
        maxsulot2 = appliance.objects.all()
        maxsulot3 = computer.objects.all()
        chegirma = Discounts_mobile.objects.all()
        return render(p, 'products2.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3, 'ch': chegirma})


def single1(s):
    if 'Review' in s.POST:
        Name = s.POST.get('Name')
        Mail = s.POST.get('Mail2')
        Telephone_no = s.POST.get('Telephone')
        Add_You_Review = s.POST.get('Review')
        Time = s.POST.get('Time')
        comment(Name=Name, Mail=Mail, Telephone_no=Telephone_no, Add_Yuor_Review=Add_You_Review, Time=Time).save()

    elif 'Mail3' in s.POST:
        EmailAddress = s.POST.get('Mail3')
        Password = s.POST.get('Password3')
        Time = s.POST.get('Time')
        signin(EmailAddress=EmailAddress, Password=Password, Time=Time).save()

    elif 'Name2' in s.POST:
        Name = s.POST.get('Name2')
        EmailAddress = s.POST.get('Mail4')
        Password = s.POST.get('Password1')
        ConfirmPassword = s.POST.get('Password2')
        Time = s.POST.get('Time')
        signup(Name=Name, EmailAddress=EmailAddress, Password=Password, ConfirmPassword=ConfirmPassword,
               Time=Time).save()

    elif s.method == "POST":
        Mail = s.POST.get('Mail')
        Time = s.POST.get('Time')
        email(Mail=Mail, Time=Time).save()

    maxsulot = mobile.objects.all()
    maxsulot2 = appliance.objects.all()
    maxsulot3 = computer.objects.all()
    chegirma = Discounts_mobile.objects.all()
    com = comment.objects.all()
    y = 0
    for st in com:
        y = y + 1
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

    elif 'Mail3' in s.POST:
        EmailAddress = s.POST.get('Mail3')
        Password = s.POST.get('Password3')
        Time = s.POST.get('Time')
        signin(EmailAddress=EmailAddress, Password=Password, Time=Time).save()

    elif 'Name2' in s.POST:
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

    css = mobile.objects.get(id=id)
    rams = ram_mobile.objects.all()
    maxsulot = mobile.objects.all()
    maxsulot2 = appliance.objects.all()
    maxsulot3 = computer.objects.all()
    chegirma = Discounts_mobile.objects.all()
    com = comment.objects.all()
    y = 0
    for st in com:
        y = y + 1
    obj = ratings.objects.filter(score=0).order_by('?').first()
    return render(s, 'single.html',{'obj':obj,'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3,'css': css, 'ra': rams, 'ch': chegirma,'com':com})


def single_compyuter(s, id):
    if 'Review' in s.POST:
        Name = s.POST.get('Name')
        Mail = s.POST.get('Mail2')
        Telephone_no = s.POST.get('Telephone')
        Add_You_Review = s.POST.get('Review')
        Time = s.POST.get('Time')
        comment(Name=Name, Mail=Mail, Telephone_no=Telephone_no, Add_Yuor_Review=Add_You_Review, Time=Time).save()

    elif 'Mail3' in s.POST:
        EmailAddress = s.POST.get('Mail3')
        Password = s.POST.get('Password3')
        Time = s.POST.get('Time')
        signin(EmailAddress=EmailAddress, Password=Password, Time=Time).save()

    elif 'Name2' in s.POST:
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

    css = computer.objects.get(id=id)
    rams = ram_compyuter.objects.all()
    corei = core_i.objects.all()
    gens = gen.objects.all()
    maxsulot = mobile.objects.all()
    maxsulot2 = appliance.objects.all()
    maxsulot3 = computer.objects.all()
    chegirma = Discounts_mobile.objects.all()
    com = comment.objects.all()
    y = 0
    for st in com:
        y = y + 1
    return render(s, 'single.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3,'css': css, 'ch': chegirma, 'ra': rams, 'co': corei, 'gen': gens,'com':com})


def single_appliance(s, id):
    if 'Review' in s.POST:
        Name = s.POST.get('Name')
        Mail = s.POST.get('Mail2')
        Telephone_no = s.POST.get('Telephone')
        Add_You_Review = s.POST.get('Review')
        Time = s.POST.get('Time')
        comment(Name=Name, Mail=Mail, Telephone_no=Telephone_no, Add_Yuor_Review=Add_You_Review, Time=Time).save()

    elif 'Mail3' in s.POST:
        EmailAddress = s.POST.get('Mail3')
        Password = s.POST.get('Password3')
        Time = s.POST.get('Time')
        signin(EmailAddress=EmailAddress, Password=Password, Time=Time).save()

    elif 'Name2' in s.POST:
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

    css = appliance.objects.get(id=id)
    maxsulot = mobile.objects.all()
    maxsulot2 = appliance.objects.all()
    maxsulot3 = computer.objects.all()
    chegirma = Discounts_mobile.objects.all()
    com = comment.objects.all()
    y = 0
    for st in com:
        y = y + 1
    return render(s, 'single.html', {'Max': maxsulot, 'Max2': maxsulot2, 'Max3': maxsulot3,'css': css, 'ch': chegirma,'com':com})


'color--prices---------------------------------------------------------------------'

'p'
def mobils(r, rang):
    chegirma = Discounts_mobile.objects.all()
    if rang == 'Red' or rang == 'Brown' or rang == 'Yellow' or rang == 'Violet' or rang == 'Orange' or rang == 'Blue':
        col = color.objects.get(Name=rang)
        colors = mobile.objects.filter(Color=col.id)
        colors2 = computer.objects.filter(Color=col.id)
        colors3 = appliance.objects.filter(Color=col.id)
        return render(r, 'products2.html', {'Max': colors, 'Max2': colors2, 'Max3': colors3, 'ch': chegirma})
    else:
        prices = mobile.objects.filter(New_price=rang)
        prices2 = computer.objects.filter(New_price=rang)
        prices3 = appliance.objects.filter(New_price=rang)
        return render(r, 'products2.html', {'Max': prices, 'Max2': prices2, 'Max3': prices3, 'ch': chegirma})

'p1'
def Computer(r, rang1):
    chegirma = Discounts_mobile.objects.all()
    if rang1 == 'Red' or rang1 == 'Brown' or rang1 == 'Yellow' or rang1 == 'Violet' or rang1 == 'Orange' or rang1 == 'Blue':
        col = color.objects.get(Name=rang1)
        colors = mobile.objects.filter(Color=col.id)
        colors2 = computer.objects.filter(Color=col.id)
        colors3 = appliance.objects.filter(Color=col.id)
        return render(r, 'products2.html', {'Max': colors, 'Max2': colors2, 'Max3': colors3, 'ch': chegirma})
    else:
        prices = mobile.objects.filter(New_price=rang1)
        prices2 = computer.objects.filter(New_price=rang1)
        prices3 = appliance.objects.filter(New_price=rang1)
        return render(r, 'products2.html', {'Max': prices, 'Max2': prices2, 'Max3': prices3, 'ch': chegirma})

'p2'
def appliances(r, rang2):
    chegirma = Discounts_mobile.objects.all()
    if rang2 == 'Red' or rang2 == 'Brown' or rang2 == 'Yellow' or rang2 == 'Violet' or rang2 == 'Orange' or rang2 == 'Blue':
        col = color.objects.get(Name=rang2)
        colors = mobile.objects.filter(Color=col.id)
        colors2 = computer.objects.filter(Color=col.id)
        colors3 = appliance.objects.filter(Color=col.id)
        return render(r, 'products2.html', {'Max': colors, 'Max2': colors2, 'Max3': colors3, 'ch': chegirma})
    else:
        prices = mobile.objects.filter(New_price=rang2)
        prices2 = computer.objects.filter(New_price=rang2)
        prices3 = appliance.objects.filter(New_price=rang2)
        return render(r, 'products2.html', {'Max': prices, 'Max2': prices2, 'Max3': prices3, 'ch': chegirma})
