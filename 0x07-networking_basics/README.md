OSI model
---------
Open System Interconnection model - framework that dictates how communication btn networks.
developed by International Organization for Standization.

Organizational Structure
------------------------
1. Layer 1 - Physical Layer: physical connection btn devices <cables,connectors,electrical-signal>
2. Layer 2 - Data link layer: transmission of data frames btn devices in the same network
3. Layer 3 - Network Layer: forwarding data packets btn different network.
4. Layer 4 - Transport Layer: manage data flow control, error checking , segmentation and reassembly of data.
5. Layer 5 - Session Layer: establish, manage, terminate sessions/connections btn application.
6. Layer 6 - Presentation Layer: translating, encrypting, compressing data, presenting data in a readable format.
7. Layer 7 - Application Layer

Purpose of OSI Model
--------------------
Dividing network communication into 7 layers to provide a modular and standardized approach
OSI model serves as a framework for understanding and designing network architectures, making it easier to develop, troubleshoot, and maintain network systems.


Local Area Network
------------------
Local Area Network - network of interconnected devices within a limited geographic, same building, campus

Uses of LAN
-----------
- file and resource sharing
- communication
- collaboration
- internet connectivity
- centralized service

Wide Area Network
-----------------
WAN is a network that spans a large geographic area, connecting multiple LANs and other types of networks

Uses of WAN
-----------
- interconnecting LAN
- remote access
- enterprise connectivity- connecting different branches of an organization.
- internet connectivity
- wide scale data transfer


Internet
--------
it is a global network of interconnected computers and networks that used Internet Protocol(IP) to communicate

IP Address
----------
it is a numerical label assigned to a device connected to a network that uses Internet Protocol to communicate.

It can be IPv4 / IPv6

IPv4 Address
------------
consists of 4 sets of numbers separated by dots.(eg 192.168.1.1)
limited to approx. 4.3 billion unique addresses

IPv6 Address
------------
consists of eight groups of hexidecimal digits separated by colon: (2001:0db8:85a3:0000:0000:8a2e:0370:7334)
allows limitless number of unique addresses

developed to address the limitations of IPv4

Localhost
----------
refers to the loopback address, which is used to access the network services that are running on the host via the network interface. commonly used loopback IP address is 127.0.0.1.

Subnet
-------
It is division of an IP network into sub-networks to improve performance and security. 
It involves breaking down a larger network into smaller, more manageable segments. Each subnet has its own range of IP addresses. 



Transmission Control Protocol
------------------------------
provides a reliable, connection-oriented communication.

Ensures that data is delivered accurately and in the correct order.

Includes error-checking mechanisms and can retransmit lost packets.

TCP establishes a connection before data exchange

It is suitable for applications where accuracy and reliability are crucial, such as file transfers and web browsing. 



User Datagram Protocol
-----------------------
offers connectionless and lightweight communication.
it does not guarantee reliable data delivery, but it is faster as it does not establish a connection and has less overhead.

It does not establish a connection and sends data without prior negotiation.

UDP is preferred for real-time applications like online gaming and streaming, where speed is prioritized over data integrity.


Port
----
is a 16-bit number used to identify specific processes to which the data is sent or from which the data is received in a network environment. 

Ports help in directing network traffic to the appropriate application or service running on a device.

Port Numbers for SSH, HTTP, and HTTPS:
    SSH (Secure Shell): Port 22
    HTTP (Hypertext Transfer Protocol): Port 80
    HTTPS (Hypertext Transfer Protocol Secure): Port 443


Tool/Protocol to Check if a Device is Connected to a Network:

    The Internet Control Message Protocol (ICMP) is often used to check if a device is connected to a network. The ping tool, which is based on ICMP, is commonly used to send echo requests and receive echo replies. If a device is reachable, it responds to the ping, indicating its connectivity.