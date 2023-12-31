from django.db import models
import uuid
from users.models import Profile
# Create your models here.


class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True,blank=True,on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)#null and blank means the field can be enpty
    featured_image = models.ImageField(
        null=True,blank=True,default="default.jpg")
    demo_link = models.CharField(max_length=2000,null=True,blank=True)
    source_link=models.CharField(max_length=2000,null=True,blank=True)#null for database and blank for django
    tags = models.ManyToManyField('Tag',blank=True)#many to many relation between Project and Tag
    votes_total = models.IntegerField(default=0,null=True,blank=True)
    vote_ratio = models.IntegerField(default=0,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)#adds the time stamp of whenever created
    id = models.UUIDField(default=uuid.uuid4,unique=True,
                          primary_key=True)#16 didgit id


    def __str__(self):
        return self.title
    
    class Meta:
        ordering =['-vote_ratio','-votes_total','title'] #descending
        # ordering =['-created'] #asecending
    
    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset
    
    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        ratio = (upVotes / totalVotes) * 100
        self.votes_total = totalVotes
        self.vote_ratio = ratio

        self.save()

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'up vote'),
        ('down','down vote')
    )

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True, blank=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)#cascade will delete all the reviews if the project is deleted
    body = models.TextField(null=True,blank=True)
    value = models.CharField(max_length=200,choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    
    class Meta:
        unique_together = [['owner','project']]

    def __str__(self):
        return self.value
    




class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,unique=True,primary_key=True)

    def __str__(self):
        return self.name
