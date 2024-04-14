# What happens when you type google.com in your browser and press Enter

Ever wondered what happens when you type a URL into the address bar of a browser and press Enter, today we are going to dive into it and see what happens behind the scenes.

## DNS Request

Everything start starts with a Domain Name System (DNS) lookup. The browser sends a request to a DNS server to translate the human-readable domain name (<www.google.com>) into an IP address, computers communicate with IP addresses, but they do not understand domain names.

## TCP/IP

The computer now sends the request to the IP address using Transmission Control Protocol/Internet Protocol (TCP/IP). The browser establishes a TCP connection with the Google server, ensuring there is reliable and error-checked delivery of data between the computer and the Google server.

## Firewall

A firewall acts like a filter that checks incoming and outgoing traffic for any malicious activity. It can block any malicious from the server.

## HTTPS/SSL

As the connection is established, the browser initiates a Hypertext Transfer Protocol Secure (HTTPS) request. HTTPS encrypts the data transmitted between the browser and Google servers using Secure Sockets Layer (SSL) or Transport Layer Security (TLS) which seals the data with a lock - only the intended receipt (Google) has the key to unlock it, protecting the data.

## Load Balancer

Google uses load balancers since it receives millions of requests per second. The load balancers handle the traffic efficiently, they act like traffic directors, distributing incoming requests to multiple web servers, ensuring smooth operation and preventing any single server from getting overloaded.

## Web Server

When your HTTPS request reaches Google's server, it will handled by a web server that processes the request. It will retrieve the necessary information such as HTML code, images, and script to build the Google search page. The web server gathers and prepares them for delivery.

## Application Server

The application server is responsible for handling your search query, interacting with databases, and personalizing your results on your past searches.

## Database

Google has databases that store information from websites Google has crawled and indexed, allowing it to find relevant results for search queries.

After the response is sent to your computer, it is interpreted by the browser, which then displays it on your screen in a user-friendly format, bringing up the Google search page.
