from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import IngredientViewSet, RecipeViewSet, TagViewSet

router_v1 = SimpleRouter()

router_v1.register('tags', TagViewSet, basename='tags')
router_v1.register('ingredients', IngredientViewSet, basename='indegrients')
router_v1.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('api/', include(router_v1.urls)),
]
