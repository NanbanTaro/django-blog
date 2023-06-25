from django.contrib import admin
from .models import Post

# Allow blog to be registered on the admin page
admin.site.register(Post)
