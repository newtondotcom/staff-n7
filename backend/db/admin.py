from django.contrib import admin
from .models import *

@admin.register(users)
class usersAdmin(admin.ModelAdmin):
    list_display = ('username','email')

@admin.register(events)
class eventsAdmin(admin.ModelAdmin):
    list_display = ('title','start','end','description','location','club')
    
@admin.register(creneau)
class creneauAdmin(admin.ModelAdmin):
    list_display = ('title','start','end','event')
    
@admin.register(answers)
class answersAdmin(admin.ModelAdmin):
    list_display = ('event','creneau','answer','user')
    
@admin.register(preferences)
class preferencesAdmin(admin.ModelAdmin):
    list_display = ('event','creneau','user')
    
@admin.register(notifSub)
class notifSubAdmin(admin.ModelAdmin):
    list_display = ('user','endpoint','p256dh','auth','expirationTime')

@admin.register(notifHist)
class notifHistAdmin(admin.ModelAdmin):
    list_display = ('user','is_group','date','title','body')
