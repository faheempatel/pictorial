# models.py for pictorial project

class Post(models.Model):
    title = models.CharField(max_length=100)
    date_posted = models.DateField(auto_now_add=True)
    date_edited = models.DateField(auto_now=True)
    content = models.TextField()

class Photograph(models.Model): 
    caption = models.CharField(max_length=50) # Designed to display as the "title" attribute in <img> tags.
    date_uploaded = models.DateField(auto_now_add=True)

class Projects(models.Model):
    name = models.CharField(max_length=50)

