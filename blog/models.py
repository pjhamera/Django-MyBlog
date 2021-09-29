from django.db import models
from django.urls import reverse
from  django.utils.text import slugify
from django.core.validators import MinLengthValidator

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_address = models.EmailField(max_length=20)
    

    def full_name(self):
        return self.first_name + " " + self.last_name
    
    def __str__(self):
        return self.full_name()     


class Tag(models.Model):
    caption = models.CharField(max_length=20)        

    def __str__(self):
        return self.caption  

class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=150)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, default="", 
                            blank=True, null=False, db_index=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, 
                                related_name="posts")
    tags = models.ManyToManyField(Tag)    

    def __str__(self):
        return self.title      

    # def get_absolute_url(self):
    #     return reverse("post-detail", args=[self.slug])

    # def __str__(self):
    #     return f'{self.title} - {self.excerpt}'    

class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

  