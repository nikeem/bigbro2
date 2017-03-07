from django.db import models

class Project(models.Model):
    ProjId = models.IntegerField()
    ProjName = models.CharField(max_length=250)
    ProjOwner = models.IntegerField()
    objsType = models.IntegerField()
    whatLookAt = models.IntegerField()
    adAccId = models.IntegerField()
    adClientId = models.IntegerField()
    targetGroupId = models.IntegerField()
    Token = models.CharField(max_length=250)
    Objs = models.TextField()
    LastState = models.TextField()

    def __str__(self):
        return str(self.ProjId) + ' - ' + str(self.ProjName)
    
class User(models.Model):
    Name = models.CharField(max_length=250)