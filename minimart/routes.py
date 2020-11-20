from minimart import api, app
from flask_restx import Resource
from minimart.controllers import store_controller

@api.route('/store')
class storeRoute(Resource):
    def get(self):
        return store_controller.listStore()