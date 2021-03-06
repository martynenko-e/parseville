"""Main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from .views import (
    index
)

urlpatterns = [
    url(r'^$', index, name='ang_index'),
    #url(r'^$', index, name='index'),
    # url(r'^add-point/$', AddPoint.as_view(), name='add-point'),
]



    # url(r'^vacancies/', main.vacancies, name='vacancies'),
    # url(r'^companies/', main.companies, name='companies'),
    # url(r'^events/', main.events, name='events'),
    # url(r'^news/', main.news, name='news'),
    # url(r'^api/init/', api.api_init, name='api_init'),
    # url(r'^api/link/(?P<count>[\d]+)?/?', api.api_link, name='api_link'),
    #               url(r'^api/get/office/', api.api_get_offices, name='api_get_offices'),
    # url(r'^api/office/', api.api_offices, name='api_offices'),
    # url(r'^api/vacancy/(?P<count>[\d]+)?/?', api.api_vacancy, name='api_vacancy'),
    # url(r'^api/company/(?P<count>[\d]+)?/?', api.api_company, name='api_company'),
    # url(r'^api/event/(?P<count>[\d]+)?/?', api.api_event, name='api_event'),
    # url(r'^api/article/(?P<count>[\d]+)?/?', api.api_article, name='api_article'),
    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),