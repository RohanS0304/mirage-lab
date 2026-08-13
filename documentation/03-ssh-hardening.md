**# 03 -** **SSH Hardening**



\## Overview



SSH is one of the primary remote administration services used in Mirage Lab.



The initial SSH configuration allowed password authentication. The configuration was subsequently hardened to require public-key authentication.



\---



\## Initial SSH Configuration



The effective SSH configuration was inspected using:



```bash

sudo sshd -T



**The initial configuration showed:**



port 22

permitrootlogin prohibit-password

pubkeyauthentication yes

passwordauthentication yes



This confirmed that public-key authentication was enabled, but password authentication was still permitted.





**SSH Hardening**



A dedicated SSH configuration file was created:



/etc/ssh/sshd\_config.d/00-mirage-hardening.conf



The following settings were applied:



PasswordAuthentication no

KbdInteractiveAuthentication no

PubkeyAuthentication yes

PermitRootLogin prohibit-password





**Configuration Validation**



Before reloading SSH, the configuration syntax was tested using:



sudo sshd -t



No output was returned, indicating that the configuration syntax was valid.



SSH was then reloaded:



sudo systemctl reload ssh





**Effective Configuration**



The final effective configuration was verified using:



sudo sshd -T | grep -E '^(port|permitrootlogin|passwordauthentication|kbdinteractiveauthentication|pubkeyauthentication)'



The resulting configuration was:



port 22

permitrootlogin prohibit-password

pubkeyauthentication yes

passwordauthentication no

kbdinteractiveauthentication no



This confirmed that password-based SSH authentication was disabled.



**Authentication Verification**



A fresh SSH connection was established from the Windows host:



ssh roney@192.168.56.101



The connection successfully authenticated using the user's Ed25519 private key.



This demonstrated that public-key authentication remained functional after password authentication was disabled.



**The SSH connection path was:**



Windows Host

192.168.56.1

&#x20;     |

&#x20;     | Host-Only Network

&#x20;     |

Ubuntu Server

192.168.56.101

&#x20;     |

&#x20;     | TCP/22

&#x20;     |

OpenSSH

&#x20;     |

Ed25519 public-key authentication



Security Improvements



**The hardening provided the following improvements:**



Password-based SSH authentication disabled

Keyboard-interactive authentication disabled

Public-key authentication explicitly enabled

Root password-based SSH login prohibited

SSH configuration syntax validated before reload

Effective configuration verified after reload

Fresh remote login tested successfully



**Key Learning**



A configuration file alone does not prove that a security control is active.



The SSH hardening process followed a verification-based approach:



Configure

&#x20;   ↓

Validate syntax

&#x20;   ↓

Reload service

&#x20;   ↓

Inspect effective configuration

&#x20;   ↓

Test a fresh connection



This demonstrated the importance of verifying the actual security state of a system rather than assuming that a configuration change has taken effect.



**Status**



SSH hardening completed and verified.



Future improvements may include:



Restricting SSH access through firewall rules

Improving SSH logging and alerting

Investigating authentication anomalies

Integrating SSH-Watch with the hardened SSH configuration

