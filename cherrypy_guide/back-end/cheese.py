"""
    Created on Mar 22 2019
    @author: 212690718  Ibrahim Chávez
    File description
    ------------------------
    Just a module for exposing the main features of the CherryPy web framework.

    File log
    ------------------------
    ===========         =============        ================
    Date                Author               Comments
    ===========         =============        ================
    Mar 22 2019           Ibrahim C.         Original version
    ===========         =============        ================
"""

# Remember to first download the required packages!
# What CherryPy am I using? 14.0
# What is the latest version? 18.1.0
# Note: v18.0+ does not support Python 2.7 D=

import cherrypy
import cherrypy_cors

import lemon

# Why do we need to import cherrypy_cors?
# Cross-Origin Resource Sharing (CORS) is a mechanism that uses additional HTTP
# headers to tell a browser to let a web application running at one origin
# (domain) have permission to access selected resources from a server at a 
# different origin. From: MDN web docs (Mozilla documentation)

# First the basics...
class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello world!"

def hello_world():
    """Runs our powerful & simple web server
    """
    cherrypy.quickstart(HelloWorld())

# Lets build our first web services!
@cherrypy.expose
class WebServices:

    @cherrypy.tools.accept(media='text/plain')
    def GET(self, data='1st param', another_param='2nd param'):
        """GET method enabled by this method. It should receive a param call
        'data'.
        Parameters
        ----------
        data : str, optional
            Just a test input (the default is 'test')
        Returns
        -------
        str
            Same value as input
        """
        return f'{data} {another_param}'

    @cherrypy.tools.json_out()
    def POST(self, json_data):
        """POST method that expects to receive a JSON containing the data
        for getting the desired action
        Parameters
        ----------
        json_data : str
            JSON input.
        Returns
        -------
        json
            Returns the result for the given input
        """
        return lemon.sum_column(json_data)

def web_services():
    """Configures how the web services should run
    
    """
    cherrypy_cors.install()
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'cors.expose.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [
                ('Content-Type', 'text/plain'), 
                ('Access-Control-Allow-Origin', '*')
            ]
        }
    }
    # cherrypy.config.update({'server.socket_host': 'localhost'})
    # cherrypy.config.update({'server.socket_host': '3.51.55.92'})
    cherrypy.config.update({'server.socket_host': '192.168.1.85'})
    cherrypy.config.update({'server.socket_port': 8086})
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.quickstart(WebServices(), '/', conf)

if __name__ == "__main__":
    # hello_world()  
    web_services()
