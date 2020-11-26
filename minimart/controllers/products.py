from minimart import api
from flask_restx import Resource
from minimart.services import store_service
from minimart.models.product import Product as product_model


ns_store = api.namespace('products', description='Products endpints')


@ns_store.route('/', endpoint='products')
class ProductsResource(Resource):
    @ns_store.marshal_with(product_model.swagger(), code=200)
    def get(self):
        return store_service.listStore()

    @ns_store.doc('create a new store')
    @ns_store.expect(product_model.swagger(edit=False))
    @ns_store.marshal_with(product_model.swagger(), code=201)
    def post(self):
        return store_service.createStore(api.payload), 201


@ns_store.route('/<int:id>')
class ProductsResourceWithRef(Resource):
    @ns_store.marshal_with(product_model.swagger(), code=200)
    def get(self, id):
        return store_service.getStore(id), 200

    @ns_store.expect(product_model.swagger(edit=True))
    def patch(self, id):
        return store_service.updateStore(id, api.payload), 202

    def delete(self, id):
        return store_service.deleteStore(id), 200
