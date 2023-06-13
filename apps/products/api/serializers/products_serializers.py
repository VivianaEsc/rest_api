from rest_framework import serializers

from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):
    #Para no mostrar solo IDs en los json de producto importar los serializers respectivos
    # category_product = CategoryProductSerializer() #Mostrará toda la información del serializer de category product
    # measure_unit = MeasureUnitSerializer()

    # category_product = serializers.StringRelatedField() #Hace referencia al metodo __str__ definido en el modelo
    # mesure_unit = serializers.StringRelatedField() 

    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','deleted_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'description': instance.description,
            'image': instance.image if instance.image != '' else '',
            'measure_unit': instance.mesure_unit.description,
            'category_product': instance.category_product.description
        }