from django.contrib import admin
from .models import User,AdminModel,App,Image

# Register your models here.
admin.site.register(User)
admin.site.register(AdminModel)
admin.site.register(App)
admin.site.register(Image)