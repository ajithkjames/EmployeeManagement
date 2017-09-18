from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from account.forms import LoginForm
from rest_framework import routers

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('employee.urls', namespace='employee')),
    url(r'^api/', include('account.urls', namespace='account')),
    url(r'^$', views.login, {'template_name': 'login.html', 
	'authentication_form': LoginForm,
	'redirect_authenticated_user': True},name='login'),
    url(r'^logout', auth_views.logout, {'next_page': 'login'}),

]
