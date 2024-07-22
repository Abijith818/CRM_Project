from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    path('individualRecord/<int:pk>',views.individual_record, name='individualRecord'),
    path('individualRecordDelete/<int:pk>',views.delete_record, name='individualRecordDelete'),
    path('addRecord/',views.add_record, name='addRecord'),
    path('updateRecord/<int:pk>',views.update_record, name='updateRecord'),


]
