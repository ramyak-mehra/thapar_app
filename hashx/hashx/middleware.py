import graphene
from graphql_jwt.decorators import login_required

class CustomAuthorizationMiddleware(object):
    
    def resolve(self, next, root, info, **args):
        return next(root, info, **args)