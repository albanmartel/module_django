from django.contrib import admin

from .models import Question
from .models import Choice

class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = "pub_date"
    # Trier de la plus récente à la plus anvienne
    ordering = ["-pub_date"]
    # Afficher les champs suivants de la liste
    list_display = ("question_text", "pub_date", "id")
    # Filtrer La liste des questions par les critères texte de la question, date de la question puis sont id
    list_filter = ("question_text", "pub_date", "id")
    # Chercher par champs
    search_fields = ("question_text", "pub_date", "id")
    # fitrer les listes de question par date de modification
    list_filter = ["pub_date"]

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)