from django.contrib import admin
from .models import Article

# ADD A + BUTTON TO ADD AN ITEM TO THE ADMINISTRATION PANEL
admin.site.register(Article)
