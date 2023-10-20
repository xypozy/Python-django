from django.http import HttpResponse
from django.template import loader
from .models import Article
def index(request):
    article = Article.objects.order_by('title')
    template = loader.get_template('index.html')
    context = {
        'article': article,
    }
    return HttpResponse(template.render(context, request))
def myNextPage(request):
    return HttpResponse("<b>To jest moja następna strona!</b>")