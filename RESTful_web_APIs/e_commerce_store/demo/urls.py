from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

import store.api_views
import store.views

urlpatterns = [
                  # connect the ListApiView to a route
                  # allows to sent get request and get back a JSON response
                  path('api/v1/products/', store.api_views.ProductList.as_view()),

                  # creating product through the ProductCreate APIView
                  path('api/v1/products/new', store.api_views.ProductCreate.as_view()),
                  # destroying the product
                  path('api/v1/products/<int:id>/destroy', store.api_views.ProductDestroy.as_view()),

                  path('admin/', admin.site.urls),
                  path('products/<int:id>/', store.views.show, name='show-product'),
                  path('cart/', store.views.cart, name='shopping-cart'),
                  path('', store.views.index, name='list-products'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
