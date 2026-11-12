from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Question, Choice, CustomUser

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = "pub_date"
    # Trier de la plus récente à la plus ancienne
    ordering = ["-pub_date"]
    # Afficher les champs suivants de la liste
    list_display = ("question_text", "pub_date", "id")
    # Filtrer La liste des questions par les critères texte de la question, date de la question puis sont id
    list_filter = ("question_text", "pub_date", "id")
    # Chercher par champs
    search_fields = ("question_text", "pub_date", "id")
    # fitrer les listes de question par date de modification
    list_filter = ["pub_date"]
    # Partager le formulaire d'administration des questions de sondages en plusieurs petits sous-ensembles.
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]


# Enregistrement indispensable de votre CustomUser pour le voir dans l'admin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('email',)

    filter_horizontal = ('groups', 'user_permissions',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_superuser')}
         ),
    )

    admin.site.register(Choice)