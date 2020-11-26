from minimart import ma, db
from minimart.models.store import Store
from minimart.dao.working_hours import WorkingHoursDao


class StoreDao(ma.SQLAlchemyAutoSchema):
    query = Store.query
    work_hours = ma.HyperlinkRelated(WorkingHoursDao)

    class Meta:
        model = Store

    def findOne(self, id):
        return self.query.get(id)

    def findAll(self):
        return self.query.all()

    def update(self, data):
        self.dump(data)

    def create(self, new_store):
        db.session.add(new_store)
        return self.dump(new_store)

    def delete(self, store):
        return db.session.delete(store)
