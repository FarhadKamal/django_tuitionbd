from pickletools import UP_TO_NEWLINE
from sre_constants import CATEGORY
from django.db import models
from django.utils.timezone import now 
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
# Create your models here.

class PostManager(models.Manager):
    def sorted(self,title):
        return self.order_by(title)
    def less_than(self,size):
        return self.filter(salary__lt=size)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    hobby = models.CharField(max_length=20)
    content = models.TextField(null=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    def get_total_post(self):
        return self.subject_set.all().count()    

class Class_in(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name        
    

class Post(models.Model) :
    CATEGORY=(('Teacher','Teacher'),('Student','Student'))
    MEDIUM=(
        ('English','English'),
        ('Bangla','Bangla'),
        ('Math','Math'),
        ('Science','Science'),
        )
    #user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True, null=True)  
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)    
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=101)
    slug=models.CharField(max_length=100, default=title)
    email= models.EmailField()
    salary= models.FloatField()
    details= models.TextField()
    available=models.BooleanField()
    category=models.CharField(max_length=100,choices=CATEGORY)
    medium=MultiSelectField(max_length=100,max_choices=5,choices=MEDIUM,default='Bangla')
    subject=models.ManyToManyField(Subject, related_name="subject_set")
    class_in=models.ManyToManyField(Class_in, related_name="class_in_set")
    
    created_at=models.DateTimeField(default=now)
    image= models.ImageField(default='default.jpg',upload_to='tuition/images')
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Post, self).save(*args,**kwargs)
        img=Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            outputsize=(100,100)
            img.thumbnail(outputsize)
            img.save(self.image.path)

    def get_subject_list(self):
        sub=self.subject.all()
        subjects=""
        for s in sub:
            subjects=subjects+str(s.name)+","
        return subjects

    def get_class_list(self):
        sub=self.class_in.all()
        classes=""
        for c in sub:
            classes=classes+str(c.name)+","
        return classes
    def get_proper_case(self):
        return self.title.title()
    def details_short(self):
        details_words=self.details.split(' ')
        if len(details_words)>5:
            return ' '.join(details_words[:5])+" ..."
        else:
            return self.details
    
    objects=models.Manager()
    items=PostManager()
