from flask_restx import Api
from .auth import auth_ns
from .core import core_ns


api = Api(
    title='magicmenuapi',
    version='1.0',
    description='A description',
    doc='/docs'
)

api.add_namespace(auth_ns, path='/auth')
api.add_namespace(core_ns, path='/health')