from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#old version of home (using functions)
# def home(request):
#     return render(request, 'rostering/home.html')
#     #old version
#     #return HttpResponse("Hello, world. You're at the polls index.")


class HomePageView(generic.TemplateView):

    template_name = "rostering/home.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['latest_articles'] = Article.objects.all()[:5]
    #     return context