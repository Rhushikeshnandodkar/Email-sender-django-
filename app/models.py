from django.db import models

# Create your models here.
class LableModel(models.Model):
    lable_name = models.CharField(max_length=200)
    def __str__(self):
        return self.lable_name
    
class GroupModel(models.Model):
    group_name = models.CharField(max_length=200)
    def __str__(self):
        return self.group_name
    
class SectorModel(models.Model):
    sector_name = models.CharField(max_length=200)
    def __str__(self):
        return self.sector_name
    
class SubscribersModel(models.Model):
    first_name =  models.CharField(max_length=200)
    last_name =  models.CharField(max_length=200)
    email =  models.CharField(max_length=200)
    label = models.ForeignKey(LableModel, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE)
    sector = models.ForeignKey(SectorModel, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    subscription = models.BooleanField(default=True)
    def __str__(self):
        return self.first_name

class CampaignsModel(models.Model):
    campaign_name = models.CharField(max_length=200)
    subject = models.TextField()
    sender = models.CharField(max_length=200)
    label = models.ForeignKey(LableModel, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupModel, on_delete=models.CASCADE)
    sector = models.ForeignKey(SectorModel, on_delete=models.CASCADE)
    template = models.FileField(upload_to='files')
    def __str__(self):
        return self.campaign_name

