from django.contrib import admin
from .models import Keyword, KeywordRelated, Question, Choice, Memorytype

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question',)
    inlines = [ChoiceInline]

    fieldsets = [
        (None, {'fields': ['question']}),
    ]
    search_fields = ['question']

class KeywordrelatedInline(admin.TabularInline):
    model = KeywordRelated

class KeywordAdmin(admin.ModelAdmin):
    list_display = ('keyword',)
    inlines = [KeywordrelatedInline]

    fieldsets = [
        (None, {'fields': ['keyword']}),
    ]
    search_fields = ['keyword']


admin.site.register(Keyword, KeywordAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Memorytype)
