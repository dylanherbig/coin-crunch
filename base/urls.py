from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('configuration/', views.configuration, name='configuration'),
    path('balances/', views.balances, name='balances'),
    path('create/', views.createWallet, name='createUser'),
    path('user-wallet/', views.getUserWallet, name='getUserWallet'),
    path('create-blockchain-address/', views.createBlockchainAddress, name='createBlockchainAddress'),
    path(r'', views.default_map, name="default"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
