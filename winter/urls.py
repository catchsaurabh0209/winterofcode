from django.conf.urls import url
from . import views


urlpatterns =[
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^register_org/$', views.register_org, name='register_org'),
	url(r'^register_stu/$', views.register_stu, name='register_stu'),
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	url(r'^dashboard_stu/$', views.dash_stu, name='dash_stu'),
	url(r'^dashboard_org/$', views.dash_org, name='dash_org'),


]