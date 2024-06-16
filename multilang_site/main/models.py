from django.db import models

## ITEM DB TABLE DEFINITION ##
class Article(models.Model):
    title = models.CharField(max_length=128) ## ATICLE'S TITLE ##
    content = models.TextField() ## ARTICLE'S CONTENT ##
    publication_date = models.DateTimeField() ## ARTICLE'S PUBLICATION DATE ##

    def __str__(self):
        return self.title
