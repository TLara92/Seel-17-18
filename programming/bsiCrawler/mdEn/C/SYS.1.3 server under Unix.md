1 description
--------------

### 1.1 Introduction

Server systems often use the Linux or Unix operating systems. Examples of classic Unix systems are the BSD series (FreeBSD, OpenBSD and NetBSD), Solaris and AIX. Linux is not a classic Unix (the kernel is not based on the original source code from which the various Unix derivatives have developed), but a functional Unix system. This module considers all operating systems of the Unix family, including Linux as a functional Unix system.

Linux is free software and is developed by the open source community. In addition, there are providers who combine the various software components into a distribution and maintain, as well as offer other services. For Linux servers are often the distributions

* Debian
* Red Hat Enterprise Linux
* SUSE Linux Enterprise Server
* Ubuntu server
used. In addition, there are custom Linux distributions for specific applications and devices, such as Endian for firewall systems, OpenMediaVault for NAS systems, or OpenWRT for routers.

The services offered on a server are often central and therefore exposed to a special degree. As a result, Unix servers are not only critical for business processes, but are often the focus of attackers. Therefore, the availability and security of Unix servers is of particular importance.

### 1.2 Objective

The goal of the module is to protect information processed by Unix servers. The requirements of the block primarily address Linux servers, but can generally be adapted for Unix servers. Requirements are formulated on how the operating system should be configured and operated.

### 1.3 Delimitation

The module contains basic requirements for setting up and operating Unix servers. It concretizes and complements the aspects that are dealt with in the module SYS.1.1 General Server to specifics of Unix systems.

If the server is not to be managed by itself, but is hosted by third parties, the requirements of the module OPS.3.1 Outsourcing usage must also be taken into account. Security requirements of possible server functions such as web server (APP.3.2 web server) or server for groupware (see APP.5.1 groupware) are the subject of our own modules, with the exception of the Unix-specific server services NIS, NFS and SSH, which are also included in this module be treated. The topic of virtualization is illuminated in the module SYS.1.5 Server Virtualization. This module is about the basic protection at the operating system level with on-board resources, regardless of the intended use of the server.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the * * server under Unix area:

### 2 1 Spying on system and user information

Through various Unix programs it is possible to query data that the IT system stores about the users. This also affects data that can provide information about the performance profile of a user. This information includes information about additional logged-in users as well as technical information about operating system installation and configuration.

For example, with a simple program that evaluates the information provided by the "who" command at a particular time interval, each user can create an accurate usage profile for an account. For example, this can be used to determine the absence time of the system administrator or administrators in order to use these times for unauthorized actions. It is also possible to determine which terminals are allowed for privileged access. Other programs with similar abuses are "finger" or "ruser".

### 2 2 Exploitation of the script environmentIn Unix operating systems, the use of scripting languages ​​is widespread. Scripts are a collection of individual commands that are stored and called up in a text file. The rich functionality of the scripting environment allows attackers to leverage scripts for their own purposes. In addition, the containment of activated scripting languages ​​is very difficult.

### 2 3 Dynamic loading of shared libraries

The command line option "LD \ _PRELOAD" loads the given library before any other libraries needed in an application and its functions are used by the application. An attacker could manipulate the operating system to carry out malicious use of certain applications.

3 requirements
---------------

The following are specific requirements for the server area under Unix. Basically, the IT operation is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### SYS.1.3.A1 User authentication under Unix

To use the Unix server, users MUST authenticate themselves to the IT system. Authentication over a network MUST be encrypted. If only certain services may be used with a user account, the user account MAY NOT be used for other services.

#### SYS.1.3.A2 Careful assignment of IDs

Each login name, user ID (UID) and group ID (GID) MUST occur only once. Each user MUST be a member of at least one group. Any GID found in the / etc / passwd file MUST be defined in the / etc / group file. Each group SHOULD only contain the users that are absolutely necessary. In networked systems MUST also be taken to ensure that the assignment of user and group names, UID and GID in the system network is consistent.

#### SYS.1.3.A3 Automatic integration of removable drives

Removable drives such. B. USB sticks or CDs / DVDs MUST NOT be included automatically.

#### SYS.1.3.A4 Protection of applications

To make it more difficult to exploit vulnerabilities in applications, "ASLR" and "DEP / NX" MUST be enabled in the kernel and used by the applications. Security features of the kernel and standard libraries, such as: Heap and stack protection, MUST NOT be disabled.

#### SYS.1.3.A5 Secure installation of software packages

The integrity and authenticity of the software packages to be installed MUST always be checked. The software packages MUST be unpacked, configured and translated under an unprivileged user account. Only the last step, the actual installation of the translated program, can be done with higher privileges. The software to be installed MAY NOT be installed uncontrolled in the root file system of the server.

If the software is translated from the source code then the selected parameters SHOULD be suitably documented. Based on this documentation, the source code SHOULD be able to be compiled comprehensibly and reproducibly at any time. All further installation steps SHOULD also be documented so that the configuration can be quickly reproduced in an emergency.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​servers under Unix. They SHOULD be implemented in principle.

#### SYS.1.3.A6 Administration of users and groupsTo manage users and groups SHOULD use the appropriate administration tools. From a direct editing of the configuration files "/ etc / passwd" and "/ etc / group" and "/ etc / sudoers" SHOULD be omitted.

#### SYS.1.3.A7 Additional protection for single-user and recovery mode access

The UNIX server SHOULD be secured by assigning a boot password in the firmware of the server. Alternatively, a predefined boot order with built-in boot disk SHOULD be set first and the bootloader backed up.

#### SYS.1.3.A8 Encrypted access via Secure Shell

To build an encrypted and authenticated interactive connection between two IT systems, SSH should be used exclusively. All other protocols whose functionality is covered by Secure Shell SHOULD be completely disabled.

#### SYS.1.3.A9 Hedging the boot process

When booting, the integrity of the (pre-) bootloader to the kernel SHOULD be checked. The keys used for this purpose SHOULD be checked during initial setup. It SHOULD be checked if Secure Boot could be used as part of the UEFI specification.

#### SYS.1.3.A10 Prevention of spread when exploiting vulnerabilities

Services and applications SHOULD be secured with individual security policies (eg with AppArmor or SELinux). Also chroot environments as well as LXC- or Docker-container SHOULD be considered. It SHOULD be ensured that the supplied standard profiles or rules are activated.

#### SYS.1.3.A11 Use of the security mechanisms of NFS

Only dedicated servers SHOULD share directories with other clients (see also APP.3.3 Fileserver). It should be exported via NFS (Network File System) only directories that are absolutely necessary. In the files "/ etc / exports" or "/ etc / dfs / fstab" the mountable directories SHOULD be reduced to the necessary size. The mountable directories SHOULD only be released for certain IT systems and users, taking into account the defined authorization structure.

#### SYS.1.3.A12 Use of the security mechanisms of NIS

NIS (Network Information Service) SHOULD ONLY be used in a secure environment. In / etc / passwd, / etc / group and all other security-related files, the entry "+ :: 0: 0 :::" SHOULD NOT be included. The server process "ypserv" SHOULD only answer requests from predefined hosts.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### SYS.1.3.A13 Additional protection of privileged credentials (CI)

The passwords of the administrative accounts SHOULD be divided into several parts and additionally protected by applying the four-eyes principle. Alternatively, the authentication SHOULD be done with smartcards.

Also, administrative accounts SHOULD be set up to be locked after a predetermined number of failed login attempts.

#### SYS.1.3.A14 Preventing spying on system and user information (C)

The output of information about the operating system and the access to protocol and configuration files SHOULD be limited to the necessary extent for users. In addition, no sensitive information should be passed as parameter during command calls.

#### SYS.1.3.A15 Additional safeguarding of boot process (CIA)Bootloader and Kernel SHOULD be signed by self-controlled key material and unneeded key material should be removed.

#### SYS.1.3.A16 Additional prevention of propagation in the exploitation of vulnerabilities (CI)

The use of system calls SHOULD be limited to the absolutely necessary system calls, especially for exposed services and applications. The default profiles or rules of e.g. SELinux, AppArmor SHOULD be manually checked and, if necessary, adapted to your own security policies. If necessary, new rules or profiles SHOULD be created.

#### SYS.1.3.A17 Additional Kernel Protection (CI)

With specially hardened kernels, it SHOULD use appropriate protection mechanisms such as storage protection, file system protection, and role-based access control designed to prevent exploitation of vulnerabilities and propagation in the operating system.

4 Further Information
------------------------------

### 4.1 Literature

Further information on threats and security measures in the section "Servers under Unix" can be found in the following publications, among others:

* #### [ISi server] Securing a server (ISi server), BSI, 09.2013

  

 Federal Office for Security in Information Technology, 02.2017
 <Https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR02102/BSI-TR-02102-2.pdf>

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008
 <Https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary threats are important for the "Server under Unix" building block.

* G 0.14 Spying out information (spying)
* G 0.20 Information or products from unreliable sources
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.25 Failure of devices or systems
* G 0.28 Software vulnerabilities or errors
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.31 Incorrect use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.39 Malware
* G 0.43 Importing messages
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.