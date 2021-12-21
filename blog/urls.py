
from django.urls import path
from blog.views import category, home, post
urlpatterns = [
    path('', home),
    path('blog/<slug:url>', post), path('category/<slug:url>', category)
]
