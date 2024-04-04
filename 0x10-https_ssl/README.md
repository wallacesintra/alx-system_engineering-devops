# HTTPS SSL

HTTPS (Hypertext Transfer Protocol Secure) relies on SSL (Secure Sockets Layer) or its successor TLS (Transport Layer Security) to provide secure communication over a computer network, typically the internet.

SSL and TLS serve several critical roles within HTTPS:

## 1. Encrytion

When client(such as web browser) communicates with a server over HTTPS, SSL/TLS ensures that the data exchanged between them is encryted.

Encryption scrambles the data in such a way that it can only be understood by the intended recipient (the server in this case) using a specific decryption key.

## 2. Authentication

SSL/TLS also provides authentication to verify the identity of the server and, in some cases, the client.

It ensures that the client is communicating with the intended server and not an imposter.

The server presents a digital certificate, which is issued by a trusted third party known as a Certificate Authority (CA). This certificate contains the server's public key and other identifying information. The client verifies the authenticity of the certificate by checking its digital signature against a list of trusted CAs stored on the client's device. If the verification is successful, the client establishes a secure connection with the server.

This authentication mechanism helps prevent man-in-the-middle attacks, where an attacker intercepts communications between the client and the server and poses as one of the parties involved.

## 3. Data Integrity

SSL/TLS ensures data integrity by using cryptographic algorithms to detect any tampering or alteration of data during transmission.

This prevents attackers from modifying the data being exchanged between the client and server without detection. By verifying the integrity of the data, SSL/TLS ensures that the information received by the recipient is exactly the same as what was sent by the sender, thus maintaining the trustworthiness of the communication.
