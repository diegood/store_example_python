from minimart import db
from flask_restx import fields


class ProductStock(db.Model):
    __tablename__ = 'products_stock'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey(
        'stores.id'), nullable=False)
    stock = db.Column(db.Integer)

    def swagger():
        return api.model('productStock', {
            'product_id': fields.String(required=True, description='The product unique identifier', example=1),
            'store_id': fields.String(required=True, description='The store unique identifier', example=1),
            'stock': fields.Integer(description='Amount for that location', example=10)
        })
