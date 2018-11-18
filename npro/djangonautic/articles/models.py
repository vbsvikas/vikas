from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default="default.png",blank=True)
    thumb_pdf = models.FileField(default="default2.pdf", blank=True)
    # add the authoyr later

    def __str__(self):
        return self.title

    # this function is for a big body having soo much text it show only first 50 letters and ..... and late add link to view all body
    def s(self):
        return self.body[:50] + '.....'
