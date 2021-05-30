from django.db import models

# Create your models here.
class Note(models.Model):
    IMP=((0,"very important"),(1,"important"),(2,"least important"))
    title=models.CharField(max_length=100)
    pub_date=models.DateTimeField(auto_now_add=True)
    description=models.TextField()
    importance=models.SmallIntegerField(choices=IMP)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-pub_date']  