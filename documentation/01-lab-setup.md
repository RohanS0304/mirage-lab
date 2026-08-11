# 01 - Lab Setup



## Overview



Mirage Lab is a personal defensive cybersecurity laboratory built using VirtualBox and Ubuntu Server.



The purpose of the lab is to gain practical experience with Linux administration, networking, SSH security, firewall configuration, logging, and security monitoring in a controlled environment.



---



## Virtualization



The lab runs inside Oracle VirtualBox on a Windows host.



### Virtual Machine



- **Name:** mirage-lab

- **Operating System:** Ubuntu Server 26.04 LTS

- **Architecture:** x86-64

- **Memory:** 2048 MB

- **Processors:** 2

- **Virtual Disk:** 30 GB

- **Virtualization Platform:** Oracle VirtualBox



The VM provides an isolated environment where security configurations and controlled tests can be performed without directly modifying the Windows host.



---



## Network Configuration



The Ubuntu VM uses two network interfaces.



### Adapter 1 â€” NAT



Interface:



`enp0s3`



IP address observed:



`10.0.2.15/24`



Purpose:



- Provides outbound Internet connectivity.

- Allows Ubuntu to download updates and packages.

- Uses VirtualBox NAT for external network access.



The default gateway observed was:



`10.0.2.2`



---



### Adapter 2 â€” Host-Only Network



Interface:



`enp0s8`



IP address observed:



`192.168.56.101/24`



Purpose:



- Provides direct communication between the Windows host and the Ubuntu VM.

- Keeps lab testing separate from the normal external network.

- Allows the Windows host to connect to Ubuntu through SSH.

- Provides a controlled network for security experiments.



The Windows host was able to reach the Ubuntu VM using:



`192.168.56.101`



This was verified using:



```text

ping 192.168.56.101





**Network Architecture:**



&#x20;                Windows Host

&#x20;                     â”‚

&#x20;                     â”‚

&#x20;             Host-Only Network

&#x20;              192.168.56.0/24

&#x20;                     â”‚

&#x20;                     â”‚

&#x20;             192.168.56.101

&#x20;                Ubuntu VM

&#x20;                mirage-lab

&#x20;                     â”‚

&#x20;                     â”‚

&#x20;                 NAT Network

&#x20;                10.0.2.0/24

&#x20;                     â”‚

&#x20;                     â–¼

&#x20;                 Internet



**SSH Access**



SSH was configured on Ubuntu Server to allow remote administration from the Windows host.



The SSH service listens on TCP port 22.



The Windows host connects to the VM using:



ssh roney@192.168.56.101



This allowed administration of the Ubuntu server from Windows without needing to interact with the VM console for every command.



**Why Two Network Interfaces?**



Using two interfaces gives the lab a useful separation of responsibilities.



NAT



Used primarily for:



Internet access

Package updates

External connectivity



**Host-Only**



Used primarily for:



Windows â†” Ubuntu communication

SSH administration

Controlled security experiments

Future monitoring and honeypot work



This separation makes the lab easier to understand and reduces the need to expose experimental services directly to the physical network.



**Initial Verification**

**Several commands were used to understand the VM and its network configuration:**



uname -a

hostnamectl

ip addr

ip route

sudo ss -tulnp



These commands provided information about:



Kernel and operating system

Hostname

Network interfaces

IP addresses

Routing

Listening services and ports



Key Learning



The initial setup established an important defensive-security principle:



Before securing a system, understand what the system is, how it communicates, and which services are exposed.



The network configuration and service enumeration performed during this stage became the foundation for later SSH hardening, firewall configuration, log analysis, and security monitoring.








