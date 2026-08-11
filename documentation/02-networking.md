\# 02 - Network Configuration and Connectivity



\## Overview



Networking is a core part of Mirage Lab because defensive security requires understanding how systems communicate and where traffic enters and leaves a system.



The Ubuntu Server VM was configured with two network interfaces using VirtualBox.



\---



\## Network Interfaces



The Ubuntu server was inspected using:



```bash

ip addr



Two active interfaces were identified.





Interface 1 - enp0s3

IP: 10.0.2.15/24



This interface is connected through VirtualBox NAT.



Its primary purpose is providing the Ubuntu VM with outbound Internet connectivity.



The routing table showed:



default via 10.0.2.2 dev enp0s3



Therefore:



10.0.2.2



is the default gateway for this interface.



Interface 2 - enp0s8

IP: 192.168.56.101/24



This interface is connected to the VirtualBox Host-Only network.



The corresponding network is:



192.168.56.0/24



The broadcast address is:



192.168.56.255



This interface allows direct communication between the Windows host and the Ubuntu VM.



Why Host-Only Networking?



The Host-Only interface is particularly useful for the security lab because it creates a controlled communication path between the Windows host and the Ubuntu server.



The Windows host can communicate with:



192.168.56.101



without requiring the Ubuntu VM to expose the lab services directly to the physical network.



This makes the interface useful for:



SSH administration

Controlled security testing

Network troubleshooting

Traffic analysis

Future honeypot experiments



Connectivity Test



Connectivity between the Windows host and Ubuntu VM was verified using:



ping 192.168.56.101



The result was:



Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)

Average = 1 ms



This confirmed that the Host-Only network was functioning correctly.



Internet Connectivity



The Ubuntu server was also able to communicate with external destinations through the NAT interface.



For example:



ping -c 4 8.8.8.8



was successful.



This demonstrated connectivity through the NAT interface.



DNS resolution was also tested using:



ping -c 4 google.com



The hostname resolved to an IP address and the ICMP requests received replies.



This confirmed both network connectivity and functional DNS resolution.



**Routing Table**



The routing table was inspected using:



ip route



Important entries included:



default via 10.0.2.2 dev enp0s3

10.0.2.0/24 dev enp0s3

192.168.56.0/24 dev enp0s8



These entries demonstrate that Ubuntu knows how to reach both networks.



**Simplified routing logic**



**Destination: Internet**

&#x20;       **|**

&#x20;       **v**

**10.0.2.2 gateway**

&#x20;       **|**

&#x20;     **enp0s3**

&#x20;       **|**

&#x20;     **NAT**

&#x20;       **|**

&#x20;   **Internet**





**Destination: 192.168.56.0/24**

&#x20;       **|**

&#x20;       **v**

&#x20;     **enp0s8**

&#x20;       **|**

**192.168.56.101**

&#x20;       **|**

&#x20;  **Windows Host**



**SSH Connectivity:**



The Host-Only interface was used for SSH administration.



Windows connected to Ubuntu using:



ssh roney@192.168.56.101



This was possible because both systems were connected to the same Host-Only network.



**The connection path was:**



**Windows Host**

**192.168.56.1**

&#x20;     **|**

&#x20;     **| Host-Only Network**

&#x20;     **|**

**Ubuntu Server**

**192.168.56.101**

&#x20;     **|**

&#x20;     **| TCP port 22**

&#x20;     **|**

&#x20;    **SSH**



**Network Security Relevance**



The network configuration demonstrated an important defensive-security concept:



Network security begins with understanding which interfaces exist, what addresses they use, how traffic is routed, and which services are reachable through those interfaces.



Before applying security controls, the system's network exposure should be understood.



This network mapping became the foundation for later SSH hardening and firewall configuration.

