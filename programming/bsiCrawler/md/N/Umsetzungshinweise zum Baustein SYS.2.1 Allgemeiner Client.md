1 Beschreibung
--------------

### 1.1 Einleitung

Als "Allgemeiner Client" wird ein IT-System mit einem beliebigen Betriebssystem bezeichnet, das die Trennung von Benutzern zulässt. Es sollten mindestens eine Administrator- und eine Benutzer-Umgebung eingerichtet werden können. Typischerweise ist ein solches IT-System vernetzt und wird als Client in einem Client-Server-Netz betrieben. Das IT-System kann auf einer beliebigen Plattform betrieben werden. Dabei kann es sich beispielsweise um einen PC mit oder ohne Festplatte, um ein mobiles oder stationäres Gerät, aber auch um eine Unix-Workstation oder einen Apple Mac handeln. Das IT-System verfügt in der Regel über Laufwerke für auswechselbare Datenträger, weitere Schnittstellen für den Datenaustausch sowie andere Peripheriegeräte.

### 1.2 Lebenszyklus

**Planung und Konzeption**

Für die sichere Nutzung von IT-Systemen müssen vorab die Rahmenbedingungen festgelegt werden. Dabei müssen die Sicherheitsanforderungen für die bereits vorhandenen IT-Systeme sowie die geplanten Einsatzszenarien von Anfang an mit einbezogen werden (siehe SYS.2.1.M9 Planung des Einsatzes von Client-Server-Netzen). Schon vor der Beschaffung der Clients und Software sollte eine Sicherheitsrichtlinie für die Clients erstellt werden (siehe SYS.2.1.M8 Festlegen einer Sicherheitsrichtlinie für ein Client-Server-Netz).

**Beschaffung**

Für die Beschaffung von Clients, die typischerweise in größeren Mengen erfolgt, müssen ausgehend von den Einsatzszenarien Kriterien für die Auswahl geeigneter Produkte formuliert werden (siehe hierzu SYS.1.1.M10 Beschaffung eines Client). Auch bei der Beschaffung von Einzelsystemen ist es wichtig, dass der Client zur vorhandenen Struktur passt, damit nicht für ein einzelnes IT-System wegen dessen Besonderheiten ein unangemessen hoher Aufwand bei Integration und Betrieb entsteht.

Falls Hard- oder Software nicht die festgelegten Sicherheitsanforderungen erfüllen, sind weitere Maßnahmen erforderlich. Diese können organisatorischer Art sein (beispielsweise durch Regelungen, dass der Client ausschließlich hinter verschlossener Bürotür betrieben werden darf) oder es können in speziellen Fällen Zusatzkomponenten beschafft werden, um die identifizierten Mankos auszugleichen.

Bei besonders hohen Anforderungen an die Verfügbarkeit der Clients ist für diese der Einsatz einer Unterbrechungsfreien Stromversorgung (USV) empfehlenswert (siehe SYS.2.1.M35 Unterbrechungsfreie und stabile Stromversorgung). Dabei kann es sich beispielsweise um eine "Einzelplatz-USV" handeln, falls die hohen Anforderungen nur für einzelne Clients gelten, oder aber um einen eigenen entsprechend abgesicherten Stromkreis ("rote Steckdose").

**Umsetzung**

Um Risiken durch Fehlbedienung oder absichtlichen Missbrauch der IT-Systeme auszuschließen, sind eine sorgfältige Auswahl der Betriebssystem- und Softwarekomponenten, eine sichere Installation und sorgfältige Konfiguration wichtig. Die dabei zu treffenden Maßnahmen sind in hohem Grade abhängig von dem eingesetzten Betriebssystem. Näheres dazu findet sich deswegen in spezifischen Bausteinen, beispielsweise in SYS.2.3 Client unter Linux oder SYS.2.3 Client unter Windows 10. 

Der Grundstein für die Sicherheit wird bereits bei der Vorbereitung der Installation gelegt. Vor der Installation sollte festgelegt werden, welche Komponenten des Betriebssystems und welche Anwendungsprogramme und Tools installiert werden sollen. Die getroffenen Entscheidungen müssen so dokumentiert werden, dass gegebenenfalls nachvollzogen werden kann, wie die IT-Systeme konfiguriert und mit welcher Software ausgestattet wurden (siehe SYS.2.1.M14 Sichere Installation und Konfiguration eines Clients).

**Betrieb**

Eine der wichtigsten Sicherheitsmaßnahmen beim Betrieb heutiger Client-Systeme ist es, die IT-Systeme durch die Installation und permanente Aktualisierung eines Virenscanners (siehe dazu auch SYS.2.1.M6 Einsatz von Viren-Schutzprogrammen) zu schützen. Daneben ist eine regelmäßige Datensicherung (siehe auch SYS.2.1.M4 Regelmäßige Datensicherung) eine grundlegende Voraussetzung dafür, dass Hardwaredefekte und Programm- oder Benutzerfehler nicht zu gravierenden Datenverlusten führen.

**Aussonderung**

Bei der Aussonderung eines Clients muss zunächst sichergestellt werden, dass alle Benutzerdaten gesichert oder auf ein Ersatzsystem übertragen werden. Anschließend muss dafür gesorgt werden, dass keine sensitiven Daten auf den Festplatten des Clients zurück bleiben. Dazu genügt es nicht, die Platten einfach neu zu formatieren, sondern sie müssen mindestens einmal vollständig überschrieben werden. Es ist zu beachten, dass die Daten nicht wirklich von den Festplatten entfernt werden, wenn sie nur logisch gelöscht oder mit den Mitteln des installierten Betriebssystems neu formatiert werden. Mit geeigneter Software können Daten, die auf diese Weise gelöscht wurden, wieder rekonstruiert werden, oft sogar ohne großen Aufwand. Nach der Aussonderung eines Clients müssen Bestandsverzeichnisse und Netzpläne aktualisiert werden. Vertiefende Informationen hierzu sind in SYS.2.1.M24 Geregelte Außerbetriebnahme eines Clients zu finden.

**Notfallvorsorge**

Das notwendige Maß an Notfallvorsorge für einen allgemeinen Client ist stark vom individuellen Einsatzszenario abhängig. Oft wird als Notfallvorsorge für einen Client ausreichend sein, regelmäßig die Daten zu sichern und einen bootfähigen Datenträger für Notfälle zu erstellen (siehe SYS.1.1.M34 Einbindung in die Notfallplanung ). Für Clients mit besonderen Anforderungen an die Verfügbarkeit kann es sinnvoll sein, weitere Maßnahmen zu ergreifen, beispielsweise ein Austauschsystem bereit zu halten.

2 Maßnahmen
-----------

Im Folgenden sind spezifische Umsetzungshinweise im Bereich "Allgemeiner Client" aufgeführt.

### 2.1 Basis-Maßnahmen

Die folgenden Maßnahmen sollten vorrangig umgesetzt werden:

#### SYS.2.1.M1 Benutzerauthentisierung

Die Identifikations- und Authentikationsmechanismen von IT-Systemen bzw. IT-Anwendungen müssen so gestaltet sein, dass Benutzer eindeutig identifiziert und authentisiert werden. Die Identifikation und Authentisierung muss vor jeder anderen Interaktion zwischen IT-System und Benutzer erfolgen. Weitere Interaktionen dürfen nur möglich sein, nachdem die Benutzer sich erfolgreiche identifiziert und authentisiert haben. Die Authentisierungsinformationen müssen so gespeichert sein, dass nur autorisierte Benutzer darauf Zugriff haben (sie prüfen oder ändern können). Bei jeder Interaktion muss das IT-System die Identität des Benutzers feststellen können.

Es gibt verschiedene Techniken, über die die Authentizität eines Benutzers nachgewiesen werden kann. Die bekanntesten sind:

* PINs (Persönliche Identifikationsnummern),
* Passwörter,
* Token wie z. B. Zugangskarten sowie
* Biometrie.
Für sicherheitskritische Anwendungsbereiche sollte starke Authentisierung verwendet werden, hierbei werden zwei oder mehr Authentisierungstechniken kombiniert, wie Passwort plus Transaktionsnummern (Einmalpasswörter) oder plus Chipkarte. Daher wird dies auch häufig als Zwei-Faktor-Authentisierung bzw. Mehr-Faktor-Authentisierung bezeichnet. Alle eingesetzten Authentisierungstechniken müssen sich auf dem Stand der Technik befinden.

**Passwörter**

Werden in einem Client Passwörter zur Authentisierung verwendet, so ist die Sicherheit der Zugangs- und Zugriffsrechteverwaltung des IT-Systems entscheidend davon abhängig, dass die Passwörter korrekt gebraucht werden. Dafür sollte eine Richtlinie zum Passwortgebrauch erstellt und veröffentlicht werden. Außerdem sollten die IT-Benutzer regelmäßig, z.B. bei Team-Meetings, darauf hingewiesen werden.

Wenn Passwörter zur Authentikation eingesetzt werden, sollte das IT-System Mechanismen bieten, die folgende Bedingungen erfüllen:

* Es wird gewährleistet, dass jeder Benutzer individuelle Passwörter benutzt (und diese auch selbst auswählen kann).
* Es wird überprüft, dass alle Passwörter den definierten Vorgaben genügen (z. B. Mindestlänge, keine Trivialpasswörter). Die Prüfung der Passwortgüte sollte individuell regelbar sein. Beispielsweise sollten vorgegeben werden können, dass die Passwörter mindestens ein Sonderzeichen enthalten müssen oder bestimmte Zeichenkombinationen verboten werden.
* Das IT-System generiert Passwörter, die den definierten Vorgaben genügen. Das IT-System muss die so erzeugten Passwörter dem Benutzer anbieten.
* Der Passwortwechsel sollte von den IT-Systemen regelmäßig initiiert werden. Die Lebensdauer eines Passwortes sollte einstellbar sein.
* Die Wiederholung alter Passwörter beim Passwortwechsel sollte vom IT-System verhindert werden (Passwort-Historie).
* Bei der Eingabe sollte das Passwort nicht auf dem Bildschirm angezeigt werden.
* Nach der Installation bzw. der Neueinrichtung von Benutzern sollte das Passwort-System einen Passwort-Wechsel nach der Erst-Anmeldung erzwingen.
Vertiefende Informationen zur Authentisierung sind in ORP.4 Identitäts- und Berechtigungsmanagement zu finden.

#### SYS.2.1.M2 Rollentrennung

Grundsätzlich kann zwischen Kennungen für Benutzer- und Administratoren unterschieden werden. Nur Administratoren verwalten die IT-Systeme, während normale Benutzerkennungen nur die Rechte besitzen, um ihre arbeitsplatzspezifischen Aufgaben erfüllen zu können. Normale Benutzerkennungen dürfen keine Administrationsrechte besitzen, damit das Betriebssystem und die Konfiguration der Clients vor versehentlicher, fahrlässiger oder vorsätzlicher Modifikation durch die Benutzer geschützt werden. 

Falls Benutzer nur bestimmte administrative Aufgaben wahrnehmen müssen, ist es oftmals nicht erforderlich, ihnen alle mit einem eigenen Login verbundenen Rechte oder sogar Systemadministrator-Rechte zu geben. Beispiele sind bestimmte Tätigkeiten der routinemäßigen Systemverwaltung, wie die Erstellung von Backups oder das Einrichten eines neuen Benutzers, die mit einem Programm menügesteuert durchgeführt werden, oder Tätigkeiten, für die ein Benutzer nur ein einzelnes Anwendungsprogramm benötigt. Insbesondere bei Aushilfskräften und externen Dienstleistern muss darauf geachtet werden, dass diese nur die Dienste verwenden und nur auf die Daten zugreifen dürfen, die sie tatsächlich benötigen. Wenn ihre Tätigkeit beendet ist, sind deren Accounts zu deaktivieren und alle Zugangsberechtigungen zu entfernen.

Wenn möglich, sollte für die Benutzer eine eingeschränkte Benutzerumgebung geschaffen werden. Sie kann zum Beispiel unter Unix durch eine Restricted Shell (rsh) und eine Beschränkung der Zugriffspfade mit dem Unix-Kommando chroot realisiert werden. Eine weitere Möglichkeit besteht darin, einzelne Anwendungsprogramme, wie Web-Browser, im sogenannten Kiosk-Modus auszuführen, so dass nur ein beschränkter Zugriff besteht.

Werden an Benutzerkennungen besonders weitgehende Rechte vergeben, so sollte dies möglichst restriktiv erfolgen. Hierbei sollte zum einem der Kreis der privilegierten Benutzer möglichst eingeschränkt werden und zum anderen nur die für die Durchführung der Arbeit benötigten Rechte vergeben werden. Für alle Aufgaben, die ohne erweiterte Rechte durchgeführt werden können, sollten auch privilegierte Benutzer unter Kennungen mit Standard-Rechten arbeiten. 

#### SYS.2.1.M3 Aktivieren von Autoupdate-Mechanismen

Viele Produkte verfügen über automatische Update-Mechanismen (Autoupdate), die die Anwender darüber informieren, wenn Patches oder Updates vorhanden sind. Häufig bieten diese auch die Option, die Updates sofort über das Internet herunterzuladen und zu installieren. Generell müssen die vorhandenen Autoupdate-Mechanismen aktiviert werden. In der Regel enthalten heute alle Betriebssysteme und verfügbaren Standardsoftwarepakete solche Mechanismen. Die Funktionsweise des Update-Mechanismus ist je nach Version, Installationsmodus und Hersteller unterschiedlich ausgeprägt.

Üblicherweise suchen IT-Produkte mit Autoupdate bei jedem Start der IT-Systeme oder bei jeder Einwahl in das Internet auf einem öffentlichen Updateserver nach neuen Versionen oder Softwarepaketen. Produkte bieten verschiedene Möglichkeiten, den Autoupdate-Mechanismus zu konfigurieren. Wenn neue IT-Komponenten in Betrieb genommen werden, sollte immer auch überprüft werden, ob und welche Update-Mechanismen diese haben und wie diese konfiguriert werden können. Dabei sollten auch kontrolliert werden, welche Daten vom Autoupdate-Mechanismus zum Hersteller übertragen werden. Es sollte zunächst grundsätzlich geklärt werden, wie mit diesen Mechanismen umgegangen wird. Danach sollte festgelegt werden, wie die Update-Funktionen konkret in den verschiedenen Produkten konfiguriert werden. Im Folgenden wird ein Überblick über verschiedene Varianten dieser Mechanismen gegeben.

Das komplette Deaktivieren wird nicht von jeder Software angeboten. Falls die Institution die unkontrollierte Kommunikation von IT-Komponenten mit der Außenwelt unterbinden will, müssen hierfür Paketfilter eingesetzt werden.

Wird eine Abfrage von einem öffentlichen Update-Server nicht gewünscht, lassen sich viele Softwareprodukte auf andere Internet-Adressen als die des Herstellers, beispielsweise interne, umlenken.

Einige Hersteller bieten Software für den Eigenbetrieb von Update-Servern oder Update-Spiegelservern an, dabei wird der Update-Server in der Institution lokal installiert (z. B. Windows Server Update Services WSUS). Der Update-Server kommuniziert dann direkt mit dem Hersteller und lädt die gewünschten Aktualisierungen direkt vom Hersteller. Der Vorteil dieser Lösung ist, dass die von der Aktualisierung betroffenen IT-Systeme einer Institution nicht selber mit dem Update-Server des Herstellers kommunizieren müssen, sondern nur mit dem lokal installierten. Dadurch kann der Datenverkehr nach Außen auf ein Mindestmaß reduziert werden. Bei vielen Produkten für Update-Servern lassen sich die gewünschten Einstellungen komfortabel über eine grafische Benutzeroberfläche (GUI) vornehmen. Allerdings gibt es auch Produkte, bei denen die notwendigen Einstellungen, um lokale Update-Server zu verwenden oder die Abfrage von einem öffentlichen Updateserver zu unterbinden, verborgen oder nur per Paketfilter bzw. Firewall zu unterbinden sind.

Falls öffentliche Update-Server genutzt werden sollen, so ist zunächst die Authentizität des Update-Servers zu prüfen. Außerdem sollte untersucht werden, ob Zeitintervalle oder Ereignisse zur Steuerung der Update-Abfrageaktion eingestellt werden können. Die Einstellungen müssen dann entsprechend der festgelegten Änderungsstrategie vorgenommen werden.

Es sollte geprüft werden, wie die Kommunikation mit Update-Servern auf das geringst mögliche Maß beschränkt werden kann. Außerdem muss entschieden werden, ob die direkte Kommunikation mit dem Hersteller als einzige Alternative oder parallel zur internen Kommunikation (Parallelkonfiguration) betrieben werden soll.

Eine Parallelkonfiguration ist häufig sinnvoll für mobile Nutzer, die nicht immer innerhalb des Behörden- oder Unternehmensnetzes kommunizieren. Bei mobilen IT-Systemen kann es beispielsweise wichtiger sein, unterwegs einen aktuellen Patch einzuspielen, wenn dieser eine gefährliche Sicherheitslücke schließt, als auf die Freigabe vom Änderungsmanagement zu warten. Es kann jedoch auch gewünscht werden, dass sämtliche Software-Änderungen ausschließlich durch die interne freigegebene Softwareverteilung erfolgen.

Bei Autoupdate-Mechanismen ist unter anderem noch zu beachten, ob die Änderungen vom Hersteller nur auf ein internes IT-System geladen werden und die Installation der Änderung danach dem Benutzer überlassen wird, oder ob diese nach dem Herunterladen sofort automatisch installiert werden.

Außerdem muss festgelegt werden, wie damit umgegangen werden soll, wenn durch ein Update das IT-System neu gestartet werden muss. Es kann entschieden werden, das IT-System sofort neu zu starten, es kann aber auch oft festgelegt werden, dass derartige Updates erst installiert werden, wenn das IT-System sowieso planmäßig runter gefahren wird. 

#### SYS.2.1.M4 Regelmäßige Datensicherung

Zur Vermeidung von Datenverlusten müssen regelmäßige Datensicherungen durchgeführt werden. In den meisten Clients können diese weitgehend automatisiert erfolgen. Es sind Regelungen zu treffen, welche Daten von wem wann gesichert werden.

Es müssen mindestens die Daten regelmäßig gesichert werden, die nicht aus anderen Informationen abgeleitet werden können. 

Es wird empfohlen, ein Datensicherungskonzept zu erstellen, hierfür sollten die Anforderungen des Baustein OPS.1.1.5 Datensicherung berücksichtigt werden 

**Hinweis: **Auch wenn Benutzer alle Arbeitsergebnisse auf zentralen Servern speichern sollen, werden sich immer wieder geschäftsrelevante Daten auf Clients finden, solange diese eine Möglichkeit dafür bieten. Daher müssen auch Clients in das Datensicherungskonzept der Institution einbezogen werden.

Abhängig von der Menge und Wichtigkeit der laufend neu gespeicherten Daten und vom möglichen Schaden bei Verlust dieser Daten ist folgendes festzulegen:

* Zeitintervall  
 Beispiele: täglich, wöchentlich, monatlich
* Zeitpunkt  
 Beispiele: nachts, freitags abends
* Anzahl der aufzubewahrenden Generationen  
 Beispiel: Bei täglicher Komplettsicherung werden die letzten sieben Sicherungen aufbewahrt, außerdem die Freitag-Abend-Sicherungen der letzten zwei Monate.
* Umfang der zu sichernden Daten  
 Am einfachsten ist es, Partitionen bzw. Verzeichnisse festzulegen, die bei der regelmäßigen Datensicherung berücksichtigt werden. Eine geeignete Differenzierung kann die Übersichtlichkeit vergrößern sowie Aufwand und Kosten sparen helfen.Beispiel: selbst erstellte Dateien und individuelle Konfigurationsdateien
* Speichermedien (abhängig von der Datenmenge)  
 Beispiele: Bänder, DVDs oder Blu-rays, Festplatten, USB-Sticks
* Vorherige Löschung der Datenträger vor Wiederverwendung (z. B. bei Bändern oder Kassetten)
* Zuständigkeit für die Durchführung (Administrator, Benutzer)
* Zuständigkeit für die Überwachung der Sicherung, insbesondere bei automatischer Durchführung (Fehlermeldungen, verbleibender Platz auf den Speichermedien)
* Dokumentation der erstellten Sicherungen (Datum, Art der Durchführung der Sicherung sowie gewählte Parameter, Beschriftung der Datenträger)
Wegen des großen Aufwands können Komplettsicherungen in der Regel höchstens einmal täglich durchgeführt werden. Die seit der letzten Sicherung erstellten Daten können nicht wieder eingespielt werden. Daher und zur Senkung der Kosten sollten zwischen den Komplettsicherungen regelmäßig differentielle oder inkrementelle Sicherungen durchgeführt werden. Hinweise zu den verschiedenen Arten von Datensicherungen finden sich in den Umsetzungshinweisen des Bausteins OPS.1.1.5 Datensicherung.

Eine differentielle oder inkrementelle Sicherung kann häufiger erfolgen, zum Beispiel sofort nach Erstellung wichtiger Dateien oder mehrmals täglich. Die Vereinbarkeit mit dem laufenden Betrieb ist sicherzustellen.

Für eingesetzte Software ist separat zu entscheiden, ob sie von der regelmäßigen Datensicherung erfasst werden muss. Dies hängt beispielsweise davon ab, wie aufwendig es, den Client neu zu installieren und Patches und Updates einzuspielen. Unter Umständen ist es ausreichend, Sicherungskopien von den Originaldatenträgern anzufertigen.

Es muss regelmäßig getestet werden, ob die Datensicherung auch wie gewünscht funktioniert, vor allem, ob gesicherte Daten problemlos zurückgespielt werden können.

Alle Benutzer sollten über die Regelungen zur Datensicherung informiert sein, um gegebenenfalls auf Unzulänglichkeiten (zum Beispiel zu geringes Zeitintervall für ihren Bedarf) hinweisen oder individuelle Ergänzungen vornehmen zu können (zum Beispiel zwischenzeitliche Spiegelung wichtiger Daten auf der eigenen Platte). Auch die Information der Benutzer darüber, wie lange die Daten wiedereinspielbar sind, ist wichtig. Werden zum Beispiel bei wöchentlicher Komplettsicherung nur zwei Generationen aufbewahrt, bleiben in Abhängigkeit vom Zeitpunkt des Verlustes nur zwei bis drei Wochen Zeit, um die Wiedereinspielung vorzunehmen.

Falls bei vernetzten Clients nur die Netzfreigaben gesichert werden, ist sicherzustellen, dass die zu sichernden Daten regelmäßig von den Benutzern oder automatisch dorthin überspielt werden, besser ist es, wenn alle Daten ausschließlich auf den Netzlaufwerken abgelegt werden. Bei größeren Änderungen an IT-Systemen oder des Informationsverbunds muss der Datensicherungsprozess entsprechend angepasst werden.

Vertrauliche Daten sollten vor der Sicherung möglichst verschlüsselt werden, dabei müssen die Daten auch nach einem längeren Zeitraum entschlüsselt werden können (siehe CON.1 Kryptokonzept).

Der Ausdruck von Daten auf Papier ist keine angemessene Art der Datensicherung.

#### SYS.2.1.M5 Bildschirmsperre [Benutzer]

Unter einer Bildschirmsperre wird die Möglichkeit verstanden, die auf dem Bildschirm aktuell gezeigten Informationen zu verbergen sowie den Rechner vor unbefugtem Zugriff zu schützen. Eine Bildschirmsperre muss nur durch eine erfolgreiche Benutzerauthentikation, also z. B. eine Passwortabfrage, deaktiviert werden können, damit bei einer kürzeren Abwesenheit des IT-Benutzers ein Zugriffsschutz für das IT-System gewährleistet wird.

Die Bildschirmsperre sollte sich sowohl manuell vom Benutzer aktivieren lassen, als auch nach einem vorgegebenen Inaktivitäts-Zeitraum automatisch gestartet werden. Alle Benutzer sollten dafür sensibilisiert sein, dass sie die Bildschirmsperre aktivieren, wenn sie den Arbeitsplatz für eine kurze Zeit verlassen. Bei längeren Abwesenheiten sollten Benutzer sich abmelden.

Der Zeitraum, nach dem sich eine Bildschirmsperre wegen fehlender Benutzereingaben aktiviert, sollte gewisse Grenzen weder unter- noch überschreiten. Der Zeitraum sollte nicht zu knapp gewählt werden, damit die Bildschirmsperre nicht bereits nach kurzen Denkpausen anspringt. Dieser Zeitraum darf aber auf keinen Fall zu lang sein, damit die Abwesenheit des Benutzers nicht von Dritten ausgenutzt werden kann. Eine sinnvolle Vorgabe ist eine Zeitspanne von 15 Minuten. Es sollten Vorgaben für die Einstellung der Wartezeit gemacht werden, die die Sicherheitsanforderungen der jeweiligen IT-Systeme und deren Einsatzumgebung berücksichtigen.

Fast alle Betriebssysteme enthalten Bildschirmsperren. Bei deren Nutzung muss darauf geachtet werden, die Passwortabfrage zu aktivieren.

#### SYS.2.1.M6 Einsatz von Viren-Schutzprogrammen

Zum Schutz vor Schadprogrammen können unterschiedliche Wirkprinzipien genutzt werden. Programme, die IT-Systeme nach sämtlichen bekannten Schadprogrammen durchsuchen, haben sich in der Vergangenheit als mögliches Mittel in der Schadprogramm-Prävention erwiesen. Entsprechend der in OPS1.1.4 Schutz vor Schadprogrammen beschriebenen Anforderungen sollten daher Viren-Schutzprogramme eingesetzt werden.

**Regelmäßige Untersuchung des gesamten Datenbestands**

Auch wenn das Viren-Schutzprogramm bei jedem Dateizugriff eine Prüfung auf Schadprogramme durchführt, ist eine regelmäßige Untersuchung aller Dateien auf Clients und Datei-Servern sinnvoll. So können auch Schadprogramme gefunden werden, für die es noch keine Erkennungssignatur gab, als sie gespeichert wurden. In derartigen Fällen muss beispielsweise untersucht werden, ob das Schadprogramm vor seiner Entdeckung bereits vertrauliche Daten gesammelt, Schutzfunktionen deaktiviert oder Code aus dem Internet nachgeladen hat.

Aus Performance-Gründen sollte eine vollständige Prüfung des Datenbestands in Zeiten durchgeführt werden, in denen die IT-Ressourcen nicht stark beansprucht werden. Ideal ist es, wenn die Software die Auslastung des Clients überwacht und dessen "Arbeitspausen" automatisch für die Überprüfung nutzt. Auf den Clients könnte das Viren-Schutzprogramm z. B. auch mit dem Start des Bildschirmschoners gekoppelt werden. Auch bei starker Auslastung empfiehlt es sich, regelmäßig eine vollständige Prüfung des Datenbestands durchzuführen.

**Datenaustausch und Datenübertragung**

Daten, die versendet werden sollen, müssen unmittelbar vor dem Versand auf Schadprogramme geprüft werden. Analog müssen empfangene Daten unmittelbar nach dem Empfang auf Schadprogramme geprüft werden. Diese Überprüfungen sind sowohl beim Zugriff auf Datenträger als auch bei der Datenübertragung über Kommunikationsverbindungen erforderlich. Die Überprüfungen sollten so weit wie möglich automatisiert werden.

**Erkennung von Schadprogrammen auch in verschlüsselten oder komprimierten Dateien**

Beim Einsatz von Verschlüsselungstechniken müssen die potentiellen Auswirkungen auf den Schutz vor Schadprogrammen bedacht werden. Werden Daten verschlüsselt, so können Systemkomponenten bzw. Anwendungen auf diese Daten nicht zugreifen, solange sie nicht über die entsprechenden Schlüssel verfügen. Dies impliziert, dass ein Viren-Schutzprogramm entweder im Kontext des Benutzers laufen oder mit den entsprechenden kryptografischen Schlüsseln ausgestattet werden muss, um eine verschlüsselte Datei auf Schadprogramme überprüfen zu können. Wird jedoch die Benutzer-Kennung, unter der das Viren-Schutzprogramm ausgeführt wird, mit den entsprechenden kryptografischen Schlüsseln ausgestattet, entstehen neue Sicherheitsrisiken, die es zu vermeiden gilt. Daher wird der Einsatz eines residenten Viren-Schutzprogramms empfohlen, das die Prüfung auf Schadprogramme im Benutzer-Kontext bei jedem Zugriff auf eine Datei durchführt.

Das Viren-Schutzprogramm sollte Schadprogramme auch in komprimierten Dateien finden, wobei alle gängigen Komprimierungsfunktionen und Archivformate unterstützt werden sollten. Schadprogramme in geschachtelten Archivdateien sollten ebenfalls gefunden werden.

**Schutz vor unerlaubter Deaktivierung oder Änderung**

Die Viren-Schutzprogramme auf den Clients und Endgeräten müssen so konfiguriert sein, dass die Benutzer keine sicherheitsrelevanten Änderungen an den Einstellungen der Viren-Schutzprogramme vornehmen können. Insbesondere muss sichergestellt sein, dass die Benutzer die Viren-Schutzprogramme nicht deaktivieren können.

#### SYS.2.1.M7 Protokollierung

Die am Client mögliche Protokollierung ist in einem sinnvollen Umfang zu aktivieren. In regelmäßigen Abständen muss der IT-Betrieb die Protokolldateien der Clients überprüfen. Es sollten alle sicherheitsrelevanten Ereignisse protokolliert werden. Dabei sind insbesondere folgende Vorkommnisse von Interesse:

* falsche Passworteingabe für eine Benutzer-Kennung bis hin zur Sperrung der Benutzer-Kennung bei Erreichen der Fehlversuchsgrenze,
* Versuche von unberechtigten Zugriffen,
* Daten, aus denen die Netzauslastung und -überlastung ermittelt werden kann.
Wie viele Ereignisse darüber hinaus protokolliert werden, hängt unter anderem vom Schutzbedarf der jeweiligen IT-Systeme ab. Je höher deren Schutzbedarf ist, desto mehr sollte protokolliert werden.

Da die Protokoll-Dateien mit der Zeit sehr umfangreich werden können, sollten die Auswertungsintervalle so kurz gewählt werden, dass eine sinnvolle Auswertung möglich ist. Um eine sinnvolle Auswertung zu ermöglichen, sollte jeder Protokoll-Eintrag Benutzer-Kennung bzw. Prozessnummer, Kennzeichnung des Endgeräts, Datum und Uhrzeit enthalten.

Es ist zu prüfen, welche gesetzlichen oder vertraglichen Aufbewahrungsfristen für Protokoll-Dateien beachtet werden müssen. Damit Aktionen lange Zeit nachvollzogen werden können, kann eine Mindestspeicherdauer vorgeschrieben sein, aus Datenschutzgründen kann es auch eine Löschungspflicht geben.

Gerade bei einer Vielzahl von Clients sollten die Protokolldaten zentral zusammengeführt und ausgewertet werden. Hierfür wird empfohlen, einen zentralen Protokollierungsserver einzusetzen, siehe OPS.1.1.6 Protokollierung.

#### SYS.2.1.M8 Absicherung des Boot-Vorgangs

Wenn von Wechselmedien gebootet oder Fremdsoftware installiert wird, können nicht nur Sicherheitseinstellungen umgangen werden, sondern das IT-System kann auch mit Schadprogrammen infiziert werden. Zusätzlich können Schadprogramme auch in den Bootvorgang eingreifen. Diesen Gefahren sollten die Verantwortlichen durch geeignete organisatorische oderund technische Sicherheitsmaßnahmen entgegenwirken. Hierfür bieten sich verschiedene Vorgehensweisen an, die konkret in den Umsetzungshinweisen des Bausteins SYS.3.4 Mobile Datenträger beschrieben sind:

* Ausbau von Laufwerken
* Verschluss von Laufwerken
* Deaktivierung von Laufwerken im BIOS bzw. Betriebssystem
* Kontrolle der Schnittstellennutzung
* Verschlüsselung (ausschließlicher Zugriff auf verschlüsselte Datenträger)
* Richtlinien für die Nutzung
Unabhängig davon, für welche Vorgehensweise sich die Institution entscheidet, ist zu verhindern, dass Inhalte von mobilen Datenträgern automatisch ausgeführt werden, wenn diese angeschlossen werden. Hierzu sind die entsprechenden Autorun- und Autoplay-Funktionen des Betriebssystems zu deaktivieren. 

Um den Bootvorgang kryptographisch abzusichern, sollten bei Systemen mit UEFI-Firmware die Option SecureBoot aktiviert und die Schlüsseldatenbanken gemäß den Vorgaben der Institution konfiguriert werden. Diese Konfiguration sollte so gesichert werden, dass sie nicht abgeschaltet werden kann. Der Zugriff auf die Konfigurationsoberfläche der Firmware sollte mindestens mit Passwort gesichert sein.

Damit die Sicherheitsmaßnahmen akzeptiert und beachtet werden, müssen die Benutzer über die Gefährdung informiert und sensibilisiert werden.

### 2.2 Standard-Maßnahmen

Gemeinsam mit den Basis-Maßnahmen entsprechen die folgenden Maßnahmen dem Stand der Technik im Bereich "Allgemeiner Client".

#### SYS.2.1.M9 Festlegung einer Sicherheitsrichtlinie für Clients

Die Sicherheitsvorgaben für alle Clients ergeben sich aus der institutionsweiten Sicherheitsrichtlinie. Ausgehend von der allgemeinen Richtlinie müssen die Anforderungen für den gegebenen Kontext konkretisiert werden und in einer Sicherheitsrichtlinie für die jeweilige Gruppe von Clients zusammengefasst werden. In diesem Zusammenhang ist zu prüfen, ob neben der institutionsweiten Sicherheitsleitlinie weitere übergeordnete Vorgaben wie IT-Richtlinien, Passwortrichtlinien oder Vorgaben zur Internet-Nutzung zu berücksichtigen sind.

Die Sicherheitsrichtlinie muss allen Anwendern und anderen Personen, die an der Beschaffung und dem Betrieb der Clients beteiligt sind, bekannt sein und Grundlage für deren Arbeit sein. Wie bei allen Richtlinien sind ihre Inhalte und ihre Umsetzung im Rahmen einer übergeordneten Revision regelmäßig zu prüfen.

Die Sicherheitsrichtlinie sollte das generell zu erreichende Sicherheitsniveau spezifizieren und grundlegende Festlegungen treffen. Um die Übersichtlichkeit zu verbessern, kann es sinnvoll sein, für verschiedene Einsatzgebiete gesonderte Sicherheitsrichtlinien zu entwickeln.

Als erstes sollte die allgemeine Konfigurations- und Administrationsstrategie ("Liberal" oder "Restriktiv") festgelegt werden, da die weiteren Entscheidungen von dieser Festlegung wesentlich abhängen.

Für Clients mit normalem Schutzbedarf kann eine relativ liberale Strategie gewählt werden, was in vielen Fällen die Konfiguration und Administration vereinfacht. Generell ist es aber auch in diesen Fällen empfehlenswert, die Strategie nur "so liberal wie nötig" auszulegen.

Bei Clients mit einem hohen Schutzbedarf wird grundsätzlich eine restriktive Strategie empfohlen. Für Clients mit höherem Schutzbedarf bezüglich eines der drei Grundwerte sollte unbedingt eine restriktive Konfigurations- und Administrationsstrategie umgesetzt werden.

Nachfolgend sind einige Punkte aufgeführt, die berücksichtigt werden sollten:

* Regelungen für die Arbeit der Benutzer der Clients: 

 
	+ Soll ein Client nur von jeweils einem einzelnen Benutzer genutzt werden, oder ist ein Betrieb mit wechselnden Benutzern vorgesehen?
	+ Dürfen Benutzer bestimmte Konfigurationseinstellungen selbst ändern (beispielsweise Bildschirmhintergrund, Bildschirmschoner oder ähnliches) oder werden alle Einstellungen zentral vorgegeben?
	+ Dürfen Benutzer auf bestimmte Bereiche der IT-Systeme keinen Zugriff haben? Diese Vorgaben haben in der Regel sowohl Auswirkungen auf die Rechtevergabe im IT-System selbst als auch auf die Vorgaben für die Installation und Grundkonfiguration.
	+ Welche Informationen dürfen die Benutzer lokal auf den Clients abspeichern? Generell sollten alle geschäftsrelevanten Informationen zentral auf einem Server abgelegt werden, auf dem sie regelmäßig gesichert werden. Andernfalls muss dafür gesorgt werden, dass alle Informationen der Benutzer, die lokal auf den Clients abgespeichert sind, im Datensicherungskonzept des Clients berücksichtigt werden.
	+ Sind die Benutzer gehalten, den Client abends herunterzufahren und auszuschalten, oder muss er rund um die Uhr in Betrieb sein?Für das Ausschalten von Clients bei Arbeitsschluss sprechen beispielsweise Brandschutz und Stromersparnis. Darüber hinaus sind etwa Festplatten, die in Clients eingesetzt werden, meist nicht für einen Dauerbetrieb geeignet. Ein durchgehender Betrieb der Clients kann dennoch erwünscht sein, beispielsweise wenn über Nacht automatische Datensicherungen erstellt werden. 
	  

 
* Regelungen für die Arbeit des IT-Betriebs und Revisoren: 

 
	+ Nach welchem Schema werden Administrationsrechte vergeben? Welcher Administrator darf welche Rechte ausüben und wie erlangt er diese Rechte?
	+ Über welche Zugangswege dürfen Administratoren und Revisoren auf die IT-Systeme zugreifen?
	+ Welche Vorgänge und Ereignisse müssen dokumentiert werden? In welcher Form wird die Dokumentation erstellt und gepflegt?
	+ Gilt für bestimmte Änderungen ein Vier-Augen-Prinzip?
	  

 
* Vorgaben für die Installation und Grundkonfiguration: 

 
	+ Welche Installationsmedien werden zur Installation verwendet?
	+ Soll ein zentraler Authentisierungsdienst genutzt werden oder erfolgt die Benutzerverwaltung und -authentisierung nur lokal?
	  

 
* Regelungen zur Benutzer- und Rollenverwaltung, Berechtigungsstrukturen (Ablauf und Methoden der Authentisierung und Autorisierung, Berechtigung zu Installation, Update, Konfigurationsänderungen etc.). Nach Möglichkeit sollte ein Rollenkonzept für die Administration erarbeitet werden. Es dürfen keine Sammelkennungen, die verschiedene Benutzer mit derselben Kennung nutzen, verwendet werden. 

 
	+ Falls bei der Planung für die Clients festgelegt wurde, dass Teile des Dateisystems verschlüsselt werden sollen, so sollte an dieser Stelle festgelegt werden, wie dies zu geschehen hat (siehe auch SYS.2.1.M25 Verschlüsselung der Clients).
	+ Beim Einsatz verschlüsselter Dateisysteme sollte hierfür ein eigenes Konzept erstellt und die Details der Konfiguration besonders sorgfältig dokumentiert werden, da im Fall von Problemen (Verlust des Schlüssels oder der Passphrase zum Schlüssel, inkorrekte Konfiguration oder ähnliches) die Daten auf den verschlüsselten Dateisystemen sonst vollständig verloren sein können.
	+ Regelungen zu Erstellung und Pflege von Dokumentation
	  

 
* Vorgaben für den sicheren Betrieb: 

 
	+ Welcher Benutzerkreis darf sich auf den IT-Systemen anmelden?
	+ Wie können sich die Benutzer gegenüber dem IT-System authentisieren? Generell sollte auf eine automatische Anmeldung, bei der die Benutzer ohne eine aktive Authentisierung beim Hochfahren des Clients angemeldet werden, verzichtet werden.
	+ Erhalten Benutzer Zugriff auf ein oder mehrere LANs oder das Internet? Welche Protokolle dürfen verwendet werden? Bei Clients, die als Arbeitsplatzrechner in einer Institution genutzt werden, ist es in der Regel nicht notwendig und oft auch nicht wünschenswert, dass normale Benutzer über das Netz auf einen anderen Arbeitsplatzrechner zugreifen.
	+ Auf welche Ressourcen dürfen die Benutzer zugreifen?
	+ Es müssen Vorgaben für die Passwortnutzung erstellt werden (Passwortregeln, Regeln und Situationen für Passwortänderungen, gegebenenfalls Hinterlegung von Passwörtern).
	+ Wie wird der Startvorgang des IT-Systems ("Booten") gegen Manipulation abgesichert? Nur Administratoren sollten die Clients von Laufwerken oder externen Speichermedien booten können. Daher sollten Clients mit einer Boot-Sperre versehen werden, die ein Starten von externen Medien wie CD-ROMs, DVDs oder USB-Speicher verhindert (siehe SYS.2.1.M12 Absicherung des Boot-Vorgangs).Es wird empfohlen, für den Normalbetrieb eine solche Sperre vorzusehen, die nur im Rahmen einer Störungssuche und -beseitigung vom IT-Betrieb aufgehoben werden kann, wenn er das IT-System mit dem Notfall-Bootmedium (siehe SYS.2.1.M4 Regelmäßige Datensicherung) startet.
	+ Soll das IT-System den Bootvorgang kryptographisch absichern, z. B. via UEFI Secure Boot?
	  

 
* Netzkommunikation und -dienste: 

 
	+ Soll ein lokaler Paketfilter aufgesetzt werden?
	+ Auf welche externen Netzdienste soll von dem Client aus zugegriffen werden können?
	+ Soll ein verteiltes Dateisystem eingebunden werden?Verteilte Dateisysteme, bei denen die Nutzdaten unverschlüsselt übertragen werden, sollten nur ausnahmsweise und ausschließlich im internen Netz verwendet werden. Soll ein verteiltes Dateisystem über ein unsicheres Netz hinweg genutzt werden, so muss es durch zusätzliche Maßnahmen (kryptographisch geschütztes VPN, Tunneling) gesichert werden.
	  

 
* Protokollierung: 

 
	+ Welche Daten werden protokolliert? Wie und in welchen Intervallen werden die Protokolldaten ausgewertet? Wer führt die Auswertung durch?
	  

 
Anhand der oben genannten Punkte kann eine Checkliste erstellt werden, die bei Audits oder Revisionen hilfreich sein kann.

Die Verantwortung für die Sicherheitsrichtlinie liegt beim Sicherheitsmanagement. Änderungen und Abweichungen hiervon dürfen nur in Abstimmung mit dem Sicherheitsmanagement erfolgen.

Bei der Erstellung einer Sicherheitsrichtlinie ist es empfehlenswert, so vorzugehen, dass zunächst ein Maximum an Forderungen und Vorgaben für die Sicherheit der IT-Systeme aufgestellt wird. Diese können anschließend den tatsächlichen Gegebenheiten angepasst werden. Idealerweise wird so erreicht, dass alle notwendigen Aspekte berücksichtigt werden. Für jede im zweiten Schritt verworfene oder abgeschwächte Vorgabe sollte der Grund für die Nicht-Berücksichtigung dokumentiert werden.

In Bezug auf Regelungen für die Benutzer sollte jedoch beachtet werden, dass diese nur so weit sinnvoll sind, wie sie im normalen Arbeitsalltag anwendbar sind, aber auch wie sie überwacht und durchgesetzt werden können. Beispielsweise ist es bei Zugriffsbeschränkungen nicht zielführend, den Benutzern nur in der Sicherheitsrichtlinie den Zugriff auf bestimmte Verzeichnisse zu verbieten, diese aber nicht auch durch eine entsprechende Rechtevergabe tatsächlich vor dem Zugriff zu schützen. Zugriffsbeschränkungen, die bei der Erstellung der Sicherheitsrichtlinie festgelegt wurden, sollten daher immer so weit wie möglich über entsprechende Vorgaben für die Installation und Konfiguration der Clients umgesetzt werden.

Während die Sicherheitsrichtlinie für Clients formuliert wird, ist es auch wichtig, eine Balance zwischen Sicherheit (indem die Funktionalität eingeschränkt und Benutzerrechte restriktiv vergeben werden) und Benutzerfreundlichkeit zu finden. Werden die Benutzer durch Regelungen, die für sie nicht transparent sind und die eventuell sogar als Schikane empfunden werden, zu sehr eingeschränkt, so kann sie dies im Gegenzug dazu verleiten, diese Beschränkungen mit besonderer Kreativität zu umgehen.

Dies unterscheidet die Sicherheitsrichtlinie für Clients von den entsprechenden Richtlinien etwa für Server oder aktive Netzkomponenten, bei denen in der Regel nur technisch versierte Anwender und Administratoren angesprochen sind, denen viele Einschränkungen eher plausibel gemacht werden können.

#### SYS.2.1.M10 Planung des Einsatzes von Clients

Eine grundlegende Voraussetzung dafür, dass Clients sicher betrieben werden können, ist ein angemessenes Maß an Planung im Vorfeld.

Die Planung des Einsatzes kann in mehreren Schritten nach dem Prinzip des Top-Down-Entwurfs erfolgen: Ausgehend von einem Grobkonzept für das Gesamtsystem werden konkrete Planungen für Teilkomponenten in spezifische Teilkonzepten festgelegt. Die Planung betrifft dabei nicht nur Aspekte, die klassischerweise mit dem Begriff Sicherheit verknüpft werden, sondern auch normale betriebliche Aspekte, die Anforderungen im Bereich der Sicherheit nach sich ziehen.

Im Grobkonzept sollten beispielsweise folgende typische Fragestellungen behandelt werden:

* Welche Aufgaben sollen die Clients erfüllen? Auf welche Dienste muss von den Clients zugegriffen werden können? Gibt es besondere Anforderungen an die Verfügbarkeit der IT-Systeme oder an die Vertraulichkeit oder Integrität der gespeicherten oder verarbeiteten Daten?
* Sollen in den IT-Systemen bestimmte Hardware-Komponenten eingesetzt werden? Dies kann beispielsweise für die Auswahl des Betriebssystems wichtig sein.
* Welche Anforderungen an die Hardwareausstattung (CPU, Arbeitsspeicher, Kapazität der Festplatten, Kapazität des Netzes etc.) ergeben sich aus den allgemeinen Anforderungen?
* Handelt es sich bei dem Netz, in dem die Clients eingesetzt werden sollen, um einen homogenen oder heterogenen Rechnerverbund?
* Dienen die Clients als Ersatz für vorhandene IT-Systeme? Sollen von den alten IT-Systemen Datenbestände oder Hardware-Komponenten übernommen werden?
* Sollen auf den Clients weitere Betriebssysteme mittels Multiboot installiert werden?
Es wird empfohlen, ein oder mehrere generische Anforderungsprofile (beispielsweise "Allgemeiner Büro-PC", "Entwicklungsrechner" oder "Administrations-Client") zu erstellen, die bei konkreten Planungen als Grundlage dienen können.

Die folgenden Teilkonzepte sollten bei der Planung berücksichtigt werden:

* Authentisierung und Benutzerverwaltung: Welche Arten der Benutzerverwaltung und Benutzer-Authentisierung sollen genutzt werden? Werden Benutzer nur lokal verwaltet oder soll ein zentrales Verwaltungssystem genutzt werden? Sollen die IT-Systeme auf einen zentralen, netzbasierten Authentisierungsdienst zugreifen oder wird nur eine lokale Authentisierung benötigt?
* Benutzer- und Gruppenkonzept: Ausgehend vom institutionsweiten Benutzer-, Rechte- und Rollenkonzept müssen entsprechende Regelungen für die Clients erstellt werden (siehe ORP.4 Identitäts- und Berechtigungsmanagement).
* Administration: Wie sollen die IT-Systeme administriert werden? Werden alle Einstellungen lokal vorgenommen oder werden die Clients in ein zentrales Administrations- und Konfigurationsmanagement integriert?
* Partitions- und Dateisystem-Layout: In der Planungsphase sollte eine erste Abschätzung des benötigten Festplattenplatzes durchgeführt werden. Zur einfacheren Administration und Wartung ist es empfehlenswert, so weit wie möglich das Betriebssystem (Systemprogramme und -konfiguration), die Anwendungsprogrammen und -daten (beispielsweise Datenbank-Server und Daten) und gegebenenfalls die Benutzerdaten voneinander zu trennen. Verschiedene Betriebssysteme bieten hierfür unterschiedliche Mechanismen an (Aufteilung in Laufwerke unter Windows, Mountpoints unter Unix). Oft kann es sinnvoll sein, bestimmte Daten sogar auf einer eigenen Festplatte oder einem eigenen Festplattensystem zu speichern. Dies erlaubt es beispielsweise, bei einer Neuinstallation oder einem Update des IT-Systems die Daten auf den anderen Partitionen ohne Umkopieren zu übernehmen.
In der Planungsphase sollte die vorgesehene Aufteilung der Partitionen und deren Größe dokumentiert werden. 

* Falls auf den Clients Daten mit hohem Schutzbedarf bezüglich der Vertraulichkeit gespeichert werden, so wird der Einsatz verschlüsselter Dateisysteme dringend empfohlen (siehe auch SYS.2.1.M25 Verschlüsselung der Clients). Dabei brauchen nicht notwendigerweise alle Dateisysteme verschlüsselt zu werden, sondern es wird oft ausreichend sein, für den Teil des Dateisystems eine Verschlüsselung vorzusehen, auf dem die Daten selbst gespeichert werden, sowie für den Teil, in dem die Daten zwischengespeichert werden können (Auslagerungsdatei/-partition oder temporäre Verzeichnisse). Es muss bei allen Varianten sichergestellt sein, dass kein Schlüsselmaterial im Klartext gespeichert wird, da dies den Schutz aushebelt. Dies wird durch eine entsprechende Planung des Partitions- und Dateisystemlayouts erleichtert.
* Bei höheren Anforderungen am Schutzbedarf bezüglich der Vertraulichkeit der Daten, die auf den Clients gespeichert sind, kann es erforderlich werden, die IT-Systeme mit einem Verschlüsselungsprogramm auszustatten, das die gesamte Festplatte verschlüsselt und bereits vor dem Start des Betriebssystems eine Benutzer-Authentisierung (beispielsweise über eine Chipkarte) durchführt ("Pre-Boot-Authentication").
* Netzdienste und Netzanbindung: In Abhängigkeit von den Sicherheitsanforderungen der Daten, auf die von den Clients aus zugegriffen werden muss, muss die Netzanbindung der Clients geplant werden.
* Abhängig vom festgelegten Einsatzzweck der Clients wird außerdem eventuell der Zugriff auf weitere Dienste im Netz benötigt. Dies muss bereits im Rahmen der Planung berücksichtigt werden, damit nicht zu einem späteren Zeitpunkt Schwierigkeiten beispielsweise durch zu geringe Übertragungskapazitäten oder Probleme mit zwischengeschalteten Sicherheitsgateways entstehen.
* Monitoring: Falls besondere Anforderungen an die Verfügbarkeit der Clients bestehen, so kann ein Monitoring-System eingesetzt werden. Dafür wird auf einem Server ein Monitoring-Daemon installiert, dem ein lokal auf dem Client installierter Agent die zu überwachenden Daten sendet, beispielsweise zur Systemauslastung oder zum verbleibenden freien Speicherplatz. Bei Problemen kann zum Beispiel automatisch ein Alarm generiert werden (siehe auch SYS.1.1.M26 Systemüberwachung).
* Protokollierung: Auch bei Clients spielt die Protokollierung eine wichtige Rolle, beispielsweise bei der Diagnose und Behebung von Störungen oder bei der Erkennung und Aufklärung von Angriffen. In der Planungsphase sollte entschieden werden, welche Informationen mindestens protokolliert werden sollen, und wie lange die Protokolldaten aufbewahrt werden sollen. Außerdem muss festgelegt werden, ob die Protokolldaten lokal auf den IT-Systemen oder auf einem zentralen Protokollierungsserver im Netz gespeichert werden sollen. Vertiefende Informationen sind in dem Baustein OPS.1.1.6 Protokollierung zu finden
* Sinnvollerweise sollte bereits in der Planungsphase festgelegt werden, wie und zu welchen Zeitpunkten Protokolldaten ausgewertet werden sollen.
* Hochverfügbarkeit: Falls an die Verfügbarkeit der Clients besondere Anforderungen gestellt werden, so sollte bereits in der Planungsphase überlegt werden, wie diese Anforderungen erfüllt werden können.
Alle Entscheidungen, die in der Planungsphase getroffen wurden, müssen so dokumentiert werden, dass sie zu einem späteren Zeitpunkt nachvollzogen werden können. Dabei ist zu beachten, dass meist andere Personen neben dem Autor diese Informationen auswerten müssen. Daher ist auf passende Strukturierung und Verständlichkeit zu achten. 

#### SYS.2.1.M11 Beschaffung von Clients

Für die Beschaffung von Clients, die typischerweise in größeren Mengen erfolgt, müssen ausgehend von den Einsatzszenarien Kriterien für die Auswahl geeigneter Produkte formuliert werden. Werden Clients beschafft, ist es wichtig, dass die IT-Systeme zur vorhandenen Struktur passen, damit nicht für ein einzelnes IT-System wegen dessen Besonderheiten ein unangemessen hoher Aufwand bei Integration und Betrieb entsteht. Vertiefende Informationen sind OPS.1.2.6 Beschaffung, Ausschreibung und Einkauf zu finden.

#### SYS.2.1.M12 Kompatibilitätsprüfung von Software

Vor einer beabsichtigten Beschaffung von Software sollte deren Kompatibilität zum eingesetzten Betriebssystem in der vorliegenden Konfiguration geprüft und die Kompatibilitätsprüfung in das Freigabeverfahren der Software aufgenommen werden. Ist vom Hersteller der Software oder aus anderen Fachkreisen keine sichere Information zur Kompatibilität vorhanden, so sollte die Kompatibilität in einer Testumgebung geprüft werden. Vor einer beabsichtigten Hardwareänderung oder bei einer Betriebssystemmigration sollte auch die Treibersoftware für alle betreffenden Komponenten auf Kompatibilität zum Betriebssystem gewährleistet werden.

#### SYS.2.1.M13 Zugriff auf Ausführungsumgebungen mit unbeobachtbarer Codeausführung

Die Nutzung von Ausführungsumgebungen mit unbeobachteter Codeausführung, wie z. B. Intel Software Guard Extensions (SGX), sollte in der Firmware des Clients im (UEFI)-Setupmenü deaktiviert werden. Die Einstellung wird von den verschiedenen Herstellern unterschiedlich benannt. Sie befindet sich zumeist in den Sicherheitseinstellungen.

Es sollte berücksichtigt werden, dass sich die Ausführungsumgebungen mit unbeobachteter Codeausführung teilweise nicht mehr abschalten lassen. Es sollte daher z. B. durch regelmäßiges Patchen sichergestellt sein, dass die dort vorhandenen Schwachstellen zeitnah behoben werden und somit nur das IT-System und der jeweilige Hersteller der Ausführungsumgebung vollen Zugriff auf diese Bereiche haben.

#### SYS.2.1.M14 Updates und Patches für Firmware, Betriebssystem und Anwendungen

Häufig werden Fehler in Produkten bekannt, die dazu führen können, dass die Informationssicherheit des Informationsverbundes, wo diese betrieben werden, beeinträchtigt wird. Entsprechende Fehler können Hardware, Firmware, Betriebssysteme und Anwendungen betreffen. Diese Schwachstellen müssen so schnell wie möglich behoben werden, damit sie nicht durch interne oder externe Angreifer ausgenutzt werden können. Dies ist ganz besonders wichtig, wenn die betreffenden IT-Systeme mit dem Internet verbunden sind. Die Hersteller von Betriebssystem- oder Software-Komponenten veröffentlichen in der Regel Patches oder Updates, die auf dem jeweiligen IT-System installiert werden müssen, um den oder die Fehler zu beheben.

Die Systemadministratoren sollten sich daher regelmäßig über bekannt gewordene Schwachstellen informieren.

Wichtig ist, dass Patches und Updates, wie jede andere Software, nur aus vertrauenswürdigen Quellen bezogen werden dürfen. Für jedes eingesetzte IT-System oder Softwareprodukt muss bekannt sein, wo Sicherheitsupdates und Patches erhältlich sind. Außerdem ist es wichtig, dass Integrität und Authentizität der bereits installierten Produkte oder der einzuspielenden Sicherheitsupdates und Patches überprüft werden (siehe Abschnitt "Verwendung von vertrauenswürdigen Installationsmedien"), bevor ein Update oder Patch installiert wird. Vor der Installation sollten sie außerdem mit Hilfe eines Computer-Virenschutzprogramms geprüft werden. Dies sollte auch bei solchen Paketen gemacht werden, deren Integrität und Authentizität verifiziert wurde.

Sicherheitsupdates oder Patches sollten schnell, jedoch nicht voreilig eingespielt werden, sondern müssen getestet werden, bevor sie eingespielt werden. Falls sich ein Konflikt mit anderen kritischen Komponenten oder Programmen herausstellt, kann ein solches Update sonst zu einem Ausfall der IT-System führen. Nötigenfalls muss ein betroffenes IT-System so lange durch andere Maßnahmen geschützt werden, bis die Tests abgeschlossen sind.

Bevor ein Update oder Patch installiert wird, sollte die Daten auf dem IT-System gesichert werden, damit der Originalzustand nach Problemen wieder hergestellt werden kann. Dies gilt insbesondere dann, wenn aus Zeitgründen oder mangels eines geeigneten Testsystems nicht ausführlich getestet werden kann.

In jedem Fall muss dokumentiert werden, wann, von wem und aus welchem Anlass Patches und Updates eingespielt wurden. Wenn Schwachstellen gekannt werden, muss sich aus der Dokumentation der aktuelle Patchlevel der IT-Systeme jederzeit schnell ermitteln lassen, um schnell Klarheit darüber zu erhalten, ob die IT-Systeme dadurch gefährdet sind.

Falls festgestellt wird, dass ein Sicherheitsupdate oder Patch mit einer anderen wichtigen Komponente oder einem Programm inkompatibel ist oder Probleme verursacht, so muss sorgfältig überlegt werden, wie weiter vorgegangen wird. Wird entschieden, dass auf Grund der aufgetretenen Probleme ein Patch nicht installiert wird, so ist diese Entscheidung auf jeden Fall zu dokumentieren. Außerdem muss in diesem Fall klar beschrieben sein, welche Maßnahmen ersatzweise ergriffen wurden, damit die Schwachstelle nicht ausgenutzt werden kann. Eine solche Entscheidung darf nicht von den Administratoren alleine getroffen werden, sondern sie muss mit den Vorgesetzten und dem ISB abgestimmt sein.

**Verwendung von vertrauenswürdigen Installationsmedien**

Durch unvorsichtiges Ausführen von Programmen, die aus "unsicheren" Quellen stammen, kann beträchtlicher Schaden entstehen. Schadsoftware (so genannte Malware) kann beispielsweise Programme zum Ausspähen von Passwörtern, Trojanische Pferde oder Backdoors auf einem Client installieren, oder ganz einfach Daten beschädigen oder löschen.

Typische Quellen für solche Schadsoftware sind beispielsweise Programme, die sich als Bildschirmschoner, Virenscanner oder sonstige Hilfsprogramme ausgeben, und per E-Mail unter gefälschten Absenderadressen an sehr viele Empfänger verschickt werden. Oft laden auch unvorsichtige Anwender die Programme aus dem Internet herunter und installieren sie ohne Überprüfung.

Software sollte grundsätzlich nur aus bekannten Quellen installiert werden, besonders dann, wenn sie nicht auf Datenträgern geliefert, sondern beispielsweise aus dem Internet heruntergeladen wurde. Dies gilt besonders für Updates oder Patches, die normalerweise nicht mehr auf Datenträgern ausgeliefert werden. Die meisten Hersteller und Distributoren bieten zu diesem Zweck kryptographische Prüfsummen an, die zumindest eine Prüfung der Integrität eines Paketes erlauben. Die Prüfsummen werden dabei meist auf den (transportverschlüsselten) Webseiten der Hersteller veröffentlicht oder auch per (signierter) E-Mail verschickt. Um die Integrität eines heruntergeladenen Programms oder einer Archivdatei zu verifizieren, wird dann die veröffentlichte Prüfsumme mit einer von einem entsprechenden Programm lokal erzeugten Prüfsumme verglichen.

Falls zu einem Softwarepaket Prüfsummen angeboten werden, so sollten diese vor der Installation des Paketes überprüft werden.

Mit Prüfsummen kann die Authentizität nicht verifiziert werden. Daher werden in vielen Fällen für Programme oder Pakete digitale Signaturen angeboten. Die zur Überprüfung der Signatur benötigten öffentlichen Schlüssel sind wiederum meist auf den Webseiten des Herstellers oder von Public-Key-Servern verfügbar. Häufig werden die Prüfsummen mit einem der Programme PGP oder GnuPG erzeugt.

Ergibt die Prüfung, dass es sich um eine gültige Signatur des jeweiligen Herstellers handelt, ist das Paket vertrauenswürdiger als ein Paket, dass über Prüfsumme verfügt. Das bei Linux-Distributionen verbreitete Paketverwaltungssystem RPM (Redhat Package Manager) hat ebenso wie das Paketverwaltungssystem APT/DPKG bei Debian-basierten Distributionen bereits eine integrierte Überprüfungsfunktionalität.

Manchmal führen selbst die eingebauten Software-Updatemechanismen des jeweiligen Betriebssystems oder der Anwendungssoftware keine kryptographischen Prüfsummenvergleiche durch. Software ohne diese Prüfungen sollte nicht verwendet werden. Wenn möglich, sollte allerdings für jedes Softwarepaket die Prüfsumme verifiziert werden, bevor es eingespielt wird.

Ferner können die Prüfsummen oft nicht automatisch verglichen werden, da die hierfür erforderlichen Checksummen, Signaturen oder Zertifikate von den Herstellern nicht auf eine einheitliche Weise bereitgestellt werden. Daher müssen sie häufig manuell über die Prüfsummen von den Herstellerseiten oder durch eine Anpassung der URLs in der Patch- und Änderungssoftware verglichen werden.

Falls zu einem Softwarepaket digitale Signaturen verfügbar sind, sollten diese auf jeden Fall überprüft werden, bevor das Paket installiert wird.

Ein prinzipielles Problem bei der Verwendung digitaler Signaturen stellt die Verifikation der Authentizität des verwendeten Schlüssels selbst dar. Trägt der öffentliche Schlüssel keine Signatur einer bekannten vertrauenswürdigen Person oder Organisation (etwa eines Trustcenters), so bieten die mit dem entsprechenden privaten Schlüssel erzeugten Signaturen keine wirkliche Sicherheit, dass das Softwarepaket tatsächlich vom Entwickler, Hersteller oder Distributor stammt. Daher sollten die öffentlichen Schlüssel, sofern sie nicht zertifiziert sind, möglichst aus einer anderen Quelle als das Softwarepaket selbst bezogen werden, beispielsweise von einer DVD des Herstellers, von einem anderen Spiegelserver, auf dem das Paket ebenfalls heruntergeladen werden kann, oder von einem Public Key Server.

Um Prüfsummen und digitalen Signaturen zu überprüfen, müssen die entsprechenden Programme lokal vorhanden sein. Die Administratoren sollten über die Bedeutung und Aussagekraft von Prüfsummen und digitalen Signaturen informiert sein. Außerdem müssen die Administratoren genügend Zeit haben, die entsprechenden Programme im Arbeitsalltag einzusetzen und sich mit der Bedienung vertraut zu machen.

Patches und Änderungen sollten aus verschiedenen Gründen nicht per E-Mail bezogen werden. Die Herkunft von E-Mails ist ohne Einsatz zusätzlicher Sicherheitsmechanismen schwer festzustellen und die Empfängeradressen in den Institutionen sind oft Verteilerlisten, deren Adresse leicht zu erraten ist. Patches und Änderungen können außerdem mittlerweile sehr umfangreich sein. Viele Unternehmen und Behörden haben die Größe von E-Mail-Anhängen beschränkt und verbieten es unter Umständen, ausführbare Anhänge anzunehmen. Ferner werden durch die großen Datenmengen die E-Mail-Systeme unnötig belastet. Daher kann eine rechtzeitige Verfügbarkeit der Software-Änderungen, welche besonders bei Sicherheitspatches kritisch sein kann, via E-Mail nicht ausreichend gewährleistet werden.

Des Weiteren bieten einige Hersteller an, Änderungen und Patches dem Kunden direkt auf Datenträgern zuzusenden. Auch in diesem Fall sollten die Patches und Änderungen möglichst anhand von Prüfsummen oder digitalen Signaturen verifiziert werden, denn Absender-Angaben auf Postsendungen und Hersteller-Logos auf CDs und DVDs lassen sich leicht fälschen.

Ein weiterer Aspekt zur Prüfung der Echtheit der Aktualisierung können vom Hersteller veröffentlichte Nachrichten auf seiner Webseite, per Newsletter oder über ähnliche Kanäle sein. Einige Hersteller haben Zyklen und Zeitpunkte etabliert, zu denen systematisch Informationen über Änderungen veröffentlicht werden.

#### SYS.2.1.M15 Sichere Installation und Konfiguration von Clients

Nachdem die Planung eines neuen Clients abgeschlossen und eine Sicherheitsrichtlinie erstellt wurde, kann mit der Installation des Clients begonnen werden.

Die Installation und Konfiguration des IT-Systems sollte nur von autorisierten Personen (Administratoren oder vertraglich gebundene Dienstleister) durchgeführt werden. Administratoren für IT-Systeme und deren Vertreter müssen sorgfältig ausgewählt werden. Sie müssen regelmäßig darüber belehrt werden, dass die Befugnisse nur für die erforderlichen Administrationsaufgaben verwendet werden dürfen. Da Administratoren hinsichtlich der Funktionsfähigkeit der eingesetzten Hard- und Software eine Schlüsselrolle innehaben, muss auch beim Ausfall von Administratoren die Weiterführung der Tätigkeiten gewährleistet sein. Hierzu müssen die benannten Vertreter über den aktuellen Stand der Systemkonfiguration verfügen sowie Zugriff auf die für die Administration benötigten Passwörter, Schlüssel und Sicherheitstoken haben. 

Es ist empfehlenswert, zunächst ein kurzes Installationskonzept entsprechend den funktionalen Anforderungen aus der Planung und den Vorgaben der Sicherheitsrichtlinie zu erstellen. Prinzipiell ist es vorteilhaft, die Installation in zwei Phasen vorzunehmen: Zunächst wird ein Grundsystem installiert und konfiguriert, anschließend werden die weiteren benötigten Anwendungen eingerichtet. Die Installationsprogramme der meisten Betriebssysteme unterstützen diese Vorgehensweise mehr oder weniger gut.

Die beschriebenen Schritte brauchen nicht notwendigerweise alle für jeden Client erneut durchgeführt zu werden. Dies könnte sogar insofern kontraproduktiv sein, als die ständige Wiederholung die Gefahr von Fehlern erhöht. Es wird daher empfohlen, die beschriebenen Schritte einmal besonders sorgfältig auf einem Referenz-System durchzuführen, die nötigen Konfigurationen genau zu dokumentieren und so ein angepasstes Installationskonzept für das betreffende Betriebssystem zu erhalten (siehe SYS.2.1.M27 Einrichten einer Referenzinstallation für Clients). Dabei muss beachtet werden, dass dieses Installationskonzept auch bei Änderungen am Betriebssystem, die kein komplett neues Release darstellen (Service-Packs, Update-Releases oder ähnliches) überprüft und gegebenenfalls angepasst werden muss.

**Installation**

Während der Installation und der späteren Konfiguration sollten zumindest die wichtigen Schritte so dokumentiert werden, dass sie zu einem späteren Zeitpunkt nachvollzogen werden können. Beispielsweise kann eine Checkliste für die Installation erstellt werden, auf der durchgeführte Schritte abgehakt und vorgenommene Einstellungen vermerkt werden können. Eine entsprechende Dokumentation ist für eine Fehleranalyse oder spätere Neuinstallation hilfreich. Dabei sollte beachtet werden, dass neben dem Autor auch weitere, auf diesem Gebiet eventuell weniger spezialisierte, Administratoren auf die Dokumentation zurückgreifen müssen. Daher ist es wichtig, dass die Dokumentation gut strukturiert und verständlich ist.

Wird der Client von Datenträgern wie DVDs oder anderen Speichermedien installiert, wird empfohlen, die Installation und Grundkonfiguration offline oder zumindest in einem sicheren Netz (Installations- oder Administrationsnetz) durchzuführen. Generell sollte verhindert werden, dass andere IT-Systeme während der Installation auf das zu installierende IT-System zugreifen können. Dies ist wichtig, weil während der Installation meist noch keine Passwörter vergeben und keine Schutzmechanismen aktiv sind, aber eventuell schon Zugriffe möglich sind. Falls die Installation mehrerer IT-Systeme teilweise über das Netz erfolgen soll (beispielsweise Nachladen von Paketen), so wird empfohlen, einen Installationsserver im Administrationsnetz zu nutzen.

Insbesondere beim Betriebssystem selbst ist es wichtig, dass die installierte Version aus einer vertrauenswürdigen Quelle stammt. Dies ist besonders wichtig, wenn beispielsweise CD -Images aus dem Internet heruntergeladen wurden. In diesem Fall sollte unbedingt geprüft werden, ob digitale Signaturen der Pakete verfügbar sind, die zur Verifikation von Integrität und Authentizität der Pakete verwendet werden können. Pakete und CD-Images, für die keine digitalen Signaturen oder wenigstens Prüfsummen existieren, sollten möglichst nicht eingesetzt werden (siehe auch SYS.2.1.M13 Updates und Patches für Firmware, Betriebssystem und Anwendungen). 

Bei der Einrichtung der Festplattenpartitionen muss das in der Planungsphase erstellte Konzept umgesetzt werden. Wenn ein verschlüsseltes Dateisystem eingesetzt werden soll, so muss es meist initialisiert werden, bevor Daten hineinkopiert werden können, denn oft lässt sich ein Dateisystem nicht im Nachhinein verschlüsseln. 

Sofern dies nicht bereits automatisch geschehen ist, sollte spätestens beim Abschluss der Grundinstallation auch die Protokollierung der Systemereignisse aktiviert werden. Die Protokolldaten können bei Problemen bei der weiteren Installation und Konfiguration wertvolle Informationen liefern.

**Konfiguration**

Die Grundeinstellungen, die vom Hersteller oder Distributor eines Betriebssystems vorgenommen werden, sind meist nicht auf Sicherheit optimiert, sondern auf eine einfache Installation und Inbetriebnahme sowie oft darauf, dass jeder Anwender möglichst einfach auf möglichst viele Features des Betriebssystems zugreifen kann. Beim Einsatz von IT-Systemen (egal, ob als Client oder Server) in Behörden oder Unternehmen ist dies oft nicht wünschenswert.

Der erste Schritt bei der Grundkonfiguration muss daher sein, die Grundeinstellungen zu überprüfen und nötigenfalls entsprechend den Vorgaben der Sicherheitsrichtlinie anzupassen. Die Grundkonfiguration ist naturgemäß relativ stark vom eingesetzten Betriebssystem abhängig. Aus diesem Grund sind in den betriebssystemspezifischen Bausteinen entsprechende detailliertere Empfehlungen enthalten.

Ziele einer sicheren Grundkonfiguration sollten sein, dass

* die Clients gegen "einfache" Angriffe über das Netz abgesichert ist,
* kein normaler Benutzer durch reine Neugierde oder gar zufällig Zugriff auf sensitive Daten erlangen kann, die nicht für ihn bestimmt sind,
* kein normaler Benutzer beim normalen Arbeiten mit den Clients durch reine Bedienungsfehler oder Leichtsinn ("Was passiert eigentlich, wenn ich diese Datei lösche?") schwerwiegenden Schaden an den IT-Systemen oder an den Daten anderer Benutzer verursachen kann, und dass
* auch für die Arbeiten der Systemadministratoren die Auswirkungen kleinerer Fehler so weit wie möglich begrenzt sind.
Die Einstellungen, die im Rahmen der Grundkonfiguration überprüft und angepasst werden sollten, betreffen insbesondere die folgenden Bereiche:

* Einstellungen für Systemadministratoren  
 Die Kennungen, unter denen Systemadministratoren arbeiten, sollten besonders stark abgesichert werden. Dies betrifft beispielsweise die Einstellungen für die Benutzerumgebung wie
*  

 
	+ Suchpfade für Programme und Dateien,
	+ Umgebungsvariablen und die
	+ Konfiguration bestimmter Programme.
	  

 
Diese Einstellungen sollten überprüft und gegebenenfalls angepasst werden. Außerdem sollten die Einstellungen für die Benutzerverzeichnisse von Systemadministratoren so gewählt werden, dass normale Benutzer keinen Zugriff darauf haben.

* Einstellungen für die Systemverzeichnisse und -dateien  
 Bei der Grundkonfiguration muss überprüft werden, ob die Berechtigungen für Systemverzeichnisse und -dateien den Vorgaben der Sicherheitsrichtlinie entsprechen. Auf einem Server sollten für die Berechtigungen der Systemverzeichnisse und -dateien relativ restriktive Einstellungen gewählt werden.
* Einstellungen für Benutzerkennungen und Benutzerverzeichnisse  
 Im Rahmen der Grundkonfiguration sollte überprüft werden, welche Standardeinstellungen für Benutzerkennungen und Benutzerverzeichnisse gelten. Die Einstellungen müssen gegebenenfalls entsprechend der Sicherheitsrichtlinie angepasst werden. Dies betrifft im Wesentlichen dieselben Parameter wie für Systemadministrator-Kennungen, für normale Benutzer können aber unter Umständen andere Einstellungen sinnvoll sein.
* Einstellungen für den Zugriff auf das Netz  
 Im Rahmen der Grundkonfiguration sollten auch die Einstellungen für den Zugriff auf das Netz sowie wichtige externe Dienste getroffen und dokumentiert werden. Dies betrifft beispielsweise (sofern nicht bereits bei der Installation geschehen): 

 
	+ Vergabe der IP-Adresse und Konfiguration der grundlegenden Netzparameter oder Konfiguration des Zugriffs auf einen Server, der automatisch, beispielsweise über DHCP (Dynamic Host Configuration Protocol) Netzeinstellungen verteilt. Für Server wird allerdings von der Verwendung von DHCP abgeraten.
	+ Konfiguration des Zugriffs auf einen DNS-Server und gegebenenfalls andere Namensdienste und die
	+ Konfiguration des Zugriffs auf verteilte Dateisysteme, Datenbanken oder sonstige externe Dienste.
	  

 
* Zusätzlicher Schutz durch einen lokalen Paketfilter  
 Clients mit hohem Schutzbedarf sollten zusätzlich zum Schutz durch die institutionsweiten Sicherheitsgateways oder Paketfilter, die das interne Netz segmentieren, mit einem lokalen Paketfilter (siehe SYS.2.1.M28 Einrichtung lokaler Paketfilter) oder einer Personal Firewall abgesichert werden. Entsprechende Funktionalitäten sind in praktisch allen modernen Betriebssystemen vorhanden.
* Deaktivierung von "Call Home"-Funktionen  
 Einige Betriebssysteme und Anwendungen senden Informationen, beispielsweise über aufgetretene Fehler oder über die Systemkonfiguration , direkt an den Hersteller, damit dieser zukünftig das Produkt an die Bedürfnisse der Anwender anpassen kann. Hierfür wird eine Datenverbindung über Datennetze, wie dem Internet, zu den Servern des Herstellers aufgebaut. Eine solche Form des Datenabflusses kann kritisch sein, vor allem, wenn die Anwender nicht über die Häufigkeit und Inhalte der Datenweitergabe informiert werden.Generell sollte dieser oft unerwünschte Informationsaustausch unterbunden werden. Ob und wie Informationen versendet werden, kann in der Regel den Lizenzvereinbarungen der eingesetzten Software entnommen werden.Viele Applikationen bieten die Möglichkeit, diese "Call Home"-Funktion zu deaktivieren. Nur in begründeten Ausnahmefällen sollte diese aktiviert bleiben. Nach Updates sollte überprüft werden, ob die "Call Home"-Funktion weiterhin deaktiviert ist.Durch lokale Paketfilter oder dem zentralen Sicherheitsgateway (Firewall) kann ebenfalls der Verbindungsaufbau mit dem Hersteller unterbunden werden. Beispielsweise könnten auf Grundlage der Zieladressen oder der Portnummern die Datenverbindungen abgewiesen werden. Hierbei ist zu beachten, dass die Berücksichtigung aller Applikationen aufwändig ist und automatische Update-Funktionen, falls benötigt, dann oft nicht mehr zur Verfügung stehen.
* Deaktivieren nicht benötigter Schnittstellen  
 In einer Grundkonfiguration sind üblicherweise alle vorhandenen oder auch potentiell nachrüstbaren Schnittstellen aktiviert. Häufig werden nicht alle davon benötigt und sollten daher entfernt oder deaktiviert werden. Einige dieser Schnittstellen können auch potentielle Sicherheitsprobleme mit sich bringen, denen durch geeignete organisatorische oder technische Sicherheitsmaßnahmen entgegengewirkt werden muss. Schnittstellen, deren Nutzung kontrolliert werden sollte, sind beispielsweise Bluetooth, WLAN, Firewire, eSATA (externer SATA-Festplattenanschluss) und Thunderbolt.
* Verzeichnisbasierte Ausführungskontrolle  
 Bei aktuellen Betriebssystemen ist eine verzeichnis- oder partitionsbasierte Ausführungskontrolle möglich. Dabei werden die Ausführungsrechte für alle Dateien in einem Verzeichnis und allen Unterverzeichnissen unterbunden. Beispielsweise kann dies auf windowsbasierten Betriebssystemen durch entsprechende Gruppenrichtlinien mit "Richtlinien für Softwareeinschränkung" erreicht werden. Auf Linux-Systemen kann die Festplatte zweckdienlich partitioniert und mit passenden mount-Optionen "ro" (read only) und "noexec" (no execute) eingebunden werden. Für hohen Schutzbedarf existieren darüber hinaus Werkzeuge, die dateibezogene Berechtigungen im Betriebssystem festlegen. Die verzeichnis- oder partitionsbasierte Ausführungskontrolle sorgt bei geeigneter Konfiguration dafür, dass Benutzer 

 
	+ aus Verzeichnissen, in die sie schreiben dürfen, keine Programme starten können und
	+ in Verzeichnisse, aus denen sie Anwendungen starten dürfen, nicht schreiben können. Dadurch wird es Benutzern erschwert, eine Programmdatei auszuführen, die sie aus dem Internet geladen oder von einem USB-Stick kopiert haben.
	  

 
* Monitoring  
 Um auf kritische Systemereignisse reagieren zu können, können diese durch Monitoring beobachtet werden. Hierfür werden in der Regel Statusinformationen von einem zentralen IT-System abgerufen, auf dem die Ereignisse ausgewertet werden. Über die Schnittstelle, die benötigt wird, um die Systemereignisse vom IT-System abzurufen, können aber oft Systemeinstellungen des Betriebssystems verändert werden, z. B. über SNMP (Simple Network Management Protocol). Ist eine solche Modifikation nicht gewünscht, dann sollten diese Merkmale deaktiviert werden.
* Speicherschutzmechanismen  
 Um Betriebssystem und Applikation vor möglichen Buffer Overflows zu schützen, sollten entsprechende Speicherschutzmechanismen aktiviert werden, sofern diese von der verwendeten Hardware (CPU) und dem Betriebssystem unterstützt werden. Beispielsweise kann mit Executable Space Protection (ESP) verhindert werden, dass Programme aus nicht dafür zugelassenen Bereichen des Arbeitsspeichers ausgeführt werden.
* Anlegen einer Integritätsdatenbank  
 Nach Abschluss der Grundkonfiguration wird empfohlen, mit einem entsprechenden Tool eine Integritätsdatenbank anzulegen. Bei manchen Betriebssystemen gehören entsprechende Programme bereits zum Umfang einer Standardinstallation. Die Integritätsdatenbank sollte nicht auf den IT-Systemen selbst, sondern auf einem schreibgeschützten Datenträger (beispielsweise CD-R) oder einem anderen, besonders gesicherten IT-System gespeichert werden. Bei einem Verdacht auf eine Kompromittierung des IT-Systems lassen sich anhand der erzeugten Prüfsummen Dateien identifizieren, die von einem Angreifer modifiziert wurden. Bei den regelmäßigen Überprüfungen der Systemintegrität dient diese Datenbank als Referenz für einen definierten, sicheren Zustand der IT-Systeme.
Es sollte dokumentiert werden, welche Einstellungen im Rahmen der Grundkonfiguration überprüft wurden, sowie ob und gegebenenfalls wie sie geändert wurden. Die Dokumentation muss so beschaffen sein, dass im Notfall auch eine andere Person als der eigentliche Administrator ohne vorherige Kenntnis der IT-Systeme anhand der Dokumentation nachvollziehen kann, was getan wurde. Im Idealfall sollte es möglich sein, alleine mit Hilfe der Dokumentation die IT-Systeme wiederherzustellen.

#### SYS.2.1.M16 Deaktivierung und Deinstallation nicht benötigter Komponenten und Kennungen

Oft wird im Rahmen der Standardinstallation eines Betriebssystems eine größere Anzahl von Benutzerkennungen, Programmen, Diensten und sonstige Komponenten eingerichtet, die für den Betrieb nicht in jedem Fall notwendig sind. Daher sollte im Rahmen der Grundkonfiguration geprüft werden, welche Benutzerkonten wirklich gebraucht werden. Nicht benötigte Benutzerkennungen sollten entweder gelöscht oder zumindest so deaktiviert werden, so dass unter der betreffenden Kennung keine Anmeldung am IT-System möglich ist.

Die Standardinstallation eines Betriebssystems enthält oft eine Reihe von Programmen und Diensten, die normalerweise nicht benötigt werden und die gerade deswegen eine Quelle von Sicherheitslücken sein können. Dies gilt insbesondere für Netzdienste. Nach der Installation sollte deswegen überprüft werden, welche Dienste und Anwendungen auf den IT-Systemen installiert und aktiviert sind. Nicht benötigte Dienste sollten deaktiviert oder ganz deinstalliert werden. Außerdem SOLLTEN nicht benötigte Laufzeitumgebungen, Interpretersprachen und Compiler deinstalliert werden. 

Die Überprüfung auf laufende Dienste kann einerseits lokal mit den Mitteln des installierten Betriebssystems und bei Netzdiensten andererseits von außen durch einen Portscan von einem anderen System aus erfolgen. Durch eine Kombination beider Methoden kann weitgehend ausgeschlossen werden, dass die IT-Systeme noch weitere ungewollte Netzdienste anbietet.

#### SYS.2.1.M17 Einsatzfreigabe

Bevor Clients im produktiven Betrieb eingesetzt und bevor sie an ein produktives Netz angeschlossen werden, sollte der Einsatz freigegeben werden, dies ist zu dokumentieren. Die Einsatzfreigabe basiert auf einer Prüfung der Installations- und Konfigurationsdokumentation und der Funktionsfähigkeit der IT-Systeme in einem Test. Sie erfolgt durch eine in der Institution dafür autorisierte Stelle.

Vertiefende Informationen hierzu sind in OPS.1.1.7 Softwaretests- und Freigaben zu finden.

Falls festgestellt wird, dass ein Sicherheitsupdate oder Patch mit einer anderen wichtigen Komponente oder einem Programm inkompatibel ist oder Probleme verursacht, so muss sorgfältig überlegt werden, wie weiter vorgegangen wird. Wird entschieden, dass auf Grund der aufgetretenen Probleme ein Patch nicht installiert wird, so ist diese Entscheidung auf jeden Fall zu dokumentieren. Außerdem muss in diesem Fall klar beschrieben sein, welche Maßnahmen ersatzweise ergriffen wurden, damit die Schwachstelle nicht ausgenutzt werden kann. Eine solche Entscheidung darf nicht von den Administratoren alleine getroffen werden, sondern sie muss mit den Vorgesetzten und dem ISB abgestimmt sein.

#### SYS.2.1.M18 Nutzung von TLS [Benutzer]

Das bei der Web-Nutzung am häufigsten verwendete Sicherheitsprotokoll ist SSL/TLS (Secure Socket Layer/Transport Layer Security), weitere Informationen sind in [TR02102], [RFC5246] und [RFC5246] zu finden. Die erste Version des SSL-Protokolls (SSL v1.0) wurde von Netscape entwickelt. Neuere Versionen sind unter der Bezeichnung TLS in verschiedenen RFCs standardisiert. SSL/TLS wird von allen aktuelleren Browsern unterstützt. Mit SSL/TLS können Verbindungen abgesichert werden:

* durch Verschlüsselung der Verbindungsinhalte,
* durch Überprüfung der Vollständigkeit und Korrektheit der übertragenen Daten,
* durch Prüfung der Identität des Servers und
* optional durch Prüfung der Identität der Client-Seite.
Zu Beginn einer neuen mit SSL/TLS abgesicherten Kommunikationsverbindung findet ein sogenannter Handshake zwischen Client und Server statt. Hierbei verständigen sich Client und Server über die kryptographischen Algorithmen, die für Schlüsselaustausch, Verschlüsselung und Integritätssicherung eingesetzt werden. Außerdem einigen sich Client und Server über die SSL-Version, die verwendet wird. Zusätzlich sendet der Server sein X.509-Zertifikat an den Client. Optional kann auch der Client dem Server sein X.509-Zertifikat übermitteln, falls dies vom Server angefordert wird. Mit Hilfe eines asymmetrischen Verschlüsselungsverfahrens wird anschließend ein symmetrischer Schlüssel sicher ausgetauscht. Für die Verschlüsselung der eigentlichen Datenübertragung wird nun ein symmetrisches Verfahren benutzt, weil hiermit dies große Datenmengen schneller verschlüsselt werden können. Bei jeder Transaktion wird ein anderer symmetrischer Schlüssel als "Session Key" ausgehandelt, mit dem dann die Verbindung verschlüsselt wird.

Ein Benutzer kann Webseiten, die eine SSL/TLS-gesicherte Datenübertragung ermöglichen, beispielsweise daran erkennen, dass die Internet-Adresse um ein "s" erweitert ist (https://www...). Zusätzlich werden solche Webseiten bei den meisten gängigen Browsern auch besonders gekennzeichnet, beispielsweise durch ein angezeigtes Symbol (Schlüssel, Vorhängeschloss etc.) oder durch eine farbliche Markierung der Internet-Adresse.

Die Nutzung von SSL/TLS ist nicht auf HTTP-Clients und -Server beschränkt. Auch Protokolle wie SMTP, FTP, IMAP oder LDAP können durch SSL/TLS kryptographisch abgesichert werden, allerdings setzt dies voraus, dass die betreffenden Clients und Server diese Sicherheitsfunktion jeweils unterstützen.

SSL/TLS besteht aus zwei Schichten. Auf der oberen Schicht arbeitet das SSL/TLS Handshake Protokoll. Dieses dient dem Client und dem Server dazu, sich gegenseitig zu authentisieren sowie dazu, für den anschließenden Datenverkehr einen Schlüssel und einen Verschlüsselungsalgorithmus auszuhandeln. Die untere Schicht, das SSL/TLS Record Protokoll, das die Schnittstelle zur TCP-Schicht bildet, ver- und entschlüsselt den eigentlichen Datenverkehr. Da SSL/TLS für den Zugriff auf TCP auf der Socket-Schnittstelle aufsetzt und diese durch eine sicherheitserweiterte Version ersetzt, ist es auch für andere Dienste verwendbar.

**Versionsnummer**

Es existieren mehrere SSL/TLS-Protokollversionen, wie SSL v2, SSL v3, TLS v1.0, TLS v1.1 und TLS v1.2. SSL v1 wurde nicht veröffentlicht. Um eine sichere Verbindung zwischen Client und Server zu gewährleisten, sollte mindestens TLS 1.2 verwendet werden.

TLS 1.1 bietet ausreichende Sicherheit, aber im Vergleich zu TLS 1.2 weist es jedoch einige Schwächen auf, z. B. sind in TLS 1.1 noch Cipher-Suites vorhanden, die auf IDEA und DES basieren, in TLS 1.2 nicht mehr.

TLS 1.0 kann in bestehenden Client-Anwendungen übergangsweise weiter eingesetzt werden, falls eine sofortige Migration zu TLS 1.1 oder vorzugsweise TLS 1.2 nicht möglich ist und geeignete Maßnahmen gegen Chosen-Plaintext-Angriffe (z. B. BEAST) auf die CBC-Implementierung getroffen werden. Generell sollte jedoch eine Migration zu TLS 1.2 schnellstmöglich erfolgen. SSL v2 und SSL v3 dürfen nicht mehr eingesetzt werden, siehe hierzu auch den BSI-Migrationsleitfaden zum Mindeststandard TLS 1.2 (siehe [MIGLFTLS]).

**Algorithmen und Schlüssellängen**

Bei SSL/TLS können verschiedene kryptographische Algorithmen mit verschiedenen Schlüssellängen eingesetzt werden. Beim Verbindungsaufbau einigen sich Client und Server auf die in der Sitzung verwendeten Verfahren.

Durch die Auswahl der Produkte (Browser, Webserver, Plug-In etc.) und geeignete Konfiguration ist sicherzustellen, dass bei der SSL/TLS-geschützten Kommunikation ausschließlich Algorithmen und Schlüssellängen eingesetzt werden, die dem Stand der Technik und den Sicherheitsanforderungen der Institution entsprechen. Darüber hinaus sollten die verwendeten Cipher-Suites Perfect Forward Secrecy (PFS) unterstützen. Weitere Hinweise zu Algorithmen und Schlüssellängen finden sich im Baustein CON.1 Kryptokonzept.

**Zertifikate**

Es ist schwierig, bei der Datenkommunikation über offene Netze die Identität der Kommunikationspartner zu überprüfen, da nicht sichergestellt ist, dass Namensangaben korrekt sind. Bei SSL/TLS erfolgt die Überprüfung der Identität des Kommunikationspartners über so genannte Zertifikate. Zertifikate enthalten deren öffentliche Schlüssel sowie eine Bestätigung einer weiteren Instanz über die korrekte Zuordnung des öffentlichen Schlüssels zu dessen "Besitzer", hier also ein Server oder Client. Der Wert eines Zertifikates hängt also nicht zuletzt davon ab, wie vertrauenswürdig diese Bestätigungsinstanz (auch Trustcenter oder Zertifizierungsstelle genannt) ist. Die Echtheit des Zertifikates lässt sich wiederum mit dem öffentlichen Schlüssel der Bestätigungsinstanz überprüfen.

Gängige Betriebssysteme und Anwendungsprogramme, wie Browser, enthalten bereits bei der Installation SSL/TLS-Zertifikate einiger Zertifizierungsstellen. Diese Zertifizierungsstellen haben sehr unterschiedliche Sicherheitsleitlinien und Bedingungen, unter denen sie Zertifikate erteilen. Bevor sicherheitskritische Informationen über eine SSL/TLS-geschützte Verbindung übertragen werden, sollte deshalb die Sicherheitsrichtlinie der jeweiligen Zertifizierungsstellen geprüft werden.

Bei der Aufnahme eines neuen Zertifikates sollte darauf geachtet werden, dieses erst nach Überprüfung des "Fingerprints" zu aktivieren. Der Fingerprint ist eine hexadezimale Zahl, die zusammen mit dem Zertifikat übermittelt wird. Zusätzlich sollte sie auf einem anderen Weg übermittelt und verglichen werden, da diese die Korrektheit des Zertifikats sicherstellen soll.

In der Vergangenheit ist es bereits vorgekommen, dass Zertifizierungsstellen kompromittiert und dadurch Hunderte gefälschte Zertifikate ausgestellt wurden, darunter auch solche für Online-Informationsdienste, Online-Portale, andere Zertifizierungsstellen und Anonymisierungsdienste. Durch Widerrufslisten und Validierungsprotokolle wie OCSP (Online Certificate Status Protocol) können gefälschte, manipulierte oder veraltete Zertifikate allerdings zeitnah als ungültig erklärt werden. Daher sollte die Validierung von Zertifikaten in Anwendungsprogrammen wie Browsern und E-Mail-Clients aktiviert werden. Dabei ist OCSP der Verwendung von Zertifikatswiderruflisten (Certificate Revocation Lists, CRLs) vorzuziehen, da OCSP zeitnahe Aktualisierungen über das Internet erlaubt.

Kann ein Zertifikat nicht validiert werden, beispielsweise weil der OSCP-Server nicht erreicht oder auf die Widerrufslisten nicht zugegriffen werden kann, dann gibt es aus Sicht des Clients zwei Möglichkeiten: Er kann die Verbindung beenden oder ein eventuell manipuliertes oder ungültiges Zertifikat akzeptieren. Die Entscheidung, was in solchen Fällen zu tun ist, sollte mit den Sicherheitsrichtlinien der Institution in Einklang stehen.

**Session Renegotation und TLS-Kompression**

Mittels der sogenannten Session Renegotiation (Session-Neuverhandlung) können sowohl Client als auch Server die Parameter einer bestehenden HTTPS-Sitzung neu aushandeln. Aufgrund eines Fehlers in der Spezifikation des TLS-Protokolls (siehe [RFC5246]) ist es einem Man-in-the-Middle-Angreifer möglich, die Session Renegotiation zu missbrauchen, um beliebige Inhalte in eine existierende HTTPS-Sitzung einzufügen. Mittlerweile wurde das TLS-Protokoll erweitert (siehe [RFC5746]) und dieser Designfehler behoben. Clientseitig sollte die Session Renegotiation deaktiviert werden. 

TLS bietet die Möglichkeit, die übertragenen Daten vor der Verschlüsselung zu komprimieren. Dies kann dazu führen, dass Seitenkanalangriffe auf die Verschlüsselung über die Länge der verschlüsselten Daten, durchgeführt werden. Ein Beispiel hierfür ist CRIME (Compression Retro Info-leak Made Easy), ein 2012 vorgestellter Seitenkanal-Angriff, der das Ziel hat, eine HTTPS-Sitzung zu übernehmen. Um dies zu verhindern, sollte die TLS-Kompression deaktiviert werden.

Hinweis: Beim Einsatz von SSL/TLS ist zu beachten, dass verschlüsselte Daten hinsichtlich aktiver Inhalte und Schadprogramme nicht zentral, also z. B.am Sicherheitsgateway, überprüft werden können. Dies muss bei der Sicherheitskonzeption berücksichtigt werden, damit keine Sicherheitslücken entstehen. Weitere Empfehlungen hierzu finden sich unter anderem im Baustein OPS1.1.4 Malware-Schutz.

#### SYS.2.1.M19 Restriktive Rechtevergabe

Grundsätzlich sollten Berechtigungen immer restriktiv vergeben werden, so dass Benutzer genau auf die Dienste und Daten zugreifen können, die sie für ihre Aufgaben benötigen. Besonders wichtig ist dies bei Systemdateien bzw. -verzeichnissen.

Systemdateien bzw. -verzeichnisse sind Dateien und Verzeichnisse, für die der IT-Betrieb zuständig ist. Diese sind entweder für alle Benutzer von Bedeutung oder sie dienen Administrationszwecken.Auf Systemdateien sollte möglichst nur der IT-Betrieb Zugriff haben. Editorprogramme oder Compiler dürfen nicht genutzt werden, wenn sie nicht für die Aufgabenerfüllung erforderlich sind. Der Kreis der zugriffsberechtigten Administratoren sollte möglichst klein gehalten werden. Auch Verzeichnisse dürfen nur die notwendigen Privilegien für die Benutzer zur Verfügung stellen. Die Vergabe von Zugriffsrechten auf Systemdateien sollte grundsätzlich restriktiv und nur in Übereinstimmung mit den hausinternen Sicherheitsrichtlinien erfolgen.

Systemdateien sollten getrennt von Applikationsdaten und Benutzerdateien gespeichert werden. Dies sorgt für eine bessere Übersicht und erleichtert es, Datensicherungen zu erstellen und den hierauf Zugriff korrekt zu schützen.

Der Zugriff auf Systemdateien sollte immer protokolliert werden. Nicht benötigte Systemdateien sollten von den IT-System entfernt werden, damit sie nicht für Angriffe missbraucht werden können und auch nicht ständig auf Integrität kontrolliert werden müssen.

Bei der restriktiven Vergabe von Zugriffsrechten reicht es nicht aus, nur die Rechte eines Programms zu überprüfen. Zusätzlich muss auch die Rechtevergabe aller Programme überprüft werden, die von diesem Programm aus aufgerufen werden.

Die Integrität aller Systemdateien und -verzeichnisse, sowie die Korrektheit der Zugriffsrechte sollte nach Möglichkeit regelmäßig verifiziert werden. Für viele Betriebssysteme gibt es dafür Tools, mit denen solche Prüfungen schnell und zuverlässig durchgeführt werden können.

#### SYS.2.1.M20 Schutz der Administrationsschnittstellen

Es gibt unterschiedliche Zugriffsmöglichkeiten, um Clients zu administrieren. Abhängig von der genutzten Zugriffsart müssen eine Reihe von Sicherheitsvorkehrungen getroffen werden. Bei größeren Netzen ist es empfehlenswert und oft unumgänglich, die Clients in ein zentrales Netzmanagement-System einzubinden, da sonst eine sichere und effiziente Administration nicht gewährleistet werden kann. Die zur Administration verwendeten Methoden sollten in der Sicherheitsrichtlinie festgelegt und die Administration nur entsprechend der Sicherheitsrichtlinie durchgeführt werden.

Es wird empfohlen, für die verschiedenen Administrationstätigkeiten eine Übersicht zu erstellen, welche Arbeiten auf welchem Weg durchgeführt werden können. Vor allem ist es wichtig festzuhalten, ob bestimmte Tätigkeiten auf einem bestimmten Weg normalerweise nicht durchgeführt werden dürfen. 

* Lokale Administration  
 Die Administration von Clients direkt durch Zugriff über die Konsole ist nur für eine kleine Zahl von Rechnern handhabbar und wird in Umgebungen mit einer größeren Anzahl von Clients meist einen Ausnahmefall darstellen. Muss der IT-Betrieb ausnahmsweise doch lokal an einem Client arbeiten, ist es beispielsweise wichtig, dass der Administrator bei der Authentisierung über ein Passwort darauf achtet, dass dieses nicht ausgespäht werden kann. Gegebenenfalls sollte überlegt werden, für solche Arbeiten Einmalpasswörter oder ähnliches zu verwenden.
* Administration mit Hilfe eines Bootmediums  
 Für bestimmte Administrationsarbeiten, die lokal an einem Client vorgenommen werden sollen kann es vorteilhaft sein, ein externes Boot-Medium einzusetzen, von dem der Client gestartet wird (siehe auch SYS.2.1.M4 Regelmäßige Datensicherung). Dies bietet den Vorteil, dass der Administrator sich einer "sauberen" Systemumgebung sicher sein kann. Allerdings hat diese Methode auch eine Reihe von Nachteilen, beispielsweise einen höheren Aufwand. Außerdem ist es auf diese Weise meist nicht möglich, bestimmte Fehlermeldungen, die im laufenden Betrieb auftreten, nachzuvollziehen. 
* Remote-Administration  
 Clients werden häufig von Administrationsrechnern aus über das Netz administriert. Um zu verhindern, dass dabei Authentisierungsinformationen der Administratoren abgehört oder gar von einem Angreifer manipuliert werden, sollte die Administration nur über sichere Protokolle (beispielsweise nicht über Telnet, sondern über SSH erfolgen. Eine ungesicherte Remote-Administration über externe (unsichere) Netze hinweg darf in keinem Fall erfolgen. Dies muss bereits bei der Festlegung der Sicherheitsrichtlinie berücksichtigt werden. Auch im internen Netz sollten soweit möglich keine unsicheren Protokolle verwendet werden.
* Administration über ein zentrales Managementsystem  
 Falls für die Administration ein zentrales Managementsystem genutzt werden soll, so müssen für diesen Zugangsweg analoge Vorüberlegungen angestellt werden, wie für die Remote-Administration. Zusätzlich ist es wichtig, dass das zentrale Managementsystem selbst entsprechend sicher konfiguriert und administriert wird. 
**Routinetätigkeiten bei der Administration**

Es wird empfohlen, für die üblichen Routinetätigkeiten des IT-Betriebs entsprechend der Sicherheitsrichtlinie Hinweise für die Administration zu erstellen. Dies umfasst beispielsweise Tätigkeiten wie

* Anlegen und Löschen von Benutzern,
* Installation und Deinstallation von Programmen,
* Einspielen von Sicherheitsupdates und Patches,
* Einspielen sonstiger Updates und Patches oder
* Regelmäßiger Integritätscheck mit entsprechenden Tools.
#### SYS.2.1.M21 Verhinderung der unautorisierten Nutzung von Rechnermikrofonen und Kameras

Viele IT-Systeme sind mit Mikrofonen und teilweise auch mit Kameras ausgestattet. Mikrofone und Kameras von vernetzten Client können von denjenigen benutzt werden, die Zugriffsrechte auf die entsprechende Gerätedatei haben. Für ein Mikrofon wäre das unter Unix zum Beispiel /dev/audio für die Soundkarte oder /dev/video für eine Kamera. Unter Windows bestimmen die Zugriffsrechte auf die entsprechenden Schlüssel der Registrierung (HKEY\_LOCAL\_MACHINE\HARDWARE\.), wer das Rechnermikrofon oder die Rechnerkamera aktivieren kann. Diese Rechte sind daher sorgfältig zu vergeben. Der Zugriff auf die Gerätedatei sollte nur möglich sein, solange jemand lokal an dem IT-System arbeitet. Wenn vorhandene Mikrofone oder Kameras nicht genutzt und damit nicht missbraucht werden sollen, müssen diese, wenn möglich, ausgeschaltet, deaktiviert oder physikalisch vom Gerät getrennt werden.

Falls das Mikrofon bzw. die Kamera in den Client fest eingebaut ist und nur durch Software ein- und ausgeschaltet werden kann, müssen die Zugriffsrechte so gesetzt sein, dass kein Unbefugter sie benutzen kann. Dies kann z. B. erfolgen, indem unter Unix allen Benutzern die Leserechte auf die Gerätedateien /dev/audio, /dev/video bzw. unter Windows die Zugriffsrechte auf die entsprechenden Schlüssel der Registrierung entzogen werden. Dadurch ist ausgeschlossen, dass ein normaler Benutzer das Mikrofon oder die Kamera benutzen kann, er kann aber weiterhin Audio- oder Video-Dateien abspielen. Kameras können auch einfach abgedeckt werden, beispielsweise mit einem geeigneten Aufkleber.

Bei IT-Systemen mit Mikrofon bzw. Kamera ist zu prüfen, ob Zugriffsrechte und Eigentümer bei einem Zugriff auf die Gerätedatei verändert werden. Falls dies der Fall ist oder falls gewünscht ist, dass jeder Benutzer Mikrofon oder Kamera benutzen kann und es nicht nur in Einzelfällen durch den IT-Betrieb freigegeben werden soll, muss der Administrator ein Kommando zur Verfügung stellen, das

* nur aktiviert werden kann, wenn jemand an dem IT-System angemeldet ist,
* nur durch diesen Benutzer aktiviert werden kann und
* die Zugriffsberechtigungen dem Benutzer nach dem Abmelden wieder entzieht.
Solange der Zugriff auf das Mikrofon oder die Kamera durch kein sicheres Kommando geregelt wird, müssen diese physikalisch vom Client oder der Client vom Netz getrennt werden.

Clients mit eingebautem Mikrofon oder Kamera sollten während einer vertraulichen Besprechung aus dem Raum entfernt werden oder zumindest ausgeschaltet werden. Bei einem Laptop sollten alle eventuell vorhandenen Verbindungen zu Kommunikationsnetzen, die nicht benötigt werden, getrennt werden. In den meisten Fällen ist es hierzu am einfachsten, das entsprechende Kabel auszustecken.

#### SYS.2.1.M22 Abmelden nach Aufgabenerfüllung [Benutzer]

Wird ein IT-System oder eine IT-Anwendung von mehreren Benutzern verwendet und besitzen die einzelnen Benutzer unterschiedliche Zugriffsrechte auf dort gespeicherte Daten oder Programme, so kann der erforderliche Schutz mittels einer Zugriffskontrolle nur dann erreicht werden, wenn jeder Benutzer sich nach Aufgabenerfüllung am IT-System oder der IT-Anwendung abmeldet. Ist es einem Dritten möglich, an einem IT-System oder in einer IT-Anwendung unter der Identität eines anderen weiterzuarbeiten, so ist jegliche sinnvolle Zugriffskontrolle unmöglich. Daher sind alle Benutzer zu verpflichten, sich nach Aufgabenerfüllung vom IT-System beziehungsweise von der IT-Anwendung abzumelden. Aus technischen Gründen (z. B. damit alle offenen Dateien geschlossen werden) sollten auch dann Regelungen für die Abmeldung von IT-Systemen und IT-Anwendungen getroffen werden, wenn keine Zugriffskontrolle realisiert ist.

Ist absehbar, dass nur eine kurze Unterbrechung der Arbeit erforderlich ist, kann an Stelle des Abmeldens auch die manuelle Aktivierung der Bildschirmsperre erfolgen (siehe auch SYS.2.1.M5 Bildschirmsperre). Bei längerer Abwesenheit sollte die Bildschirmsperre automatisch aktiviert werden.

Einige IT-Systeme und IT-Anwendungen bieten die Möglichkeit, einen Zeitraum vorzugeben, nach dessen Ablauf ein Benutzer bei Inaktivität automatisch vom IT-System abgemeldet wird. Es sollte überlegt werden, ob dieses Verfahren benutzt wird, da es auch zu Datenverlusten führen kann. Eine automatische Abmeldung kann z. B. bei PC-Pools mit starkem Publikumsverkehr eingesetzt werden, da hier ein angemeldeter Benutzer den Arbeitsplatz mit Hilfe der Bildschirmsperre unberechtigterweise blockieren kann.

Je nach Arbeitsplatzumgebung ist abzuwägen, welche Vorkehrungen für kurzfristige Abwesenheiten von Benutzern zu treffen sind. So sollte eine automatische Aktivierung der Bildschirmsperre bei Mehr-Benutzer-Systemen schneller erfolgen als bei solchen für einen Benutzer, also z. B. bereits nach fünf Minuten. 

#### SYS.2.1.M23 Nutzung von Client-Server-Diensten

Der Informationsaustausch zwischen gleichberechtigten IT-Systemen wird oft als "Client-to-Client" oder oft als"Peer-to-Peer" bezeichnet. Jedes IT-System kann hierbei Dienste anbieten oder nutzen. Über die hierfür aufgebaute Kommunikationsverbindung können sich mehrere IT-Systeme Ressourcen dezentral untereinander teilen. Somit werden die typischen Funktionen eines Servers und eines Clients auf einem IT-System vereint.

Oft werden entsprechende Anwendungen genutzt, um folgende Dienste anderen IT-Systemen bereitzustellen:

* Nutzung von Druckern, die lokal an einem IT-System angeschlossen sind, durch Benutzer an anderen IT-Systemen,
* Zugriff auf Speicherbereiche der im IT-System eingebauten oder lokal angeschlossenen Festplatten ("File Sharing"),
* Direktkommunikation über Kurzmitteilungen ("Messaging") und
* Internettelefonie.
**Vorteile von Client-to-Client-Diensten**

Im Gegensatz zu einer servergestützten Architektur haben Client-to-Client-Dienste zahlreiche Vorteile:

* Ein dedizierter Server verursacht in der Anschaffung und im Betrieb zusätzliche Kosten.
* Fällt der zentrale Server aus, stehen die Ressourcen nicht mehr zur Verfügung ("Single Point of Failure"). Fällt bei Client-to-Client-Diensten ein Client aus, können im Allgemeinen genügend andere Clients einspringen.
* Geographisch benachbarte Clients können effizienter Informationen direkt untereinander austauschen, als wenn hierfür ein Server benutzt wird, der sich weit entfernt befindet.
* Server benötigen eine höhere Bandbreite, mehr CPU-Leistung und umfangreicheren Festplatten- und Arbeitsspeicher als Clients. Diese Anforderungen können in Client-to-Client-Netzen auf die Clients verteilt und dort ungenutzte Ressourcen verwendet werden.
* Freigegebene Informationen liegen oft auf mehreren Clients gleichzeitig und damit redundant vor.
Die Nutzung von Client-to-Client-Diensten hat allerdings auch eine Vielzahl von Nachteilen, die in vielen Fällen auf der fehlenden Zentralisierung zurückzuführen sind. Beispielsweise können die ausgetauschten Informationen nicht zentral auf Schadsoftware untersucht werden.

**Architektur**

Je nach Anforderungen können Client-to-Client-Dienste nur in einem lokalen Netz oder im gesamten Internet genutzt werden. Die Anzahl der IT-Systeme, die sich untereinander diese Ressourcen teilen können, reichen von nur wenigen, ausgewählten Clients bis zu einer unüberschaubaren Menge von unbekannten Clients. Generell kann aber zwischen zwei Arten von Client-to-Client-Diensten unterschieden werden:

* Lokale Client-to-Client-Dienste  
 Bei lokalen Client-to-Client-Diensten können einzelne Clients anderen Clients in einem LAN Ressourcen freigeben. Diese Freigaben können oft direkt vom Betriebssystem verwaltet werden. Ein Beispiel hierfür ist die Datei- und Druckerfreigabe in Windows-Betriebssystemen.Der Zugriff dieser Dienste kann oft über Passwörter oder eine Auswahl an IP-Adressen eingeschränkt werden. In der Regel werden diese Dienste nicht über das lokale Netz hinaus genutzt und werden am Sicherheitsgateway (Firewall) abgewiesen.Da für diese Dienste kein eigener Server benötigt wird, können Kosten für die Beschaffung von Hard- und Software eingespart werden. 
* Öffentliche Client-to-Client-Dienste  
 Um Informationen mit Anwendern, die keinen Zugriff auf das LAN haben, auszutauschen, können öffentliche Client-to-Client-Dienste eingesetzt werden. Hierfür müssen in der Regel zusätzliche Applikationen auf dem jeweiligen IT-System installiert werden, damit diese die von anderen Clients bereitgestellten Dienste nutzen zu können. Da bei Client-to-Client-Diensten direkt zwischen zwei oder mehreren IT-Systemen Informationen ausgetauscht werden, sind für einen Verbindungsaufbau zusätzliche Informationen nötig, wie diese IT-Systeme erreichbar sind. Aus diesem Grund sollte es besonders bei großen Client-to-Client-Netzen eine Übersicht geben, auf welchem Client welche Ressourcen bereitgestellt werden.  
 Prinzipiell werden folgende Typen unterschieden: 

 
	+ Zentrale Client-to-Client-Dienste  
	 Die installierte Applikation baut eine Verbindung zu einem Server auf, der Informationen zu anderen Clients verwaltet. Hierfür muss vorher die Applikation des Clients Informationen über die Ressourcen, die er bereitstellen möchte, an den Server übertragen. Erst nach diesem Schritt kann in der Regel ein IT-System auf Informationen über die anderen angemeldeten Clients zugreifen. Hierzu gehören beispielsweise die IP-Adresse, der Benutzer und die bereitgestellten Inhalte. Mit Hilfe dieser Informationen kann eine direkte Verbindung zu dem entfernten Client aufgebaut und dessen Ressourcen genutzt werden.Fällt der zentrale Server aus, stehen die Kontaktinformationen der angeschlossenen IT-Systeme nicht mehr zur Verfügung und die Clients können keine Datenverbindung mehr untereinander aufbauen. Dies hat den Ausfall des gesamten Client-to-Client-Netzes zur Folge.
	+ Dezentrale Client-to-Client-Dienste:  
	 Bei dezentralen Client-to-Client-Diensten wird kein zentraler Server, der die angeschlossenen Benutzer verwaltet, benötigt. Die IT-Systeme der Benutzer dieser Dienste bauen untereinander Datenverbindungen auf, um Informationen über die bereitgestellten Ressourcen auszutauschen. Hierbei können nicht nur die Ressourcen der IT-Systeme, mit denen direkt eine Verbindung aufgebaut wird, durchsucht werden, sondern auch Informationen über andere Clients, die hiermit wiederum eine Datenverbindung aufgebaut haben, abgerufen werden. Da jeder Client mit mehreren Clients eine Verbindung aufbauen kann, entsteht ein Netz, über das jeder Client Informationen zu den bereitgestellten Ressourcen anderer Clients abrufen kann.Diese dezentralen Client-To-Client-Dienste setzen voraus, dass die Applikation mit einem Client aufgebaut werden muss, der Bestandteil dieses Netzes ist, um ebenfalls Mitglied des Netzes werden zu können. Die hierfür benötigten Kontaktinformationen müssen vorher bekannt sein. Da viele Netze von einer großen Menge von angeschlossenen IT-Systemen profitieren, werden diese Kontaktinformationen oft auf Webseiten veröffentlicht.
	+ Hybride Client-to-Client-Dienste  
	 Hybride Client-to-Client-Dienste sind mit zentralen Client-to-Client-Diensten vergleichbar, mit dem Unterschied, dass mehrere voneinander unabhängige Server eingesetzt werden können. Wie bei zentralen Client-to-Client-Diensten übermitteln die Clients einem Server die Ressourcen, die sie bereitstellen und Kontaktinformationen, wie sie erreicht werden können. Die Server wiederum teilen diese Informationen weiteren Servern mit. Bei Bedarf können die Clients auf die Ressourcen anderer Clients zugreifen, die nicht vom selben Server verwaltet werden.
	  

 
**Alternativen für den Einsatz von Client-to-Client-Diensten**

Nur bei wenigen Diensten ist eine Client-to-Client-Kommunikation zwischen IT-Systemen zwingend erforderlich. Beispielsweise können Ressourcen auch zentral von Servern bereitgestellt werden. Erst durch einen Einsatz von Servern können Vorgaben zentral umgesetzt werden, beispielsweise dass nur berechtigte Personen auf die Informationen zugreifen dürfen. Folgende Dienste, die typischerweise über Client-to-Client-Netze verteilt werden können, können zentralisiert bereitgestellt werden:

* Bereitstellung von Druckern  
 Wenn mehrere Personen in einem LAN Zugriff auf Drucker benötigen, können diese zentral im Netz bereitgestellt werden. Hierfür eignet sich der Einsatz netzfähiger Drucker oder die Verwaltung über Druckserver (siehe SYS.4.1 Drucker, Kopierer und Multifunktionsgeräte).
* File-Sharing  
 Statt Speicher auf mehreren Clients im LAN freizugeben, können die Informationen zentral auf einem Dateiserver abgelegt werden. Sollen nur die Benutzer innerhalb eines LANs auf den Server zugreifen dürfen, können beispielsweise Samba-Server (siehe APP.3.4 Samba) oder NFS-Server (siehe SYS.1.3 Server unter Unix) die Informationen bereitstellen., allgemeine Empfehlungen sind in APP3.3 Fileserver zu finden. Sollen auch externe Benutzer auf die Informationen zugreifen dürfen, könnten die Informationen auf einen extern erreichbaren Webserver (siehe APP.3.2 Webserver) abgelegt werden.
* Messaging  
 Wenn es nötig ist, Kurzmitteilungen zu versenden und nicht auf E-Mail zurückgegriffen werden soll, ist zu überlegen, einen Instant Messaging Server, wie beispielsweise Jabber, zu betreiben. Über diesen Server könnten die Nachrichten zentralisiert auf Schadsoftware überprüft werden.  
 Auch die Kommunikation mit externen Gesprächspartnern kann mit Hilfe eines zentralen Instant Messaging Server, der von der Institution betrieben wird und sowohl von intern als auch von extern erreichbar ist, erfolgen. Vertiefende Informationen sind in APP.1.5 Instant Messaging zu finden
* VoIP (Voice over Internet Protocol) und Internettelefonie  
 VoIP-Lösungen, wie im Baustein NET.4.2 VoIP beschrieben, unterscheiden zwischen der Signalisierung und dem Medientransport. Für die Signalisierung werden oft Server vorausgesetzt, auf denen die Teilnehmer verwaltet werden. Nachdem über die Signalisierung ein Gespräch zwischen zwei oder mehreren Benutzern eingeleitet wurde, werden bei vielen Lösungen die Sprachinformationen direkt zwischen den Benutzern ausgetauscht. Diese Art von Client-to-Client ist in einem LAN sinnvoll und sollte genutzt werden.  
 Über die Grenzen eines LANs hinweg sollte Client-to-Client nicht zur Telefonie genutzt werden, beispielsweise sollte eine Institution keine solche Kommunikation zulassen, um mit externen Gesprächspartner zu kommunizieren ("Internettelefonie"). Auch in diesem Fall sollte sowohl die Signalisierung als auch der Medientransport auf einem Konzentrator, ähnlich einem Proxy, gebündelt werden. Auf dieser Weise wird der direkte Verbindungsaufbau einzelner Clients auf externe Gesprächspartner, die sich beispielsweise im Internet befinden können, vermieden.
**Empfehlungen für den Einsatz von lokalen Client-to-Client-Diensten**

Wenn möglich, sollten statt Freigaben über Client-to-Client-Dienste dedizierte Server zum Informationsaustausch genutzt werden. In Ausnahmefällen ist aber auch der Einsatz von Client-to-Client-Lösungen nötig, wie beispielsweise bei VoIP. Daher ist festzulegen:

* welche Client-to-Client-Dienste genutzt und
* welche Informationen ausgetauscht 
werden dürfen. Wenn erforderlich, sind die Benutzer für die Nutzung von Client-to-Client-Diensten zu schulen. Es ist darauf zu achten, dass sich die Client-to-Client-Dienste nur auf das LAN beschränken.

**Empfehlungen für den Einsatz von öffentlichen Client-to-Client-Diensten**

Generell muss der unkontrollierte Informationsfluss aus einem LAN unterbunden werden. Hierzu gehören auch direkte Client-to-Client-Verbindungen von Clients zu IT-Systemen, die sich nicht im LAN befinden. Durch die fehlende Zentralisierung können unkontrolliert Informationen das LAN verlassen (z. B. vertrauliche Informationen) oder hinein gelangen (z. B. Schadsoftware). Durch folgende Maßnahmen kann die Nutzung von öffentlichen Client-to-Client-Diensten verhindert werden:

* Lokale Paketfilter  
 Durch den Einsatz lokaler Paketfilter kann die Kommunikation der Clients auf wenige IT-Systeme beschränkt werden (siehe SYS.2.1.M28 Einrichtung lokaler Paketfilter). Beispielsweise könnten die Filterregeln so festgelegt werden, dass nur mit Servern kommuniziert werden darf.  
 Auf Grundlage der IP-Adresse des Servers und der Portnummer des erlaubten Dienstes kann ein unerwünschter Kommunikationsaufbau erschwert werden. Durch den Einsatz von lokalen Paketfiltern kann sowohl die Verwendung von lokalen als auch öffentlichen Client-to-Client-Netzen unterbunden werden.
* Zentrale Filterung am Sicherheitsgateway (Firewall)  
 Generell sollte das Sicherheitsgateway nur die notwendige Kommunikation in oder aus dem lokalen Netz zulassen, alle anderen Verbindungen sollten abgewiesen werden (siehe NET.3.2 Firewall). Verhindert das Sicherheitsgateway die Kommunikation der Clients aus dem LAN mit IT-Systemen im Internet, kann die Nutzung von öffentlichen Client-to-Client-Netzen verhindert werden.
* Richtlinie  
 Neben technischen Empfehlungen sollte den Mitarbeitern der Institution auch die Verwendung von Client-to-Client-Diensten untersagt werden. Diese Anweisung kann in der Sicherheitsrichtlinie für Benutzer formuliert werden.
Wenn in der Institution Client-to-Client-Dienste genutzt werden sollen, muss dies durch die Leitungsebene der Institution beschlossen werden. Der Informationssicherheitsbeauftragte muss hierbei einbezogen werden, außerdem ist die Entscheidung inklusive der Restrisiken zu dokumentieren. 

#### SYS.2.1.M24 Umgang mit Wechseldatenträgern im laufenden System

Handelsübliche PCs sind heute in der Regel mit einem CD-/DVD-/Blu-ray-Laufwerk bzw. CD-/DVD-/Blu-ray-Brenner ausgestattet, daher sollten die Empfehlungen des Bausteins OPS.1.2.3 Datenträgeraustausch und SYS.3.4 Mobile Datenträger berücksichtigt werden. Zusätzlich besteht die Möglichkeit, über Schnittstellen externe Speichermedien anzuschließen, die von vielen Betriebssystemen automatisch erkannt und eingebunden werden. Beispiele sind USB-Speicher, die an die USB-Schnittstelle angeschlossen werden, und Firewire-Festplatten. Außerdem sind in vielen IT-Systemen Kartenleser für Speicherkarten eingebaut. Durch solche Laufwerke für Wechselmedien und externe Datenspeicher ergeben sich folgende potentielle Sicherheitsprobleme:

* Das IT-System könnte von solchen Laufwerken unkontrolliert gebootet werden.
* Es könnte unkontrolliert Software von solchen Laufwerken eingespielt werden.
* Daten könnten unberechtigt auf Wechselmedien kopiert werden.
Wird von Wechselmedien gebootet oder wird hiervon Fremdsoftware installiert, können nicht nur Sicherheitseinstellungen außer Kraft gesetzt werden, sondern das IT-System kann auch mit Computer-Viren und anderen Schadprogrammen infiziert werden.

Diesen Gefahren muss durch geeignete organisatorische oder technische Sicherheitsmaßnahmen entgegengewirkt werden. Hierfür bieten sich verschiedene Vorgehensweisen an, deren spezifische Vor- und Nachteile im Folgenden kurz dargestellt werden:

* Ausbau von Laufwerken  
 Der Ausbau der Laufwerke für Wechselmedien (bzw. der Verzicht bei der Beschaffung) bietet zwar den sichersten Schutz vor den oben genannten Gefährdungen, ist aber meist mit erheblichem Aufwand verbunden. Oft ist ein Ausbau überhaupt nicht möglich, z. B. bei Speicherkartenlesern bei Notebooks. Weiterhin ist zu berücksichtigen, dass der Ausbau unter Umständen die Administration und Wartung des IT-Systems behindert. Diese Lösung sollte in Betracht gezogen werden, wenn besondere Sicherheitsanforderungen bestehen. Wenn abzusehen ist, dass die Laufwerke für Wechselmedien nicht benötigt werden, sollten schon bei der Beschaffung Geräte ohne verbaute Laufwerke bevorzugt werden.
* Verschluss von Laufwerken  
 Für einige Laufwerksarten gibt es abschließbare Einschubvorrichtungen, mit denen die unkontrollierte Nutzung verhindert werden kann. Bei der Beschaffung sollte sichergestellt werden, dass die Laufwerksschlösser für die vorhandenen Laufwerke geeignet sind und diese nicht beschädigen können. Es muss beachtet werden, dass nicht für alle Laufwerksarten, wie für eingebaute Speicherkartenleser, Schlösser angeboten werden. Außerdem sollte darauf geachtet werden, dass die Schlösser herstellerseitig mit hinreichend vielen unterschiedlichen Schlüsseln angeboten werden. Nachteilig sind die Beschaffungskosten für die Laufwerksschlösser und der Aufwand für die erforderliche Schlüsselverwaltung. Daher ist diese Lösung nur bei höherem Schutzbedarf oder besonderen Sicherheitsanforderungen sinnvoll.
* Deaktivierung im BIOS bzw. Betriebssystem  
 Im BIOS bieten die meisten PCs Einstellmöglichkeiten dafür, von welchen Laufwerken gebootet werden kann. In Verbindung mit einem Passwort-Schutz der BIOS-Einstellungen kann dadurch das unkontrollierte Booten von Wechselmedien und mobilen Datenträgern unterbunden werden. Weiterhin können die vorhandenen Laufwerke und Schnittstellen bei modernen Betriebssystemen einzeln deaktiviert werden.  
 Der Client kann auf diese Weise nun nur schwer unberechtigt genutzt werden, da z.B. von den Wechselmedien keine Fremdsoftware installiert oder Informationen hierauf kopiert werden können. Werden die Laufwerke im BIOS bzw. Betriebssystem deaktiviert, hat dies den Vorteil, dass die Hardware nicht verändert werden braucht. Die entsprechenden Einstellungen im Betriebssystem können gegebenenfalls sogar zentral vorgenommen werden. Damit diese Vorgehensweise wirksam ist, muss sichergestellt sein, dass die Benutzer nicht über die Berechtigungen im Betriebssystem verfügen, um die Deaktivierung der Laufwerke rückgängig zu machen.
* Verschlüsselung  
 Es gibt Produkte, die dafür sorgen, dass ausschließlich Zugriffe auf dafür zugelassene mobile Datenträger möglich sind. Eine Lösung ist beispielsweise, dass nur noch mobile Datenträger gelesen und beschrieben werden können, die mit bestimmten kryptographischen Schlüsseln verschlüsselt worden sind. Dies schützt nicht nur vor unbefugtem Zugriff über manipulierte mobile Datenträger, sondern schützt auch die Daten auf den mobilen Datenträgern bei Verlust oder Diebstahl.
* Richtlinien für die Nutzung  
 In vielen Fällen dürfen die Benutzer die eingebauten Laufwerke für Wechselmedien oder Speichermedien an externen Schnittstellen durchaus verwenden, die Nutzung ist jedoch durch entsprechende Richtlinien reglementiert. Auf technischer Ebene sollte dann das Booten von Wechselmedien im BIOS deaktiviert werden. Somit ist es nicht notwendig, die Laufwerke auszubauen, zu verschließen und im Betriebssystem zu deaktivieren.  
 In diesem Fall sollten die Richtlinien für die Nutzung der Laufwerke und Speichermedien so explizit wie möglich definiert werden. Beispielsweise kann alles generell verboten werden, nicht öffentliche Text-Dokumente dürften kopiert werden. Die Richtlinien müssen allen Benutzern bekannt gemacht und die Einhaltung kontrolliert werden. Es sollte untersagt werden, Programme, die von Wechselmedien eingespielt wurden, zu installieren und zu starten, dies sollte soweit wie möglich auch technisch unterbunden werden.  
 Diese rein organisatorische Lösung sollte nur dann gewählt werden, wenn die Benutzer mindestens hin und wieder auf die Laufwerke zugreifen müssen. Anderenfalls sollte der Zugriff, wie oben beschrieben, durch technische Maßnahmen unterbunden werden.
Bei der Auswahl einer geeigneten Vorgehensweise müssen immer alle Laufwerke für Wechselmedien berücksichtigt werden, aber ebenso auch alle Möglichkeiten, über Vernetzung Daten auszutauschen, also insbesondere auch E-Mail und Internet-Anbindungen. Wenn das IT-System über eine Verbindung zum Internet verfügt, ist es nicht allein ausreichend, alle Laufwerke für Wechselmedien zu deaktivieren oder auszubauen. Besonderes Augenmerk ist auf den Schutz vor Schadprogrammen, z. B. Computer-Viren oder Trojanische Pferde, zu richten (siehe auch SYS.2.1.M6 Einsatz von Virenschutzprogrammen).

Unabhängig von der Auswahl einer geeigneten Vorgehensweise sollte verhindert werden, dass Inhalte von Wechseldatenträgern automatisch ausgeführt werden, wenn die Datenträger angeschlossen werden. Hierzu sind die entsprechenden Autorun- und Autoplay-Funktionen des Betriebssystems zu deaktivieren.

Damit die Sicherheitsmaßnahmen akzeptiert und beachtet werden, müssen die Benutzer über die Gefährdung durch Laufwerke für Wechselmedien informiert und sensibilisiert werden.

**Umgang mit USB-Geräten**

Über die USB-Schnittstelle lassen sich eine Vielzahl von Zusatzgeräten an PCs anschließen. Beispiele sind Festplatten, CD/DVD-Brenner und USB-Sticks. Trotz großer Speicherkapazität sind USB-Sticks so handlich, dass sie beispielsweise in Form von Schlüsselanhängern hergestellt werden und in jede Hosentasche passen. In modernen Betriebssystemen sind die Treiber für USB-Massenspeichergeräte bereits integriert, so dass zum Betrieb keine Softwareinstallation mehr notwendig ist. Im Allgemeinen bezieht sich diese Empfehlungen nicht ausschließlich auf USB-Speichermedien, sondern generell auf alle USB-Geräte, die Daten speichern können. Unter anderem können auch USB-Drucker und USB-Kameras zum Speichern der Daten "missbraucht" werden. Dies gilt insbesondere für "intelligente" Geräte mit USB-Anschluss, die jede beliebige USB-Identität annehmen können, wenn sie mit spezieller Software ausgestattet sind. Dies können programmierbare USB-Entwicklerboards sein, aber auch bei vielen Smartphones ist ein solcher Einsatz möglich.

Über USB-Speichermedien können unkontrolliert Informationen und Programme ein- oder ausgelesen werden. Daher ist mit USB-Speichermedien generell genauso wie mit herkömmlichen Speichermedien umzugehen. Der Betrieb von USB-Speichermedien lässt sich nur sehr schwer verhindern, wenn die USB-Schnittstelle für andere Geräte genutzt wird. So werden beispielsweise Notebooks ausgeliefert, die zum Anschluss einer Maus nur die USB-Schnittstelle zur Verfügung stellen. Deswegen ist es meist nicht sinnvoll, ein "USB-Schloss" zu verwenden oder die Schnittstelle durch andere mechanische Maßnahmen zu deaktivieren. Die Nutzung von Schnittstellen sollte daher durch entsprechende Rechtevergabe auf Ebene des Betriebssystems oder mit Hilfe von Zusatzprogrammen geregelt werden. Alternativ kann überwacht werden, ob Geräte hinzugefügt werden. Um Datenspeicher an externen Schnittstellen anzuschließen, werden oftmals vom Betriebssystem Treiber bzw. Kernelmodule geladen oder Einträge in Konfigurationsdateien (wie der Windows-Registry) erzeugt, die detektiert werden können. Nachdem die Veränderungen festgestellt wurden, kann dann beispielsweise eine Protokolldatei erstellt oder der IT-Betrieb benachrichtigt werden. Dies alles kann jedoch nur mit Hilfe von Zusatzsoftware realisiert werden. Hierfür ist entweder eine Eigenentwicklung oder ein Drittprodukt notwendig.

**Umgang mit USB-Geräten**

Über die USB-Schnittstelle lassen sich eine Vielzahl von Zusatzgeräten an PCs anschließen. Beispiele sind Festplatten, CD/DVD-Brenner und USB-Sticks. Trotz großer Speicherkapazität sind USB-Sticks so handlich, dass sie beispielsweise in Form von Schlüsselanhängern hergestellt werden und in jede Hosentasche passen. In modernen Betriebssystemen sind die Treiber für USB-Massenspeichergeräte bereits integriert, so dass zum Betrieb keine Softwareinstallation mehr notwendig ist. Im Allgemeinen bezieht sich diese Empfehlungen nicht ausschließlich auf USB-Speichermedien, sondern generell auf alle USB-Geräte, die Daten speichern können. Unter anderem können auch USB-Drucker und USB-Kameras zum Speichern der Daten "missbraucht" werden. Dies gilt insbesondere für "intelligente" Geräte mit USB-Anschluss, die jede beliebige USB-Identität annehmen können, wenn sie mit spezieller Software ausgestattet sind. Dies können programmierbare USB-Entwicklerboards sein, aber auch bei vielen Smartphones ist ein solcher Einsatz möglich.

Über USB-Speichermedien können unkontrolliert Informationen und Programme ein- oder ausgelesen werden. Daher ist mit USB-Speichermedien generell genauso wie mit herkömmlichen Speichermedien umzugehen. Der Betrieb von USB-Speichermedien lässt sich nur sehr schwer verhindern, wenn die USB-Schnittstelle für andere Geräte genutzt wird. So werden beispielsweise Notebooks ausgeliefert, die zum Anschluss einer Maus nur die USB-Schnittstelle zur Verfügung stellen. Deswegen ist es meist nicht sinnvoll, ein "USB-Schloss" zu verwenden oder die Schnittstelle durch andere mechanische Maßnahmen zu deaktivieren. Die Nutzung von Schnittstellen sollte daher durch entsprechende Rechtevergabe auf Ebene des Betriebssystems oder mit Hilfe von Zusatzprogrammen geregelt werden. Alternativ kann überwacht werden, ob Geräte hinzugefügt werden. Um Datenspeicher an externen Schnittstellen anzuschließen, werden oftmals vom Betriebssystem Treiber bzw. Kernelmodule geladen oder Einträge in Konfigurationsdateien (wie der Windows-Registry) erzeugt, die detektiert werden können. Nachdem die Veränderungen festgestellt wurden, kann dann beispielsweise eine Protokolldatei erstellt oder der IT-Betrieb benachrichtigt werden. Dies alles kann jedoch nur mit Hilfe von Zusatzsoftware realisiert werden. Hierfür ist entweder eine Eigenentwicklung oder ein Drittprodukt notwendig.

#### SYS.2.1.M25 Richtlinie zur sicheren IT-Nutzung [Benutzer]

Um einen sicheren und ordnungsgemäßen Einsatz von Informationstechnik in größeren Unternehmen bzw. Behörden zu fördern, sollte eine Richtlinie erstellt werden, in der verbindlich vorgeschrieben wird, welche Randbedingungen eingehalten werden müssen und welche Sicherheitsmaßnahmen zu ergreifen sind. Die Richtlinie ist allen Benutzern zur Kenntnis zu geben, beispielsweise in elektronischer Form auf einem Intranet-Server. Jeder neue Benutzer muss die Kenntnisnahme der Richtlinie bestätigen, bevor er die Informationstechnik nutzen darf. Nach größeren Änderungen an der Richtlinie oder nach spätestens zwei Jahren ist eine erneute Bestätigung erforderlich.

Im Folgenden soll grob umrissen werden, welche Inhalte für eine solche Richtlinie sinnvoll sind:

**Zielsetzung und Begriffsdefinitionen**

Der erste Teil der Richtlinie dient dazu, die Anwender für Informationssicherheit zu sensibilisieren und zu motivieren. Gleichzeitig werden die für das gemeinsame Verständnis notwendigen Begriffe definiert, wie z. B. PC, Server, Netz, Anwender, Benutzer, schutzbedürftige Objekte.

**Geltungsbereich**

In diesem Teil muss verbindlich festgelegt werden, für welche Teile des Unternehmens bzw. der Behörde die Richtlinie gilt.

**Rechtsvorschriften und interne Regelungen**

Hier wird im Überblick dargestellt, welche wesentlichen Rechtsvorschriften, z. B. das Bundesdatenschutzgesetz und das Urheberrechtsgesetz, einzuhalten sind. Anhand von Beispielen sollte deutlich gemacht werden, welche Auswirkungen dies auf die Nutzung der Informationstechnik im jeweiligen Umfeld hat. Darüber hinaus kann diese Stelle genutzt werden, um alle relevanten betriebsinternen Regelungen aufzuführen.

**Verantwortungsverteilung**

In diesem Teil wird definiert, welcher Funktionsträger im Zusammenhang mit dem IT-Einsatz welche Verantwortung tragen muss. Dabei sind insbesondere die Rollen Benutzer, Vorgesetzte, IT-Betrieb, Revisor, Datenschutzbeauftragter und Sicherheitsmanagement-Team zu unterscheiden.

**Ansprechpartner**

Die Richtlinie sollte Ansprechpartner und Kontaktinformationen (Telefon, E-Mail etc.) für die Benutzer zu Fragen der Informationssicherheit enthalten oder aufzeigen, wo diese Informationen gefunden werden können. Dabei sollte beachtet werden, dass es häufig zu Verwirrung führt, wenn den Benutzern zu viele unterschiedliche Ansprechpartner genannt werden. Besser ist es meist, nur wenige unterschiedliche Ansprechpartner zu benennen, die dann bei Bedarf die Benutzer an die richtige Stelle verweisen (Help-Desk-Konzept).

**Umzusetzende und einzuhaltende Sicherheitsmaßnahmen**

Im letzten Teil der Richtlinie für die IT-Nutzung ist festzulegen, welche Sicherheitsmaßnahmen vom Benutzer einzuhalten bzw. umzusetzen sind. Dies kann je nach Schutzbedarf auch über die IT-Grundschutz-Maßnahmen hinausgehen. Typische Beispiele für Sicherheitsmaßnahmen am Arbeitsplatz sind das sichere An- und Abmelden am PC, der ordnungsgemäße Umgang mit Passwörtern und Verhaltensregeln bei der Nutzung des Internets.

Sind Telearbeiter im Unternehmen bzw. in der Behörde beschäftigt, sollte die Richtlinie um die Telearbeitsplatz-spezifischen Regelungen ergänzt werden.

#### SYS.2.1.M26 Schutz von Anwendungen

Um auf kritische Systemereignisse reagieren zu können, sollte für Clients ein geeignetes Systemüberwachungs- bzw. Monitoringkonzept erstellt werden. Dazu gehört, dass Systemzustand und Funktionsfähigkeit der Clients laufend überwacht werden. Wenn Fehler auftreten oder definierte Grenzwerte über- oder unterschritten werden, sollte dies automatisch an das Betriebspersonal gemeldet werden. 

Hierfür werden in der Regel Statusinformationen von einem zentralen IT-System abgerufen, auf dem die Ereignisse ausgewertet werden. Über die Schnittstelle, die benötigt wird, um die Systemereignisse vom IT-System abzurufen, können aber oft Systemeinstellungen des Betriebssystems verändert werden, z. B. über SNMP (Simple Network Management Protocol). Ist eine solche Modifikation nicht gewünscht, dann sollten diese Merkmale deaktiviert werden. 

#### SYS.2.1.M27 Geregelte Außerbetriebnahme eines Clients

Bei der Außerbetriebnahme eines Clients muss vor allem sichergestellt werden, dass

* keine wichtigen Daten, die eventuell auf dem Client gespeichert sind, verloren gehen, und dass
* keine sensitiven Daten auf den Datenträgern des Clients zurück bleiben.
Dazu ist es insbesondere wichtig, einen Überblick darüber zu haben, welche Daten wo auf den IT-Systemen gespeichert sind.

* Datensicherung  
 Vor der Außerbetriebnahme des Clients müssen lokal gespeicherte Daten, die noch benötigt werden, entweder extern gesichert bzw. archiviert (beispielsweise auf externen Festplatten, CDs oder DVDs) oder auf ein Ersatzsystem oder einen Fileserver übertragen werden. Nach der Sicherung sollte überprüft werden, dass wirklich alle Daten korrekt gesichert wurden.  
 In diesem Zusammenhang kann es sinnvoll sein, den Benutzern für die Sicherung eventuell gespeicherter lokaler Daten ein geeignetes Laufwerk, beispielsweise einen externen CD- oder DVD-Brenner, zur Verfügung zu stellen.  
 Weitere Informationen zu diesem Themenkomplex finden sich in SYS.2.1.M4 Regelmäßige Datensicherung sowie den Bausteinen OPS.1.1.5 Datensicherung und OPS.1.1.2 Archivierung.
* Austragen des IT-Systems aus Verzeichnisdiensten und Datenbanken  
 Etwaige Berechtigungen im Netz, die an den Client selbst (und nicht an einen Benutzer) gekoppelt sind, müssen gelöscht werden. Beispiele hierfür sind Einträge auf Proxyservern am Sicherheitsgateway oder Zugriffsrechte auf Netzdienste, die anhand der IP-Adresse gewährt werden. Ist der Client in netzweiten Verzeichnisdiensten oder Datenbanken eingetragen (etwa in einer Windows Domäne, Active Directory, NIS oder ähnlichen), so müssen die zugehörigen Einträge gelöscht oder zumindest die entsprechenden Kennungen deaktiviert werden. 
* Löschen der Daten auf dem IT-System  
 Es muss sichergestellt werden, dass keine schützenswerten Informationen mehr auf den Festplatten vorhanden sind. Dazu genügt es nicht, die Platten einfach neu zu formatieren, sondern sie müssen mindestens einmal vollständig überschrieben werden. Es ist zu beachten, dass weder das logische Löschen mit den Löschfunktionen des Betriebssystems noch das Neuformatieren der Platten die Daten tatsächlich von den Festplatten entfernt. Mit geeigneter Software können Daten in solchen Fällen, oft sogar ohne großen Aufwand, wieder rekonstruiert werden.  
 SSDs können wegen Wear Leveling und Reservekapazitäten nicht effektiv überschrieben werden, außerdem reduziert sich hierbei die erwartete Restlebensdauer der SSD. Bei SSDs empfiehlt sich stattdessen, die von der SSD bereitgestellte SECURE ERASE Funktionalität zu nutzen und anschließend das Ergebnis zu prüfen. 
* Löschen von Datensicherungsmedien  
 Nach der Außerbetriebnahme der IT-Systeme müssen gegebenenfalls auch die entsprechenden Datensicherungsmedien gelöscht werden, wenn die darauf gespeicherten Daten nicht mehr benötigt werden.
* Entfernen sonstiger Informationen  
 Sind auf einem Client noch an anderen Stellen als auf der Festplatte (etwa in einem nichtflüchtigen Speicher) potentiell sensitive Daten gespeichert (beispielsweise bestimmte Konfigurationsdaten), so müssen auch diese vor der Weitergabe des Geräts entfernt werden. 
Es wird empfohlen, anhand der oben gegebenen Empfehlungen eine Checkliste zu erstellen, die abgearbeitet werden kann, wenn das IT-Systeme außer Betrieb genommen wird. Auf diese Weise kann vermieden werden, dass einzelne Schritte vergessen werden. Vertiefende Informationen sind auch in OPS.1.2.7 Verkauf/Aussonderung von IT zu finden.

### 2.3 Maßnahmen für erhöhten Schutzbedarf

Im Folgenden sind Maßnahmenvorschläge aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und bei erhöhtem Schutzbedarf in Betracht gezogen werden sollten. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Maßnahme vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### SYS.2.1.M28 Verschlüsselung der Clients(C)

Vertrauliche Informationen auf Datenträgern können auf verschiedene Weise verschlüsselt und damit vor unbefugter Kenntnisnahme geschützt werden. So können beispielsweise der komplette Datenträger, eine einzelne Partition oder nur einzelne Dateien verschlüsselt werden. Aus Sicherheitssicht ist es besser, den kompletten Datenträger zu verschlüsseln, da dann weniger Benutzereingriffe erforderlich sind und alle Daten vor unbefugtem Zugriff geschützt sind. Die Verschlüsselung eines gesamten Datenträgers oder einer kompletten Partition ist für die Benutzer nahezu transparent. Lediglich beim Booten oder dem ersten Zugriff auf die Partition müssen sich die Benutzer authentisieren. Werden nur einzelne Dateien oder Dateicontainer verschlüsselt, besteht die Gefahr, dass versehentlich schützenswerte Daten in unverschlüsselten Bereichen der Festplatte abgelegt werden. Zudem muss hierfür ein Verschlüsselungsprogramm explizit von den Benutzern gestartet werden.

Auch wenn einzelne Partitionen komplett verschlüsselt werden, kann dies dazu führen, dass aus verschiedenen Gründen vertrauliche Informationen auf unverschlüsselten Partitionen landen. Daher ist eine vollständige Verschlüsselung von Datenträgern die beste und effizienteste Methode, um vertrauliche Daten zuverlässig vor unbefugtem Zugriff zu schützen.

Datenträgerverschlüsselung lässt sich mit Software, aber auch mit Hardware-Unterstützung umsetzen. Software-Lösungen sind BitLocker von Microsoft oder entsprechende Open-Source-Programme, wie dm-crypt oder Veracrypt.

Mobile Datenträger, wie USB-Sticks und Laptops, sollten möglichst immer vollständig verschlüsselt werden, auch wenn sie nur gelegentlich für vertrauliche Informationen eingesetzt werden. Bei stationären IT-Systemen sollten die Datenträger bei hohem Schutzbedarf bezüglich Vertraulichkeit komplett verschlüsselt werden. 

Neben dem Verschlüsselungsprogramm (siehe Abschnitt "Einsatz eines Verschlüsselungsproduktes") selbst sind für die Datenträgerverschlüsselung noch die kryptographischen Schlüssel nötig. Die kryptographischen Schlüssel sollten geeignet erzeugt und getrennt vom verschlüsselten Datenträger aufbewahrt werden. Hierfür können beispielsweise Chipkarten oder USB-Token eingesetzt werden. Eine solche Trennung ist bei der Verschlüsselung von USB-Sticks in der Regel nicht möglich, was bei der Sicherheitsanalyse berücksichtigt werden sollte. Weitere Informationen sind in CON.1 Kryptokonzept zu finden.

Natürlich müssen auch die auf den verschlüsselten Datenträgern gespeicherten Daten regelmäßig gesichert werden.

Einige Programme zur Datenträger- oder Partitionsverschlüsselung oder für den Einsatz von verschlüsselten Dateicontainern bieten die Möglichkeit, die verschlüsselten Bereiche zu "verstecken". Da solche Funktionen schwierig anzuwenden sind und Fehlbedienung zu vollständigem Datenverlust führen kann, sollten sie nur in besonderen Fällen angewendet werden.

Vertiefende Informationen zur Verschlüsselung von Festplatten sind unter [NIST800111] zu finden.

**Einsatz eines Verschlüsselungsproduktes**

Um zu verhindern, dass aus einem trotz aller Vorsichtsmaßnahmen gestohlenen tragbaren IT-System schutzbedürftige Daten ausgelesen werden können, sollte ein Verschlüsselungsprogramm oder eine vorhandene Betriebssystemfunktion eingesetzt werden. Mit Hilfe der marktgängigen Produkte ist es möglich, einzelne Dateien, bestimmte Bereiche oder die ganze Festplatte so zu verschlüsseln, dass nur derjenige, der über den geheimen Schlüssel verfügt, in der Lage ist, die Daten zu lesen und zu gebrauchen.

Die Sicherheit der Verschlüsselung hängt dabei von drei verschiedenen Punkten zentral ab:

* Der verwendete Verschlüsselungsalgorithmus muss so konstruiert sein, dass es ohne Kenntnis des verwendeten Schlüssels nicht möglich ist, den Klartext aus dem verschlüsselten Text zu rekonstruieren. Nicht möglich bedeutet dabei, dass der erforderliche Aufwand um den Algorithmus zu brechen oder den Klartest zu entschlüsseln in keinem Verhältnis zum dadurch erzielbaren Informationsgewinn seht.
* Der Schlüssel ist geeignet zu wählen. Nach Möglichkeit sollte ein Schlüssel zufällig erzeugt werden. 
* Der Verschlüsselungsalgorithmus, die verschlüsselten Dateien und die Schlüssel dürfen nicht zusammen auf einem Datenträger gespeichert werden. Es bietet sich an, den Schlüssel einzeln aufzubewahren. Die kryptographischen Schlüssel sollten auf einem auswechselbaren Datenträger, wie z. B. auf Chipkarte oder USB-Stick, gespeichert werden und getrennt vom tragbaren IT-System aufbewahrt werden (z. B. in der Brieftasche).
Eine Verschlüsselung kann online oder offline vorgenommen werden. Online bedeutet, dass sämtliche Daten der Festplatte (bzw. einer Partition) verschlüsselt werden, ohne dass der Benutzer dies aktiv veranlassen muss. Eine Offline-Verschlüsselung wird explizit vom Benutzer initiiert. Er muss dann auch entscheiden, welche Dateien verschlüsselt werden sollen.

**Selbstverschlüsselnde Festplatten**

Um zu verhindern, dass Unbefugte an vertrauliche Daten auf Festplatten gelangen können, sollten diese nach Möglichkeit komplett verschlüsselt werden. Es gibt Hard- und Software-basierte Verfahren zur Verschlüsselung, an dieser Stelle wird die hardware-basierte Verschlüsselung in Form von selbstverschlüsselnden Festplatten (englisch: "Self-Encrypting Device", SED) behandelt. SEDs greifen für die Verschlüsselung auf einen speziellen Hardware-Kryptocontroller zu und sind dadurch sehr performant. Die eingesetzten Verschlüsselungslösungen sehen oft nur vor, dass diese nur durch einen Benutzer genutzt werden, Mehr-Benutzer-Lösungen sind im Allgemeinen nicht vorgesehen. 

Werden selbstverschlüsselnde Festplatten genutzt, kann das IT-System unter Umständen nicht mehr in den Arbeitsspeicher suspendiert werden, da alle Daten verschlüsselt werden, wenn die Festplatte abgeschaltet wird, und ein im RAM gespeicherter Schlüssel ein Sicherheitsrisiko wäre. Dies ist vor dem Einsatz zu bedenken.

Selbstverschlüsselnde Festplatten sollten nicht mit einem TPM-Modul kombiniert werden, da es bei einer solchen Kombination in der Regel keine Möglichkeit gibt, die Festplatte in einem anderen IT-System mit einem Master-Key zu entschlüsseln. Wird in so einem Fall das IT-System beschädigt, lassen sich die Daten auf der Festplatte nicht mehr entschlüsseln, da die Festplatte durch das TPM-Modul fest mit dem IT-System verwoben ist.

Bei selbstverschlüsselnden Festplatten wird in der Regel AES eingesetzt. Der Schlüssel, mit dem die Informationen verschlüsselt werden, ist der sogenannte "Data Encryption Key" (DEK). Es sollte darauf geachtet werden, dass sich der DEK nur im Kryptocontroller befindet und dieser vor Manipulationen (z.B. Auslesen) besonders geschützt ist. Der DEK sollte auf Basis zufälliger Hardware-Ereignisse generiert werden. Dieser DEK wird mit einem "Authentication Key" (AK) verschlüsselt. Der AK wird typischerweise vom Benutzer durch die Wahl eines Passwortes erzeugt. Bei einigen selbstverschlüsselnden Festplatten kann auch der AK auf einem Token, beispielsweise einer Chipkarte oder einem Stick, gespeichert und zusätzlich mit einem Passwort verschlüsselt werden. Dies ermöglicht die Umsetzung einer Zwei-Faktor-Authentisierung. 

Zusätzlich zum DEK und AK gibt es in der Regel auch noch einen Master-Key, der es erlaubt, die Daten zu entschlüsseln, auch wenn das Passwort oder der Token verloren wurde. Ein solcher Schlüssel muss bei der Installation erzeugt und für den Fall, dass das Passwort bzw. der Token verloren geht, sicher aufbewahrt werden. Es muss geregelt werden, wie organisatorisch vorgegangen wird, wenn ein Benutzer das Passwort zu einer verschlüsselten Festplatte vergisst. In diesem Fall muss mit dem Master-Key das Passwort zurückgesetzt werden und der Benutzer ein neues Passwort setzen. 

Wenn sich der Benutzer erfolgreich authentisiert hat, wird der DEK entschlüsselt. Mit dem DEK werden alle auf der Festplatte befindlichen Daten ent- und verschlüsselt, ohne dass der Benutzer im Betrieb etwas davon bemerkt. Fährt der Rechner herunter oder wird die Laufwerkseinbindung des SEDs gelöst, werden alle Daten mit dem DEK und der DEK mit dem AK verschlüsselt. 

Generell sollte die verwendete Schlüssellänge des von der Festplatte verwendeten Verschlüsselungsverfahrens hinreichend lang sein. Es sollte darauf geachtet werden, dass der Verschlüsselungsalgorithmus in einem für eine Festplattenverschlüsselung sicheren Modus betrieben wird. Ansonsten können beim Entschlüsseln Probleme auftreten, wenn das Chiffrat zwischen zwei Sektoren verschoben wird.

Bevor selbstverschlüsselnde Festplatten beschafft werden, sollte geprüft werden, ob die Festplatten mit der übrigen Hardware des IT-Systems kompatibel sind. Ferner sollte geprüft werden, ob die Schreib- und Leserate der ausgesuchten Festplatte angemessen ist. Überdies sollte geprüft werden, ob weitere Randbedingungen für den Einsatz beim IT-System erfüllt werden müssen. Zum Beispiel lassen sich nur sehr wenige Modelle von selbstverschlüsselnden Festplatten in einer bestehenden "Single-Sign-On"-Architektur integrieren. Auch sollte überprüft werden, ob und wie IT-Systeme mit normalen Festplatten zu selbstverschlüsselnden Festplatten migriert werden können (mit einem mitgelieferten Programm oder über eine Neuinstallation). 

Die Installation einer selbstverschlüsselnden Festplatte sollte in Institutionen durch geschulte Administratoren durchgeführt werden. Dafür müssen diese zunächst einen neuen DEK erzeugen und ein Passwort vergeben sowie einen Master-Key erstellen, der sicher aufbewahrt werden muss. Das DEK-Startpasswort muss der Benutzer des Clients als Erstes in ein sicheres Passwort ändern.

Wird eine selbstverschlüsselnde Festplatte repariert oder soll sie verkauft bzw. entsorgt werden, so muss sichergestellt sein, dass sich von ihr keine schützenswerten Informationen entnehmen lassen. Dazu sollte vor Reparatur, Verkauf oder Entsorgung der DEK neu generiert oder ein Löschbefehl "ATA Secure Erase" ausgeführt werden. 

#### SYS.2.1.M29 Systemüberwachung(A)

Um auf kritische Systemereignisse reagieren zu können, sollte für Clients ein geeignetes Systemüberwachungs- bzw. Monitoringkonzept erstellt werden. Dazu gehört, dass Systemzustand und Funktionsfähigkeit der Clients laufend überwacht werden. Wenn Fehler auftreten oder definierte Grenzwerte über- oder unterschritten werden, sollte dies automatisch an das Betriebspersonal gemeldet werden. 

Hierfür werden in der Regel Statusinformationen von einem zentralen IT-System abgerufen, auf dem die Ereignisse ausgewertet werden. Über die Schnittstelle, die benötigt wird, um die Systemereignisse vom IT-System abzurufen, können aber oft Systemeinstellungen des Betriebssystems verändert werden, z. B. über SNMP (Simple Network Management Protocol). Ist eine solche Modifikation nicht gewünscht, dann sollten diese Merkmale deaktiviert werden. 

#### SYS.2.1.M30 Einrichten einer Referenzinstallation für Clients(CIA)

Es wird empfohlen, für Clients eine Referenzinstallation zu erstellen, in der die Grundkonfiguration und alle Konfigurationsänderungen, Updates und Patches vor dem Einspielen auf den Clients bei den Anwendern vorab getestet werden können. Dies betrifft die Grundeinstellungen des IT-Systems, Sicherheitspatches und -updates und auch normale Updates, die vom Hersteller herausgegeben werden.

Darüber hinaus kann eine solche Referenzinstallation gegebenenfalls auch dazu genutzt werden, die Installation oder das Wiederaufsetzen von Clients zu vereinfachen, indem eine entsprechend vorkonfigurierte Installation auf geeignete Art und Weise auf den zu installierenden Client überspielt wird ("klonen"). Im Idealfall brauchen anschließend nur noch wenige Einstellungen angepasst zu werden. Eine Referenzinstallation, die zum Klonen von Clients verwendet wird, muss mit besonderer Sorgfalt konfiguriert und getestet werden.

Die Referenzinstallation muss so beschaffen sein, dass die wesentlichen Parameter der Hard- und Softwareplattform für alle IT-Systeme, die von dieser Referenzinstallation abgeleitet werden, dieselben sind. Dies bedeutet nicht notwendigerweise, dass deswegen auf sämtlichen Clients eine identische Hard- und Softwarekonfiguration bestehen muss. Die Konfiguration verschiedener Clients muss aber hinreichend ähnlich sein, damit der Referenzcharakter der Installation erhalten bleibt.

Bei Tests von Anwendungsprogrammen und Einstellungen, die die Anwender auf den Clients betreffen, ist es darüber hinaus besonders wichtig, dass der IT-Betrieb diese nicht mit Administratorrechten durchführen, sondern unter einer Benutzerkennung, der dieselben Berechtigungen besitzt und für den dieselben Einstellungen für die Benutzerumgebung gewählt wurden, wie die Anwender, die mit dem IT-System arbeiten sollen.

Gegebenenfalls kann es vorteilhaft sein, für verschiedene Arten von Tests unterschiedliche Testsysteme zu nutzen, etwa ein oder mehrere IT-Systeme für Tests von Gerätetreibern oder systemnaher Programme und von Betriebssystempatches, und ein anderes für Tests im Zusammenhang mit Anwendungsprogrammen. In einem solchen Fall ist es jedoch wichtig, sich bewusst zu sein, dass auf diese Weise gewisse Arten von Wechselwirkungen zwischen Betriebssystemumgebung und Anwendungsprogrammen nicht abgedeckt werden können. Bei besonderen Anforderungen an die Sicherheit der Clients kann es deswegen erforderlich werden, tatsächlich für bestimmte Einsatzszenarien nur identisch ausgestattete und konfigurierte IT-Systeme einzusetzen.

Für verschiedene typische und häufiger wiederkehrende Testfälle sollten Checklisten erstellt werden, die beim Testen abgearbeitet werden können und die neben der reinen Dokumentation des Tests oft auch zu einer Erhöhung der Effizienz und zur Vermeidung von Fehlern beitragen können.

Alle Tests sollten so dokumentiert werden, dass sie zu einem späteren Zeitpunkt nachvollzogen werden können. Dies ist insbesondere bei Tests von Sicherheitsupdates und von neuen Gerätetreibern notwendig, bei denen eine fehlerhafte Konfiguration oder ein Fehlschlagen der Installation dazu führen kann, dass die betroffenen Clients keinen Zugang mehr zum Netz erhalten oder gar überhaupt nicht mehr starten. Gerade in solchen Fällen kann eine aussagekräftige Dokumentation die notwendige Zeit für die Fehlersuche und -beseitigung wesentlich verkürzen. 

#### SYS.2.1.M31 Einrichtung lokaler Paketfilter(CIA)

Das gesamte Netz einer Institution sollte durch ein entsprechendes Sicherheitsgateway geschützt sein. Zusätzlich ist es empfehlenswert, auch auf jedem Client entsprechende Zugriffsbeschränkungen auf Anwendungs- oder Netzebene einzurichten. 

Ein lokaler Paketfilter kann einen Client gegen Angriffe schützen, die aus demselben Subnetz heraus gestartet werden. Außerdem kann ein solcher Paketfilter dazu benutzt werden, eine feiner abgestufte Zugriffskontrolle für einzelne Dienste zu realisieren, als dies beispielsweise mit Paketfiltern nur an Netzübergängen möglich ist.

Darüber hinaus kann ein lokaler Paketfilter auch dazu benutzt werden, ausgehende Netzverbindungen zu beschränken und so die Folgen einer Kompromittierung der IT-Systeme zu begrenzen. Ein solcher Schutz kann zwar eventuell von einem Angreifer nach einer erfolgreichen Kompromittierung des Clients deaktiviert werden, andererseits wird ein Angreifer auf diese Weise zumindest behindert. Auf diese Weise kann entscheidende Zeit bei der Entdeckung und für mögliche Reaktionen gewonnen werden.

Zuletzt kann die Protokollfunktion eines lokalen Paketfilters es ermöglichen, bestimmte Angriffe überhaupt zu entdecken.

Praktisch alle aktuellen Betriebssysteme bieten die Möglichkeit, Filter zu definieren, die alle empfangenen oder zu sendenden Pakete nach bestimmten Regeln untersuchen und behandeln. Die Filtermöglichkeiten unterscheiden sich dabei zwischen den einzelnen Betriebssystemen teilweise erheblich. Praktisch immer können jedoch Regeln basierend auf der Quell- und Zieladresse des Pakets sowie auf dem verwendeten Protokolltyp (TCP/IP, UDP/IP, ICMP etc.) sowie gegebenenfalls dem Quell- oder Zielport definiert werden. Mit Hilfe von Paketfilterregeln können so beispielsweise Pakete, die von bestimmten IT-Systemen oder aus bestimmten Subnetzen stammen, gezielt verworfen werden.

Manche Anwendungen besitzen eigene Mechanismen, um den Zugriff auf den Dienst für einzelne IP-Adressen oder Adressbereiche zu erlauben oder zu verbieten. Gegenüber diesen Mechanismen hat ein lokaler Paketfilter auf Betriebssystemebene den Vorteil, dass er den Dienst selbst gegen mögliche Angriffe schützt, die zu einer Kompromittierung führen, bevor die eingebaute Zugriffsbeschränkung überhaupt wirksam werden kann.

Es gibt zwei allgemeine Strategien, mit der Paketfilter-Regeln implementiert werden können: Die Blacklist-Strategie erlaubt alle Arten von Verbindungen, die nicht bestimmte Ausschlusskriterien erfüllen (Freizügige Strategie: "Alles ist erlaubt, was nicht explizit verboten ist"). Der Vorteil liegt dabei in einem eventuell geringeren Aufwand bei der Administration und der Fehlersuche. Ein schwerwiegender Nachteil ist jedoch, dass vergessene Regeln, die den Zugriff auf nicht geschützte Netzdienste ermöglichen, als Grundlage für einen Angriff dienen können.

Demgegenüber werden bei der Whitelist-Strategie alle Arten von Verbindungen blockiert, die nicht zu einer Liste erlaubter Dienste gehören (Restriktive Strategie: "Alles ist verboten, was nicht explizit erlaubt ist").

Die Whitelist-Strategie bietet die größere Sicherheit und sollte daher grundsätzlich verwendet werden, wenn nicht wichtige Gründe dagegen sprechen. Der Nachteil liegt in einem tendenziell höheren Administrationsaufwand, da bei jeder Änderung der Anforderungen neue Regeln definiert werden müssen. In Ausnahmefällen, beispielsweise wenn ein Protokoll nicht auf fest definierten Ports arbeitet, kann auf die Blacklist-Strategie zurückgegriffen werden.

Es ist empfehlenswert, auf Clients, die besondere Anforderungen an die Sicherheit stellen, im Rahmen der Grundkonfiguration einen lokalen Paketfilter mit einem Basis-Regelwerk einzurichten, bei dem grundsätzlich alle Verbindungsanfragen von außen abgewiesen werden. Dieses Regelwerk sollte aktiv sein, wenn der Client ans Netz angeschlossen wird. Je nachdem, welche Dienste von dem Client genutzt werden sollen, können nach deren Konfiguration die dafür benötigten Protokolle und Ports freigeschaltet werden. 

Paketfilter erlauben meist ein detailliertes Protokollieren des Netzverkehrs. Das Aufsetzen eines lokalen Paketfilters ist daher auch in sicheren Netzen, die mit einem Sicherheitsgateway von einem unsicheren Netz wie dem Internet getrennt sind, sinnvoll, denn gewonnen Informationen können für die Erkennung von Angriffen hilfreich sein. Allerdings muss dabei darauf geachtet werden, dass keine Datenschutzbestimmungen verletzt werden. Gegebenenfalls sollten die entsprechenden Stellen (Datenschutzbeauftragter, Personalvertretung oder andere) beteiligt werden.

**Problem ICMP**

Das Internet Control Message Protocol ICMP wird dazu verwendet, Nachrichten über Fehler bei der Übertragung von IP-Paketen zu übermitteln. Beispielsweise existieren Nachrichten, die dem Sender eines Pakets mitteilen, dass das Zielnetz nicht erreichbar ist oder dass das Paket zu groß war, um an das Zielsystem weitergeleitet zu werden. Die Funktion der Tools ping und traceroute beruhen ebenfalls auf ICMP.

Neben vielen nützlichen Eigenschaften gibt es jedoch einige ICMP-Nachrichtentypen, mit denen Angreifer sich wichtige Informationen über ein Netz verschaffen und diese direkt für Angriffe benutzen können. Leider ist der radikale Ansatz, ICMP grundsätzlich am Sicherheitsgateway zu blockieren, ebenfalls keine befriedigende Lösung, da bestimmte Funktionen dann nicht mehr verfügbar sind. Auf ping und traceroute kann zwar in der Regel auf normalen Arbeitsplatzrechnern und Servern verzichtet werden, eine globale Blockierung von ICMP kann aber zu Beeinträchtigungen führen, die schwer zu diagnostizieren sind. Daher sollte überlegt werden sowohl am Sicherheitsgateway, als auch beim lokalen Paketfilter eine selektive ICMP-Filterung vorzunehmen, sofern dieser die entsprechenden Möglichkeiten zur Verfügung stellt. Dies sollte stets unter der Berücksichtigung des Einsatzzweckes des Clients, dessen Schutzbedarfs und die am Sicherheitsgateway getroffenen Maßnahmen geschehen. Beispielsweise kann für das interne Netz eine größere Zahl von Nachrichtentypen zugelassen werden, als für das externe Netz.

**Umsetzung und Überprüfung**

Welche Möglichkeiten der Filterung und Protokollierung zur Verfügung stehen, unterscheidet sich je nach Betriebssystem. Vor dem Aufsetzen eines lokalen Paketfilters sollte die vorhandene Dokumentation zu Rate gezogen werden.

Bei der Einrichtung von Paketfilterregeln sollte mit großer Sorgfalt vorgegangen werden, da ein Fehler in einer Regel unter Umständen dazu führen kann, dass sich ein Administrator, der über das Netz auf dem Client arbeitet, auf diese Weise "aussperrt" und die Korrekturen von der Systemkonsole aus vornehmen muss.

Nach dem Aktivieren des lokalen Paketfilters sollte einerseits geprüft werden, ob die benötigten Dienste noch erreichbar sind, andererseits sollte mit einem Portscan überprüft werden, ob die restlichen Ports alle blockiert sind.

#### SYS.2.1.M32 Einsatz zusätzlicher Maßnahmen zum Schutz vor Exploits(CIA)

Je nachdem, welche Sicherheitsanforderungen an ein IT-System gestellt werden, reichen eventuell die vorhandenen Sicherheitsfunktionalitäten nicht aus, so dass zusätzlich geeignete Sicherheitsprodukte eingesetzt werden sollten. Typische Beispiele dafür sind Zugangskontrolle, Zugriffsrechteverwaltung und -prüfung, Protokollierung oder Verschlüsselung.

Bei IT-Systemen muss beispielsweise sichergestellt werden, dass

* nur autorisierte Personen das IT-System benutzen können. Hierfür sind geeignete Authentisierungsmechanismen auszuwählen.
* die Benutzer auf die Daten nur in der Weise zugreifen können, die sie zur Aufgabenerfüllung benötigen. Hierbei unterstützen geeignete Benutzertrennung und Rechtevergabe.
* Unregelmäßigkeiten und Manipulationsversuche erkennbar werden. Hierbei helfen Protokollierungsfunktionen, Verschlüsselung und digitale Signatur.
* Daten gegen zufällige Zerstörung oder Verlust geschützt sind (Verfügbarkeitskontrolle). Hierbei unterstützen beispielsweise Backup-Programme.
Reichen die Protokollierungsmöglichkeiten des IT-Systems nicht aus, um eine ausreichende Beweissicherung zu gewährleisten, so müssen diese nachgerüstet werden. Hierzu gibt es auch verschiedene Gesetze, die dies erfordern. Beispielsweise ist nach BDSG bei der Eingabekontrolle "zu gewährleisten, dass nachträglich überprüft und festgestellt werden kann, ob und von wem personenbezogene Daten in Datenverarbeitungssysteme eingegeben, verändert oder entfernt worden sind".

Ist es mit dem IT-System nicht möglich, den Administrator daran zu hindern, auf bestimmte Daten zuzugreifen oder zumindest diesen Zugriff zu protokollieren und zu kontrollieren, dann kann z. B. mit einer Verschlüsselung der Daten verhindert werden, dass der Administrator diese Daten im Klartext liest, wenn er nicht im Besitz des zugehörigen Schlüssels ist.

**Empfohlene Mindestfunktionalitäten**

IT-Systeme sollten mindestens die folgenden Sicherheitseigenschaften besitzen. Wenn diese nicht im Standardumfang vorhanden sind, sollten diese über zusätzliche Sicherheitsprodukte nachgerüstet werden.

* Identifikation und Authentisierung: Es sollte eine Sperre des IT-Systems nach einer vorgegebenen Anzahl fehlerhafter Authentisierungsversuche stattfinden, die nur der IT-Betrieb zurücksetzen kann. Wird ein Passwort verwendet, sollte das Passwort mindestens acht Stellen umfassen und dürfen nicht unverschlüsselt in den IT-Systemen gespeichert werden.
* Rechteverwaltung und -kontrolle: Es sollte eine Rechteverwaltung und -kontrolle auf Festplatten und Dateien vorhanden sein, wobei zumindest zwischen lesendem und schreibendem Zugriff unterschieden werden soll. Für Benutzer sollte kein Systemzugriff auf Betriebssystemebene möglich sein.
* Rollentrennung zwischen Administrator und Benutzer: Es sollte eine klare Trennung zwischen Administrator und Benutzer möglich sein, wobei nur der Administrator Rechte zuweisen oder entziehen können sollte.
* Protokollierung der Vorgänge Anmelden, Abmelden und Rechteverletzung sollte möglich sein.
Sollte ein oder mehrere dieser Sicherheitsfunktionalitäten nicht vom Betriebssystem unterstützt werden, so müssen ersatzweise geeignete zusätzliche Sicherheitsprodukte eingesetzt werden.

Zusätzliche Forderungen an Sicherheitsprodukte:

* Benutzerfreundliche Oberfläche zur Erhöhung der Akzeptanz.
* Aussagekräftige und nachvollziehbare Dokumentation für IT-Betrieb und Benutzer.
Wünschenswerte Zusatzfunktionalität von Sicherheitsprodukten:

* Rollentrennung zwischen Administrator, Revisor und Benutzer; nur der Administrator kann Rechte zuweisen oder entziehen und nur der Revisor hat Zugriff auf die Protokolldaten,
* Protokollierung von Administrationstätigkeiten,
* Unterstützung der Protokollauswertung durch konfigurierbare Filterfunktionen,
* Verschlüsselung der Datenbestände mit einem geeigneten Verschlüsselungsalgorithmus und in einer Weise, dass ein Datenverlust bei Fehlfunktion (Stromausfall, Abbruch des Vorgangs) systemseitig abgefangen wird.
Die Realisierung dieser Funktionalität kann sowohl in Hardware wie auch in Software erfolgen. Bei der Neubeschaffung eines Produktes sollte der Baustein OPS.1.2.6 Beschaffung, Ausschreibung und Einkauf berücksichtigt werden.

**Übergangslösung**

Sollte es nicht möglich sein, kurzfristig ein geeignetes Sicherheitsprodukt zu beschaffen, sind andere geeignete Sicherheitsmaßnahmen zu ergreifen. Diese sind dann typischerweise organisatorischer Natur und müssen von den Benutzern konsequent eingehalten werden. Wenn ein IT-System beispielsweise keine Bildschirmsperre hat, muss dieses in den kurzen Phasen, wo es nicht benutzt wird, ein- oder weggeschlossen werden.

#### SYS.2.1.M33 Application Whitelisting(CIA)

Grundsätzlich müssen Clients nur Anwendungen ausführen können, die dafür notwendig sind, dass die angebotenen Dienste funktionieren. Entsprechende Whitelist-Lösungen können sicherstellen, dass nur erlaubte Programme ausgeführt werden können. Es gibt hier betriebssystemeigene Mechanismen und Lösungen von Drittanbietern, die zur Umsetzung von Whitelisting infrage kommen.

Ein einfacher Ansatz ist pfadbasiertes Application Whitelisting für vollständige Pfade, bei dem z. B. Programmverzeichnisse oder Verzeichnisse mit Betriebssystemdateien erlaubt werden. So kann verhindert werden, dass etwa ein Schadprogramm aus dem Browser-Cache oder einem temporären Ordner heraus ausgeführt wird.

Alternativ kann explizit einzelnen Anwendungen die Ausführung gestattet werden. Dieser Ansatz erhöht die Sicherheit zusätzlich, da nur vorab festgelegte Anwendungen gestartet werden können. Gleichzeitig erhöht sich aber auch der Aufwand, da z. B. sichergestellt werden muss, dass alle nötigen Betriebssystemkomponenten ausgeführt werden können. Auch bei Updates ist zusätzlicher Aufwand nötig, um geänderte Programme in der Whitelist nachzupflegen.

Bei Whitelisting ist zu beachten, dass z.B. auch Skripte nicht ausgeführt werden dürfen. 

#### SYS.2.1.M34 Einsatz von Anwendungsisolation(CIA)

Die verschiedenen Betriebssysteme bieten unterschiedliche Möglichkeiten, um Anwendungen zu isolieren. Hierzu zählen Container-Lösungen wie AppContainer (Windows), Linux Containers (LXC) oder Docker wie auch mit den Betriebssystemen mitgelieferte Virtualisierungslösungen wie Hyper-V (Windows), KVM/Xen (Linux), VMware Workstation oder Virtualbox. Darüber hinaus können spezialisierte Lösungen von Drittherstellern genutzt werden. Dies hat den Vorteil, dass Anwendungen, mit denen Internetinhalte oder Daten von externen Stellen geöffnet werden, einen deutlichen Sicherheitsgewinn durch eine Isolation erhalten können. Dies umfasst z. B. Webbrowser, Office-Anwendungen, E-Mail-Programme und PDF-Betrachter.

#### SYS.2.1.M35 Aktive Verwaltung der Wurzelzertifikate(CI)

Weitere Informationen zur Verwaltung von Wurzelzertifikaten befinden sich in den folgenden Dokumenten:

* Windows: Configure Trusted Roots and Disallowed Certificates [MSROOT
* Mozilla: CA:Root Change Process [MOZRCP]
* Java: keytool - Key and Certificate Management Tool [KEYTOOL]
* OpenSSL: Certificate Installation with OpenSSL [OPENSSL]
* GnuPG: Agent Configuration - Using the GNU Privacy [GNUPG]
#### SYS.2.1.M36 Selbstverwalteter Einsatz von SecureBoot und TPM

Auf UEFI-kompatiblen Systemen sollten Bootloader, Kernel sowie alle benötigten Firmware-Komponenten durch selbstkontrolliertes Schlüsselmaterial signiert und nicht benötigtes Schlüsselmaterial entfernt werden. Sofern das TPM nicht benötigt wird, sollte es deaktiviert werden.

#### SYS.2.1.M37 Schutz vor unbefugten Anmeldungen (CIA)

Um einen Zugang zum System durch kompromittierte Anmeldeinformationen zu verhindern, sollte eine Mehrfaktorauthentisierung verwendet werden.

#### SYS.2.1.M38 Einbindung in die Notfallplanung(A)

Im Rahmen der Notfallvorsorge ist ein Konzept zu entwerfen, wie die Folgen eines Ausfalls minimiert werden können und welche Aktivitäten im Falle eines Ausfalls durchzuführen sind.

Folgende Aspekte müssen dabei berücksichtigt werden:

* Die Notfallplanung für die Clients sollte in den existierenden Notfallplan integriert werden (siehe auch Baustein DER.4 Notfallmanagement).
* Durch einen Systemausfall können Daten verloren gehen. Daher ist im Rahmen des allgemeinen Datensicherungskonzepts (siehe auch OPS.1.1.5 Datensicherung) ein Datensicherungskonzept für die Clients zu erstellen.
* Im Rahmen von Wartungs- und Serviceverträgen oder durch eigene Lagerhaltung muss die Versorgung mit Ersatzteilen innerhalb einer Frist sichergestellt werden. 
* Die Systemkonfiguration muss dokumentiert werden. Wichtige Aufgaben müssen so beschrieben sein, dass das Gesamtsystem im Notfall auch ohne vorherige Kenntnis dieser Systemkonfiguration wiederhergestellt werden kann. 
**Erstellen eines Notfall-Bootmediums**

Wird ein Client eingerichtet, sollte direkt ein Bootmedium erstellt werden. Auf diese Weise kann das IT-System gestartet werden, wenn eine Festplatte ausfällt, außerdem kann es genutzt werden, um einen kontrollierten Systemzustand wieder herzustellen, nachdem z.B. ein Schadprogramm aufgetreten ist. Solche Medien können beispielsweise DVDs sein, die vom jeweiligen Betriebssystem erstellt werden, es können aber auch eigens eingerichtete DVDs oder portable Laufwerke (beispielsweise USB-Sticks oder externe Festplatten) erstellt werden. Art und Umfang des Notfall-Bootmediums richten sich nach dem Einsatzzweck des Clients und den vorhandenen Schnittstellen.

Das Notfall-Bootmedium kann unter anderem bei folgenden Problemen eingesetzt werden:

* Datenverlust durch Fehlbedienung,
* Bedienungs- und Administrationsfehler, die die Benutzung und einen Neustart verhindern,
* Infektion des IT-Systems mit Schadprogrammen (beispielsweise Computer-Viren),
* Kompromittierung des IT-Systems durch einen Angreifer, oder auch
* Hardware-Probleme.
Idealerweise sollte das Notfall-Bootmedium alle Programme und Daten enthalten, die benötigt werden, um das IT-System untersuchen und um Probleme beseitigen zu können. Gegebenenfalls können unterschiedliche Medien für verschiedene Problemszenarien erstellt werden.

Als "Grundausstattung" für ein Notfall-Bootmedium werden folgende Programme empfohlen:

* Viren-Schutzprogramme mit aktuellen Signaturen,
* Programme zur Bearbeitung von Konfigurationsdateien oder Datenbanken des IT-Systems (Editoren für Dateien, Registry oder ähnliches),
* Programme zur Wiederherstellung von Datenstrukturen der Systemfestplatte wie Bootsektor und MBR (Master Boot Record) oder GPT (GUID Partition Table),
* Backup- / Recovery-Programme,
* Diagnoseprogramme zur Analyse von Hardware-Defekten.
Darüber hinaus können Programme zur weitergehenden Analyse hinzugefügt werden, etwa um kompromittierte IT-System forensisch zu untersuchen.

Dabei ist es wichtig, dass alle Programme und Bibliotheken ausschließlich vom Bootmedium geladen werden. Es dürfen keine Komponenten des installierten IT-Systems verwendet werden. Wird ein Bootmedium erstellt, istaußerdem darauf zu achten, dass neben den notwendigen Programmen auch alle Treiber vorhanden sind, die für den Zugriff auf die eingebauten Platten des Clients benötigt werden. Dazu zählen beispielsweise Treiber für Festplattencontroller (insbesondere RAID-Controller) und Treiber für eine Festplattenverschlüsselung oder Festplattenkomprimierung.

Falls das Bootmedium genügend Speicherplatz bietet, können weitere Programme oder Dokumentation auf dem Medium gespeichert werden. Beispielsweise kann es die Effizienz der Fehlersuche erhöhen, wenn auf dem Bootmedium stets eine aktuelle Dokumentation der Systemkonfiguration enthalten ist.

Das Notfall-Bootmedium muss selbst frei von Viren und anderen Schadprogrammen sein. Es dürfen deshalb nur Programme eingesetzt werden, die aus vertrauenswürdigen Quellen (etwa direkt von der CD/DVD des Herstellers) stammen oder deren digitale Signatur überprüft wurde. Nachdem das Bootmedium erstellt und nachdem es geändert wurde, sollte es außerdem mit einem Viren-Schutzprogramm überprüft werden.

Es ist nicht unbedingt notwendig, für jedes IT-System ein eigenes Bootmedium zu erstellen. Ein entsprechend flexibel angelegtes Bootmedium kann für eine große Anzahl verschiedener IT-Systeme ausreichend sein. Auf dem Bootmedium braucht nicht einmal notwendigerweise dasselbe Betriebssystem eingesetzt zu werden, wie auf dem Zielsystem selbst. Aus Gründen der Kompatibilität ist dies jedoch oft vorteilhaft. Es muss allerdings unbedingt durch entsprechende Tests sichergestellt werden, dass das Medium auch wirklich bei allen Clients funktioniert, für die es eingesetzt werden soll. Je nach Betriebssystem müssen außerdem noch systemspezifische Aspekte beachtet werden, die in den jeweiligen IT-Grundschutz-Bausteinen beschrieben werden.

Wurde das Zielsystem verändert, etwa nach einem Update des Betriebssystems oder Konfigurationsänderungen, muss gegebenenfalls das Notfall-Bootmedium und die darauf gespeicherte Dokumentation aktualisiert werden. Wird das Bootmedium geändert, muss dies dokumentiert werden.

Das Notfall-Bootmedium muss für die Systembetreuer schnell greifbar sein, damit im Falle einer Störung nicht wertvolle Zeit verloren geht. Andererseits muss es auch so sicher aufbewahrt werden, dass Unbefugte keinen Zugriff darauf haben.

Die Funktion des Notfall-Bootmediums sollte regelmäßig getestet und die Bedienung der darauf gespeicherten Programme geübt werden, damit sichergestellt ist, dass das Medium im Fall von Problemen funktioniert und der IT-Betrieb mit der Bedienung vertraut sind. Es sollte überlegt werden, mit dem Medium eine kurze gedruckte Anleitung aufzubewahren, die für typische Einsatzszenarien die wichtigsten Schritte zusammenfasst.

#### SYS.2.1.M39 Unterbrechungsfreie und stabile Stromversorgung [Haustechnik](A)

Wenn es bei Clients erhöhte Anforderungen an die Verfügbarkeit gibt, sollten diese an eine unterbrechungsfreie Stromversorgung (USV) angeschlossen werden, damit Stromausfälle solange überbrückt werden können, bis entweder die (Ersatz-) Energieversorgung wieder sichergestellt ist oder die Clients geordnet heruntergefahren sind. Vertiefende Informationen zu einer unterbrechungsfreien und stabilen Stromversorgung sind in dem Baustein und den Umsetzungshinweisen zum SYS.1.1 Allgemeiner Server zu finden.

#### SYS.2.1.M40 Betriebsdokumentation

Um einen reibungslosen Betriebsablauf zu gewährleisten, müssen Administratoren einen Überblick über die IT-Systeme haben bzw. sich verschaffen können. Dieses muss auch für deren Vertreter möglich sein, falls ein Administrator unvorhergesehen ausfällt. Der Überblick wird oft vorausgesetzt, um die IT-Systeme (z. B. auf problematische Einstellungen, Konsistenz bei Änderungen) prüfen zu können.

Daher sollten die Veränderungen, die Administratoren an den IT-Systemen vornehmen, dokumentiert werden, nach Möglichkeit automatisiert. Dieses gilt insbesondere für Änderungen an Systemverzeichnissen und -dateien.

Bei Installation neuer Betriebssysteme oder bei Updates sind die vorgenommenen Änderungen besonders sorgfältig zu dokumentieren. Indem neue Systemparameter aktiviert oder bestehende geändert werden, kann das Verhalten eines IT-Systems (insbesondere auch Sicherheitsfunktionen) maßgeblich verändert werden.

#### SYS.2.1.M41 Verhinderung der Überlastung der lokalen Festplatte

Es sollte überlegt werden, Quotas einzurichten. Alternativ sollten Mechanismen des verwendeten Datei- oder Betriebssystemsystems genutzt werden, die die Benutzer bei einem bestimmten Füllstand der Festplatte warnen oder nur noch dem Systemadministrator Schreibrechte einräumen.

3 Weiterführende Informationen
------------------------------

### 3.1 Wissenswertes

Hier werden ergänzende Informationen aufgeführt, die im Rahmen der Maßnahmen keinen Platz finden, aber dennoch beachtenswert sind. Derzeit liegen für diesen Baustein keine entsprechenden Informationen vor. Sachdienliche Hinweise nimmt die IT-Grundschutz-Hotline gerne unter grundschutz@bsi.bund.de entgegen.

### 3.2 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Allgemeiner Client" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [GNUPG] Using the GNU Privacy Guard

  

 Agent Configuration, (zuletzt abgerufen 05.10.2017)  
 <https://www.gnupg.org/documentation/manuals/gnupg/Agent-Configuration.html>

 
* #### [ISiClient] Absicherung eines PC-Clients (ISi-Client),

  

 (zuletzt abgerufen am 27.09.2017)  
 [https://www.bsi.bund.de/DE/Themen/StandardsKriterien/Isi-Reihe/Isi-Client/client\_node.html](https://www.bsi.bund.de/DE/Themen/StandardsKriterien/Isi-Reihe/Isi-Client/client_node.html)

 
* #### [KEYTOOL] Key and Certificate Management Tool

  

 Oracle, (zuletzt abgerufen 05.10.2017)  
 <https://docs.oracle.com/javase/6/docs/technotes/tools/windows/keytool.html>

 
* #### [MIGLFTLS] Migrationsleitfaden zum Mindeststandard TLS 1.2

  

 Bundesamt für Sicherheit in der Informationstechnik, Stand 2015  
 [https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Migrationsleitfaden\_Mindeststandard\_BSI\_TLS\_1\_2\_Version\_1\_2.pdf](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Mindeststandards/Migrationsleitfaden_Mindeststandard_BSI_TLS_1_2_Version_1_2.pdf)

 
* #### [MOZRCP] Mozilla CA: Root Change Prozess

  

 Mozilla Wiki, (zuletzt abgerufen 05.10.2017)  
 [https://wiki.mozilla.org/CA:Root\_Change\_Process](https://wiki.mozilla.org/CA:Root_Change_Process)

 
* #### [MSROOT] Configure Trusted Roots and Disallowed Certificates

  

 Configure Trusted Roots and Disallowed Certificates, (zuletzt abgerufen 05.10.2017)  
 <https://technet.microsoft.com/en-us/library/dn265983(v=ws.11).aspx>

 
* #### [NIST800111] NIST Special Publication 800-111

  

 Guide to Storage Encryption Technologies for End User Devices, 2007  
 <http://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-111.pdf>

 
* #### [NISTSP800123] NIST Special Publication 800-123

  

 Guide to General Server Security, NIST, 07.2008  
 <https://csrc.nist.gov/publications/nistpubs/800-123/SP800-123.pdf> 

 
* #### [OPENSSL] Certificate Installation with OpenSSL- Other People´s Certificates

  

 (zuletzt abgerufen 05.10.2017)  
 <http://gagravarr.org/writing/opensslcerts/other.shtml>

 
* #### [RFC5246] RFC 5246, The Transport Layer Security (TLS) Protocol

  

 Internet Engineering Task Force (IETF), (zuletzt aufgerufen 05.10.2017)  
 <https://tools.ietf.org/html/rfc5>

 
* #### [RFC5746] RFC 5746, Transport Layer Security (TLS) Renegotiation Indication Extension

  

 Internet Engineering Task Force (IETF), (zuletzt abgerufen 05.10.2017)  
 <https://tools.ietf.org/html/rfc5746>

 
* #### [TR02102] Kryptographische Verfahren- Empfehlungen und Schlüssellängen

  

 BSI, (zuletzt abgerufen am 27.09.2017)   
 [https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index\_htm.html](https://www.bsi.bund.de/DE/Publikationen/TechnischeRichtlinien/tr02102/index_htm.html)

 
