1 description
--------------

### 1.1 Introduction

To limit damage and prevent further damage, detected security incidents must be dealt with quickly and efficiently. Therefore, it is necessary to establish a predetermined and proven procedure for the handling of security incidents (* Security Incident Handling or Security Incident Response) *.

A security incident can have a strong impact on an institution and cause major damage. For example, such incidents are misconfigurations that cause confidential information to be disclosed or criminal acts such Hacking of servers, theft of confidential information, sabotage or IT-related blackmail.

The causes of security incidents are manifold: Malware, obsolete system infrastructures, or perpetrators play a role. Attackers often exploit zero-day exploits. Another growing threat is Advanced Persistent Threats (APT).

In addition, users, administrators, or external service providers may not behave properly, causing system parameters to change security-critical or violate internal policies. Furthermore, the cause may be that access rights are violated, that software, hardware, or rooms and buildings in need of protection are insufficiently secured.

### 1.2 Objective

The aim of this module is to show a systematic way how a concept for the treatment of security incidents can be created.

### 1.3 Delimitation

The focus of this module is on the handling of security incidents from the point of view of information technology. However, before security incidents can be handled, they must be detected. Safety requirements for this are contained in block DER.1 * Detection of safety-relevant events * and are assumed in the present block. The initial forensic investigation is dealt with in the module DER.2.2 * Forensics * and the correction after an APT incident in the module DER.2.3 * Clearance of far-reaching security incidents (APT responders) *. A special area of ​​the treatment of security incidents is the emergency management, which is discussed in the module DER.4 * emergency management * and will not be considered further here. However, it should be noted that the decision as to whether an emergency exists or not, is made in the present module.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the handling of security incidents:

### 2 1 Inappropriate handling of security incidents

In practice, it can never be ruled out that security incidents will occur. This also applies if a large number of security measures have been implemented. Responding to acute security incidents either unresponsive or inadequate will result in major damage, including catastrophes. Examples are:

* In the log files of a firewall are noticeable entries. Failure to promptly assess whether the first sign of a break-in attempt is to allow attackers to pass the firewall unnoticed and penetrate the internal network of the institution with a successful attack.
* Vulnerabilities in the IT systems or applications used are known. If this information is not obtained on time and necessary countermeasures are not promptly initiated and implemented, these vulnerabilities can be exploited by attackers.Failure to take appropriate action to handle security incidents can result in wrong decisions in a hurry and under stress. These can be z. For example, misleading the press and causing a negative external impact, third parties being harmed by their own IT systems and claiming for damages, or no evasion or recovery measures being foreseen, thus significantly increasing the damage to the institution ,

### 2 2 Unrecognized security incidents

In the daily operation of an institution many errors and errors can occur. It may happen that security incidents are not identified as such by the personnel and an attack or attempted attack remains unrecognized. Even though the employees are sufficiently sensitized or trained for the interests of information security, it can not be ruled out that they do not recognize security incidents. Examples for this are:

* A user who has not been logged into the institution's local area network for a long time thinks that the significant slowdown in their notebook during the internet access that occurred a week ago is normal and does not detect that a malicious program is running in the background. He was not or insufficiently trained to inform the security officer in case of suspicious abnormalities.
* A production manager does not notice that the data in the production systems and also the control display systems have been secretly changed. He does not suspect, as the SCADA control of the production plant shows strange values, since this was only for a short time. The incident is not reported because all values ​​are back to the expected display values. Nobody is struck by the fact that a malicious software has manipulated the display values.
* A burglary in a store is considered a case of procuring crime as notebooks and flat screens have been stolen. The fact that the notebooks contained confidential information and access data for IT systems on the intranet is given no greater importance and the ISB is not informed. Therefore, the institution is not prepared for the subsequent attacks on the IT systems of other locations and the company headquarters. The attack uses the data found on the stolen notebooks.
### 2 3 Destruction of evidence traces in the handling of security incidents

Careless or non-compliant handling of security incidents may result in the inadvertent destruction or non-judicialization of important evidence traces for the investigation or subsequent legal prosecution.

Examples for this are:

* An attacker placed malicious software on a workstation, whose operation and target can only be analyzed while it is still running. For this, information about the active processes and the contents of the main memory would have to be backed up and evaluated. If the workstation is now shut down prematurely, the information from the current state can no longer be used to analyze and clarify the security incident.
* An administrator finds a running process on a server that causes an above-average CPU usage. In addition, this process creates temporary files and sends unknown information over the Internet. If the process is terminated prematurely and the temporary files are simply deleted, it can not be determined if confidential information has been successfully stolen.* An important server is compromised because the administrator could not bring in the latest security updates as planned due to the heavy workload and a lack of maintenance window. In order to avoid possible disciplinary consequences, the administrator enters the missing updates before a security team can analyze the reason for the break-in and the damage incurred. Lack of error culture has thus prevented an analysis of the problem.
3 requirements
---------------

The following are specific requirements for the handling of security incidents. Basically, the information security officer is responsible for meeting the requirements. The Information Security Officer (ISB) should always be involved in strategic decisions. In addition, the ISB is responsible for ensuring that all requirements are met and verified in accordance with the established security policy. In addition, there may be other roles that have additional responsibilities in the implementation of requirements. These are then listed explicitly in square brackets in the heading of the respective requirements.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### DER.2.1.A1 Definition of a security incident [Head IT]

In an institution MUST be clearly defined what a security incident is. A security incident MUST be separated as far as possible from disruptions in daytime operations. All employees involved in the incident handling process MUST know the definition of a security incident. The definition and entry thresholds SHOULD be based on the protection needs of the affected business processes, IT services, IT systems or IT applications.

#### DER.2.1.A2 Create a policy to handle security incidents

A policy to handle security incidents MUST be created. It will need to define the purpose and purpose of the policy and all aspects of incident handling. Thus, rules of conduct for the various types of security incidents MUST be described. In addition, there is a need for target group-oriented and practically applicable instructions for all employees. Furthermore, the interfaces to other management areas SHOULD be considered, e.g. B. for emergency management.

The policy MUST be known to all employees. It MUST be coordinated with the IT management or the IT operation and approved by the institution's management. The policy MUST be reviewed and updated regularly.

#### DER.2.1.A3 Definition of responsibilities and contact persons in case of security incidents [Head IT]

It must be regulated who is responsible for what happens in the event of a security incident. For all employees the tasks and competences MUST be defined during security incidents. Even employees who are supposed to handle security incidents MUST be informed about their duties and competences. It must be regulated, who makes the possible decision for a forensic investigation, according to which criteria this is done and when it should take place.

The contact persons for all types of security incidents MUST be known to the employees. Contact Information MUST always be up to date and available in a workable format.

#### DER.2.1.A4 Notification of affected persons in case of security incidents [Head of IT, Emergency Representative, Press Office, Data Protection Officer, Head of Institution]A security incident MUST inform all relevant internal and external bodies in a timely manner. It MUST be checked whether the data protection officer, the works council / staff council and employees from the legal department must be involved. Likewise, the reporting requirements for authorities and regulated industries MUST be taken into account. It is also necessary to ensure that affected bodies are informed of the necessary measures.

#### DER.2.1.A5 Security Incident [Head IT, IT Operations]

For a security incident to be successfully resolved, the person responsible first has to narrow down the problem and find the cause. He then has to select the necessary remedial action and obtain approval from the IT supervisor before implementing it. Subsequently, the cause MUST be removed and a safe state established (see DER.2.1.A6 * Restoring the operating environment after security incidents *).

There must be an up-to-date list of internal and external security experts who can be involved in security incidents for questions from the various required subject areas. Secure communication procedures with these internal and external agencies MUST be established.

#### DER.2.1.A6 Restoring the operating environment after security incidents [Head of IT, IT Operations]

In order to eliminate the effects of security incidents, the affected components MUST be disconnected from the grid and all necessary data backed up to provide information on the nature and cause of the problem that has occurred. On all affected components, the operating system and all applications MUST be examined for changes.

The original data MUST be restored from read-only media. All security-relevant configurations and patches MUST be installed. When restoring data from backups, you MUST ensure that they were not affected by the security incident. Before restarting after an attack, all passwords on the affected components MUST be changed. The affected components SHOULD undergo a penetration test before being reused.

When restoring the secure operating environment, users MUST be included in the application health tests. After everything has been restored, the components, including the gateways, MUST be monitored in order to be able to detect attempts to attack again.

If external service providers are used to remedy the malfunction, it is necessary to regulate what information about the security incident is made available to whom.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the area of ​​handling security incidents. They SHOULD be implemented in principle.

#### DER.2.1.A7 Establishment of a procedure for the handling of security incidents

In order for institutions to respond adequately to security incidents, an appropriate incident handling procedure SHOULD be defined. The procedures, processes and specifications for the various security incidents SHOULD be clearly regulated and suitably documented. The institutional management SHOULD implement and publish the completed procedure. The procedure SHOULD be checked and updated regularly.

#### DER.2.1.A8 Structure of organizational structures for handling security incidentsFor dealing with security incidents, suitable organizational structures SHOULD be defined. Thus, a security incident team should be set up whose members can be convened according to the nature of the incident. Even if the security incident team only meets for a specific security incident, suitable members SHOULD be named in advance and instructed in their tasks. The structure of the security incident team SHOULD be updated regularly.

#### DER.2.1.A9 Definition of reporting procedures for security incidents [Head IT]

For the various types of security incidents, the appropriate reporting paths SHOULD be constructed. It should be ensured that employees can quickly and easily report security incidents via reliable and trusted channels.

If a single point of contact is set up for reporting incidents or incidents, this should also be communicated to all employees.

There SHOULD be a communication and contact strategy. In this SHOULD be regulated, who must be informed in principle and who may be informed, by whom in what order and in what depth is informed. It SHOULD be defined who passes on information about security incidents to third parties. Likewise, it should be ensured that no unauthorized persons pass on information about the security incident.

#### DER.2.1.A10 Damming the impact of security incidents [Emergency Representative, IT Manager, IT Operations]

In parallel to analyzing the causes of a security incident, it should be decided whether it is more important to contain or clarify the damage that has occurred. In order to assess the impact of a security incident, sufficient information should be available. For selected security incident scenarios, worst-case considerations SHOULD be carried out in advance.

#### DER.2.1.A11 Classification of security incidents [Head of IT, IT operations]

A uniform procedure should be established to classify security incidents and incidents. The security incidents classification SHOULD be aligned between security management and incident management.

#### DER.2.1.A12 Determination of the interfaces of the incident handling for troubleshooting [DPO]

The interfaces between troubleshooting and troubleshooting, emergency management and security management SHOULD be analyzed. It should also be possible to identify any shared resources.

The staff members involved in troubleshooting should be sensitized for security incident handling and emergency management issues. The security management SHOULD have read access to used incident management tools.

#### DER.2.1.A13 Integration into the security and emergency management [Emergency Response Officer]

As part of security management, the handling of security incidents SHOULD be governed by the security policy or security concept of the institution. The handling of security incidents SHOULD also be coordinated with the emergency management. If there is a special role in the institution for troubleshooting, this should also be included.

#### DER.2.1.A14 Escalation Strategy for Security Incidents [IT Leader]

In addition to the communication and contact strategy (see DER.2.1.A9 * Definition of reporting procedures for security incidents *), an escalation strategy SHOULD be formulated. This SHOULD be reconciled between those responsible for troubleshooting and troubleshooting and information security management.The escalation strategy SHOULD include clear instructions on who, by what means, in what kind of identifiable or suspected security breaches, in what period of time to be involved. It should be regulated to which measures an escalation leads and which activities should be triggered.

For the specified escalation strategy, suitable tools SHOULD be selected. These SHOULD also be suitable for confidential information. It should be ensured that the tools are also available during a security incident or emergency.

The escalation strategy SHOULD be regularly reviewed and updated if necessary. The checklists (Matching Scenarios) for troubleshooting and troubleshooting SHOULD be regularly supplemented or updated with safety-relevant topics. The specified escalation routes SHOULD be tested in exercises.

#### DER.2.1.A15 Training of employees of the central contact point of the IT organization for the handling of security incidents [Head of IT]

Service Desk staff SHOULD know the guidelines for handling security incidents. They SHOULD have appropriate tools at their disposal to help them detect such incidents. They SHOULD be sufficiently trained in their operation. The employees of the service desk SHOULD know the protection requirements of the affected systems. The service desk checklists SHOULD include questions to help identify security incidents.

#### DER.2.1.A16 Documentation of the handling of security incidents

The resolution of security incidents SHOULD be documented according to a standardized procedure. Both the actions performed, including the times, as well as the log data of the affected components SHOULD be documented. The confidentiality of the documentation and archiving of the reports SHOULD be guaranteed.

The required information SHOULD be entered into the respective documentation systems before the fault is marked as completed and completed. The required quality assurance requirements SHOULD be defined in advance with the safety management.

#### DER.2.1.A17 Post-processing of security incidents

Security incidents SHOULD be standardized. The aim was to investigate how quickly security incidents were detected and corrected, whether the reporting channels were working, whether sufficient information was available for the assessment and whether the detection measures were effective. Likewise, it should be examined whether the measures and activities taken were effective and efficient.

The experiences from previous security incidents SHOULD be used to create instructions for comparable security incidents. These instructions SHOULD be communicated to the relevant groups of persons and regularly updated on the basis of new findings.

In addition, the management level SHOULD be informed annually about the security incidents. However, the management level SHOULD be informed immediately if there is an immediate need for action.

#### DER.2.1.A18 Further development of processes through insights from security incidents and industry developments [Specialists]

Responses to security incidents SHOULD be analyzed and evaluated to see if processes and operations need to be changed or evolved. In doing so, those involved in response to security incidents as well as those responsible should report on their respective experiences.

It SHOULD be examined whether new developments in incident management and in forensics exist and can be incorporated into the respective documents and processes.Be aids and checklists z. For example, for service desk employees, SHOULD it be checked if they need to be expanded to include any relevant questions and information.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### DER.2.1.A19 Establishment of priorities for the handling of security incidents (CIA)

In order to resolve the causes of the incident and the damage done efficiently and in a reasonable order, the priorities SHOULD be set in advance and regularly updated. The classification of security incidents should also be taken into account (see DER.2.1.A11 * Classification of security incidents *).

The priorities SHOULD be approved and put into effect by the institution's management. They SHOULD be known to all decision-makers involved in the handling of security incidents. The defined priority classes SHOULD also be stored in Incident Management.

#### DER.2.1.A20 Establishment of an internal security incident reporting office (CIA)

An internal security incident reporting unit SHOULD be set up. It SHOULD be ensured that the hotline is available at normal working hours. However, it should also be possible for security incidents to be reported by employees outside normal working hours. The employees of the reporting office SHOULD be adequately trained and sensitized to the interests of information security. All information about security incidents SHOULD be kept confidential at the registration office.

#### DER.2.1.A21 Establishment of a Security Incident Response Team (CIA)

To be able to competently accompany security incidents throughout the entire lifecycle of the incident handling process, a team of experienced and trusted specialists SHOULD be assembled for this purpose. In addition to technical understanding, the team members SHOULD also have competencies in communication skills. The trustworthiness of the members of the expert team SHOULD be checked. The structure of the expert team SHOULD be updated regularly.

The members of the expert team SHOULD be involved in the escalation and reporting channels. The team of experts SHOULD be trained to analyze security incidents in the systems used in the institution. The members of the expert team SHOULD train on a regular basis, both on the systems used and on the detection and response to security incidents. The team of experts SHOULD have all the documentation and financial and technical resources to deal with security incidents quickly and discreetly.

The team of experts SHOULD be considered and integrated appropriately in the organizational structures (see DER.2.1.A8 * Structure of organizational structures for handling security incidents *). The responsibilities of the team of experts SHOULD be agreed in advance with those of the incident team (see DER.2.1.A4 * Defining responsibilities and contact persons in case of security incidents *).

#### DER.2.1.A22 Security Incident Management System Review (CIA)The incident management management system SHOULD regularly review if it is still up to date and effective. Both announced and unannounced exercises SHOULD be performed. The exercises SHOULD be coordinated with the management level beforehand. It SHOULD evaluate the metrics that occur, for example, when security incidents are recorded, reported and escalated.

In addition, security incident management games SHOULD be conducted to promote the necessary practice.

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and safety measures in the area of ​​"treatment of security incidents" can be found in the following publications, among others:

* #### [27001A16] ISO / IEC 27001: 2013 - Annex A.16 Information security incident management

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013, in particular Annex A, A.16 Information security incident management
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [27035] ISO / IEC 27035: 2016

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 09.2011
 <Https://www.iso.org/standard/44379.html>

 
* #### [ISFSATS14] The Standard of Good Practices Area SA System Access and TS1.4 Technical Security Management

  

 Information Security Forum (ISF), in particular Area SA (System Access) and TS1.4 (Technical Security Management, Identity and Access Management), 06.2016

 
* #### [NIST80061] NIST Special Publication 800-61 Revision 2

  

 NIST, Computer Security Incident Handling Guide, 08.2012
 <Http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf>

 
* #### [NST80083] NIST Special Publication 800-83 Revision 1

  

 NIST, Guide to Malware Incident Prevention and Handling in Front of Desktops and Laptops, 07.2013
 <Http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-83r1.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the module "Handling of security incidents".

* G 0.11 Failure or disruption of service providers
* G 0.18 Missing planning or missing adjustment
* G 0.19 Disclosure of information worthy of protection
* G 0.20 Information or products from unreliable sources
* G 0.22 Manipulation of information
* G 0.25 Failure of devices or systems
* G 0.27 Resource shortage
* G 0.29 Violation of laws or regulations
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.32 Abuse of permissions
* G 0.33 Personnel loss
* G 0.45 data loss
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.