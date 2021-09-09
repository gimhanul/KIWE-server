from django.contrib import admin
from .models import Keyword, Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question',)
    inlines = [ChoiceInline]

    fieldsets = [
        (None, {'fields': ['question']}),
    ]
    search_fields = ['question']


admin.site.register(Keyword)
admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
