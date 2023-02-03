from django.urls import path, include
from rest_framework_nested import routers
from . import views
from pprint import pprint

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='product')
router.register('collections', views.CollectionViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

urlpatterns = router.urls + products_router.urls

pprint(router.urls)
# if you have specific urls other than the ones coming from the router u can
# include the router urls and the rest like below

# urlpatterns = [
# path('', include(router.urls))
#     other url patterns
# ]
