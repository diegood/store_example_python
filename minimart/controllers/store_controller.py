from minimart.dao import store as dao
from minimart.models import store as model
from minimart.models import working_hours as working_hours_model


def listStore():
    return dao.StoreDao().findAll()


def getStore(id):
    return dao.StoreDao().findOne(id)


def createStore(data):
    wh = working_hours_model.WorkingHours(**data['work_address'])
    new_store = model.Store(data['name'], data['logo'], data['address'], wh)
    return dao.StoreDao().create(new_store)
