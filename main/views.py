from .models import Tour, Rating, Order, Guide, Views
from django.shortcuts import render, get_object_or_404, redirect, reverse
from .recommender import get_recommend, get_sim, get_sviews
from bootstrap_modal_forms.generic import BSModalCreateView
from django.urls import reverse_lazy
from .form import OrderModelForm
from django.http import HttpResponseRedirect


def mainpage(req):
    return render(req, 'main/mainpage.html')


def tour_cat(req):
    tours = Tour.objects.all().order_by('-view')

    context = {'tours': tours}
    return render(req, 'main/tour_cat.html', context)


def tour_detail(request, slug, id):
    tour = get_object_or_404(Tour, slug=slug, id=id)

    tour.view = tour.view + 1
    tour.rating = tour.get_rating()
    tour.save()

    if (len(Views.objects.all().values().filter(user=request.user, tour=tour)) == 0):
        Views.objects.create(tour=tour, user=request.user)

    if request.user.is_authenticated:
        if (len(Order.objects.filter(tour=tour, user=request.user))>0):
            update=True
        else:
            update=False

        if request.POST:
            stars=request.POST.get('stars')
            if Rating.objects.all().values().filter(tour=tour, user=request.user):
                Rating.objects.all().values().filter(tour=tour, user=request.user).update(rating=stars)
            else:
                Rating.objects.create(tour=tour, user=request.user, rating=stars)

            return redirect('tourpage', slug=slug, id=id)

        if (len(Rating.objects.filter(user=request.user)) == 0):
            if (len(Views.objects.filter(user=request.user)) > 1):
                tour_list = get_sviews(tour.id, request)
                #tour_list = get_sim(tour.id, 3)
            else:
                tour_list = get_sim(tour.id, 3)
        else:
            tour_list = get_recommend(request, tour.id)

        context = {'tour': tour, 'tour_list': tour_list, 'update': update}

        return render(request, 'main/tourpage.html', context)
    else:
        return render(request, 'main/tourpage.html', {'tour': tour})


class OrderCreateView(BSModalCreateView):
    template_name = 'main/order.html'
    form_class = OrderModelForm
    success_message = 'Ваш запрос отправлен'
    model = Tour

    def form_valid(self, form):

        update=True
        i=self.kwargs['id']
        param=Tour.objects.get(id=i)
        form.instance.user = self.request.user
        form.instance.tour = param
        form.instance.order=update
        return super().form_valid(form)

    def get_success_url(self, **kwargs):

        i = self.kwargs['id']
        sl=Tour.objects.values('slug').get(id=i)
        slug=str(sl.pop('slug'))

        return reverse('tourpage', kwargs={'slug':slug, 'id':i})



def guide_detail(request, id):
    guide = get_object_or_404(Guide, id=id)
    context = {'guide': guide}
    return render(request, 'main/guide.html', context)
