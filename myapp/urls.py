from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='index'),
   path('registration/',views.StudentRegistration,name ='registration'),
   path('querry/',views.StudentQuerry,name = 'querry'),
   path('login/',views.StudentLogin,name = 'login'),
   path('profile/',views.StudentProfile,name = 'profile'),
   path('logout/',views.StudentLogout,name='logout'),
   path('<int:id>/',views.edit_query,name='edit'),
   path('delete/<int:id>/',views.delete_Query,name= 'delete',)
]
