# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-22 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
        ('classificacoes', '0001_initial'),
        ('unidades_medida', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id_aula', models.AutoField(primary_key=True, serialize=False)),
                ('nome_aula', models.CharField(max_length=200)),
                ('data_aula', models.DateField(default='01 de janeiro de 2000', null=True)),
                ('descricao_aula', models.CharField(max_length=200)),
                ('aula_agendada', models.BooleanField(default=True)),
                ('aula_concluida', models.BooleanField(default=True)),
                ('periodo_aula', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AulaReceita',
            fields=[
                ('id_aula_receita', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade_receita', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('id_aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relacionamentos.Aula')),
            ],
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id_ingrediente', models.AutoField(primary_key=True, serialize=False)),
                ('nome_ingrediente', models.CharField(max_length=200)),
                ('quantidade_calorica_ingrediente', models.DecimalField(decimal_places=1, max_digits=6)),
                ('aproveitamento_ingrediente', models.DecimalField(decimal_places=1, max_digits=4)),
                ('quantidade_estoque_ingrediente', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('quantidade_reservada_ingrediente', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('valor_ingrediente', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('motivo_retirada_estoque', models.CharField(max_length=200, null=True)),
                ('id_unidade_medida', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='unidades_medida.UnidadeMedida')),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id_receita', models.AutoField(primary_key=True, serialize=False)),
                ('nome_receita', models.CharField(max_length=100)),
                ('modo_preparo_receita', models.TextField(max_length=6500)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.Categoria')),
                ('id_classificacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classificacoes.Classificacao')),
            ],
        ),
        migrations.CreateModel(
            name='ReceitaIngrediente',
            fields=[
                ('id_receita_ingrediente', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade_bruta_receita_ingrediente', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('custo_bruto_receita_ingrediente', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('id_ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relacionamentos.Ingrediente')),
                ('id_receita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relacionamentos.Receita')),
            ],
        ),
        migrations.AddField(
            model_name='receita',
            name='ingredientes',
            field=models.ManyToManyField(through='relacionamentos.ReceitaIngrediente', to='relacionamentos.Ingrediente'),
        ),
        migrations.AddField(
            model_name='aulareceita',
            name='id_receita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relacionamentos.Receita'),
        ),
        migrations.AddField(
            model_name='aula',
            name='receitas',
            field=models.ManyToManyField(through='relacionamentos.AulaReceita', to='relacionamentos.Receita'),
        ),
    ]
