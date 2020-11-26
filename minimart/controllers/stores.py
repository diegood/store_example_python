from minimart import api
from flask_restx import Resource
from minimart.services import store_service
from minimart.models import store as store_model


ns_store = api.namespace('stores', description='Stores endpints')


@ns_store.route('/', endpoint='stores')
class StoreRoutes(Resource):
    @ns_store.marshal_with(store_model.Store.swagger(), code=200)
    def get(self):
        return store_service.listStore()

    @ns_store.doc('create a new store')
    @ns_store.expect(store_model.Store.swagger(edit=False))
    @ns_store.marshal_with(store_model.Store.swagger(), code=201)
    def post(self):
        return store_service.createStore(api.payload), 201


@ns_store.route('/<int:id>')
class storeWithRefRoutes(Resource):
    @ns_store.marshal_with(store_model.Store.swagger(), code=200)
    def get(self, id):
        return store_service.getStore(id), 200

    @ns_store.expect(store_model.Store.swagger(edit=True))
    def patch(self, id):
        return store_service.updateStore(id, api.payload), 202

    def delete(self, id):
        return store_service.deleteStore(id), 200
