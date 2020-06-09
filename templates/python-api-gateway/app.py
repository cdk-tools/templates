from aws_cdk.core import App, Stack
from stacks.api import ApiStack

app = App()
stack = Stack(app, 'api-stack')

ApiStack(stack)
