import json
from wsgiref.simple_server import make_server


def application(environ, start_response):
    headers = [('Content-Type', 'application/json')]

    status = '200 OK'
    output = 'Hola Desarrolladores TdeA estoy en el server!'

    start_response(status, headers)

    response = {'mensaje': output}

    return [ bytes(json.dumps(response), 'utf8') ]


server = make_server('localhost', 8000, application)
server.handle_request()