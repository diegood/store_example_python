from minimart import db, api
from minimart.models.product_stock import ProductStock
from flask_restx import fields


class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(50))  # TODO move to a relationship
    stock=  db.relationship(ProductStock, backref=db.backref(
        'products_stock', lazy='joined'), cascade="all", uselist=False)

    def __init__(self, name, category):
        self.name = name
        self.category = category

    def swagger(edit=False):
        schema = {
            'id': fields.Integer(readonly=True, description='The store unique identifier'),
            'name': fields.String(required=True, description='Store name', example='COCO Downtown'),
            'category': fields.String(required=True, description='Store logo url', example='https://www.sightseeingpass.com/images/attractions/attraction-images-670x270/san-francisco/attimg_cocofreshteajuice1_large.jpg'),
            'stock': fields.Nested(ProductStock.swaggerSchema())
        }
        base = api.model('StoreBase', schema)
        if edit:
            del schema['name']
            del schema['address']
        editable = api.model('StoreEditable', schema)
        return editable if edit else base
