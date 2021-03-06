# Generated by Django 3.1.2 on 2021-01-15 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUsuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='caja_iot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sincronizacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='chef_receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=20)),
                ('id_chef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionUsuarios.chef')),
            ],
        ),
        migrations.CreateModel(
            name='cocina_iot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sincronizacion', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=1000)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pedidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion_entrega', models.CharField(max_length=50)),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=1000)),
                ('propina', models.IntegerField()),
                ('forma_pago', models.CharField(max_length=20)),
                ('total', models.IntegerField()),
                ('fecha_pedido', models.TimeField()),
                ('id_chef_recetas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionUsuarios.chef_receta')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionUsuarios.cliente')),
                ('id_domiciliario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionUsuarios.domiciliario')),
            ],
        ),
        migrations.AddField(
            model_name='chef_receta',
            name='id_receta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionUsuarios.receta'),
        ),
        migrations.AddField(
            model_name='chef',
            name='id_cocina_iot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestionUsuarios.cocina_iot'),
        ),
        migrations.AddField(
            model_name='domiciliario',
            name='id_caja_iot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestionUsuarios.caja_iot'),
        ),
    ]
