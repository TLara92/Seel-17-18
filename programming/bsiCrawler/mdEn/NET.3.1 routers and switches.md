1 description
--------------

### 1.1 Introduction

Routers and switches form the backbone of today's IT networks. Failure of one or more of these devices may result in the complete shutdown of the entire IT infrastructure. They must therefore be specially secured.

Routers work on the OSI layer 3 (network layer) and transmit data packets based on the destination IP address in the IP header. Routers are able to connect networks with different topographies. They are used to segment local area networks or to connect local area networks over wide area networks. A router identifies a suitable connection between the source system or source network and the destination system or destination network. In most cases, this is done by passing the data packets to the next router.

Switches originally worked on OSI Layer 2, but now they are available with different features. Manufacturers usually identify the devices with the OSI layer being supported. This gave rise to the terms layer 2, layer 3 and layer 4 switch, although layer 3 and layer 4 switches are actually already functionally routers. The originally different functions of switches and routers are thus often combined on one device.

### 1.2 Objective

The module describes how routers and switches are operated safely.

### 1.3 Delimitation

There is a large selection of different routers and switches from different manufacturers available in the market. The module does not describe specific requirements for specific products. He is as far as possible kept manufacturer independent.

By blending the functionality of routers and switches, most of the requirements can be used for both routers and switches. The present module does not differentiate between the device types.

Today, almost all operating systems also offer routing functionality. This block does not specify requirements for enabled routing functions in operating systems.

In addition, aspects of infrastructural safety (eg suitable installation or power supply or cabling) are not listed in this module, but can be found in the respective building blocks of the layer INF * Infrastructure *.

This module does not describe requirements for how virtual routers and switches can be protected. Security aspects of virtual active network components are dealt with in the module NET.1.4 * Network Virtualization *. Similarly, it will not address any existing firewall features of routers and switches. In addition, the block NET.3.2 * Firewall * must be implemented. Some aspects of network design and management are also relevant to the use of routers and switches and are mentioned in the context of the requirements. Further information on the structure, design and management of a network can be found in the building blocks NET.1.1 * Network architecture and design * and NET.1.2 * Network management *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to * routers and switches *:

### 2 1 Distributed Denial of Service (DDoS)

In a DDoS attack on a protected network, for example, by TCP SYN flooding or UDP packet storm, the router can fail due to the many network connections that need to be processed. This can result in certain services in the Local Area Network (LAN) becoming unavailable or the entire LAN failing.

### 2 2 Manipulation

If an attacker succeeds in gaining unauthorized access to a router or switch, he can reconfigure the devices or start additional services. For example, the configuration can be changed to block services, clients, or entire network segments.

### 2 3 Software vulnerabilities or errors

Routing and switch manufacturers regularly release updates and patches to address software bugs and known vulnerabilities in their products. However, if these are not recorded or played too late, the router or switch can be successfully attacked. This makes it possible for attackers to manipulate systems so that business-critical data drains, services fail, or entire production processes stand still.

### 2 4 Incorrect configuration of a router or switch

Routers and switches ship with a standard configuration in which many services are enabled. For example, login banners reveal the model and version number of the device. If routers and switches with insecure factory settings are used productively, they can be accessed more easily without authorization. This can lead to z. B. Services are no longer available.

### 2 5 Incorrect planning and conceptionMany institutions plan and design the use of routers and switches incorrectly. Among other devices are procured, which are not sufficiently dimensioned, z. For example, in terms of port number or performance. As a result, a router or switch is already overloaded when it is first used. As a result, services or entire networks may not be accessible and the error must be corrected consuming.

### 2 6 Incompatible active network components

Compatibility problems can arise in particular when existing networks are supplemented by active network components from other manufacturers or when networks are operated with network components from different manufacturers. If active network components with different implementations of the same communication method are operated together in one network, individual subareas of the network, certain services or even the entire network can fail.

### 2 7 MAC flooding

In MAC flooding, an attacker sends many requests with changing source MAC addresses to a switch. Once the switch has reached the limits of the MAC addresses it can store, it will send all requests to all IT systems on the network. This allows the attacker to see the network traffic.

### 2 8 spanning tree attacks

In spanning tree attacks, an attacker sends so-called Bridge Protocol Data Units (BPDUs) with the aim of making the switches look at their own (malicious) switch as a root bridge. This redirects network traffic through the attacker's switch so that he can log all information sent through him. As a result, he can initiate DDoS attacks and force the network to rebuild the spanning tree topology, causing the network to fail due to incorrect BPDUs.

### 2 9 GARP attacks

For Gratuitous ARP (GARP) attacks, the attacker sends unsolicited ARP responses to specific victims or to all IT systems on the same subnet. In this spoofed ARP response, the attacker enters his MAC address as a mapping to a foreign IP address and causes the victim to change his ARP table so that network traffic is now sent to the attacker instead of the valid target. Thereby he can record the communication between the victims or manipulate them.

3 requirements
---------------

The following are specific requirements for protecting * routers and switches *. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. He is also responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### NET.3.1.A1 Secure basic configuration of a router or switch

Before a router or switch is used, it MUST be securely configured. The devices MUST ONLY be installed and configured by authorized persons. All configuration changes SHOULD be traceable documented (see NET.3.2.A9 * operating documentation *). The integrity of the configuration files MUST be properly protected. Access passwords MUST be stored encrypted.

Routers and switches MUST be configured to use only mandatory services, protocols, and functional enhancements. Unnecessary services, protocols, and enhancements MUST be disabled or completely uninstalled. Also, unused interfaces MUST be disabled on routers and switches, or at least assigned to a dedicated * unassigned VLAN *.

If functional enhancements are used, the institution's security policies MUST continue to be met. Also SHOULD be justified and documented, why such extensions are used.

Information about the internal configuration and operating state MUST be hidden to the outside. Unnecessary information services MUST be disabled.

Before routers and switches are brought into operation, the default user accounts MUST be changed. Passwords of these accounts MUST be changed. Unused user accounts MUST be disabled. According to the rights and roles concept, the intended user accounts and roles MUST then be set up.

#### NET.3.1.A2 Importing Updates and PatchesThose responsible MUST inform themselves about known vulnerabilities. Updates and patches MUST be loaded as soon as possible. First, it should be checked on a test system, whether the security updates are compatible and do not cause any errors. Unless patches for known vulnerabilities are available, other appropriate measures MUST be taken to protect routers and switches.

It MUST be taken care that patches and updates are obtained only from trustworthy sources. If offered by the manufacturer, the update checksums SHOULD be compared or the digital signatures checked.

#### NET.3.1.A3 Restrictive assignment of rights

It must be regulated, who may access a router or switch. ONLY ONCE as many access rights must be granted as are required for the respective tasks (minimum principle). Unused user accounts MUST be removed. It MUST be ensured that administrator rights (or root rights) are only used when necessary.

#### NET.3.1.A4 Protection of administration interfaces

All administration and management accesses of the routers and switches MUST be restricted to individual source IP addresses or address ranges. It MUST be ensured that it is not possible to access the administration interfaces directly from untrusted networks.

To administer and monitor routers and switches, sufficiently encrypted protocols should be used. If unencrypted and thus insecure protocols are still used, a separate administration network (out-of-band management) MUST be used for the administration. The management interfaces and administration connections MUST be protected by a separate firewall. Suitable time limits MUST be specified for the interfaces.

All services not required for the management interface MUST be deactivated. If a network component has a dedicated hardware interface, unauthorized access to it MUST be prevented.

#### NET.3.1.A5 Protection against fragmentation attacks

At the router and Layer 3 switch, protections MUST be enabled to fend off both IPv4 and IPv6 fragmentation attacks.

#### NET.3.1.A6 Emergency access to routers and switches

It MUST always be possible for administrators to directly access routers and switches so that they can continue to be administered locally, even if the entire network fails.

#### NET.3.1.A7 Logging on Routers and Switches

A router or switch MUST be configured to log events such as:

* Configuration changes (as automatic as possible),
* Reboot,
* System error,
* Status changes per interface, system and network segment,
* Login errors (at least if they occur repeatedly)
The persons responsible MUST take care that the logging complies with all legal framework conditions. Changes to the configuration SHOULD also be automatically logged.

#### NET.3.1.A8 Regular backup

The configuration files of routers and switches MUST be backed up regularly. The backup copies MUST be stored so that they can be accessed in an emergency.

#### NET.3.1.A9 operating documentation

The most important operational tasks of a router or switch MUST be suitably documented. It SHOULD document all configuration changes as well as safety related tasks. The documentation SHOULD be protected against unauthorized access.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements are state-of-the-art in the area of ​​routers and switches. They SHOULD be implemented in principle.

#### NET.3.1.A10 Creation of a Security Policy [Information Security Officer (ISB)]

On the basis of the institution's general security policy, a specific security policy SHOULD be created in which comprehensible requirements and specifications are described, how routers and switches can be operated safely. The policy SHOULD be known to all administrators and fundamental to their work. If the policy is changed or deviated from the requirements, this should be agreed and documented with the ISB. It SHOULD be checked on a regular basis to see if the directive is still correctly implemented. The results SHOULD be suitably documented.

#### NET.3.1.A11 Obtain a router or switchBefore routers or switches are procured, a list of requirements SHOULD be created to evaluate the products available on the market. It SHOULD be ensured that the level of security sought by the institution can be achieved with the equipment to be procured. The basis for procurement SHOULD therefore be the requirements of the safety guideline.

#### NET.3.1.A12 Creation of a configuration checklist for routers and switches

IT SHOULD A CONFIGURATION CHECKLIST be created to check the most important security-related settings on routers and switches. Since the safe configuration depends heavily on the intended use, the different requirements of the devices in the configuration checklist SHOULD be taken into account.

#### NET.3.1.A13 Administration via a separate management network

Routers and switches SHOULD only be administered via a separate management network (out-of-band management). Any existing administration interface over the actual data network (in-band) SHOULD be deactivated. The available security mechanisms of the used management protocols for authentication, integrity assurance and encryption SHOULD be activated and all insecure management protocols deactivated (see NET.1.2 * Network Management *).

#### NET.3.1.A14 Protection against misuse of ICMP messages

IT SHOULD be ensured that the ICMP and ICMPv6 protocols are filtered restrictively.

#### NET.3.1.A15 Bogon and spoofing filtering

It SHOULD prevent intruders from entering the routers and switches using forged, reserved or unassigned IP addresses.

#### NET.3.1.A16 Protection against "IPv6 Routing Header Type-0" attacks

When using IPv6, mechanisms SHOULD be used to detect and prevent attacks on the Type-0 routing header.

#### NET.3.1.A17 Protection against DoS and DDoS attacks

It SHOULD use mechanisms that detect and fend off high-volume attacks as well as TCP state exhaustion attacks.

#### NET.3.1.A18 Setup of Access Control Lists

Access to routers and switches SHOULD be defined using Access Control Lists (ACL). In the ACL, the institution's security policy SHOULD specify which IT systems or networks are allowed to access a router or switch by which method. In the event that no specific rules exist, the more restrictive whitelist approach should generally be preferred.

#### NET.3.1.A19 Backup of switch ports

The ports of a switch SHOULD be protected against unauthorized access.

#### NET.3.1.A20 Security Issues of Routing Protocols

Routers SHOULD authenticate themselves by exchanging routing information or sending updates to routing tables. Only routing protocols that support this should be used.

Dynamic routing protocols SHOULD ONLY be used in secure networks. They MUST NOT be used in demilitarized zones (DMZ). In DMZs, static routes SHOULD be entered instead.

#### NET.3.1.A21 Identity and permissions management in the network infrastructure

Routers and switches SHOULD be connected to a central identity and authorization management (see ORP.4 * Identity and authorization management) *.

#### NET.3.1.A22 Emergency Prevention for Routers and Switches

To be able to react effectively and quickly in disruptive situations, diagnosis and troubleshooting should be planned and prepared in advance. For typical failure scenarios, appropriate action instructions SHOULD be defined.

The emergency plans for routers and switches SHOULD be aligned with the comprehensive incident and emergency preparedness and based on the general emergency preparedness concept (see DER.4 * emergency management *). It SHOULD be ensured that the documentation on emergency preparedness and the instructions contained therein exist in paper form. The procedure descriptions necessary in the emergency preparedness SHOULD be rehearsed regularly.

#### NET.3.1.A23 Revision and Penetration Tests

Routers and switches SHOULD regularly check for known security issues. Also, regular revisions should be made. It SHOULD z. For example, check whether the actual status corresponds to the specified safe basic configuration. The results SHOULD be traceable documented and compared with the target state. Deviations SHOULD be investigated.

### 3.3 Requirements for increased protection requirements