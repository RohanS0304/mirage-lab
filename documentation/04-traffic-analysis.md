**# 04 — Traffic Analysis with tcpdump and Wireshark**



\## Objective



This phase focused on observing and analyzing SSH network traffic generated inside the Mirage Lab environment.



The goal was to understand how an SSH connection appears at the packet level and to become familiar with basic network traffic analysis using tcpdump and Wireshark.



\## tcpdump



tcpdump was used from the Ubuntu VM to capture traffic on the host-only interface:



text

enp0s8



The host-only interface was used because it provides the controlled lab network between the Windows host and Ubuntu VM.



**SSH traffic was captured using:**



sudo tcpdump -i enp0s8 -nn 'tcp port 22'



A packet capture was also saved for later analysis:



sudo tcpdump -i enp0s8 -nn -w \~/ssh-capture.pcap



The resulting PCAP file was opened in Wireshark for detailed inspection.

**TCP Three-Way Handshake**



The captured SSH connection began with the TCP three-way handshake:



Client → Server    SYN

Server → Client    SYN + ACK

Client → Server    ACK



The handshake establishes the TCP connection before SSH application data is exchanged.



In the captured session:



Client: 192.168.56.1

Server: 192.168.56.101

Server Port: 22



The client used an ephemeral source port while the Ubuntu SSH server listened on port 22.

**SSH Protocol Exchange**



After the TCP connection was established, the SSH protocol began its negotiation.



The capture showed:



Client SSH version identification

Server SSH version identification

Client Key Exchange Init

Server Key Exchange Init

Curve25519-based key exchange

Server key-exchange reply

New Keys

Encrypted SSH traffic



The SSH versions observed in the capture identified OpenSSH implementations on both sides.

**Key Exchange**



The captured session used:



curve25519-sha256



as the key-exchange method.



The server's key-exchange reply included:



ECDH server's ephemeral public key

KEX host key

KEX host signature



The host key was identified as:



ssh-ed25519



The ephemeral key-exchange material is used to establish fresh session key material, while the host key helps authenticate the server during the exchange

**Encrypted SSH Traffic**



After the key exchange completed, the capture showed:



New Keys



followed by:



Encrypted packet



The session identified:



chacha20-poly1305@openssh.com



as the encryption algorithm.



At this point, the SSH application data was no longer directly readable from the packet capture.



This demonstrates the difference between observing network metadata and reading protected application contents.

**Wireshark Filters**



The following display filters were used during analysis.



Show SSH/TCP port 22 traffic:



tcp.port == 22



Show TCP packets with the SYN flag:



tcp.flags.syn == 1



These filters helped isolate the SSH connection and identify the TCP connection-establishment phase.

**Key Observations**



The traffic analysis demonstrated that:



SSH operates over TCP.

TCP establishes the connection before SSH communication begins.

SSH performs its own protocol and cryptographic negotiation after TCP is established.

Key exchange occurs before encrypted application traffic.

Packet captures can reveal useful metadata such as IP addresses, ports, protocol versions, packet sizes, and connection behavior.

Encryption prevents a passive observer from simply reading the contents of the SSH session.





**Security Relevance**



Packet analysis is useful for detecting unusual network behavior, investigating connections, and understanding how security protocols operate.



The techniques learned here will be used in later Mirage Lab phases to analyze activity generated against the honeypot.

