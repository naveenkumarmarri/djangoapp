from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from article.models import Article

# Create your views here.


def articles(request):
	language = 'en-us'
	session_language = 'en-us'
	if 'lang' in request.COOKIES:
		language = request.COOKIES['lang']
	if 'lang' in request.session:
		session_language = request.session['lang']	

	return render_to_response('articles.html',
								{'articles':Article.objects.all(),
								 'language' : language,
								  'session_language' : session_language})

def article(request, article_id=1):
	return render_to_response('article.html',
								{'article': Article.objects.get(id=article_id)})

def language(request,language='en-us'):
	response = HttpResponse("setting language to %s" % language)
	response.set_cookie('lang',language)
	request.session['lang'] = language
	return response


def hello(request):
	name = "naveen"
	html = "<html><body> hi this is %s, this seems to be worked " %name
	return HttpResponse(html)

def hello_template(request):
	name = 'naveen'
	t = get_template('hello.html')
	html = t.render(Context({'name' : name}))
	return HttpResponse(html)

def hello_template_simple(request):
	name = 'naveen'
	return render_to_response('hello.html', {'name' : name})

class HelloTemplate(TemplateView):
	
	template_name = 'hello_class.html'
	def get_context_data(self, **kwargs):
		context = super(HelloTemplate, self).get_context_data(**kwargs)
		context['name'] = 'naveen'
		return context  