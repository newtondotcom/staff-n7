from django.db import models

class users(models.Model):
    username = models.CharField(max_length=100,default="leo")
    email = models.CharField(max_length=100)
    
class events(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    
class creneau(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    event = models.ForeignKey(events, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    
    
class answers(models.Model):
    event = models.ForeignKey(events, on_delete=models.CASCADE)
    creneau = models.ForeignKey(creneau, on_delete=models.CASCADE)
    answer = models.BooleanField()
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    
class preferences(models.Model):
    event = models.ForeignKey(events, on_delete=models.CASCADE)
    creneau = models.ForeignKey(creneau, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    
class notifSub(models.Model):
    endpoint = models.CharField(max_length=500,blank=True,null=True)
    p256dh = models.CharField(max_length=500,blank=True,null=True)
    auth = models.CharField(max_length=500,blank=True,null=True)
    expirationTime = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    
class notifHist(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    is_group = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True, null=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=200)
