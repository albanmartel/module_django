from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Page d'accueil racine qui pointe vers un fichier home.html
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # Chemin /home/ explicitement autorisé (http://127.0.0.1:8000/home/)
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),

    # Panneau d'administration
    path('admin/', admin.site.urls),

    # Vos routes pour polls
    path('polls/', include('polls.urls')),
]


# Inclure les urls django-debug-toolbar
if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns