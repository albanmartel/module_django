from django import forms
from django.forms import ModelForm, Textarea, formset_factory
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from .models import Question, Choice
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User

NB_MAX_CHOIX = 5

User = get_user_model()

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class QuestionAddForm(forms.Form):
    question_text = forms.CharField(label='Question text')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for i in range(NB_MAX_CHOIX):
            self.fields[f"choice_{i}"] = forms.CharField(
                label=f"Choice #{i + 1}",
                max_length=200,
                required=False
            )


class VoteForm(forms.Form):

    def __init__(self, question_text, choices, *args, **kwargs):
        super(VoteForm, self).__init__(*args, **kwargs)
        self.fields['choice'] = \
            forms.ChoiceField(label=question_text,
                              widget=forms.RadioSelect,
                              choices=choices)

class AuthenticateView(LoginView):
    template_name = "polls/authenticate.html"

    def get_context_data(self, **kwargs):
        # On récupère le contexte de base (qui contient déjà le formulaire de connexion prêt à l'emploi)
        context = super().get_context_data(**kwargs)
        # On ajoute juste votre titre personnalisé
        context['title'] = "Log in"
        return context

class QuestionForm(ModelForm):
    template_name = "polls/form.html"

    class Meta:
        model = Question
        fields = ["question_text"]
        widgets = {
            "question_text": Textarea(attrs={"cols": 80, "rows": 3}),
        }
        help_texts = {
            "question_text": "Intitulé de la question"
        }

class ChoiceForm(ModelForm):
    template_name = "polls/form.html"

    class Meta:
        model = Choice
        fields = ["choice_text"]
        widgets = {
            "choice_text": Textarea(attrs={"cols": 80, "rows": 2}),
        }


ChoiceFormSet = formset_factory(
    ChoiceForm,
    extra=5,
    max_num=5,
    validate_max=True
)

class InscriptionForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["email", "first_name", "last_name"]

class PasswordForm(PasswordChangeForm):
    pass