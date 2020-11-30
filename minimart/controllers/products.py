from minimart import api
from flask_restx import Resource
from minimart.services import product_service
from minimart.models.product import Product as product_model
from minimart.models.product_stock import ProductStock as product_stock_model


ns_product = api.namespace('products', description='Products endpints')


@ns_product.route('/', endpoint='products')
class ProductsResource(Resource):
    @ns_product.marshal_with(product_model.swagger(), code=200)
    def get(self):
        return product_service.listProduct()

    @ns_product.doc('create a new Product')
    @ns_product.expect(product_model.swagger(create=True))
    @ns_product.marshal_with(product_model.swagger(create=True), code=201)
    def post(self):
        return product_service.createProduct(api.payload), 201


@ns_product.route('/<int:id>')
class ProductsResourceWithRef(Resource):
    @ns_product.marshal_with(product_model.swagger(), code=200)
    def get(self, id, store=None):
        return product_service.getProduct(id), 200

    @ns_product.expect(product_model.swagger())
    def patch(self, id):
        return product_service.updateProduct(id, api.payload), 202

    def delete(self, id):
        return product_service.deleteProduct(id), 200


@ns_product.route('/<int:id>/stock')
class ProductStockReource(Resource):
    @ns_product.expect(product_stock_model.swagger(), 201)
    def put(self, id):
        return product_service.setStock(id, api.payload), 201


@ns_product.route('/<int:id>/stock/store/<int:store_id>')
class ProductStockByStoreReource(Resource):
    def get(self, id, store_id):
        return product_service.getProductStore(id, store_id), 200
