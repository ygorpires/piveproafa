from django.urls import path
from .views import home, my_logout

urlpatterns = [
    path('', home,name='home'),
<<<<<<< Updated upstream
    path('logout',my_logout,name='logout'),
=======
    path('/logout',my_logout,name='logout'),
>>>>>>> Stashed changes
]