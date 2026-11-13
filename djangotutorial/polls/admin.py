from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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

# Formulaire personnalisé pour la création d'un utilisateur dans l'admin (avec gestion du hash du mot de passe)
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

# Formulaire personnalisé pour la modification d'un utilisateur dans l'admin
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')

# Configuration de l'interface d'administration
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    filter_horizontal = ('groups', 'user_permissions',)

    # Organisation des champs dans la page de modification d'un utilisateur
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name')}),
        ('Permissions et rôles', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates importantes', {'fields': ('last_login',)})
    )

    # Organisation des champs dans la page de création d'un utilisateur
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_superuser')}
         ),
    )

    admin.site.register(Choice)