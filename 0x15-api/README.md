# API

An API, or Application Programming Interface, is a set of rules and protocols that allows different software applications to communicate and interact with each other. It defines the methods and data formats that applications can use to request and exchange information.

API acts as a contract between different software components, defining how they can communicate and interact, which ultimately enables the creation of complex and integrated software systems.

## REST API

A REST API (Representational State Transfer API) is a type of web service that follows the principles of REST architectural style. REST is an architectural style for designing networked applications. It is based on a stateless, client-server communication model where web services are viewed as resources that can be identified by their URLs (Uniform Resource Locators).

### Characteristics and Principles of REST API

1. Resource-Based: everything is treated as a resource, each resource has an unique identifier by a URI(Uniform Resource Identifier), example user profile might be represented by URI like `/users/johndoe`

2. Uniform Interface: REST APIs use standard HTTP methods (GET, POST, PUT, DELETE) to perform CRUD (Create, Read, Update, Delete) operations on resources. Each HTTP method has a specific meaning:
    * GET : retrieve a resource
    * POST : create a resource
    * PUT : update an existing resource
    * DELETE : remove a resource

3. Stateless:  REST APIs are stateless, meaning that each request from a client to the server must contain all the information necessary to understand and process the request. The server does not maintain any client state. Sessions and state are managed on the client side.

4. Representation of Resources: Resources in a REST API can have different representations, such as JSON, XML, HTML, or others. Clients can request a specific representation using the Accept header in the HTTP request.
