from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.AutoField(
        db_column='id_category',
        null=False,
        primary_key=True
    )
    description = models.CharField(
        db_column='tx_description',
        null=False,
        max_length=104,
        unique=True
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )

    class Meta:
        db_table = 'category'
        managed = True


class Product(models.Model):
    id = models.AutoField(
        db_column='id_product',
        null=False,
        primary_key=True
    )
    description = models.CharField(
        db_column='tx_description',
        null=False,
        max_length=104,
        unique=True
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.DO_NOTHING,
        db_column='id_category',
        null=False,
        db_index=False
    )

    class Meta:
        db_table = 'product'
        managed = True
        indexes = [
            models.Index(fields=['category'])
        ]