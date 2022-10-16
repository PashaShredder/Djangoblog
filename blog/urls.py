from django.urls import path
from blog.views import hi_shredder

urlpatterns = [
    path('hi-shredder/', hi_shredder),
]
