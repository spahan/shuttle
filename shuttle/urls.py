from django.urls import path

from . import views

app_name = 'shuttle'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:shuttle_id>', views.detail, name="detail"),
    path('<int:shuttle_id>/add', views.add_passenger, name="add"),
    path('<int:shuttle_id>/remove/<token>', views.remove_passenger, name="remove"),
    path('<int:shuttle_id>/driver/<int:driver_id>', views.add_driver, name="driver"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]
