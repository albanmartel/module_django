from django.db.models import F, Sum, Max
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from django.db import transaction
from django.views.generic import TemplateView
from django.core.mail import send_mail

from .utils import minimax
from .forms import NameForm, QuestionAddForm, VoteForm, QuestionForm, ChoiceFormSet, InscriptionForm, PasswordForm
from .models import Choice, Question, CustomUser

NB_MAX_CHOIX = 5
User = get_user_model()

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

    def get_context_data(self, **kwargs):
        # récupération du contexte qui contient  "latest_question_list"
        context = super().get_context_data(**kwargs)
        # Ajout d'une variable pour le titre
        context["title"] = "Application de sondages"

        return context


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

    def get_context_data(self, **kwargs):
        # 1. Récupérer le contexte existant (qui contient déjà 'question')
        context = super().get_context_data(**kwargs)

        # 2. Ajouter votre variable de titre personnalisée
        context['title'] = "Vote for a question"

        # (Optionnel) Si vous voulez aussi passer le formulaire initialisé dans la DetailView en GET
        # choices_form = [(choice.id, choice.choice_text) for choice in self.object.choice_set.all()]
        # context['form'] = VoteForm(self.object.question_text, choices_form)

        return context

    def vote(request, question_id):
        question = get_object_or_404(Question, pk=question_id)

        choices_form = [(choice.id, choice.choice_text)
                        for choice in question.choice_set.all()]
        if request.method == 'POST':
            form = VoteForm(question.question_text, choices_form, request.POST)
            if form.is_valid():
                selected_choice = question.choice_set.get(pk=form.cleaned_data['choice'])
                selected_choice.votes += 1
                selected_choice.save()
                return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
            return None
        else:
            form = VoteForm(question.question_text, choices_form)
            # En cas d'erreur de formulaire,
            # le template en incluant aussi le titre pour garder la cohérence
            return render(request, 'polls/detail.html', {
                'form': form,
                'question': question,
                'title': f"Sondage : {question.question_text}"
            })


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


class AllView(IndexView):
    template_name = "polls/all.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "All polls"
        return context

    def get_queryset(self):
        """Return all published questions."""
        return Question.objects.order_by("-pub_date")


class FrequencyView(generic.DetailView):
    model = Question
    template_name = "polls/frequency.html"
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["frequencies"] = self.object.get_choices()

        return context


def statistics(request):
    nbr_sondages = Question.objects.count()
    nbr_choix = Choice.objects.count()
    nbr_votes = Choice.objects.aggregate(somme=Sum('votes'))['somme'] or 0
    moyenne_par_sondage = nbr_votes / nbr_sondages if nbr_sondages > 0 else 0

    question_la_moins_populaire, question_la_plus_populaire = minimax() if nbr_sondages > 0 else (None, None)

    id_derniere_question = Question.objects.aggregate(max=Max('id'))['max']
    derniere_question = Question.objects.get(pk=id_derniere_question) if id_derniere_question else None

    return render(request, 'polls/statistics.html', {
        'nbr_sondages': nbr_sondages,
        'nbr_choix': nbr_choix,
        'nbr_votes': nbr_votes,
        'moyenne_par_sondage': moyenne_par_sondage,
        'question_la_plus_populaire': question_la_plus_populaire,
        'question_la_moins_populaire': question_la_moins_populaire,
        'derniere_question': derniere_question,
        'title': "Statistics",
    })


def add(request):

    if request.method == 'POST':
        form = QuestionAddForm(request.POST)
        if form.is_valid():
            question = \
                Question(question_text= \
                             form.cleaned_data['question_text'],
                         pub_date=timezone.now())
            question.save()
            # on traite à présent les champs de choix remplis
            # (on s'arrête au premier vide)
            for no_choix in range(NB_MAX_CHOIX):
                nom_champ = 'choice_{}'.format(no_choix)
                choice_text = form.cleaned_data[nom_champ].strip()
                if choice_text:
                    choice = Choice(question=question,
                                    choice_text=choice_text)
                    choice.save()
                else:
                    break
            return HttpResponseRedirect(reverse("polls:index"))
    else:
        form = QuestionAddForm()

    # Définition du contexte avec le formulaire ET le titre
    context = {
        'form': form,
        'title': "Add a question",  # <-- Votre variable accessible via {{ title }} dans le HTML
    }

    return render(request, 'polls/add.html', context)


def get_name(request):
    # Si c'est un POST, on passe les données. Si c'est un GET, request.POST est vide donc vaut None (formulaire vide)
    form = NameForm(request.POST or None)

    # Si la méthode est POST et que le formulaire est valide
    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data["your_name"]
        request.session["submitted_name"] = name
        return HttpResponseRedirect("/polls/thanks/")

    # Dans tous les autres cas (GET initial ou POST invalide), on affiche le formulaire
    return render(request, "polls/name.html", {
        "form": form,
        "title": "Get Name",
    })


def thanks_view(request):
    # On récupère le nom depuis la session (avec une valeur par défaut si vide)
    name = request.session.get("submitted_name", "invité")

    return render(request, "polls/thanks.html", {
        "name": name,
        'title': "Thanks",
    })


class AuthenticateView(LoginView):
    template_name = "polls/authenticate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Log in"
        return context

@login_required(login_url="polls:login")
def get_question(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        form_choices = ChoiceFormSet(request.POST)

        if form.is_valid() and form_choices.is_valid():
            choices = [
                choice_form.save(commit=False)
                for choice_form in form_choices
                if choice_form.cleaned_data
                and choice_form.cleaned_data.get("choice_text", "").strip()
            ]

            if not choices:
                form_choices._non_form_errors = form_choices.error_class(
                    ["Saisissez au moins une réponse."]
                )
            else:
                with transaction.atomic():
                    question = form.save(commit=False)
                    question.pub_date = timezone.now()
                    question.save()

                    for choice in choices:
                        choice.question = question
                        choice.votes = 0
                        choice.save()

                return redirect("polls:index")

    else:
        form = QuestionForm()
        form_choices = ChoiceFormSet()

    return render(
        request,
        "polls/add.html",
        {
            "form": form,
            "form_choices": form_choices,
        }
    )
@user_passes_test(lambda user: user.is_authenticated and user.is_staff)
def change_question(request, pk):

    question = get_object_or_404(Question, pk=pk)
    choix = list(question.choice_set.all())

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        form_choices = ChoiceFormSet(request.POST)

        if form.is_valid() and form_choices.is_valid():

            nouvelles_reponses = [
                choice_form.cleaned_data["choice_text"].strip()
                for choice_form in form_choices
                if choice_form.cleaned_data
                and choice_form.cleaned_data.get("choice_text", "").strip()
                and not choice_form.cleaned_data.get("DELETE", False)
            ]

            if not nouvelles_reponses:
                form_choices._non_form_errors = form_choices.error_class(
                    ["Saisissez au moins une réponse."]
                )

            else:
                with transaction.atomic():

                    form.save()

                    for i, texte in enumerate(nouvelles_reponses):

                        if i < len(choix):
                            choice = choix[i]
                            choice.choice_text = texte
                            choice.save()
                        else:
                            Choice.objects.create(
                                question=question,
                                choice_text=texte,
                                votes=0
                            )

                    for choice in choix[len(nouvelles_reponses):]:
                        choice.delete()

                return redirect("polls:detail", pk=question.pk)

    else:
        form = QuestionForm(instance=question)

        form_choices = ChoiceFormSet(
            initial=[
                {"choice_text": choice.choice_text}
                for choice in choix
            ]
        )

    return render(
        request,
        "polls/change_question.html",
        {
            "form": form,
            "form_choices": form_choices,
            "question": question,
        }
    )

def register(request):
    if request.method == "POST":
        form = InscriptionForm(request.POST)

        if form.is_valid():
            utilisateur = form.save()
            return redirect("polls:login")
    else:
        form = InscriptionForm()

    return render(
        request,
        "polls/register.html",
        {"form": form}
    )

class UserView(generic.DetailView):
    model = User
    template_name = "polls/account.html"
    context_object_name = "customuser"

class ChangePasswordView(PasswordChangeView):
    template_name = "polls/change_password.html"
    form_class = PasswordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Change password"
        return context

    # On remplace l'attribut statique success_url par cette méthode dynamique
    def get_success_url(self):
        # self.request.user contient l'utilisateur actuellement connecté
        # On récupère sa clé primaire (pk) pour l'injecter dynamiquement dans l'URL
        return reverse_lazy("polls:account", kwargs={'pk': self.request.user.pk})