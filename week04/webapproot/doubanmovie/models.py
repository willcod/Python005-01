from django.db import models

# Create your models here.
class Movie(models.Model):
    """Movie table"""
    Id = models.CharField(primary_key=True, max_length=100)
    title = models.CharField(max_length=200)
    
    def __str__(self):
        """Return the title of the movie"""
        return self.title

class Comment(models.Model):
    """Comment of movie"""

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField()
    rate = models.IntegerField()

    class Meta:
        verbose_name_plural = 'comments'
    
    def __str__(self):
        """Return a brief"""
        return f"{self.text[:30]}..."