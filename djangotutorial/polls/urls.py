from debug_toolbar.toolbar import debug_toolbar_urls
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
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
    path('contact/', views.get_name, name='contact'),
    # ex /polls/thanks
    path("thanks/", views.thanks_view, name="thanks"),
    # ex /polls/authenticate
    path("authenticate/", views.AuthenticateView.as_view(), name="authenticate"),
    # ex /polls/login
    path("login/", LoginView.as_view(template_name = "polls/login.html", next_page = "polls:index"), name = "login"),
    # ex /polls/logout
    path("logout/", LogoutView.as_view(next_page="polls:index"), name="logout"),
    # ex /polls/register
    path("register/", views.register, name="register"),
    # ex /polls/account/1
    path("account/<int:pk>/", views.UserView.as_view(), name="account"),
    # ex /polls/change_question/1
    path("change_question/<int:pk>/", views.change_question, name="change_question"),
    # ex /polls/password
    path("password/", views.ChangePasswordView.as_view(), name="change_password"),
]