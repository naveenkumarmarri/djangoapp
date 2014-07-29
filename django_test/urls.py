from django.conf.urls import patterns, include, url
from article.views import HelloTemplate
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r"^admin/", include(admin.site.urls)),
    url(r"^articles/", include("article.urls")),
    url(r"^hello/$", "article.views.hello"),
    url(r"^hello_template/$", "article.views.hello_template"),
    url(r"^hello_template_class/$", HelloTemplate.as_view()),
    url(r"^hello_template_simple/$", "article.views.hello_template_simple"),
)
