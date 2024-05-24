from spyne import Application, rpc, ServiceBase, Integer, Unicode
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

class HelloWorldService(ServiceBase):

    @rpc(Unicode, _returns=Unicode)
    def say_hello(ctx, name):
        return f"Hello, {name}!"

# Create the application with the specified service
application = Application([HelloWorldService], tns='soap_service', in_protocol=Soap11(validator="lxml"), out_protocol=Soap11())


wsgi_application = WsgiApplication(application)

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    server = make_server('0.0.0.0', 8000, wsgi_application)
    print("\nServer running 0.0.0.0:8000")
    server.serve_forever()