%title: CherryPy (The Simple Guide)
%author: Ibrahim Chávez
%date: 03-24-2019

-> # Hi everyone! <-

I am Ibrahim Chávez and I will guide you on how to use CherryPy.

# Who am I?

* Engineering/Technology Intern at GEIQ (Mexico)
* Member of the Services & Shop Analytics team
* (Really) Enthusiastic Python Developer
* Current project: Test Cell Advisor (TCA)
    * Web services
    * General back-end development

-------------------------------------------------
 
-> # What are the topics for this presentation? <-

* CherryPy -> Python Micro Web Framework
* Pickle   -> Module for [de-]serialization

-------------------------------------------------
 
-> # What is CherryPy? <-

Pythonic, object-oriented web framework.

-------------------------------------------------

-> # Wait... What does that mean? <-

* What does object-oriented means?
* What is a web framework?
* So...

------------------------------------------------- 
 
-> # Why? <-

* Fast development
* Pythonic
* Oldest web frameworks (10+ years old)
* Lets you make the decisions
* Clean
* Small learning curve
* Great community (https://gitter.im/cherrypy/cherrypy)
* It's free!

-------------------------------------------------
 
-> # When you should use it? <-

Whenever you want to build a web application in just a couple of minutes, 
without losing reliability and with full control of how your application 
must works.

-------------------------------------------------
 
-> # Let's run your first web server <-
 
This example shows how to run a simple web server with CherryPy.
 
    1   # Hello World program
    2
    3   import cherrypy
    4
    5   class Foobar(object):
    6       @cherrypy.expose
    7       def index(self):
    8           return 'Hello World!'
    9
    10  cherrypy.quickstart(Foobar())

-------------------------------------------------
 
# Pretty cool, huh?

Lets jump into more interesting code...
