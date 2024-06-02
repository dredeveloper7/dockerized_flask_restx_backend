from flask_restx import Namespace, Resource

core_ns = Namespace('HealthCheck', description='Health check proving the backend and front can speak - check front end chrome developer console')

@core_ns.route('/')
class HealthCheck(Resource):
    def get(self):
        return {'message': 'Backend Reached'}, 200
