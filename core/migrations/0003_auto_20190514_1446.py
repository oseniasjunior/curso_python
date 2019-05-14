# Generated by Django 2.2.1 on 2019-05-14 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190514_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(db_column='id_product_category', primary_key=True, serialize=False)),
                ('category', models.ForeignKey(db_column='id_category', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Category')),
                ('product', models.ForeignKey(db_column='id_product', db_index=False, on_delete=django.db.models.deletion.DO_NOTHING, to='core.Product')),
            ],
            options={
                'db_table': 'product_category',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(through='core.ProductCategory', to='core.Category'),
        ),
        migrations.AddIndex(
            model_name='productcategory',
            index=models.Index(fields=['category'], name='product_cat_id_cate_a590c6_idx'),
        ),
        migrations.AddIndex(
            model_name='productcategory',
            index=models.Index(fields=['product'], name='product_cat_id_prod_f6235a_idx'),
        ),
    ]
