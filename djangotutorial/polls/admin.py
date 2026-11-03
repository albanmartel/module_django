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


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)