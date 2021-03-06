# Generated by Django 3.0.8 on 2021-10-05 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientecedula', models.CharField(max_length=13)),
                ('clientenombre', models.CharField(max_length=150)),
                ('clientetelefono', models.CharField(max_length=50)),
                ('clienteanulado', models.CharField(choices=[('1', 'Activo'), ('0', 'No Activo')], default='1', help_text='Seleccione el Estado', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gruponombre', models.CharField(max_length=150)),
                ('grupoanulado', models.CharField(choices=[('1', 'Activo'), ('0', 'No Activo')], default='1', help_text='Seleccione el Estado', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productonombre', models.CharField(max_length=150)),
                ('productopreciovta', models.FloatField()),
                ('productocodigo', models.CharField(max_length=50)),
                ('productoexistencia', models.CharField(max_length=50)),
                ('productoanulado', models.CharField(choices=[('1', 'Activo'), ('0', 'No Activo')], default='1', help_text='Seleccione el Estado', max_length=1)),
                ('productogrupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.grupo')),
            ],
        ),
        migrations.CreateModel(
            name='proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedorcedula', models.CharField(max_length=13)),
                ('proveedornombre', models.CharField(max_length=150)),
                ('proveedortelefono', models.CharField(max_length=50)),
                ('proveedoranulado', models.CharField(choices=[('1', 'Activo'), ('0', 'No Activo')], default='1', help_text='Seleccione el Estado', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ventaEnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ventaEncfechaventasEnc', models.DateField(blank=True, null=True)),
                ('ventaEncobservacion', models.CharField(max_length=150)),
                ('ventanofactura', models.CharField(max_length=50)),
                ('ventaEncfechafactura', models.DateField()),
                ('ventaEncsubtotal', models.FloatField(default=0)),
                ('ventaEncdescuento', models.FloatField(default=0)),
                ('ventaEnctotal', models.FloatField(default=0)),
                ('ventaEncliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='ventaEncdetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ventadetallecantidad', models.IntegerField()),
                ('ventadetalleprecio', models.FloatField()),
                ('ventadetallesubtotal', models.FloatField()),
                ('ventadetalledescuento', models.FloatField()),
                ('ventacomprasdetalletotal', models.FloatField()),
                ('ventadetalleproducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
                ('ventadetalleventaEnc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.ventaEnc')),
            ],
        ),
        migrations.CreateModel(
            name='comprasEnc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprasEncfecha', models.DateField(blank=True, null=True)),
                ('comprasEncobservacion', models.CharField(max_length=150)),
                ('comprasnofactura', models.CharField(max_length=50)),
                ('comprasEncfechafactura', models.DateField()),
                ('comprasEncsubtotal', models.FloatField(default=0)),
                ('comprasEncdescuento', models.FloatField(default=0)),
                ('comprasEnctotal', models.FloatField(default=0)),
                ('comprasEncproveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.proveedor')),
            ],
        ),
        migrations.CreateModel(
            name='comprasdetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comprasdetallecantidad', models.IntegerField()),
                ('comprasdetalleprecio', models.FloatField()),
                ('comprasdetallesubtotal', models.FloatField()),
                ('comprasdetalledescuento', models.FloatField()),
                ('comprasdetalletotal', models.FloatField()),
                ('comprasdetallecomprasEnc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.comprasEnc')),
                ('comprasdetalleproducto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.producto')),
            ],
        ),
    ]
