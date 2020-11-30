from minimart import ma
from minimart.models.product_stock import ProductStock


class ProductStockDao(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = ProductStock