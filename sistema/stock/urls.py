from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    ##Login
    path('procesar_login/', views.procesar_login, name='login'),
    path('', RedirectView.as_view(url='procesar_login/', permanent=True)),

    ##Apertura caja
    path('apertura_caja/', views.apertura_caja, name='apertura_caja'),
    ##Cierre caja
    path("cierre_caja", views.cierre_caja, name="cierre_caja"),

    ##Inicio
    path('inicio/', views.inicio, name='inicio'),

    ##Cierre sesion
    path('logout/', LogoutView.as_view(next_page="login"), name='logout'),

    ##CRUD Articulos
    path('mostrar_articulos/', views.mostrar_articulos, name='mostrar_articulos'),
    path("editar_articulos", views.editar_articulos, name="editar_articulos"),
    path("editar_articulos/<int:id_prod>/", views.editar_articulos, name="editar_articulos"),
    path("crear_articulos", views.crear_articulos, name="crear_articulos"),
    path("eliminar_producto/<int:id_prod>",views.eliminar_productos, name="eliminar_producto"),

    ##CRUD Clientes
    path('mostrar_clientes/', views.mostrar_clientes, name='mostrar_clientes'),
    path("editar_clientes/",views.editar_clientes, name="editar_clientes"),
    path("editar_clientes/<int:id_cli>/",views.editar_clientes, name="editar_clientes"),
    path("crear_clientes", views.crear_clientes, name="crear_clientes"),
    ##Borrado_clientes
    path("eliminar_clientes/<int:id_cli>",views.eliminar_clientes, name="eliminar_clientes"),


    ##CRUD Proveedores
    path("mostrar_proveedores",views.mostrar_proveedores ,name="mostrar_proveedores"),
    path("editar_proveedores",views.editar_proveedores ,name="editar_proveedores"),
    path("editar_proveedores/<int:id_prov>",views.editar_proveedores ,name="editar_proveedores"),
    path("crear_proveedores",views.crear_proveedores ,name="crear_proveedores"),
    ##Borrado_proveedores
    path("eliminar_proveedores/<int:id_prov>",views.eliminar_proveedores, name="eliminar_proveedores" ),
    ##CRUD Empleados
    path("mostrar_empleados",views.mostrar_empleados, name="mostrar_empleados"),
    path("editar_empleados", views.editar_empleados, name="editar_empleados"),
    path("editar_empleados/<int:id_emplead>", views.editar_empleados, name="editar_empleados"),
    path("editar_empleados", views.editar_empleados, name="editar_empleados"),
    path("crear_empleados", views.crear_empleados, name="crear_empleados"),
    ##Borrado_empleados
    path("eliminar_empleados/<int:id_emplead>",views.eliminar_empleados, name="eliminar_empleados"),
    ##Compras
    path("mostrar_compras",views.mostrar_compras,name="mostrar_compras"),
    ##Ventas
    path("crear_venta",views.crear_venta, name="crear_venta"),
]