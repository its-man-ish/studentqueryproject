from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('registration/',views.StudentRegistration,name ='registration'),
   path('querry/',views.StudentQuerry,name = 'querry'),
   path('login/',views.StudentLogin,name = 'login'),
   path('logout/',views.StudentLogout,name='logout'),
   path('dashboard/',views.dashboard,name='dashboard'),
   path('<int:id>/',views.edit_query,name='edit'),
   path('delete/<int:id>/',views.delete_Query,name= 'delete'),
]
