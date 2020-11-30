from minimart.dao import product as dao
from minimart.models import product as model
from minimart.models import product_stock as product_stock_model
from flask_restx import fields


def listProduct():
    return dao.ProductDao().findAll()


def getProduct(id):
    return dao.ProductDao().findOne(id)

def getProductStore(id, store_id):
    return dao.ProductDao().findByParams({'id':id, 'store_id':store_id})


def updateProduct(id, data):
    db_Product = getProduct(id)
    for key in data['working_hours'].keys():
        val = fields.datetime_from_iso8601(data['working_hours'][key])
        setattr(db_Product.working_hours, key, val)
    setattr(db_Product, 'logo', data['logo'])
    return dao.ProductDao().update(db_Product)


def createProduct(data):
    new_Product = model.Product(data['name'], data['category'])
    return dao.ProductDao().create(new_Product)


def deleteProduct(id):
    return dao.ProductDao().delete(getProduct(id))

def setStock(id, data):
    new_product_stock = product_stock_model.ProductStock()
    new_product_stock.product_id = id
    new_product_stock.store_id = data['store_id']
    new_product_stock.stock = data['stock']
    return dao.ProductDao().updateStock(new_product_stock)