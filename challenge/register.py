from flask_restx import Api
from infraestructure.routes.processAccount import api as ns1

api = Api(
    title='demo app',
    version='1.0',
    description='demo app',
)

api.add_namespace(ns1, path='/api')
