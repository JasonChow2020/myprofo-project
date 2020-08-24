from django.db import models

class Blog(models.Model): #defines what properties Blog will have
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title #show title in the admin UI

    def abbrev(self):
        return self.body[:100] #shorten to 100 characters

    def date(self):
        return self.pub_date.strftime('%b %e %Y') #month, date , Year
