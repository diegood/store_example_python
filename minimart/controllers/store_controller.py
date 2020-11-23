from minimart.dao import store as dao
from minimart.models import store as model


def listStore():
    return dao.StoreDao().findAll()


def createStore(data):
    # input_wh = data['work_address']
    # wh = working_hours_model.WorkingHous(input_wh)
    new_store = model.Store(
        data['name'],
        data['logo'],
        data['address'],
        
    )
    return dao.StoreDao().dump(new_store, many=True)
