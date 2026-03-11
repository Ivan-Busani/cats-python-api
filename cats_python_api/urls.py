from django.urls import path
from cats_python_api.views import cat_views, utils_views

urlpatterns = [
    path('health', utils_views.health_check, name='health-check'),
    path('api/v1/cats/list', cat_views.cats_list, name='cats-list'),
    path('api/v1/cats/<int:id>', cat_views.cat_get_by_id, name='cat-get-by-id'),
    path('api/v1/cats/cat_id/<str:cat_id>', cat_views.cat_get_by_cat_id, name='cat-get-by-cat-id'),
    path('api/v1/cats/save', cat_views.cat_save, name='cat-save'),
    path('api/v1/cats/update/<int:id>', cat_views.cat_update, name='cat-update'),
    path('api/v1/cats/delete/<int:id>', cat_views.cat_delete, name='cat-delete'),
]