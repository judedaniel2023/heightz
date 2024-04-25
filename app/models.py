from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=255, default='Company')
    location = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    open_hours = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.company_name
    
    # class Meta:
    #     db_table = "custome_table"
    
    

class Service(models.Model):
    icon = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    
    
    def __str__(self):
        return self.title
        

class Testimonial(models.Model):
    STARS_COUNTS = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five')
    ]
    user_image = models.ImageField(upload_to="uploads/testimonial/", default="images.png")
    rating_count = models.IntegerField(choices=STARS_COUNTS)
    username =  models.CharField(max_length=50)
    user_job_title = models.CharField(max_length=50)
    review = models.TextField()
    
    def __str__(self):
        return f"{self.username} - {self.user_job_title}"
    

class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    
    def __str__(self):
        return self.question    
    
    
class ContactFormLog(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    action_time = models.DateTimeField(null=True, blank=True)
    is_success = models.BooleanField(default=False)
    is_error = models.BooleanField(default=False)
    error_message = models.TextField(null=True, blank=True)
        
    def __str__(self):
        return self.email
    
    
class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now())
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories' 
        
    def __str__(self):
        return self.cat_name
    
class Blog(models.Model):
    blog_image = models.ImageField(default="uploads/blogs/")
    category = models.ForeignKey(Category, models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(default = timezone.now())
    content = RichTextField()

    
    
    def __str__(self):
        return self.title
    