from django.urls import reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalLoginView
from .form import CustomUserCreationForm, CustomAuthenticationForm
import csv
from django.http import HttpResponse
from main.models import Tour

class CustomLoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'
    success_message = 'Вход выполнен'
    extra_context = dict(success_url=reverse_lazy('tour_cat'))

class SignUpView(BSModalCreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_message = 'Успешная регистрация.'
    success_url = reverse_lazy('login')


def csvD(request):

    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="tour.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['id', 'title', 'description', 'type', 'guide', 'group', 'price','duration'])
    for t in Tour.objects.all().values_list('id', 'title', 'description', 'type', 'guide', 'group', 'price','duration'):
        writer.writerow(t)

    return response
