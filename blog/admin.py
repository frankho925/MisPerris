from django.contrib import admin
from .models import Post
from .models import Form
from .models import Mascota

admin.site.register(Post)
admin.site.register(Form)
admin.site.register(Mascota)

# Register your models here.
