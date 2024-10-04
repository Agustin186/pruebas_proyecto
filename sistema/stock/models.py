# stock/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Proveedores(models.Model):
    id_prov = models.AutoField(primary_key=True)
    nombre_prov = models.CharField(max_length=100, verbose_name="nombre del proveedor", null=False, blank=True)
    cuit_prov = models.CharField(max_length=100 ,verbose_name="cuit del proveedor",null=True, blank=True)
    tipo_prov = models.CharField(max_length=100,verbose_name="tipo de proveedor", null=True, blank=True)
    direcc_prov = models.CharField(max_length=100,verbose_name="direccion del proveedor", null=False)
    tel_prov = models.CharField(max_length=50,verbose_name="telefono del proveedor", null=True, blank=True)
    correo_prov = models.EmailField(max_length=100,verbose_name="email del proveedor", null=True, blank=True)

    def __str__(self):
        return self.nombre_prov
    
class Clientes(models.Model):
    id_cli=models.AutoField(primary_key=True)
    nombre_cli=models.CharField(max_length=100, verbose_name="Nombre del cliente",null=False)
    apellido_cli=models.CharField(max_length=100, verbose_name="Apellido del cliente", null=False)
    cuit_cli=models.CharField(max_length=100 ,verbose_name="cuit-dni del cliente", null=False)
    direcc_cli=models.CharField(max_length=100, verbose_name="Direccion del cliente", null=True, blank=True)
    tel_cli=models.CharField(max_length=50, verbose_name="Telefono del cliente", null=True, blank=True) 

    def __str__(self):
        return self.nombre_cli
    

class Empleados(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='empleado', null=True, blank=True)
    id_emplead = models.AutoField(primary_key=True)
    nombre_emplead = models.CharField(max_length=100, verbose_name="Nombre del empleado", null=False)
    apellido_emplead = models.CharField(max_length=100, verbose_name="Apellido del empleado", null=False)
    dni_emplead = models.CharField(max_length=100, verbose_name="DNI del empleado", null=False)
    direcc_emplead = models.CharField(max_length=100, verbose_name="Dirección del empleado", null=True, blank=True)
    tel_emplead = models.CharField(max_length=50, verbose_name="Teléfono del empleado", null=True, blank=True)
    correo_emplead = models.EmailField(max_length=100, verbose_name="Email del empleado", null=True, blank=True)
    sueldo_emplead = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Sueldo del empleado", null=True, blank=True)
    fecha_inicio = models.DateField(verbose_name="Fecha de inicio", null=False)
    fecha_fin = models.DateField(verbose_name="Fecha de finalización", null=True, blank=True)

    def delete(self, *args, **kwargs):
        # Si el empleado tiene un usuario asociado, eliminarlo también
        if self.user:
            self.user.delete()
        super().delete(*args, **kwargs)
        
    def __str__(self):
        return f"{self.nombre_emplead} {self.apellido_emplead}"


class Productos(models.Model):
    id_prod= models.AutoField(primary_key=True)
    id_prov=models.ForeignKey(Proveedores, on_delete=models.SET_NULL, null=True, blank=True, related_name="productos")
    nombre_prod=models.CharField(max_length=100, verbose_name="Nombre del Articulo", null=False)
    precio_prod=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio", null=False)
    stock_min=models.IntegerField(null=True, blank=True)
    stock_max=models.IntegerField(null=True, blank=True)
    stock_actual=models.IntegerField(null=True,blank=True)
    punto_reposicion=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.nombre_prod
    
class Cajas(models.Model):
    id_caja=models.AutoField(primary_key=True, verbose_name="caja")
    id_emplead=models.ForeignKey(Empleados,on_delete=models.SET_NULL, null= True, related_name="cajas")
    fecha_hs_apertura=models.DateTimeField(verbose_name="Fecha y hora de apertura", null=False)
    fecha_hs_cierre=models.DateTimeField(verbose_name="Fecha y hora de cierre", null=False)
    saldo_caja=models.DecimalField(max_digits=10, decimal_places=2,verbose_name="Saldo", null=True, blank=True)
    monto_inicial=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Monto inicial", null=True, blank=True)
    total_ingreso=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ingreso total del dia", null=False)
    total_egreso=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Gastos del dia", null=True, blank=True)
    abierto_caja=models.BooleanField(default=False)
    def __str__(self):
        return f"compra: {self.id_caja}"

     
class Compras(models.Model):
    id_compra=models.AutoField(primary_key=True)
    id_prov=models.ForeignKey(Proveedores, on_delete=models.SET_NULL, null=True, blank=True, related_name="compras")
    id_caja=models.ForeignKey(Cajas, on_delete=models.SET_NULL, null=True, blank=True, related_name="compras")
    fecha_compra=models.DateField(verbose_name="Fecha de compra", null=False)
    total_compra=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total de la compra", null=False)
    descrip_compra=models.CharField(max_length=150, verbose_name="Agregue un comentario", null=True, blank=True)

    def __str__(self):
        return f"Compra: {self.id_compra}"
    
class det_compras(models.Model):
    id_det_compra=models.AutoField(primary_key=True)
    id_compra=models.ForeignKey(Compras, on_delete=models.SET_NULL, null=True, blank=True, related_name="det_compras")
    id_prod=models.ForeignKey(Productos, on_delete=models.SET_NULL, null=True, blank=True, related_name="det_compras")
    cant_comprada=models.IntegerField(verbose_name="Cantidad unitaria", null=False)
    precio_unitario=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio", null=False)
    subtotal_compra=models.DecimalField(max_digits=10, decimal_places=2, null=False)
    
    def __str__(self):
        return f"det_venta: {self.id_det_compra}"


class Ventas(models.Model):
    id_venta=models.AutoField(primary_key=True)
    id_caja=models.ForeignKey(Cajas, on_delete=models.SET_NULL, null=True, related_name="ventas")
    id_cli=models.ForeignKey(Clientes, on_delete=models.SET_NULL, null=True, related_name="ventas")
    fecha_hs=models.DateTimeField(null=False)
    total_venta=models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total de la venta",null=False)

    def __str__(self):
        return f"Venta: {self.id_venta}"

class det_ventas(models.Model):
    id_det_venta=models.AutoField(primary_key=True)
    id_prod=models.ForeignKey(Productos, on_delete=models.SET_NULL,null= True, blank=True, related_name="det_ventas" )
    id_venta=models.ForeignKey(Ventas, on_delete=models.SET_NULL, null=True, blank=True, related_name="det_ventas")
    precio_prod=models.DecimalField(max_digits=10, decimal_places=2,null=False, verbose_name="Precio")
    subtotal_venta=models.DecimalField(max_digits=10, decimal_places=2, null=False, verbose_name="Subtotal")
    cant_vendida=models.IntegerField(null=False, verbose_name="Cantidad")

    def __str__(self):
        return f"det_venta: {self.id_det_venta}"
    
