# Generated by Django 2.2.1 on 2019-05-14 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(db_column='id_category', primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='tx_description', max_length=104, unique=True)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
            ],
            options={
                'db_table': 'category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_column='id_product', primary_key=True, serialize=False)),
                ('description', models.CharField(db_column='tx_description', max_length=104, unique=True)),
                ('active', models.BooleanField(db_column='cs_active', default=True)),
                ('category', models.ForeignKey(db_column='id_category', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Category')),
            ],
            options={
                'db_table': 'product',
                'managed': True,
            },
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['category'], name='product_id_cate_95fea8_idx'),
        ),
    ]