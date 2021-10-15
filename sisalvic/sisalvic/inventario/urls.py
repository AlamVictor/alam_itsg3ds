from django.contrib import admin
from django.urls import path
from . import views
from . views import grupolistar,grupoguardar,hello_pdf,grupomodificar
from . views import clientelistar,clienteguardar,clientemodificar
from . views import productolistar,productoguardar,productomodificar
from . views import proveedorlistar, proveedorguardar, proveedormodificar

urlpatterns = [

    path('grupolistar', views.grupolistar.as_view() ,name='grupolistar'),
    path('grupoguardar', views.grupoguardar.as_view() , name='grupoguardar'),
    path('grupomodificar/<int:pk>', views.grupomodificar.as_view(), name='grupomodificar'),
    path('holapdf',views.hello_pdf,name='holapdf'),
    path('grupospdf', views.grupo_print, name='grupospdf'),
    path('grupoindividual/<int:pk>', views.grupo_print, name='grupoindividual'),
    ##############################   CLIENTE  ################################
    path('clientelistar', views.clientelistar.as_view() ,name='clientelistar'),
    path('clienteguardar', views.clienteguardar.as_view() , name='clienteguardar'),
    path('clientemodificar/<int:pk>', views.clientemodificar.as_view(), name='clientemodificar'),
    path('clientespdf', views.cliente_print, name='clientespdf'),
    path('clienteimprimir/<int:pk>', views.cliente_print, name='clienteimprimir'),
    ##############################   PROVEEDOR   ################################
    path('proveedorlistar', views.proveedorlistar.as_view(), name='proveedorlistar'),
    path('proveedorguardar', views.proveedorguardar.as_view(), name='proveedorguardar'),
    path('proveedormodificar/<int:pk>', views.proveedormodificar.as_view(), name='proveedormodificar'),
    path('proveedorimprimir/<int:pk>', views.proveedor_print, name='proveedorimprimir'),
    path('proveedorpdf', views.proveedor_print, name='proveedorpdf'),
    ################################   PRODUCTO  #############################
    path('productolistar', views.productolistar.as_view(), name='productolistar'),
    path('productoguardar', views.productoguardar.as_view(), name='productoguardar'),
    path('productomodificar/<int:pk>', views.productomodificar.as_view(), name='productomodificar'),
    path('productoimprimir/<int:pk>', views.producto_print, name='productoimprimir'),
    path('productopdf', views.producto_print, name='productopdf'),


]

