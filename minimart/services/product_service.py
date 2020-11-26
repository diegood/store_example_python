from minimart.dao import store as dao
from minimart.models import store as model
from minimart.models import working_hours as working_hours_model
from flask_restx import fields


def listProduct():
    return dao.ProductDao().findAll()


def getProduct(id):
    return dao.ProductDao().findOne(id)


def updateProduct(id, data):
    db_Product = getProduct(id)
    for key in data['working_hours'].keys():
        val = fields.datetime_from_iso8601(data['working_hours'][key])
        setattr(db_Product.working_hours, key, val)
    setattr(db_Product, 'logo', data['logo'])
    return dao.ProductDao().update(db_Product)


def createProduct(data):
    wh = working_hours_model.WorkingHours(**data['working_hours'])
    new_Product = model.Product(data['name'], data['logo'], data['address'], wh)
    return dao.ProductDao().create(new_Product)


def deleteProduct(id):
    return dao.ProductDao().delete(getProduct(id))
