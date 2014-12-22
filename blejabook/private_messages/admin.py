from django.contrib import admin
from private_messages.models import Msg
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User

# Register your models here.
#class MessageAdmin(admin.ModelAdmin):
	
	#list_display = ['sender', 'recipient', 'message_text', 'sent_at']

#admin.site.register(Message, MessageAdmin)
admin.site.register(Msg)