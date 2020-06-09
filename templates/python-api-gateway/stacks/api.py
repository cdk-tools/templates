from aws_cdk import (
  core,
  aws_apigateway as ag
)

class ApiStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        rest_api = ag.RestApi(self, 'Api')
        
        users_resource = rest_api.root.add_resource('users')
        
        
        

        