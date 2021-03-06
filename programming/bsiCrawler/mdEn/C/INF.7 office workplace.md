1 description
--------------

### 1.1 Introduction

An office space is the area within an institution where one or more employees are located to perform their duties. This module describes the typical threats and requirements for information security for an office room.

### 1.2 Objective

The aim of the module is to protect the information that is processed in offices.

### 1.3 Delimitation

This module considers technical and non-technical security requirements for office space. Recommendations on how to configure and secure the IT systems in these rooms are not covered in this module. Hints are u. a. in SYS.2.1 * General Client * as well as in the operating system-specific blocks.

Also on the wiring of offices is not discussed. To do this, the components INF.3 * Electrotechnical cabling * and INF.4 * IT cabling * must be considered separately. Requirements for fire protection and access control in buildings can be found in building block INF.1 * General building *.

2 risk situation
-----------------

The following specific threats and vulnerabilities are of particular importance in the field of * * office space:

### 2 1 Unauthorized access

If access controls are lacking or insufficient, unauthorized persons can enter an office room and steal sensitive data, steal devices or manipulate them. This may affect the availability, confidentiality, or integrity of devices and information. Even if no immediate damage can be detected, the operation can be disturbed by the fact that it must be investigated how such an incident was possible, whether damage has occurred or tampering.

### 2 2 Impairment due to unfavorable working conditions

An office space that is not ergonomically designed or an unfavorable working environment can result in employees not working undisturbed or being unable to use the IT that is used optimally. The disturbances range from noise or heavy traffic to unfavorable lighting and poor ventilation. As a result, work processes are restricted and employee potential is used insufficiently. There may also be errors in the work, which may reduce the integrity of data.

### 2 3 Cleaning and external staff or visitors

For smaller or short meetings, it is usually more efficient to receive a visit to the office. Visitors as well as cleaners and third-party personnel can view internal information in various ways, endanger business processes and manipulate IT systems, from improper handling of technical equipment to attempts to "play" IT systems to theft of documents or IT components. For example, by cleaning personnel accidentally a plug connection can be solved or water get into the IT, even documents can be misplaced or even disposed of with the waste.

### 2 4 Manipulation or destruction of IT, accessories, information and software in the office

Attackers can try to manipulate or destroy IT systems, accessories, and other data carriers for a variety of reasons. Attacks can be all the more effective the later they are discovered by the employee or the institution itself, the more extensive the knowledge of the perpetrators and the more profound the consequences for a job. The manipulations range from the unauthorized inspection of the employee's sensitive data to the destruction of data carriers or IT systems. Significant downtime and process limitations can be the result.

### 2 5 TheftAs IT devices become more manageable, it's easier to pocket them unnoticed. The theft of data carriers, IT systems, accessories, software or data incurs reimbursement costs and the restoration of a workable state, as well as losses due to a lack of availability. In addition, the person who stole the IT equipment could view and disclose sensitive information, which could lead to further damage. In many cases, these weigh considerably more heavily than the mere material loss of the device.

In addition to expensive IT systems, mobile devices are often stolen, which can be transported inconspicuously and easily. If the office space is not locked, supervised or the IT systems are not sufficiently secured, the technology can be stolen accordingly quickly and inconspicuously.

### 2 6 Flying cabling

Depending on the location of the connection points of the sockets, the power supply and the data network in the office room, cables could be routed across the room, even across traffic routes. Such "flying" cables are not just tripping hazards that can injure people. If people get stuck, IT equipment can be damaged.

### 2 7 Vandalism

Vandalism destroys or damages foreign property. The effects are very similar to those of an attack, only that vandalism is not deliberately planned and implemented like this, but is usually the expression of spontaneous, blind destructiveness. Both external perpetrators (disappointed burglars) and culprits (frustrated or mentally unstable staff) are eligible. Possible triggers for vandalism may include disagreements, personal problems, bullying or a bad working atmosphere.

3 requirements
---------------

The following are specific requirements for office protection. Basically, the Information Security Officer (ISB) is responsible for meeting the requirements. Deviations from this are mentioned separately in the corresponding requirements. The ISB should always be involved in strategic decisions. He is also responsible for ensuring that all requirements are met and verified in accordance with the established security policy.

### 3.1 Basic requirements

The following requirements MUST be implemented as a priority:

#### INF.7.A1 Appropriate selection and use of an office space [staff, supervisors]

Only suitable rooms may be used as office space. Also, the offices MUST be adequately selected and equipped for the protection needs or level of protection of the information processed there. For example, offices with public access in non-security-related areas MUST lie. For the workplace and for the furnishing of an office space, the Workplace Ordinance MUST be implemented.

#### INF.7.A2 Closed windows and closed doors [Staff]

When employees leave their offices, all windows MUST be closed. If there is confidential information in the office, the doors should be locked when leaving. This SHOULD be respected especially in areas with public access. The corresponding specifications SHOULD be recorded in a suitable instruction. All employees SHOULD be required to implement the instruction. In addition, it is necessary to check regularly whether the windows are closed when leaving and, if necessary, the doors are locked. Likewise MUST be taken to ensure that fire and smoke protection doors are actually closed.

### 3.2 Standard requirements

Together with the basic requirements, the following requirements correspond to the state of the art in the field of office workplaces. They SHOULD be implemented in principle.

#### INF.7.A3 Flying cablingThe electrical connections and access to the data network in the office room SHOULD be located near the location where the IT equipment is located. Cabling over the floor SHOULD be covered with a cable duct.

#### INF.7.A4 access regulations and control

It SHOULD be ensured that unauthorized persons can not enter the office. For this, a security concept SHOULD be created and implemented. In addition, SHOULD regularly check that the measures taken are effective.

#### INF.7.A5 Ergonomic workplace [Head of Domestic Engineering]

The workplaces of all employees SHOULD be ergonomically designed. Above all, the screens SHOULD be set up so that an ergonomic and undisturbed work is possible. It should be noted that screens can not be viewed by unauthorized persons. The Bildschirmarbeitsschutzverordnung (BildscharbV) SHOULD be implemented. All workstations SHOULD be individually adjustable for the most error-free operation of IT.

#### INF.7.A6 Tidy Workplace [Staff]

Each employee SHOULD be encouraged to leave their workspace tidy. Users SHOULD make sure that unauthorized persons can not access IT applications or see confidential information. All employees should carefully inspect their workplaces and ensure that confidential information is not freely accessible. Supervisors should sporadically check jobs to see if vulnerable information is open to them.

#### INF.7.A7 Suitable storage of official documents and data carriers [staff, Head of Building Services]

Employees SHOULD be instructed to keep confidential documents and data carriers locked when not in use. For this purpose, suitable containers should be placed in the offices or in their surroundings.

### 3.3 Requirements for increased protection requirements

Listed below are exemplary proposals for requirements that exceed the state of the art level of protection and should be considered IN THE EVENT OF INCREASED PROTECTION. The concrete determination takes place within the framework of a risk analysis. The letters in parentheses indicate which basic values ​​are given priority protection by the requirement (C = confidentiality, I = integrity, A = availability).

#### INF.7.A8 Use of anti-theft devices [Staff, Head of IT] (CIA)

If access to the rooms can not be suitably restricted, anti-theft systems SHOULD be used for all IT systems. In areas with public traffic, anti-theft devices SHOULD generally be used.

4 Further Information
------------------------------

### 4.1 Literature

Further information on hazards and security measures in the area of ​​"office workplaces" can be found in the following publications, among others:

* #### [27001A12.2] ISO / IEC 27001: 2013 - Annex A.12.2 Protecting from malware

  

 Information technology - Security technigues - Information security management systems - Requirements, in particular Annex A, A.12.2 Protection from malware, 2013
 <Https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [ArbStättV] Workplace regulation

  

 Federal Ministry of Labor and Social Affairs (BMAS), (last accessed on 28.09.2017)
 <Http://www.bmas.de/DE/Service/Gesetze/arbeitsstaettenverordnung.html>

 
* #### [BildscharbV] VDU work protection ordinance

  

 ArbSchG, (last accessed on 28.09.2017)
 <Https://www.arbeitsschutzgesetz.org/bildscharbv/>

 
* #### [DIN1627] DIN EN 1627: 2011-09

  

 Doors, windows, curtain walls, grilles and shutters - Burglar resistance - Requirements and classification, 2011

 
* #### [ISFCF19] The Standard of Good Practice - AREA CF19 Physical and Environmental Security

  

 especially AREA CF19 Physical and Environmental Security, ISF, 06.2014* #### [NIST80053PEP] NIST Special Publication 800-53 Revision 4 - APPENDIX PAGE F-213

  

 Assesing Security and Privacy Controls for Federal Information Systems and Organizations, in particular APPENDIX F-PS PAGE F-213, FAMILY: PHYSICAL AND ENVIRONMENTAL PROTECTION, NIST, 2013
 <Http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf>

 
5 Appendix: Cross reference table for elementary hazards
-------------------------------------------------- --------

The following elementary hazards are important for the module "office workplace".

* G 0.2 Unfavorable climatic conditions
* G 0.13 Interception of compromising radiation
* G 0.14 Spying out information (spying)
* G 0.15 Listening
* G 0.16 Theft of devices, data carriers or documents
* G 0.18 Missing planning or missing adjustment
* G 0.21 Manipulation of hardware or software
* G 0.22 Manipulation of information
* G 0.23 Unauthorized intrusion into IT systems
* G 0.24 Destruction of equipment or data media
* G 0.30 Unauthorized use or administration of devices and systems
* G 0.44 Unauthorized intrusion into premises
* G 0.46 Loss of integrity of sensitive information
The cross reference tables can be found in the download area due to their size.