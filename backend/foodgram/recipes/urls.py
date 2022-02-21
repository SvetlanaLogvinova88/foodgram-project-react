from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router1 = DefaultRouter()

router1.register('tags', views.TagViewset, basename='tag')
router1.register('ingredients', views.IngredientViewset, basename='ingredient')
router1.register('recipes', views.RecipeViewset, basename='recipe')

urlpatterns = [
    path('', include(router1.urls))
]
