# Postmortem : E-Commerce Checkout Outage(10:00 AM PST - 11:30 AM PST)

## Issue Summary

Our e-commerce platform experienced a checkout outage on Thursday, May 9th, 2024, from 10:00 AM PST to 11:30 AM PST. This resulted in people being unable to finalize their transactions for 1.5 hours. During this time, about 20% of our website traffic, or an estimated 1,000 individuals, was disrupted.

## Timeline

* 10:00 AM PST: Monitoring warnings were triggered, indicating an increase in unsuccessful transactions during the payment processing step.
* 10:05 AM PST: An engineer on duty researched the problem and discovered a large number of problems connected to database connection failures.
* 10:10 AM PST: The initial idea was that the database would be overloaded owing to increasing traffic. The database team was contacted and began looking into scaling alternatives.
* 10:30 AM PST: Despite scaling database resources, the problem persisted. Further analysis identified issues coming from the payment gateway API.
* At 10:45 a.m. PST, the matter was escalated to the payments team and payment gateway provider.
* 11:00 AM PST: The payment gateway provider discovered a configuration mistake on their end that was resulting in invalid requests from our platform.
* 11:15 AM PST: The payment gateway provider implemented a patch on their end.
* 11:30 a.m. PST: Checkout functionality has been restored, and monitoring confirms steady operation.

## Root Cause and Resolution

The disruption was caused by a misconfiguration on the payment gateway provider's side. This setup issue caused our platform's requests to be refused, resulting in failed database transactions during checkout. The payment gateway provider implemented a hotfix to rectify the issue.

## Corrective and Preventive Measures

* Improved Communication: We will build a more direct communication route with our payment gateway provider to enable faster issue identification and resolution in the future.
* Enhanced Monitoring: To discover potential difficulties early on, we will add extra monitoring checks to the payment gateway API's health and configuration status.
* Redundancy Planning: We will look into adding a secondary payment gateway provider to provide redundancy in the event of a primary provider outage.

## TODO List

* Conduct a post-mortem review with all concerned teams (technical, payments, and customer service).
* Update internal documentation to reflect the payment gateway provider's new communication protocols.
* Add additional API health checks for the payment gateway.
* Evaluate and start the process of integrating a second payment gateway supplier.
