from django.db import models


# Create your models here.

class grupo(models.Model):
    gruponombre = models.CharField(max_length=150)
    Estado = (
        ('1','Activo'),
        ('0', 'No Activo'),
    )
    grupoanulado = models.CharField(max_length=1,choices=Estado,help_text="Seleccione el Estado",default='1')

    def __str__(self):
        return '{}'.format(self.gruponombre)


class producto(models.Model):

    productogrupo = models.ForeignKey(grupo, on_delete=models.CASCADE,related_name="productogrupo_p")
    productonombre = models.CharField(max_length=150)
    productopreciovta = models.FloatField()
    productocodigo = models.CharField(max_length=50)
    productoexistencia = models.IntegerField()
    Estado = (
        ('1', 'Activo'),
        ('0', 'No Activo'),
    )
    productoanulado = models.CharField(max_length=1,choices=Estado,help_text="Seleccione el Estado",default='1')

    def __str__(self):
        return '{}'.format(self.productogrupo)


class proveedor(models.Model):
    proveedorcedula = models.CharField(max_length=13)
    proveedornombre = models.CharField(max_length=150)
    Estado = (
        ('1', 'Activo'),
        ('0', 'No Activo'),
    )
    proveedortelefono = models.CharField(max_length=50)
    proveedoranulado = models.CharField(max_length=1,choices=Estado,help_text="Seleccione el Estado",default='1')

    def __str__(self):
        return self.proveedorcedula

class cliente(models.Model):
    clientecedula = models.CharField(max_length=13)
    clientenombre = models.CharField(max_length=150)
    Estado = (
        ('1', 'Activo'),
        ('0', 'No Activo'),
    )
    clientetelefono = models.CharField(max_length=50)
    clienteanulado = models.CharField(max_length=1,choices=Estado,help_text="Seleccione el Estado",default='1')

    def __str__(self):
        return self.clientecedula

class comprasEnc(models.Model):
    comprasEncproveedor = models.ForeignKey(proveedor, on_delete=models.CASCADE)
    comprasEncfecha = models.DateField(null=True, blank=True)
    comprasEncobservacion = models.CharField(max_length=150)
    comprasnofactura = models.CharField(max_length=50)
    comprasEncfechafactura = models.DateField()
    comprasEncsubtotal = models.FloatField(default=0)
    comprasEncdescuento = models.FloatField(default=0)
    comprasEnctotal = models.FloatField(default=0)

    def __str__(self):
        return self.comprasEncproveedor

class comprasdetalle(models.Model):
    comprasdetallecomprasEnc = models.ForeignKey(comprasEnc, on_delete=models.CASCADE)
    comprasdetalleproducto = models.ForeignKey(producto, on_delete=models.CASCADE)
    comprasdetallecantidad = models.IntegerField()
    comprasdetalleprecio = models.FloatField()
    comprasdetallesubtotal = models.FloatField()
    comprasdetalledescuento = models.FloatField()
    comprasdetalletotal = models.FloatField()

    def __str__(self):
        return self.comprasdetallecomprasEnc

class ventaEnc(models.Model):
    ventaEncliente = models.ForeignKey(cliente, on_delete=models.CASCADE)
    ventaEncfechaventasEnc = models.DateField(null=True, blank=True)
    ventaEncobservacion = models.CharField(max_length=150)
    ventanofactura = models.CharField(max_length=50)
    ventaEncfechafactura = models.DateField()
    ventaEncsubtotal = models.FloatField(default=0)
    ventaEncdescuento = models.FloatField(default=0)
    ventaEnctotal = models.FloatField(default=0)

    def __str__(self):
        return self.ventaEncliente


class ventaEncdetalle(models.Model):
    ventadetalleventaEnc = models.ForeignKey(ventaEnc, on_delete=models.CASCADE)
    ventadetalleproducto = models.ForeignKey(producto, on_delete=models.CASCADE)
    ventadetallecantidad = models.IntegerField()
    ventadetalleprecio = models.FloatField()
    ventadetallesubtotal = models.FloatField()
    ventadetalledescuento = models.FloatField()
    ventacomprasdetalletotal = models.FloatField()

    def __str__(self):
        return self.ventadetalleventasEnc








