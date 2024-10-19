from django.db import models

# Create your models here.



class LaunchRegistrants(models.Model):
    fullname = models.CharField(max_length = 1000)
    email= models.EmailField(max_length = 1000)
    phonenumber = models.CharField(max_length = 1000)
    referralcode = models.CharField(max_length = 1000)
    referercode = models.CharField(max_length = 200, null=True, blank=True)
    # numberOfReferrals = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-edited_at', '-created_at']
        
    def __str__(self):
        return f'{self.fullname} | {self.fullname} | {self.referralcode}'





class ReferralRecords(models.Model):
    fullname = models.CharField(max_length = 1000)
    email= models.EmailField(max_length = 1000)
    numberOfReferrals = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-edited_at', '-created_at']
        
    def __str__(self):
        return f'{self.email} | {self.numberOfReferrals}'




