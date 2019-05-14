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
    products = models.ManyToManyField(
        to='Product',
        through='ProductCategory'
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
    categories = models.ManyToManyField(
        to='Category',
        through='ProductCategory'
    )

    class Meta:
        db_table = 'product'
        managed = True


class ProductCategory(models.Model):
    id = models.AutoField(
        db_column='id_product_category',
        null=False,
        primary_key=True
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.DO_NOTHING,
        db_column='id_category',
        null=False,
        db_index=False
    )
    product = models.ForeignKey(
        to='Product',
        on_delete=models.DO_NOTHING,
        db_column='id_product',
        null=False,
        db_index=False
    )

    class Meta:
        db_table = 'product_category'
        managed = True
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['product'])
        ]


class Department(models.Model):
    id = models.AutoField(
        db_column='id_department',
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
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        null=False,
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        null=False,
        auto_now=True
    )

    class Meta:
        db_table = 'department'
        managed = True


class Employee(models.Model):
    id = models.AutoField(
        db_column='id_employee',
        null=False,
        primary_key=True
    )
    name = models.CharField(
        db_column='tx_name',
        null=False,
        max_length=104,
        unique=True
    )
    active = models.BooleanField(
        db_column='cs_active',
        null=False,
        default=True
    )
    department = models.ForeignKey(
        to='Department',
        on_delete=models.DO_NOTHING,
        db_column='id_department',
        null=False,
        db_index=False,
        related_name='employees'
    )
    created_at = models.DateTimeField(
        db_column='dt_created_at',
        null=False,
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        db_column='dt_modified_at',
        null=False,
        auto_now=True
    )
    gender = models.CharField(
        db_column='cs_gender',
        null=True,
        max_length=1
    )

    class Meta:
        db_table = 'employee'
        managed = True
        indexes = [
            models.Index(fields=['department'])
        ]
