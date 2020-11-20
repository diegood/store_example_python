from minimart import ma
from minimart.models import store


class StoreDao(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = store.Store
