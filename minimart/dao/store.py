from minimart import ma
from models import store


class StoreDao(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = store.Store
