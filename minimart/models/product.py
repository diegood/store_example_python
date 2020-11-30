from minimart import db, api
# from minimart.models.product_stock import ProductStock
from flask_restx import fields


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(50))  # TODO move to a relationship
    # stock=  db.relationship(ProductStock, backref=db.backref('products_stock', lazy='joined'), cascade="all", uselist=False)

    def __init__(self, name, category):
        self.name = name
        self.category = category

    def swagger(create=False):
        schema = {
            'id': fields.Integer(readonly=True, description='The product unique identifier'),
            'name': fields.String(required=True, description='Product name', example='Nuka-Cola'),
            'category': fields.String(required=True, description='Category type', example='sodas', enum=['soda', 'food', 'cleaning', 'bathroom', ])
        }
        if create:
            return api.model('ProductBase', schema)
        else:
            # schema['stock'] = fields.Nested(ProductStock.swagger())
            return api.model('ProductEditable', schema)
