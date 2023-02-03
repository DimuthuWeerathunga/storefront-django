from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from pprint import pprint

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
pprint(router.urls)

urlpatterns = router.urls

# if you have specific urls other than the ones coming from the router u can
# include the router urls and the rest like below

# urlpatterns = [
# path('', include(router.urls))
#     other url patterns
# ]
