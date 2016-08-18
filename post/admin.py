from django.contrib import admin

# Register your models here.
from .models import Message

# class MessageAdmin(admin.ModelAdmin):
#     list_display = ["title", "content", "timestamp", "author"]
#     class Meta:
#         model = Message

admin.site.register(Message)
