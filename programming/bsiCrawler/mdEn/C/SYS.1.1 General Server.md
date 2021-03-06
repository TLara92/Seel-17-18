1 description
--------------

### 1.1 Introduction

This module covers general security requirements for all IT systems that provide services to other IT systems, such as clients or other servers. These services may be basic services for the local or external network, but also allow e-mail exchange or offer databases and print services. Servers are of central importance to information technology and thus to the functioning work processes of an institution. Often, servers perform tasks without any direct interactive use by a user. In addition, there are server services that interact directly with the users and are not perceived at first glance as a server service, for example, X servers under Unix.

### 1.2 Objective

The goal of this module is to protect information that is processed, offered or transmitted on servers, as well as the related services.

### 1.3 Delimitation

Usually, server systems are run under operating systems that have specific security requirements in each case. For common server operating systems, the IT-Grundschutz Compendium has its own modules that specify this module. The module "general server" forms the basis for the concrete building blocks on which they are based. If a specific block exists for a considered system, it must be used in addition to the module General Server. If no specific module exists for server systems used, the requirements of this module must be suitably specified.

The specific services offered by the server are not part of this module. For these server services, additional blocks must be implemented in addition to this block, according to the results of the modeling according to IT-Grundschutz. Insofar as an interactive use by users is provided for a server system in individual cases (eg terminal server), the associated security aspects are likewise to be considered separately, for example by applying the corresponding concretized components.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance to General Servers.

### 2 1 Software vulnerabilities or errors

The more complex the software, the more frequently programming or design errors occur. Software vulnerabilities are unintentional program errors that are not or not yet known to the user and that pose a security risk to the IT system. There are constantly new security vulnerabilities found in existing, even in widespread or completely new software.

If software errors are not detected and corrected promptly, the errors that arise during the application can have far-reaching consequences. With widespread standard software, software vulnerabilities can quickly lead to serious security problems for all types of institutions.

In particular, errors in server services can have serious consequences. In the case of a vulnerability or an error in a network service, local access rights are not required to exploit them; it is often enough for the attacker to be able to access the network. If the server offers the server service with the vulnerability or error on the Internet, it could potentially exploit this error or vulnerability from any IT system worldwide.

### 2 2 Data loss

The loss of data can have a significant impact on business processes and thus on the entire institution, especially for servers. Many IT systems, such as clients or other servers, often rely on the central data stored there being available.If business-relevant information of any kind is destroyed or falsified, business processes and specialized tasks can be delayed or even prevented from running. Overall, the loss of stored data, in addition to the loss and cost of recovering the data, especially long-term consequences, such as loss of trust among customers and partners, legal effects and a negative impact on the public lead. In many institutions regulations exist that no data may be stored on the local clients, but centralized storage on the servers must be used for this purpose. Data loss of this data then has serious consequences; the direct and indirect damage caused may even threaten the existence of institutions.

### 2 3 Prevention of services

One type of availability attack called "denial of service" aims to prevent users from using features or devices normally available to them. Often, this attack is associated with distributed resources, as an attacker uses these resources to the detriment of other users and prevents them from accessing the resources they depend on. In general, IT systems are also highly dependent on each other, the scarcity of resources of a server are quickly affected more servers. For example, CPU time, memory or bandwidth may be artificially curtailed, which may result in the service or resource being unusable at all.

### 2 4 Provision of unused operating system components and applications

Even with the installation of the server operating system, it is possible to install all supplied applications and services. Even in operation often software is installed, which is briefly tested, but then no longer needed. Often it is not known that these unused applications and services exist on the servers. In this way, there are numerous applications and services on the server, which are not used, thus unnecessarily burdening the server.

Such unused applications and services can contain vulnerabilities. If the applications are no longer updated then they can be an attack gate for attackers. If the installed applications and services are unknown, the IT operation is unaware that they also need to be updated.

### 2 5 overloading of servers

If servers are not adequately dimensioned, then at some point the point is reached where they no longer meet the requirements of the users. Depending on the type of systems involved, this can have a variety of negative consequences, such as the servers or services being temporarily unavailable, or data loss. Overloading a single server in complex IT landscapes can cause problems or failures for other servers.

Triggers for the overload of information systems can be that

* installed services or applications are misconfigured, unnecessarily consuming memory
* existing storage capacities are exceeded,
Numerous requests at the same time overstrain a system and overload the processors,
* too much computing power is claimed by the services or
* a large number of messages will be sent at the same time.
3 requirements
---------------The following are specific requirements for general server protection. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### SYS.1.1.A1 Suitable installation [building services]

Servers MUST be operated in locations to which only authorized persons have access. Servers MUST therefore be installed or installed in data centers, computer rooms or lockable server cabinets, see the relevant modules. It is MUST be regulated who gets access to the rooms or physical access to the server itself. Servers MUST NOT be used as workstations.

It is important to ensure proper spatial separation of the systems to be backed up from backup systems, such as backup servers in different firing ranges, to limit the impact of physical damage.

#### SYS.1.1.A2 user authentication

To use the server, users MUST authenticate themselves to the IT system. If users and administrators use passwords, secure passwords MUST be used. There should be a password policy for this. These passwords MUST be complex enough to be kept secret and changed regularly.

#### SYS.1.1.A3 Restrictive rights assignment

Access rights to files stored on servers MUST be restricted. Each user MAY only get access to the files he needs to perform his task. The access right itself MUST be limited to the necessary access, so it is for example in the rarest cases necessary to assign a write right to program files.

It SHOULD be checked periodically if the permissions, especially for system directories and files, comply with the requirements of the security policy. System files SHOULD have access only to system administrators if possible. The circle of authorized administrators SHOULD be kept as small as possible. Even system directories SHOULD only provide the necessary privileges for the users.

#### SYS.1.1.A4 Role separation

It MUST be ensured that identifiers with administrator rights are only used for administration tasks. For all administrators, additional user IDs MUST be set up, which have only the limited rights that administrators need to perform non-administration tasks. For non-administration work, administrators MUST use only these user identifiers. Beyond the necessary user IDs, no additional users SHOULD be created on the server.

#### SYS.1.1.A5 Protection of administration interfaces

Depending on the type of access used (local, remote or central system management), suitable security measures MUST be taken. The methods used for administration MUST be specified in the security policy. The administration MUST be performed according to the security policy.

To register users and services with the system, authentication procedures MUST be used that are appropriate to the protection needs of the servers. This should be taken into special account for administrative access. As far as possible, use should be made of central, network-based authentication services.The administration MUST be done via secure protocols. It SHOULD be considered, alternatively set up a separate administration network.

#### SYS.1.1.A6 Deactivation of unneeded services and identifiers

All unnecessary services MUST be disabled or uninstalled by servers, especially network services. Unnecessary user IDs MUST either be deleted or at least deactivated in such a way that no logins to the system are possible under these IDs. Existing standard IDs MUST be changed or deactivated as far as possible. Default passwords of standard identifiers MUST be changed. On servers, the space SHOULD be suitably restricted for individual users, but also for applications.

The decisions made SHOULD be documented in such a way that it is possible to trace the configuration and software equipment selected for the servers.

#### SYS.1.1.A7 Updates and patches for firmware, operating system and applications

Administrators MUST regularly check for known vulnerabilities in operating systems, applications, and services. The identified vulnerabilities MUST be fixed as soon as possible so that they can not be exploited by attackers. Generally MUST be taken to ensure that patches and updates are obtained only from trusted sources.

Unless patches are available, other appropriate measures to protect the system MUST be made, depending on the severity of the vulnerabilities and threats.

#### SYS.1.1.A8 Regular backup

Data backups MUST be made prior to installation and extensive configuration changes, as well as at fixed intervals. These MUST allow you to restore the data stored on the server. In virtual environments, SHOULD check if the system backup can be realized by snapshot mechanisms of the virtualization environment.

#### SYS.1.1.A9 Use of virus protection programs

Depending on the operating system installed, the service provided and other existing server protection mechanisms MUST be checked as to whether virus protection programs should and can be used. Concrete statements as to whether virus protection is necessary can generally be found in the operating system-specific blocks of IT-Grundschutz. The corresponding signatures of a virus protection program MUST be updated regularly. In addition to real-time and on-demand scans, a solution MUST provide the ability to scan even compressed and encrypted data for malicious programs.

#### SYS.1.1.A10 logging

It MUST be decided which information should be logged by the server at least, how long the log data is kept and who can see the log data under which conditions. Data protection regulations MUST be considered. In general, all safety-related system events MUST be logged. These include at least:

* System starts and reboots,
* successful and unsuccessful logins to the system (operating system and application software),
* failed authorization checks,
* blocked data streams (violations of ACLs or firewall rules),
* Setup or changes of users, groups and permissions,
* safety-relevant error messages (eg hardware defects, exceeding of capacity limits),
* Warning messages from security systems (eg virus protection).
### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​general servers. They SHOULD be implemented in principle.

#### SYS.1.1.A11 Setting a security policy for serversBased on the general security policy of the institution, the requirements for servers SHOULD be specified. The policy SHOULD be known to all administrators and other persons involved in the procurement and operation of the servers and should be the basis for their work. The implementation of the content required in the directive SHOULD be regularly reviewed and the results SHOULD be documented in a meaningful way.

#### SYS.1.1.A12 Planning the server deployment

Each server system SHOULD be planned appropriately, taking into account at least the following points:

* Choice of hardware platform, operating system and application software
* Dimensioning of the hardware (power, memory, bandwidth, ...)
* Type and number of communication interfaces
* Power consumption and heat load, space requirement and design
* Implementation of administrative accesses (see SYS.1.1.A3 Protection of the administration interfaces)
* User access
* Realization of logging (see SYS.1.1.A7 logging)
* Implementation of the system update (see SYS.1.1.A5 Updates and patches for operating system and applications)
* Integration into system and network management, data backup and protection systems (virus protection, IDS, etc.)
All decisions made in the planning phase SHOULD be documented in a way that can be understood later.

#### SYS.1.1.A13 Obtaining servers

Before one or more servers are procured, a list of requirements SHOULD be created to evaluate the products available on the market.

#### SYS.1.1.A14 Creation of a user and administration concept

Process, conditions and requirements for administrative tasks, as well as the task separation between the different roles of the users of the IT system SHOULD be codified in a user and administration concept.

#### SYS.1.1.A15 Uninterruptible and stable power supply [Building Services]

Each server SHOULD be connected to an uninterruptible power supply (UPS). The UPS SHOULD be sufficiently dimensioned in terms of power and support time. If changes have been made to the consumers, SHOULD check again if the support time is sufficient. Both the UPS devices and the servers SHOULD have an overvoltage protection.

The actual capacity of the battery and thus the support time of the UPS SHOULD be tested regularly. The UPS SHOULD be maintained regularly. The UPS SHOULD be integrated into an existing system and network management.

#### SYS.1.1.A16 Secure installation and basic configuration of servers

Servers SHOULD be set up so that only the required services are selected during installation. Installations on a server SHOULD only be performed by authorized persons (administrators or contracted service providers) according to a defined installation process. System and application software SHOULD be obtained from trusted installation sources. For repetitive installations, suitable installation templates SHOULD be created and applied.

All installation steps SHOULD be documented in such a way that the installation can be reconstructed and repeated by a knowledgeable third party based on the documentation.

The default settings of servers SHOULD be reviewed and, if necessary, adjusted according to the security policy. Only after the installation and the configuration is completed, the server SHOULD be connected to the internet.

#### SYS.1.1.A17 deployment clearanceBefore the server system is used in productive operation and before it is connected to a productive network, a deployment clearance SHOULD be made. This SHOULD be suitably documented. For deployment clearance, the installation and configuration documentation and system functionality SHOULD be tested in a test. It SHOULD be done by a body authorized to do so in the institution.

#### SYS.1.1.A18 Encryption of communication links

For all network services offered and used by the server, it should be checked whether encryption of the communication connections is possible and practicable with reasonable effort. If this is possible with reasonable effort, the encryption SHOULD be activated.

#### SYS.1.1.A19 Set up local packet filter

Existing local packet filters SHOULD be configured via a set of rules so that the incoming and outgoing communication is restricted to the required communication partners, communication protocols or ports and interfaces.

#### SYS.1.1.A20 Restriction of access via networks

In general, the entire network of an institution SHOULD be protected by a corresponding security gateway against unauthorized access. Servers that provide services to the outside SHOULD be deployed in a Demilitarized Zone (DMZ).

Servers SHOULD NOT be placed on the same IP subnet as the clients. Servers SHOULD at least be separated from the clients by a router.

#### SYS.1.1.A21 Operation documentation

Operational tasks that are performed on a server SHOULD be traceable documented (who, when, what, what?). In particular, configuration changes SHOULD be traceable from the documentation. Security-related tasks (for example, who is authorized to install new hard disks) SHOULD be documented. Everything that can be automatically documented SHOULD also be automatically documented. The documentation SHOULD be protected against unauthorized access and loss.

#### SYS.1.1.A22 Integration into emergency planning

The server SHOULD be considered in the emergency management process. To this end, the emergency requirements for the system SHOULD be determined and appropriate emergency measures implemented, eg. By creating recovery plans or by securely storing passwords and cryptographic keys.

#### SYS.1.1.A23 system monitoring

The server system SHOULD be integrated into a suitable system monitoring or monitoring concept, which continuously monitors the system status and the functionality of the system and the services operated on it, and reports fault conditions and the exceeding of defined limit values ​​to the operating personnel.

#### SYS.1.1.A24 security checks

Server systems SHOULD undergo regular security testing that verifies compliance with security requirements and identifies any vulnerabilities that may exist. This SHOULD be especially true for systems with external interfaces. In view of indirect attacks on infected systems in their own network, however, internal server systems SHOULD also be checked in defined cycles. It SHOULD be checked if the security checks are also automated, eg. B. by means of suitable scripts can be realized.

#### SYS.1.1.A25 Regulated decommissioning of a server

When decommissioning a server SHOULD ensure that no important data that may be stored on the disks are lost, and that no sensitive data is left behind. It SHOULD give an overview of what data is stored on the server. It SHOULD also be ensured that services offered by the server have been taken over by another server, if necessary.It SHOULD create a checklist that can be processed when a server is decommissioned. This checklist SHOULD include at least aspects of data backup, migration of services and the subsequent secure deletion of all data.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.1.1.A26 Multi-factor authentication (C)

With a higher protection requirement, a secure two- or more-factor authentication for access to the server SHOULD be set up. B. with cryptographic certificates, smart cards or tokens. First and foremost, all administrative accesses to the server SHOULD be secured with multi-factor authentication.

#### SYS.1.1.A27 Host-based Attack Detection (IA)

With the use of host-based intrusion detection systems (IDS), the system behavior SHOULD be monitored for anomalies and misuse. The used IDS / IPS mechanisms SHOULD be suitably selected, configured and extensively tested. In the case of attack detection, the operating personnel SHOULD be alerted appropriately.

Through operating system mechanisms or suitable additional products, changes to system files and configuration settings SHOULD be checked, restricted and reported.

#### SYS.1.1.A28 Redundancy (A)

Server systems with high availability requirements SHOULD be suitably protected against failures. For this, at least suitable redundancies SHOULD be available and / or maintenance contracts concluded with the suppliers. It SHOULD be checked to see if very high requirements require high availability architectures with automatic failover, possibly across different sites.

#### SYS.1.1.A29 Setting up a test environment (CIA)

In order to be able to test changes to the system or the configuration without jeopardizing the productive operation, appropriate test systems SHOULD be provided or made available as needed (eg as virtual images). The test systems SHOULD conform to the production systems as far as possible (software versions, configuration). For application systems, appropriate test data SHOULD be generated that does not include any sensitive or personal content of the productive data.

#### SYS.1.1.A30 One service per server (CIA)

Depending on the threat situation and the protection requirements of the services, only one service SHOULD be operated on one server.

#### SYS.1.1.A31 Application whitelisting (CI)

It should be ensured with increased protection requirements via application whitelisting that only permitted programs are executed. On the one hand, complete paths or directories should be defined from which this may be possible. On the other hand, alternatively, individual applications should explicitly be allowed execution.

4 Further Information
------------------------------

### 4.1 Literature

Additional information on threats and security measures in the "General Server" area can be found in the following publications, among others:

* #### [ISi server] Securing a server (ISi server), BSI, 09.2013

  

 Federal Office for Security in Information Technology, 02.2017
 <Https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102-2.pdf>

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008
 <Https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf>5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the module "General Server".

* G 0.8 Failure or malfunction of the power supply
* G 0.9 Failure or malfunction of communication networks
* G 0.14 Spying out information (spying)
* G 0.16 Theft of devices, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.26 Malfunction of equipment or systems
* G 0.27 Resource shortage
* G 0.28 Software vulnerabilities or errors
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.39 Malware
* G 0.40 Denial of Service
* G 0.43 Importing messages
* G 0.44 Unauthorized intrusion into premises
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.