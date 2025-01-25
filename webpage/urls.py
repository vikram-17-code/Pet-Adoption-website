from django.urls import path
from . import views

urlpatterns = [
   path('',views.home, name="home"),
   path('About/',views.About, name="About"),
   path('login/',views.login_user,name="login"),
   path('logout/',views.logout_user,name="logout"),
   path('register/',views.register, name="register"),
   path('profile/',views.profile, name="profile"),
   path('update_user/',views.update_user, name="update_user"),
   path('change_password/',views.change_password, name="change_password"),
   path('user_info/',views.user_info, name="user_info"),
   path('staff_login/',views.staff_login, name="staff_login"),
   path('add_pet/',views.add_pet, name="add_pet"),
   path('add_breed/', views.add_breed, name='add_breed'),
   path('pet/<int:pk>',views.Pet_detail, name="petP"),
   path('breed/<str:bre>',views.breed_detail, name="breed_Page"),
   path('manage_pets',views.manage_pets, name="manage_pets"),
   path('update_pet/<int:pk>/', views.update_pet, name="update_pet"),
   path('manage_breeds/', views.manage_breeds, name='manage_breeds'),
   path('update_breed/<int:pk>/', views.update_breed, name='update_breed'),
   path('delete_breed/<int:pk>/', views.delete_breed, name='delete_breed'),
   path('breed_recommendation/',views.breed_recommendation, name="breed_recommendation"),
   path('adopt_pet/<int:pk>/',views.adopt_pet, name="adopt_pet"),
   path('manage_adoptions/', views.manage_adoptions, name='manage_adoptions'),
   path('my_adopted_pets/', views.user_adopted_pets, name='user_adopted_pets'),
   path('staff_home/', views.staff_home, name='staff_home'),
   path('payment/', views.payment, name='payment'),
   path('search/', views.search_pets, name='search_pets'),
   path('generate_report/', views.generate_report, name='generate_report'),
   

]