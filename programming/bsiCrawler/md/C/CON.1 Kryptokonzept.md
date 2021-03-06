1 Beschreibung
--------------

### 1.1 Einleitung

Mit der in diesem Baustein beschriebene Vorgehensweise wird ein Überblick über kryptografische Verfahren und Produkte gegeben, die in einer Institution eingesetzt werden können. Es wird beschrieben, wie in einer heterogenen Umgebung sowohl die lokal gespeicherten Daten als auch die zu übertragenden Daten wirkungsvoll durch kryptografische Verfahren und Techniken geschützt werden können. Darüber hinaus werden geeignete organisatorische und prozessuale Anforderungen beschrieben, mit denen die Vertraulichkeit, Integrität und Authentizität gewährleistet werden können.

Ergänzend zu den Verfahren und Techniken, mit denen lokal gespeicherte Daten und übertragene Informationen geschützt werden können, werden im vorliegendem Baustein auch Kryptomodule beschrieben. Mit einem Kryptomodul ist ein Produkt gemeint, das die im Kryptokonzept dargelegte Sicherheitsfunktionalität bietet. Ein solches Produkt kann dabei aus Hardware, Software, Firmware oder aus einer Kombination hieraus bestehen. Hinzukommen noch Bauteile wie Speicher, Prozessoren, Busse und Stromversorgung, die notwendig sind, um die Kryptoprozesse umzusetzen. Ein Kryptomodul kann in unterschiedlichsten Rechner- oder Telekommunikationssystemen verwendet werden, um sensible Daten bzw. Informationen zu schützen. Dies ist im vorliegenden Baustein erst bei erhöhtem Schutzbedarf relevant.

### 1.2 Zielsetzung

Der Baustein beschreibt, wie Informationen in Institutionen kryptografisch abgesichert werden und wie hierfür ein entsprechendes Kryptokonzept erstellt werden sollte. 

### 1.3 Abgrenzung

In diesem Baustein werden allgemeine Anforderungen, organisatorische Rahmenbedingungen und prozessuale Abläufe für kryptografische Produkte und Verfahren betrachtet. Die mit dem Betrieb von Kryptomodulen zusammenhängenden Kern-IT-Aufgaben werden nicht in diesem Baustein behandelt. Dafür müssen die Anforderungen der Bausteine der Schicht OPS.1.1 *Kern-IT-Betrieb* erfüllt werden. 

Wie einzelne Anwendungen (z. B. E-Mails) oder IT-Systeme (z. B. Laptops) kryptografisch abgesichert werden können, ist nicht Gegenstand des vorliegenden Bausteins, sondern wird in den entsprechenden Bausteinen behandelt.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind im Bereich Kryptokonzept von besonderer Bedeutung:

### 2 1 Unzureichendes Schlüsselmanagement bei Verschlüsselung

Durch ein unzureichendes Schlüsselmanagement könnten Angreifer auf verschlüsselte Daten zugreifen. So kann es beispielsweise sein, dass sich aufgrund fehlender Regelungen verschlüsselte Informationen mitsamt den zugehörigen Schlüsseln auf demselben Datenträger befinden. Dadurch kann bei symmetrischen Verfahren jeder, der auf den Datenträger oder den Kommunikationskanal zugreifen kann, die Informationen entschlüsseln, sofern das eingesetzte Verschlüsselungsverfahren bekannt ist.

### 2 2 Verstoß gegen rechtliche Rahmenbedingungen beim Einsatz von kryptografischen Verfahren

Wenn Institutionen kryptografische Verfahren und Produkte einsetzen, müssen sie dabei diverse gesetzliche Rahmenbedingungen beachten. In einigen Ländern dürfen beispielsweise kryptografische Verfahren nicht ohne staatliche Genehmigung eingesetzt werden. Das kann dazu führen, dass Empfänger im Ausland verschlüsselte Datensätze nicht lesen können, da sie die benötigten kryptografischen Produkte nicht einsetzen dürfen oder sich vielleicht sogar strafbar machen.

Außerdem ist in sehr vielen Ländern auch der Export von Produkten mit starker Kryptografie erheblich eingeschränkt. Das kann dazu verleiten, schützenswerte Daten unverschlüsselt zu lassen oder mit unsicheren Verfahren zu schützen. Dadurch sind einerseits Angreifern Tür und Tor geöffnet und andererseits kann so auch gegen nationales Recht verstoßen werden. So können beispielsweise Datenschutzgesetze vorschreiben, dass adäquate kryptografische Verfahren eingesetzt werden müssen, um personenbezogene Daten zu schützen.

### 2 3 Vertraulichkeits- oder Integritätsverlust von Daten durch Fehlverhalten

Setzt beispielsweise eine Institution ein Kryptomodul ein, das entweder zu kompliziert zu bedienen ist oder sich nicht intuitiv bedienen lässt, könnten die Benutzer aus Bequemlichkeit oder aus pragmatischen Gründen darauf verzichten, dieses zu benutzen und stattdessen die Informationen im Klartext übertragen. Dadurch können die übertragenen Informationen von Angreifern abgehört werden.

Auch kann eine Fehlbedienung eines Kryptomoduls dazu führen, dass vertrauliche Informationen von Angreifern abgegriffen werden, etwa wenn diese im Klartext übertragen werden, weil versehentlich der Klartext-Modus aktiviert wurden. 

### 2 4 Software-Schwachstellen oder -Fehler in Kryptomodulen

Software-Schwachstellen oder -Fehler in Kryptomodulen schwächen die Sicherheit der eingesetzten kryptografischen Verfahren und können dazu führen, dass die damit geschützten Informationen mitgelesen werden. Dadurch ist es möglich, dass Angreifer die Kryptomodule manipulieren (z. B. über Schadsoftware) und so sensible Daten abfließen oder auch ganze Produktionsprozesse stillstehen, weil sich Daten nicht mehr entschlüsselt lassen.

### 2 5 Ausfall eines Kryptomoduls

Kryptomodule können durch technische Defekte, Stromausfälle oder absichtliche Zerstörung ausfallen. Dadurch könnten bereits verschlüsselte Daten sich nicht mehr entschlüsseln lassen, solange das erforderliche Kryptomodul nicht mehr verfügbar ist. Dadurch können ganze Prozessketten stillstehen, z. B. wenn weitere IT-Anwendungen auf die Daten angewiesen sind.

### 2 6 Unsichere kryptografische Algorithmen oder Produkte

Unsichere oder veraltete kryptografische Algorithmen lassen sich von einem potenziellen Angreifer mit vertretbaren Ressourcen brechen. Bei Verschlüsselungsalgorithmen bedeutet dies, dass es gelingt, aus dem verschlüsselten Text den ursprünglichen Klartext zu ermitteln, ohne dass zusätzliche Informationen, wie z. B. der verwendete kryptografische Schlüssel, bekannt sind. Werden unsichere kryptographische Algorithmen eingesetzt, können Angreifer den kryptographischen Schutz unterlaufen und somit auf schützenswerte Informationen der Institution zugreifen.

Selbst wenn in einer Institution ausschließlich sichere (z. B. zertifizierte) Produkte eingesetzt werden, kann eine Kommunikation dennoch unsicher werden, beispielsweise wenn der Kommunikationspartner kryptografische Verfahren benutzt, die nicht dem Stand der Technik entsprechen. 

### 2 7 Fehler in verschlüsselten Daten oder kryptografischen Schlüsseln

Werden Informationen verschlüsselt und die Chiffrate dann verändert, lassen sich die verschlüsselten Informationen eventuell nicht mehr korrekt entschlüsseln. Je nach Betriebsart der Verschlüsselungsroutinen kann dies bedeuten, dass nur wenige Bytes falsch entschlüsselt oder auch sämtliche Daten falsch entschlüsselt werden. Ist keine Datensicherung vorhanden, sind solche Daten verloren. 

Noch kritischer kann sich ein Fehler in den verwendeten kryptografischen Schlüsseln auswirken. Schon die Änderung eines einzigen Bits eines kryptografischen Schlüssels führt dazu, dass sämtliche damit verschlüsselten Daten nicht mehr entschlüsselt werden können. 

### 2 8 Unautorisierte Nutzung eines Kryptomoduls

Gelingt es einem Angreifer, ein Kryptomodul unautorisiert zu benutzen, kann er kritische Sicherheitsparameter manipulieren. Hierdurch bieten die kryptografischen Verfahren keine ausreichende Sicherheit mehr. Weiterhin kann ein Angreifer das Kryptomodul so manipulieren, dass es zwar auf den ersten Blick korrekt arbeitet, sich jedoch tatsächlich in einem unsicheren Zustand befindet. Dadurch bleibt er längere Zeit unentdeckt und kann auf zahlreiche sensible Informationen zugreifen. 

### 2 9 Kompromittierung kryptografischer Schlüssel

Die Sicherheit kryptografischer Verfahren hängt entscheidend davon ab, wie vertraulich die verwendeten kryptografischen Schlüssel bleiben. Daher wird ein potenzieller Angreifer in der Regel versuchen, die verwendeten Schlüssel zu ermitteln. Das könnte ihm zum Beispiel gelingen, indem er flüchtige Speicher ausliest oder ungeschützte Schlüssel findet, die zum Beispiel in einer Datensicherung hinterlegt sind. Kennt er den verwendeten Schlüssel und das eingesetzte Kryptoverfahren, kann er relativ leicht die Daten entschlüsseln. 

Bei einer Festplattenverschlüsselung (etwa Trusted Disk) kann ein Angreifer z. B. einen Keylogger zwischen Tastatur und Rechner schalten, um an das Passwort zu gelangen, das dazu benötigt wird, um die Festplatte zu entschlüsseln.

### 2 10 Gefälschte Zertifikate

Zertifikate dienen dazu, einen öffentlichen kryptografischen Schlüssel an eine Person zu binden. Diese Bindung des Schlüssels an den Namen der Person wird wiederum kryptografisch mittels einer digitalen Signatur häufig von einer vertrauenswürdigen dritten Stelle abgesichert. 

Diese Zertifikate werden von Dritten dann benutzt, um digitale Signaturen der im Zertifikat ausgewiesenen Person zu prüfen bzw. um dieser Person Daten mit dem im Zertifikat aufgezeichneten Schlüssel verschlüsselt zuzusenden.

Ist ein solches Zertifikat gefälscht, werden digitale Signaturen fälschlicherweise als korrekt geprüft und der Person im Zertifikat zugeordnet oder es werden Daten mit einem möglicherweise unsicheren Schlüssel verschlüsselt und versandt. 

3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für Kryptokonzepte aufgeführt. Grundsätzlich ist der Informationssicherheitsbeauftragte (ISB) dafür zuständig, die Anforderungen zu erfüllen. Außerdem ist er dafür verantwortlich, dass alle Anforderungen gemäß dem festgelegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### CON.1.A1 Auswahl geeigneter kryptografischer Verfahren [Fachverantwortliche]

Es MÜSSEN geeignete kryptografische Verfahren ausgewählt werden. Dabei MUSS sichergestellt sein, dass etablierte Algorithmen verwendet werden, die von der Fachwelt intensiv untersucht wurden und von denen keine Sicherheitslücken bekannt sind. Ebenso MÜSSEN aktuell empfohlene Schlüssellängen eingesetzt werden. 

#### CON.1.A2 Datensicherung bei Einsatz kryptografischer Verfahren [IT-Betrieb]

In Datensicherungen MÜSSEN kryptografische Schlüssel derart gespeichert bzw. aufbewahrt werden, dass Unbefugte nicht darauf zugreifen können. Langlebige kryptografische Schlüssel MÜSSEN außerhalb der eingesetzten IT-Systeme aufbewahrt werden. Bei einer Langzeitspeicherung verschlüsselter Daten SOLLTE regelmäßig geprüft werden, ob die verwendeten kryptografischen Algorithmen und die Schlüssellängen noch dem Stand der Technik entsprechen. Es MUSS sichergestellt sein, dass auf verschlüsselt gespeicherte Daten auch nach längeren Zeiträumen noch zugegriffen werden kann. Verwendete Kryptoprodukte SOLLTEN archiviert werden. Die Konfigurationsdaten von Kryptoprodukten SOLLTEN gesichert werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Kryptokonzept. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### CON.1.A3 Verschlüsselung der Kommunikationsverbindungen

Es SOLLTE geprüft werden, ob mit vertretbarem Aufwand eine Verschlüsselung der Kommunikationsverbindungen möglich und praktikabel ist. Ist dies der Fall, SOLLTEN Kommunikationsverbindungen geeignet verschlüsselt werden.

#### CON.1.A4 Geeignetes Schlüsselmanagement [IT-Betrieb, Fachverantwortliche]

Kryptografische Schlüssel SOLLTEN immer mit geeigneten Schlüsselgeneratoren und in einer sicheren Umgebung erzeugt werden. Ein Schlüssel SOLLTE möglichst nur einem Einsatzzweck dienen. Insbesondere SOLLTEN für die Verschlüsselung und Signaturbildung unterschiedliche Schlüssel benutzt werden.

Wenn Schlüssel verwendet werden, SOLLTE die authentische Herkunft und die Integrität der Schlüsseldaten überprüft werden.

Alle kryptografischen Schlüssel SOLLTEN hinreichend häufig gewechselt werden. Es SOLLTE eine festgelegte Vorgehensweise für den Fall geben, dass ein Schlüssel offen gelegt wurde. Alle erzeugten kryptografischen Schlüssel SOLLTEN sicher aufbewahrt und verwaltet werden. 

#### CON.1.A5 Sicheres Löschen und Vernichten von kryptografischen Schlüsseln [IT-Betrieb]

Nicht mehr benötigte Schlüssel und Zertifikate SOLLTEN sicher gelöscht bzw. vernichtet werden. Auf Produkte mit unkontrollierbarer Schlüsselablage SOLLTE generell verzichtet werden.

#### CON.1.A6 Bedarfserhebung für kryptografische Verfahren und Produkte [IT-Betrieb, Fachverantwortliche]

Es SOLLTE festgelegt werden, für welche Aufgaben kryptografische Verfahren eingesetzt werden sollen. Danach SOLLTEN die Anwendungen, IT-Systeme und Kommunikationsverbindungen identifiziert werden, die notwendig sind, um die Aufgaben zu erfüllen. Diese SOLLTEN kryptografisch abgesichert werden.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### CON.1.A7 Erstellung einer Sicherheitsrichtlinie für den Einsatz kryptografischer Verfahren und Produkte(CIA)

Ausgehend von der allgemeinen Sicherheitsrichtlinie der Institution SOLLTE eine spezifische Richtlinie für den Einsatz von Kryptoprodukten erstellt werden. In der Sicherheitsrichtlinie SOLLTE geregelt werden, wer für den sicheren Betrieb der kryptografischen Produkte verantwortlich ist. Für die benutzen Kryptoprodukte SOLLTEN es Vertretungsregelungen geben.

Auch SOLLTEN notwendige Schulungs- und Sensibilisierungsmaßnahmen für Benutzer sowie Verhaltensregeln und Meldewege bei Problemen oder Sicherheitsvorfällen festgelegt werden. Weiter SOLLTE die Richtlinie definieren, wie sichergestellt wird, dass Kryptomodule sicher konfiguriert, korrekt eingesetzt und regelmäßig gewartet werden. 

Die Richtlinie SOLLTE allen relevanten Mitarbeitern bekannt und grundlegend für ihre Arbeit sein. Wird die Richtlinie verändert oder wird von ihr abgewichen, SOLLTE dies mit dem ISB abgestimmt und dokumentiert werden. Es SOLLTE regelmäßig überprüft werden, ob die Richtlinie noch korrekt umgesetzt ist. Die Ergebnisse SOLLTEN sinnvoll dokumentiert werden.

#### CON.1.A8 Erhebung der Einflussfaktoren für kryptografische Verfahren und Produkte(CIA)

Bevor eine Entscheidung getroffen werden kann, welche kryptografischen Verfahren und Produkte bei erhöhtem Schutzbedarf eingesetzt werden, SOLLTEN unter anderem folgende Einflussfaktoren ermittelt werden:

* Sicherheitsaspekte (siehe CON.1.A6 *Bedarfserhebung für kryptografische Verfahren und Produkte*),
* technische Aspekte,
* personelle und organisatorische Aspekte,
* wirtschaftliche Aspekte,
* Lebensdauer von kryptografischen Verfahren und der eingesetzten Schlüssellängen
* Zulassung von kryptografischen Produkten und 
* gesetzliche Rahmenbedingungen.
#### CON.1.A9 Auswahl eines geeigneten kryptografischen Produkts [IT-Betrieb, Fachverantwortliche](CI)

Bevor ein kryptografisches Produkt ausgewählt wird, SOLLTE die Institution festlegen, welche Anforderungen das Produkt erfüllen muss. Dabei SOLLTEN Aspekte, wie Funktionsumfang, Interoperabilität, Wirtschaftlichkeit sowie Fehlbedienungs- und Fehlfunktionssicherheit betrachtet werden. Es SOLLTE geprüft werden, ob zertifizierte Produkte vorrangig eingesetzt werden sollen. Auch die zukünftigen Einsatzorte SOLLTEN bei der Auswahl beachtet werden, da es z. B. Export- und Importbeschränkungen für kryptografische Produkte gibt.

#### CON.1.A10 Entwicklung eines Kryptokonzepts(CI)

Es SOLLTE ein Kryptokonzept entwickelt werden, das in das Sicherheitskonzept der Institution integriert wird. Im Konzept SOLLTEN alle technischen und organisatorischen Vorgaben für die eingesetzten kryptografischen Produkte beschrieben werden. Auch SOLLTEN alle relevanten Anwendungen, IT-Systeme und Kommunikationsverbindungen aufgeführt sein. Das erstellte Kryptokonzept SOLLTE regelmäßig aktualisiert werden. 

#### CON.1.A11 Sichere Konfiguration der Kryptomodule [IT-Betrieb](CI)

Kryptomodule SOLLTEN sicher installiert und konfiguriert werden. Es SOLLTEN alle voreingestellten Schlüssel geändert werden. Anschließend SOLLTE getestet werden, ob die Kryptomodule korrekt funktionieren und vom Benutzer auch bedient werden können. 

Weiterhin SOLLTEN die Anforderungen an die Einsatzumgebung festgelegt werden. Wenn ein IT-System geändert wird, SOLLTE getestet werden, ob die eingesetzten kryptografischen Verfahren noch greifen. Die Konfiguration der Kryptomodule SOLLTE dokumentiert und regelmäßig überprüft werden.

#### CON.1.A12 Sichere Rollenteilung beim Einsatz von Kryptomodulen [IT-Betrieb](CI)

Bei der Konfiguration eines Kryptomoduls SOLLTEN Benutzerrollen festgelegt werden. Es SOLLTE mit Zugriffskontroll- und Authentisierungsmechanismen verifiziert werden, ob ein Mitarbeiter den gewünschten Dienst auch tatsächlich benutzen darf. Das Kryptomodul SOLLTE so konfiguriert sein, dass bei jedem Rollenwechsel oder bei Inaktivität nach einer bestimmten Zeitdauer die Authentisierungsinformationen erneut eingegeben werden müssen.

#### CON.1.A13 Anforderungen an die Betriebssystem-Sicherheit beim Einsatz von Kryptomodulen(CI)

Das Zusammenwirken von Betriebssystem und Kryptomodulen SOLLTE gewährleisten, dass

* die installierten Kryptomodule nicht unbemerkt abgeschaltet oder umgangen werden können, 
* die angewendeten oder gespeicherten Schlüssel nicht kompromittiert werden können, 
* die zu schützenden Daten nur mit Wissen und unter Kontrolle des Benutzers auch unverschlüsselt auf Datenträgern abgespeichert werden bzw. das informationsverarbeitende System verlassen können und
* Manipulationsversuche am Kryptomodul erkannt werden.
#### CON.1.A14 Schulung von Benutzern und Administratoren [Vorgesetzte, Leiter IT, Fachverantwortliche](CIA)

Es SOLLTEN Schulungen durchgeführt werden, in denen Benutzern und Administratoren der Umgang mit den von ihnen zu bedienenden Kryptomodulen vermittelt wird. Den Benutzern SOLLTEN genau erläutert werden, was die spezifischen Sicherheitseinstellungen von Kryptomodulen bedeuten und warum sie wichtig sind. Außerdem SOLLTEN sie auf die Gefahren hingewiesen werden, wenn diese Sicherheitseinstellungen aus Bequemlichkeit umgangen oder deaktiviert werden. Die Schulungsinhalte SOLLTEN immer entsprechend der jeweiligen Einsatzszenarien angepasst werden. 

Administratoren SOLLTEN zudem lernen, wie sie mit Hilfsmitteln zur Untersuchung kryptografischer Einstellungen umgehen müssen. Auch SOLLTEN sie einen Überblick über kryptografische Grundbegriffe erhalten.

#### CON.1.A15 Reaktion auf praktische Schwächung eines Kryptoverfahrens(CI)

Es SOLLTE ein Prozess etabliert werden, der im Falle eines geschwächten kryptografischen Verfahrens herangezogen werden kann, um die Informationssicherheit der Institution zu gewährleisten. Dabei SOLLTE sichergestellt werden, dass das geschwächte kryptografische Verfahren abgesichert werden kann oder durch eine geeignete Alternative abgelöst wird.

#### CON.1.A16 Physische Absicherung von Kryptomodulen [Leiter IT](CI)

Es SOLLTE verhindert werden, dass unautorisiert physisch auf Modulinhalte des Kryptomoduls zugegriffen wird. Hard- und Softwareprodukte, die als Kryptomodule eingesetzt werden, SOLLTEN einen Selbsttest durchführen können.

#### CON.1.A17 Abstrahlsicherheit [Leiter IT](C)

Es SOLLTE untersucht werden, ob zusätzliche Maßnahmen hinsichtlich der Abstrahlsicherheit notwendig sind. Dies SOLLTE insbesondere gemacht werden, wenn staatliche Verschlusssachen (VS) der Geheimhaltungsgrade VS-VERTRAULICH und höher verarbeitet werden.

#### CON.1.A18 Kryptografische Ersatzmodule [Leiter IT](CIA)

Es SOLLTEN Ersatzkryptomodule vorrätig gehalten werden.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Kryptokonzept" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001A10] ISO/IEC 27001:2013 - Annex A.10 Cryptography

  

 Information technology - Security techniques - Information security management systems - Requirements, insbesondere Annex A, A.10 Cryptography, 2013  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [BSILEK] Leitfaden Erstellung von Kryptokonzepten

  

 Bundesamt für Sicherheit in der Informationstechnik (BSI), 07.2008  
 [https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Arbeitshilfen/Kryptokonzept/Kryptokonzept\_node.html](https://www.bsi.bund.de/DE/Themen/Sicherheitsberatung/Arbeitshilfen/Kryptokonzept/Kryptokonzept_node.html)

 
* #### [BSIMKK] Musterkryptokonzept

  

 BSI, 05.2010  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Sicherheitsberatung/Krypto/2010-04-28\_Musterkryptokonzept\_V12\_pdf.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Sicherheitsberatung/Krypto/2010-04-28_Musterkryptokonzept_V12_pdf.pdf)

 
* #### [ISFTS2] The Standard of Good Practice - Area TS2 Cryptography

  

 Information Security Forum (ISF), insbesondere Area TS2 Cryptography, 06.2016

 
* #### [NIST800175B] NIST Special Publication 800-175B

  

 Guidelines for Using Cryptographic Standards in the Federal Goverment, 03.2013  
 [https://csrc.nist.gov/publications/drafts/800-175/sp800-175b\_draft.pdf](https://csrc.nist.gov/publications/drafts/800-175/sp800-175b_draft.pdf)

 
* #### [TR02102] Kryptographische Verfahren- Empfehlungen und Schlüssellängen

  

 BSI, (zuletzt abgerufen am 27.09.2017)   
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Kryptokonzept" von Bedeutung.

* G 0.13 Abfangen kompromittierender Strahlung
* G 0.14 Ausspähen von Informationen (Spionage)
* G 0.15 Abhören
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.21 Manipulation von Hard- oder Software
* G 0.22 Manipulation von Informationen
* G 0.23 Unbefugtes Eindringen in IT-Systeme
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.26 Fehlfunktion von Geräten oder Systemen
* G 0.27 Ressourcenmangel
* G 0.28 Software-Schwachstellen oder -Fehler
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.31 Fehlerhafte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.37 Abstreiten von Handlungen
* G 0.40 Verhinderung von Diensten (Denial of Service)
* G 0.43 Einspielen von Nachrichten
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

