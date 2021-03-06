1 description
--------------

### 1.1 Introduction

A Programmable Logic Controller (PLC) is an ICS component. It handles control and regulating tasks in operational technology (English: Operational Technology, OT). The boundaries between different device classes and designs are today fluent: For example, a remote terminal unit (RTU) can take over the functions of a PLC or a Programmable Automation Controller (PAC) can try the advantages of a PLC and an industry To unite -PCs. However, the PLC is still the classic automation device, so in this module these terms are used synonymously.

A PLC has digital inputs and outputs, a real-time operating system (firmware) and other interfaces for Ethernet or fieldbuses. The connection to sensors and actuators takes place via the analog or digital inputs or outputs or via a fieldbus. Communication with process control systems usually takes place via the Ethernet interface and IP-based networks.

The possible implementations are manifold: PLCs can be used as a module, as a single unit, as a PC plug-in card (slot PLC) or as software emulation (soft PLC). The most common are modular PLCs, which are composed of different functional plug-in modules. Increasingly, other functions such as visualization, alarming and logging are realized by the PLC.

Due to the high availability requirements typical in the OT environment and the often extreme environmental conditions (climate, dust, vibration, corrosion), ICS components have always been designed as robust devices with high reliability and a long service life.

PLCs are usually configured or programmed using special software from the respective manufacturer. This is done either via so-called programming devices (eg as an application under Windows or Linux) or via an engineering station that distributes the data over a network.

### 1.2 Objective

The aim of the device is to protect all types of programmable logic controllers, regardless of manufacturer, type, purpose and location. It can be applied to a single PLC or a contiguous board used as a PLC.

### 1.3 Delimitation

The present system block is to be used to protect all types of programmable logic controllers (that is, PLCs and devices that integrate the same or similar functions). It supplements the module IND.2.1 * General ICS Component *. In the application this is therefore also to be considered.

The module contains no organizational requirements for securing an ICS component. For this, the requirements of the block IND.1 * Operating and Control Technology * must be implemented. Similarly, the area of ​​functional safety (safety) is not covered.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the field of PLC:

### 2 1 Incomplete documentation

Programmable logic controllers are often incompletely documented, so not all product functions are known. Information about the services used, protocols and communication ports as well as authorization management are often particularly incomplete. However, this makes the risk analysis more difficult because interfaces, functions and security-relevant mechanisms are overlooked. As a result, potential hazards can not be taken into account. In addition, it can not or only partially react to new vulnerabilities, if this is not detected.

3 requirements
---------------The following are specific requirements for the PLC area. Basically, the ICS Information Security Officer (ICS-ISB) is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the defined security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of programmable logic controller PLC. They SHOULD be implemented in principle.

#### IND.2.2.A1 Advanced System Documentation for Programmable Logic Controllers [ICS Administrator]

Control programs and configurations SHOULD always be archived if something is changed about them. Changes to the configuration or replacement of components SHOULD be fully documented.

#### IND.2.2.A2 User Account Control and Restricted Rights Assignment [ICS Administrator]

Access rights to functions and interfaces of a PLC SHOULD be assigned restrictively. Existing user accounts SHOULD periodically be checked to determine if they are still required, the assigned permissions are still correct. If something changes in the responsibilities of the employees, the permissions SHOULD be adjusted immediately.

#### IND.2.2.A3 Time Synchronization [ICS Administrator]

For the system time, a central automated time synchronization SHOULD be set up.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and safety measures in the area "programmable logic controller (PLC)" can be found in the following publications, among others

5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the block "Programmable Logic Controller (PLC)".

* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.19 Disclosure of information worthy of protection
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.41 Sabotage
The cross reference tables can be found in the download area due to their size.