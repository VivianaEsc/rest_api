from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords

class MeasureUnit(BaseModel):
    description = models.CharField('Descripcion', max_length=50, blank=False, null=False, unique= True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _histoy_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Modelo Unidades'
        verbose_name_plural = 'Modelos Unidades'

    def __str__(self):
        return self.description
    

class CategoryProduct(BaseModel):
    description = models.CharField('Descripcion', max_length=50, blank=False, null=False, unique= True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _histoy_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Categoria de producto'
        verbose_name_plural = 'Categorias de productos'

    def __str__(self):
        return self.description
    

class Indicador(BaseModel):
    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey( CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de oferta')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _histoy_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Indicador de oferta'
        verbose_name_plural = 'Indicadores de ofertas'

    def __str__(self):
        return f'Oferta de la categoría {self.category_product}: {self.descount_value}%'
    
class Product(BaseModel):
    name = models.CharField('Nombre del Producto', max_length=150, unique=True,blank=False,null=False)
    description = models.TextField ( 'Descripcion de Producto', blank=False,null=False)
    category_product = models.ForeignKey( CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de oferta')
    mesure_unit = models.ForeignKey( MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de medida', null=True)
    image = models.ImageField('Imagen del Producto',upload_to='products/',blank=True, null=True)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Categoría de Producto', null=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _histoy_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name