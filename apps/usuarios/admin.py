from django.contrib import admin
from django.contrib.admin.decorators import register
from usuarios.models import Usuario


# Register your models here.
admin.site.register(Usuario)

