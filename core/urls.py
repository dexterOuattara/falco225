from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('course', views.course, name='course'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('upload', views.upload, name='upload'),
    path('uploadCourse', views.upload, name='uploadCourse'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('home', views.home, name='home'),
    path('faq', views.faq, name='faq'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('classroom', views.classroom, name='classroom'),
    path('listclassroom', views.listclassroom, name='listclassroom'),
    path('student', views.student, name='student'),
    path('revenus', views.revenus, name='revenus'),
    path('add_class', views.add_class, name='add_class'),
    path('video_call', views.video_call, name='video_call'),
    path('profile2', views.profile2, name='profile2'),
    path('services', views.services, name='services'),
    path('contact-us', views.contact, name='contact-us'),
    path('callvideo', views.callvideo, name='callvideo'),
]
