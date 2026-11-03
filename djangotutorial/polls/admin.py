from django.contrib import admin

from .models import Question
from .models import Choice

class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = "pub_date"
    # Trier de la plus récente à la plus anvienne
    ordering = ["-pub_date"]
    list_display = ("question_text", "pub_date", "id")
    list_filter = ("question_text", "pub_date", "id")


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)