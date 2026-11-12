from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import path, include

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="vote"),
    # ex: /polls/5/results/
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.DetailView.vote, name="vote"),
    # ex /polls/all
    path("all/", views.AllView.as_view(), name="all"),
    # ex /polls/1/frequency
    path("<int:pk>/frequency", views.FrequencyView.as_view(), name="frequency"),
    # ex /polls/statistics
    path('statistics/', views.statistics, name='statistics'),
    # ex /polls/add
    path('add/', views.add, name='add'),
    # ex /polls/contacts
    path('contact/', views.get_name, name='get_name'),
    # ex /polls/thanks
    path("thanks/", views.thanks_view, name="thanks"),

]