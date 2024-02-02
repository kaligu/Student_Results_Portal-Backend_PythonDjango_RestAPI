from django.urls import path
from school import views

urlpatterns = [
    path('get-all/', views.get_all_schools, name='school_get_all'),
    path('add-school/', views.add_school, name='add_school')
]