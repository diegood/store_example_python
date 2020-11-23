from minimart import ma, db
from minimart.models import store



class StoreDao(ma.SQLAlchemyAutoSchema):
    query = store.Store.query

    class Meta:
        model = store.Store

    def findAll(self):
        return self.dump(self.query.all(), many=True)

    def create(self, new_store):
        id= db.session.add(new_store)
        # db.session.commit()
        return id
