import operator
from minimart import ma, db
from minimart.models.product import Product
from minimart.models.product_stock import ProductStock as product_stock_model
from minimart.dao.product_stock import ProductStock as product_stock_dao


class ProductDao(ma.SQLAlchemyAutoSchema):
    query = Product.query
    work_hours = ma.HyperlinkRelated(product_stock_dao)
    stock = ma.Nested(product_stock_dao)

    class Meta:
        model = Product

    def findOne(self, id):
        return self.query.get(id)

    def findAll(self):
        return self.query.all()

    def findByParams(self, params):
        result = self.query.get(1)
        return result
        # result = product_stock_dao().load({'stock': params})
        # result = self.query.filter_by(stock.store_id == params['store_id']).all()
        # return self.query.filter(operator.eq(Product.stock.has('store_id'), params['store_id'])).all()
        # Book.query.filter(operator.eq(Book.author, "some author")).all()
        # return .filter(ProductStock.product_id == params['id'])
        # return self.query.filter(params)

    def update(self, data):
        self.dump(data)

    def updateStock(self, data):
        db.session.add(data)

    def create(self, new_store):
        db.session.add(new_store)
        return self.dump(new_store)

    def delete(self, store):
        return db.session.delete(store)
