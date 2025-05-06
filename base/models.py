from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
class Roll(models.Model):
    roll_id = models.CharField(max_length=50)
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.roll_id,self.name
    
class UserAttributes(models.Model):
    id = models.AutoField(primary_key=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    roll = models.ForeignKey(Roll, on_delete=models.SET_NULL, null=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    status = models.BooleanField(default=True)
    last_login = models.DateTimeField(auto_now=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    def __str__(self):
        return self.user.username

class Task(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField(blank=True, null=True)
    status = models.BooleanField(default=True)

    collaboration = models.CharField(max_length=100, primary_key=True, unique=True)
    project = models.CharField(max_length=100)
    
    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Urgent', 'Urgent'),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default="Personal")
    priority = models.IntegerField(default=1)

    assigned_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks"
    )
    assigned_to = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks_to"
    )

    def __str__(self):
        return self.name
