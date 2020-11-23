from minimart import ma
from minimart.models import store


class StoreDao(ma.SQLAlchemyAutoSchema):
    query = store.Store.query

    class Meta:
        model = store.Store

    def findAll(self):
        return self.dump(self.query.all(), many=True)

    def create(new_store):
        return self.query.add_entity(new_store)
