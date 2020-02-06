from django.db import models

# Create your models here.
class job(models.Model):
    title = models.CharField(default="job_title",max_length=50)
    keywords = models.TextField(blank=True)
    job_description = models.TextField()
    hr_email = models.EmailField(max_length=254)
    salary = models.CharField(max_length=50)
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "jobs"