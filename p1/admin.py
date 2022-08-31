from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
# Register your models here.
class TestsAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'created_at', 'updated_at']
    list_filter = ['title', 'created_at', 'updated_at']

    class Meta:
        model = Test

admin.site.register(Test, TestsAdmin)


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['Question_Text']
    search_fields = ['Question_Text', 'created_at', 'updated_at']
    list_filter = ['Question_Text', 'created_at', 'updated_at']

    class Meta:
        model = Questions

admin.site.register(Questions, QuestionsAdmin)

class OptionsAdmin(admin.ModelAdmin):
    list_display = ['Option_Text','Question', 'created_at', 'updated_at']
    search_fields = ['Option_Text','Question', 'created_at', 'updated_at']
    list_filter = ['Option_Text','Question', 'created_at', 'updated_at']

    # def Question(self, obj):
    #     return obj.Question.Question_Text
    class Meta:
        model = Options

admin.site.register(Options,OptionsAdmin)

class AnswersAdmin(admin.ModelAdmin):
    list_display = ['user','Option','number']
    search_fields = ['user','Option','number', 'created_at', 'updated_at']
    list_filter = ['user','Option','number', 'created_at', 'updated_at']

    class Meta:
        model = Answers

admin.site.register(Answers,AnswersAdmin)