from django.db.models import F, Sum, Max
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.generic import TemplateView
from django.core.mail import send_mail


from .utils import minimax
from .forms import NameForm
from .models import Choice, Question

NB_MAX_CHOIX = 5

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


class AllView(IndexView):
    template_name = "polls/all.html"

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
    })

def add(request):
    return render(request, 'polls/add.html', {
        'liste_no_choix': range(NB_MAX_CHOIX)
    })

def confirm_add(request):
    question_text = request.POST.get('question_text', '').strip()
    if question_text:
        question = Question(question_text=question_text, pub_date=timezone.now())
        question.save()
        for no_choix in range(NB_MAX_CHOIX):
            nom_champ = 'choix_{}'.format(no_choix)
            choice_text = request.POST.get(nom_champ, '').strip()
            if choice_text:
                choice = Choice(question=question, choice_text=choice_text)
                choice.save()
            else:
                break
        return render(request, 'polls/confirm_add.html')
    else:
        return render(request, 'polls/add.html', {
            'error_message': "You didn't enter a question text",
            'liste_no_choix': range(NB_MAX_CHOIX)
        })

def get_name(request):
  # Si c'est un POST, on passe les données. Si c'est un GET, request.POST est vide donc vaut None (formulaire vide)
  form = NameForm(request.POST or None)

  # Si la méthode est POST et que le formulaire est valide
  if request.method == "POST" and form.is_valid():
    name = form.cleaned_data["your_name"]
    request.session["submitted_name"] = name
    return HttpResponseRedirect("/polls/thanks/")

  # Dans tous les autres cas (GET initial ou POST invalide), on affiche le formulaire
  return render(request, "polls/name.html", {"form": form})


def thanks_view(request):
    # On récupère le nom depuis la session (avec une valeur par défaut si vide)
    name = request.session.get("submitted_name", "invité")

    return render(request, "polls/thanks.html", {"name": name})

