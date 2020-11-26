from minimart.dao import store as dao
from minimart.models import store as model
from minimart.models import working_hours as working_hours_model
from flask_restx import fields


def listStore():
    return dao.StoreDao().findAll()


def getStore(id):
    return dao.StoreDao().findOne(id)


def updateStore(id, data):
    db_store = getStore(id)
    for key in data['working_hours'].keys():
        val = fields.datetime_from_iso8601(data['working_hours'][key])
        setattr(db_store.working_hours, key, val)
    setattr(db_store, 'logo', data['logo'])
    return dao.StoreDao().update(db_store)


def createStore(data):
    wh = working_hours_model.WorkingHours(**data['working_hours'])
    new_store = model.Store(data['name'], data['logo'], data['address'], wh)
    return dao.StoreDao().create(new_store)


def deleteStore(id):
    return dao.StoreDao().delete(getStore(id))
