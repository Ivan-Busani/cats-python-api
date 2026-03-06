from django.urls import path
from cats_python_api.views import cat_views, utils_views

urlpatterns = [
    path('health/', utils_views.health_check, name='health-check'),
    path('api/v1/cats/list/', cat_views.cats_list, name='cats-list'),
    path('api/v1/cats/save/', cat_views.cat_save, name='cat-save'),
]