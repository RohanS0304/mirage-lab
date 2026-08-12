\# Mirage Lab 🔐



A hands-on defensive cybersecurity home lab built to understand Linux security, networking, SSH hardening, firewall configuration, security logging, and basic threat detection.



\## 🎯 Objective



Mirage Lab is a personal cybersecurity laboratory running Ubuntu Server inside VirtualBox.



The goal is to learn defensive security by building, configuring, testing, and investigating a real Linux environment rather than relying only on theoretical study.



\## 🏗️ Lab Architecture



```text

Windows Host

          │

          │ VirtualBox

          ▼

Ubuntu Server

mirage-lab

          │

          ├── NAT Network

          │

          └── Host-Only Network

                  │

                  └── Windows Host




🔐 Security Configuration



The lab currently includes:



Ubuntu Server 26.04 LTS

VirtualBox virtualization

Dual network interfaces

SSH remote administration

SSH public-key authentication

SSH password authentication hardening investigated

Root SSH login restricted

UFW firewall

Default-deny incoming traffic

Explicit SSH access rule

Service and port enumeration

SSH authentication log analysis





🔎 Security Monitoring



SSH authentication logs were investigated using journalctl.



The lab was used to generate controlled failed authentication events and observe how Ubuntu records them.



Example workflow:

SSH Authentication Attempt

               ↓

              sshd

               ↓

           System Logs

               ↓

           Log Analysis

               ↓

         Suspicious Activity


🐍 SSH-Watch



ssh-watch is a small Python-based security monitoring tool developed as part of this lab.



It currently:



Reads SSH authentication logs

Identifies suspicious authentication events

Extracts usernames

Extracts source IP addresses

Extracts source ports

Groups events by source connection

Detects repeated authentication activity

Generates a basic brute-force warning



Example:

=== SSH Security Monitor v4 ===



Source IP analysis:



IP: 192.168.56.1

Unique connections: 4

🚨 ALERT: Possible brute-force activity



This is an educational detection tool and is not intended to replace production security monitoring systems.



📚 Skills Practiced

Linux administration

Linux networking

SSH

Public-key authentication

Firewall configuration

Network troubleshooting

Security logging

Log parsing

Python

Regular expressions

Basic security event correlation

Defensive security concepts

🚧 Roadmap



The lab is actively being developed.



Planned areas include:



Network traffic analysis

Packet inspection

Advanced log correlation

Improved SSH attack detection

Honeypot deployment

Security event investigation

Additional defensive security tooling

⚠️ Disclaimer



This laboratory is intended for educational purposes and controlled testing on systems owned or authorized by the user.



No unauthorized systems or networks are targeted.





