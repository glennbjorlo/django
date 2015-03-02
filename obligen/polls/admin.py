from django.contrib import admin

# Register your models here.

from polls.models import Choice, Question

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
	]

admin.site.register(Question)
admin.site.register(Choice)
