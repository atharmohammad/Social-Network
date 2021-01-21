from django.db import models
from django.urls import reverse
from groups.models import Group
# Create your models here.
import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

class Post(models.Model):
    group = models.ForeignKey(Group,on_delete=models.CASCADE,related_name='posts',null=True,blank=True)
    message = models.TextField()
    message_html=models.TextField(editable=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='posts')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    def save(self,*args,**kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('posts:single',kwargs={'username':self.user.username , 'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','message']
