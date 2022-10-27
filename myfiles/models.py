from django.db import models

# Create your models here.

class type_mobile(models.Model):
    Name = models.CharField(null=True, blank=True,max_length=25)
    def __str__(self):
        return self.Name

class type_computer(models.Model):
    Name = models.CharField(null=True, blank=True,max_length=25)
    def __str__(self):
        return self.Name

class type_appliance(models.Model):
    Name = models.CharField(null=True, blank=True,max_length=25)
    def __str__(self):
        return self.Name

class core_i(models.Model):
    Core_i = models.IntegerField()
    def __str__(self):
        return str(self.Core_i)

class gen(models.Model):
    Gen = models.IntegerField()
    def __str__(self):
        return str(self.Gen)

from django.core.validators import MaxValueValidator,MinValueValidator
'-----------------------------'
class color(models.Model):
    Name = models.CharField(max_length=25)
    def __str__(self):
        return self.Name

class ram_mobile(models.Model):
    Ram = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.Ram)

class ram_computer(models.Model):
    Ram = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.Ram)

'-------------Asosiy---------------'
class mobile(models.Model):
    Name = models.CharField(max_length=25)
    Old_price = models.IntegerField()
    New_price = models.IntegerField()
    Image = models.ImageField(null=True,blank=True,upload_to='media')
    Image2 = models.ImageField(null=True,blank=True,upload_to='media')
    Image3 = models.ImageField(null=True,blank=True,upload_to='media')
    Image4 = models.ImageField(null=True,blank=True,upload_to='media')
    Image5 = models.ImageField(null=True,blank=True,upload_to='media')
    Rating = models.IntegerField(null=True,blank=True)
    Product_Information = models.TextField(null=True,blank=True)
    Color = models.ForeignKey(color, null=True, blank=True, on_delete=models.CASCADE)
    Ram = models.ForeignKey(ram_mobile, null=True, blank=True, on_delete=models.CASCADE)
    Type = models.ForeignKey(type_mobile, null=True, blank=True, on_delete=models.CASCADE)
    Time = models.DateTimeField(auto_now=True,blank=True,null=True)

class computer(models.Model):
    Name = models.CharField(max_length=25)
    Old_price = models.IntegerField()
    New_price = models.IntegerField()
    Core_i = models.ForeignKey(core_i,null=True,blank=True,on_delete=models.CASCADE)
    Gen = models.ForeignKey(gen,null=True,blank=True,on_delete=models.CASCADE)
    Image = models.ImageField(null=True,blank=True,upload_to='media')
    Image2 = models.ImageField(null=True,blank=True,upload_to='media')
    Image3 = models.ImageField(null=True,blank=True,upload_to='media')
    Image4 = models.ImageField(null=True,blank=True,upload_to='media')
    Image5 = models.ImageField(null=True,blank=True,upload_to='media')
    Rating = models.IntegerField(null=True,blank=True)
    Product_Information = models.TextField(null=True,blank=True)
    Color = models.ForeignKey(color, null=True, blank=True, on_delete=models.CASCADE)
    Ram = models.ForeignKey(ram_computer, null=True, blank=True, on_delete=models.CASCADE)
    Type = models.ForeignKey(type_computer, null=True, blank=True, on_delete=models.CASCADE)
    Time = models.DateTimeField(auto_now=True,blank=True,null=True)

class appliance(models.Model):
    Name = models.CharField(max_length=25)
    Old_price = models.IntegerField()
    New_price = models.IntegerField()
    Image = models.ImageField(null=True,blank=True,upload_to='media')
    Image2 = models.ImageField(null=True,blank=True,upload_to='media')
    Image3 = models.ImageField(null=True,blank=True,upload_to='media')
    Image4 = models.ImageField(null=True,blank=True,upload_to='media')
    Image5 = models.ImageField(null=True,blank=True,upload_to='media')
    Rating = models.IntegerField(null=True,blank=True)
    Product_Information = models.TextField(null=True,blank=True)
    Color = models.ForeignKey(color,null=True, blank=True,on_delete=models.CASCADE)
    Type = models.ForeignKey(type_appliance, null=True, blank=True, on_delete=models.CASCADE)
    Time = models.DateTimeField(auto_now=True,blank=True,null=True)


class email(models.Model):
    Mail = models.EmailField()
    Time = models.DateTimeField(auto_now=True)


"Adminga murojat"
class Contact(models.Model):
    Your_name = models.CharField(max_length=25)
    Your_email = models.EmailField()
    Telephone_no = models.IntegerField()
    Send_message = models.TextField()
    Time = models.DateTimeField(auto_now=True)

class Contact_Answer(models.Model):
    Answer = models.TextField()
    Time = models.DateTimeField(auto_now=True)

"Brentlar"
class TopBrent(models.Model):
    Name = models.CharField(null=True,blank=True,max_length=25)
    Image = models.ImageField(null=True,blank=True,upload_to='media')
    Time = models.DateTimeField(auto_now=True)

'Bizning jamoa'
class MeetOurTeam(models.Model):
    Name = models.CharField(max_length=25)
    Image = models.ImageField(upload_to='media')
    occupation = models.CharField(max_length=25)
    Facebook = models.EmailField(null=True,blank=True)
    Twitter = models.EmailField(null=True, blank=True)
    Google = models.EmailField(null=True, blank=True)
    Pinterest = models.EmailField(null=True, blank=True)
    Time = models.DateTimeField(auto_now=True)

'Izox'
class comment(models.Model):
    Name = models.CharField(max_length=25)
    Mail = models.EmailField()
    Telephone_no = models.IntegerField(null=True,blank=True)
    Add_Yuor_Review = models.TextField(null=True,blank=True)
    Time = models.DateTimeField(null=True,blank=True,auto_now=True)

'Chegirmalar'
class Discounts_mobile(models.Model):
    Percent = models.IntegerField()
    comment = models.TextField(null=True, blank=True)
    Time = models.DateTimeField(auto_now=True)

#Profil
