from django.contrib import admin
from myfiles.models import *
# Register your models here.
class admin_type_mobile(admin.ModelAdmin):
    list_display = ['id','Name']

class admin_type_computer(admin.ModelAdmin):
    list_display = ['id','Name']

class admin_type_appliance(admin.ModelAdmin):
    list_display = ['id','Name']

class admin_core_i(admin.ModelAdmin):
    list_display = ['id','Core_i']

class admin_gen(admin.ModelAdmin):
    list_display = ['id','Gen']

'----------------'

class admin_color(admin.ModelAdmin):
    list_display = ['id','Name']

class admin_mobile(admin.ModelAdmin):
    list_display = ['id','Name','Old_price','New_price','Image','Image2','Image3','Image4','Image5','Rating','Product_Information','Color','Ram','Type','Time']

class admin_computer(admin.ModelAdmin):
    list_display = ['id','Name','Old_price','New_price','Core_i','Gen','Image','Image2','Image3','Image4','Image5','Rating','Product_Information','Color','Ram','Type','Time']

class admin_appliance(admin.ModelAdmin):
    list_display = ['id','Name','Old_price','New_price','Image','Image2','Image3','Image4','Image5','Rating','Product_Information','Color','Type','Time']

class admin_email(admin.ModelAdmin):
    list_display = ['id','Mail','Time']

class admin_signin(admin.ModelAdmin):
    list_display = ['id','EmailAddress','Password','Time']

class admin_signup(admin.ModelAdmin):
    list_display = ['id','Name','EmailAddress','Password','ConfirmPassword','Time']

class admin_Contact(admin.ModelAdmin):
    list_display = ['id','Your_name','Your_email','Telephone_no','Send_message','Time']

class admin_Contact_Answer(admin.ModelAdmin):
    list_display = ['id','Answer','Time']

class admin_TopBrent(admin.ModelAdmin):
    list_display = ['id','Name','Image','Time']

class admin_MeetOurTeam(admin.ModelAdmin):
    list_display = ['id','Name','Image','occupation','Facebook','Twitter','Google','Pinterest','Time']

class admin_comment(admin.ModelAdmin):
    list_display = ['id','Name','Mail','Image','Telephone_no','Add_Yuor_Review','Time']

class admin_ram_mobile(admin.ModelAdmin):
    list_display = ['id','Ram']

class admin_ram_compyuter(admin.ModelAdmin):
    list_display = ['id','Ram']

class admin_Discounts_mobile(admin.ModelAdmin):
    list_display = ['id','Percent','comment','Time']

admin.site.register(mobile,admin_mobile)
admin.site.register(computer,admin_computer)
admin.site.register(appliance,admin_appliance)
admin.site.register(email,admin_email)
admin.site.register(signin,admin_signin)
admin.site.register(signup,admin_signup)
admin.site.register(Contact,admin_Contact)
admin.site.register(Contact_Answer,admin_Contact_Answer)
admin.site.register(type_mobile,admin_type_mobile)
admin.site.register(type_computer,admin_type_computer)
admin.site.register(type_appliance,admin_type_appliance)
admin.site.register(color,admin_color)
admin.site.register(TopBrent,admin_TopBrent)
admin.site.register(MeetOurTeam,admin_MeetOurTeam)
admin.site.register(comment,admin_comment)
admin.site.register(ram_mobile,admin_ram_mobile)
admin.site.register(ram_computer,admin_ram_compyuter)
admin.site.register(gen,admin_gen)
admin.site.register(core_i,admin_core_i)
admin.site.register(Discounts_mobile,admin_Discounts_mobile)

'''
Rank	Brand	Brand Value % change from 2020
1	Amazon	64%
2	Apple	74%
3	Google	42%
4	Microsoft	26%
'''

"""
Brand	2022 Value
1	Nike	$33.1 B
2	Gucci	$18.1 B
3	Louis Vuitton	$15.1 B
4	Adidas	$14.3 B
"""
