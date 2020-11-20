from minimart.dao import store as dao
from minimart.models import store as model

def listStore():
    dataset = model.Store.query.all()
    return dao.StoreDao().dump(dataset, many=True)
