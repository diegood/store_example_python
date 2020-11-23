from minimart import api, app
from flask_restx import Resource
from minimart.controllers import store_controller
from minimart.models import store as store_model


ns_store = api.namespace('Stores', description='Stores endpints')


@ns_store.route('/stores', endpoint='stores')
class StoreRoutes(Resource):
    def get(self):
        return store_controller.listStore()

    @ns_store.doc('create a new store')
    @ns_store.expect(store_model.Store.swagger())
    @ns_store.marshal_with(store_model.Store.swagger(), code=201)
    def post(self):
        return store_controller.createStore(api.payload), 201


@ns_store.route('/stores/<int:id>')
class storeWithRefRoutes(Resource):
    def get(self):
        return store_controller.listStore()

    @ns_store.expect(store_model.Store.swagger())
    def patch(self):
        return store_controller.listStore()

    def delete(self):
        return store_controller.listStore()


ns_product = api.namespace('Products', description='producs')


@ns_product.route('/products', endpoint='products')
class GetProducts(Resource):
    def get(self):
        return store_controller.listStore()
