from apps.products.models import MeasureUnit, CategoryProduct, Indicador
from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ('state','created_date','modified_date','deleted_date') # Campos que no quiero retornar

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude = ('state','created_date','modified_date','deleted_date') # Campos que no quiero retornar

class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        exclude = ('state','created_date','modified_date','deleted_date') # Campos que no quiero retornar
