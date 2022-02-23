from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_chain/', views.get_chain),
    path('mine_block/', views.mine_block),
    path('is_chain_valid/', views.is_chain_valid),
    path('temper_blockchain/', views.temper_blockchain),
]
