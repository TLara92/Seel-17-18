1 Beschreibung
--------------

### 1.1 Einleitung

Um Schäden zu begrenzen und um weitere Schäden zu vermeiden, müssen erkannte Sicherheitsvorfälle schnell und effizient bearbeitet werden. Dafür ist es notwendig, ein vorgegebenes und erprobtes Verfahren zur Behandlung von Sicherheitsvorfällen (*Security Incident Handling oder auch Security Incident Response) *zu etablieren.

Ein Sicherheitsvorfall kann sich sehr stark auf eine Institution auswirken und große Schäden nach sich ziehen. Solche Vorfälle sind beispielsweise Fehlkonfigurationen, die dazu führen, dass vertrauliche Informationen offengelegt werden oder kriminelle Handlungen, z. B. Hacking von Servern, Diebstahl von vertraulichen Informationen, Sabotage oder Erpressung mit IT-Bezug.

Die Ursachen für Sicherheitsvorfälle sind vielfältig: So spielen unter anderem Malware, veraltete Systeminfrastrukturen oder Innentäter eine Rolle. Angreifer nutzen aber auch oft Zero-Day-Exploits aus. Eine weitere erst zunehmende Gefährdung sind sogenannte Advanced Persistent Threats (APT). 

Außerdem könnten sich Benutzer, Administratoren oder externe Dienstleister nicht korrekt verhalten, sodass Systemparameter sicherheitskritisch geändert werden oder dass gegen interne Richtlinien verstoßen wird. Weiter ist als Ursache denkbar, dass Zugriffsrechte verletzt werden, dass Software, Hardware geändert oder schutzbedürftiger Räume und Gebäude unzureichend gesichert werden.

### 1.2 Zielsetzung

Ziel dieses Bausteins ist es, einen systematischen Weg aufzuzeigen, wie ein Konzept zur Behandlung von Sicherheitsvorfällen erstellt werden kann. 

### 1.3 Abgrenzung

Der Fokus dieses Bausteins liegt auf der Behandlung von Sicherheitsvorfällen aus Sicht der Informationstechnik. Bevor Sicherheitsvorfälle behandelt werden können, müssen sie jedoch detektiert werden. Sicherheitsanforderungen dazu sind im Baustein DER.1 *Detektion von sicherheitsrelevanten Ereignissen* enthalten und werden im vorliegenden Baustein vorausgesetzt. Die initiale forensische Untersuchung wird im Baustein DER.2.2 *Forensik* und die Bereinigung nach einem APT-Vorfall im Baustein DER.2.3 *Bereinigung weit­reichender Sicherheitsvorfälle (APT-Responder)* behandelt. Ein besonderer Bereich der Behandlung von Sicherheitsvorfällen ist das Notfallmanagement, das im Baustein DER.4 *Notfallmanagement *thematisiert und hier nicht weiter betrachtet wird. Es ist jedoch zu beachten, dass die Entscheidung darüber, ob ein Notfall vorliegt oder nicht, im vorliegenden Baustein getroffen wird.

2 Gefährdungslage
-----------------

Folgende spezifische Bedrohungen und Schwachstellen sind bei der Behandlung von Sicherheitsvorfällen von besonderer Bedeutung:

### 2 1 Ungeeigneter Umgang mit Sicherheitsvorfällen

In der Praxis kann nie ausgeschlossen werden, dass Sicherheitsvorfälle auftreten. Das gilt auch dann, wenn eine Vielzahl von Sicherheitsmaßnahmen umgesetzt ist. Wird auf akute Sicherheitsvorfälle entweder nicht oder nicht angemessen reagiert, können sich daraus große Schäden bis hin zu Katastrophen entwickeln. Beispiele dafür sind:

* In den Protokolldateien einer Firewall finden sich auffällige Einträge. Wird nicht zeitnah untersucht, ob das erste Anzeichen für einen Einbruchsversuch sind, können Angreifer die Firewall mit einem erfolgreichen Angriff unbemerkt überwinden und in das interne Netz der Institution eindringen.
* Es werden Sicherheitslücken in den verwendeten IT-Systemen bzw. Anwendungen bekannt. Werden diese Informationen nicht rechtzeitig beschafft und notwendige Gegenmaßnahmen nicht zügig eingeleitet und umgesetzt, können diese Sicherheitslücken von Angreifern ausgenutzt werden.
Wenn für die Behandlung von Sicherheitsvorfällen keine geeignete Vorgehensweise vorgegeben ist, können in der Eile und unter Stress falsche Entscheidungen getroffen werden. Diese können z. B. dazu führen, dass die Presse falsch informiert und dadurch eine negative Außenwirkung erzielt wird, dass Dritte durch die eigenen IT-Systeme geschädigt werden und Schadenersatz fordern oder dass keinerlei Ausweich- oder Wiederherstellungsmaßnahmen vorgesehen sind und sich somit der Schaden für die Institution deutlich erhöht.

### 2 2 Nicht erkannte Sicherheitsvorfälle

Im täglichen Betrieb einer Institution können viele Störungen und Fehler auftreten. Dabei kann es passieren, dass Sicherheitsvorfälle durch das Personal nicht als solche identifiziert werden und ein Angriff bzw. Angriffsversuch unerkannt bleibt. Auch wenn die Mitarbeiter ausreichend für die Belange der Informationssicherheit sensibilisiert bzw. geschult sind, kann trotzdem nicht ausgeschlossen werden, dass sie Sicherheitsvorfälle nicht erkennen. Beispiele hierfür sind:

* Ein Benutzer, der seit längerer Zeit nicht im lokalen Netz seiner Institution angemeldet war, hält die seit einer Woche auftretende deutliche Verlangsamung seines Notebooks während des Internetzugangs für normal und bemerkt nicht, dass ein Schadprogramm im Hintergrund aktiv ist. Er wurde nicht oder nur unzureichend geschult, bei verdächtigen Auffälligkeiten den Sicherheitsverantwortlichen zu informieren.
* Ein Produktionsleiter bemerkt nicht, dass die Daten in den Produktionssystemen und auch die Steuerungsanzeigesysteme heimlich verändert wurden. Er schöpft keinen Verdacht, als die SCADA-Steuerung der Produktionsanlage seltsame Werte anzeigt, da dies nur kurzzeitig erfolgte. Der Vorfall wird nicht gemeldet, da alle Werte wieder den erwarteten Anzeigewerten entsprechen. Dass eine Schadsoftware die Anzeigewerte manipuliert hat, fällt somit niemandem auf.
* Ein Einbruchsdiebstahl in einer Filiale wird für einen Fall von Beschaffungskriminalität gehalten, da Notebooks und Flachbildschirme entwendet wurden. Der Tatsache, dass sich auf den Notebooks vertrauliche Informationen und Zugangsdaten für IT-Systeme im Intranet befunden haben, wird keine größere Bedeutung beigemessen und der ISB nicht informiert. Auf die nachfolgenden Angriffe auf die IT-Systeme anderer Standorte und der Firmenzentrale ist die Institution daher nicht vorbereitet. Für den Angriff werden die auf den gestohlenen Notebooks gefundenen Daten verwendet.
### 2 3 Zerstörung von Beweisspuren bei der Behandlung von Sicherheitsvorfällen

Wenn bei der Behandlung von Sicherheitsvorfällen unvorsichtig oder nicht nach Vorgaben agiert wird, kann das dazu führen, dass wichtige Beweisspuren für die Aufklärung oder spätere juristische Verfolgung unbeabsichtigt zerstört oder nicht gerichtsverwertbar gemacht werden.

Beispiele hierfür sind:

* Auf einem Arbeitsplatzrechner hat ein Angreifer eine Schadsoftware platziert, deren Arbeitsweise und Ziel nur im laufenden Zustand analysiert werden kann. Dafür müssten Informationen über die aktiven Prozesse und der Inhalt des Hauptspeichers gesichert und ausgewertet werden. Wird der Arbeitsplatzrechner nun voreilig heruntergefahren, können die Informationen aus dem laufenden Zustand nicht mehr für eine Analyse und Aufklärung des Sicherheitsvorfalls herangezogen werden.
* Ein Administrator findet auf einem Server einen laufenden Prozess, der eine überdurchschnittliche CPU-Auslastung verursacht. Zusätzlich erzeugt dieser Prozess temporäre Dateien und versendet unbekannte Informationen über das Internet. Wird der Prozess voreilig beendet und werden die temporären Dateien einfach gelöscht, kann nicht herausgefunden werden, ob vertrauliche Informationen erfolgreich entwendet werden konnten.
* Ein wichtiger Server wird kompromittiert, weil der Administrator durch die starke Arbeitsbelastung und ein fehlendes Wartungsfenster die letzten Sicherheitsupdates nicht wie geplant einspielen konnte. Um möglichen disziplinarischen Konsequenzen zu entgehen, spielt der Administrator die fehlenden Updates ein, bevor ein Sicherheitsteam die Einbruchsursache und den entstandenen Schaden analysieren kann. Mangelnde Fehlerkultur hat somit eine Analyse des Problems verhindert.
3 Anforderungen
---------------

Im Folgenden sind spezifische Anforderungen für den Bereich Behandlung von Sicherheitsvorfällen aufgeführt. Grundsätzlich ist der Informationssicherheitsbeauftragte für die Erfüllung der Anforderungen zuständig. Der Informationssicherheitsbeauftragte (ISB) ist bei strategischen Entscheidungen stets einzubeziehen. Außerdem ist der ISB dafür verantwortlich, dass alle Anforderungen gemäß dem festlegten Sicherheitskonzept erfüllt und überprüft werden. Zusätzlich kann es noch andere Rollen geben, die weitere Verantwortlichkeiten bei der Umsetzung von Anforderungen haben. Diese sind dann jeweils explizit in eckigen Klammern in der Überschrift der jeweiligen Anforderungen aufgeführt.

### 3.1 Basis-Anforderungen

Die folgenden Anforderungen MÜSSEN vorrangig umgesetzt werden:

#### DER.2.1.A1 Definition eines Sicherheitsvorfalls [Leiter IT]

In einer Institution MUSS klar definiert sein, was ein Sicherheitsvorfall ist. Ein Sicherheitsvorfall MUSS so weit wie möglich von Störungen im Tagesbetrieb abgegrenzt sein. Alle am Prozess zur Sicherheitsvorfallbehandlung beteiligten Mitarbeiter MÜSSEN die Definition eines Sicherheitsvorfalls kennen. Die Definition und die Eintrittsschwellen SOLLTEN auf dem Schutzbedarf der betroffenen Geschäftsprozesse, IT-Dienste, IT-Systeme bzw. IT-Anwendungen basieren.

#### DER.2.1.A2 Erstellung einer Richtlinie zur Behandlung von Sicherheitsvorfällen

Es MUSS eine Richtlinie zur Behandlung von Sicherheitsvorfällen erstellt werden. Darin MÜSSEN der Zweck und das Ziel der Richtlinie definiert sowie alle Aspekte der Sicherheitsvorfallbehandlung geregelt werden. So MÜSSEN Verhaltensregeln für die verschiedenen Arten von Sicherheitsvorfällen beschrieben sein. Zusätzlich MUSS es für alle Mitarbeiter zielgruppenorientierte und praktisch anwendbare Handlungsanweisungen geben. Weiterhin SOLLTEN die Schnittstellen zu anderen Managementbereichen berücksichtigt werden, z. B. zum Notfallmanagement.

Die Richtlinie MUSS allen Mitarbeitern bekannt sein. Sie MUSS mit der IT-Leitung oder dem IT-Betrieb abgestimmt und durch die Institutionsleitung verabschiedet sein. Die Richtlinie MUSS regelmäßig geprüft und aktualisiert werden.

#### DER.2.1.A3 Festlegung von Verantwortlichkeiten und Ansprechpartnern bei Sicherheitsvorfällen [Leiter IT]

Es MUSS geregelt werden, wer bei auftretenden Sicherheitsvorfällen für was verantwortlich ist. Für alle Mitarbeiter MÜSSEN die Aufgaben und Kompetenzen bei Sicherheitsvorfällen festgelegt werden. Auch Mitarbeiter, die Sicherheitsvorfälle bearbeiten sollen, MÜSSEN über ihre Aufgaben und Kompetenzen unterrichtet werden. Dabei MUSS geregelt sein, wer die mögliche Entscheidung für eine forensische Untersuchung trifft, nach welchen Kriterien dies vorgenommen wird und wann sie erfolgen soll.

Die Ansprechpartner für alle Arten von Sicherheitsvorfällen MÜSSEN den Mitarbeiten bekannt sein. Kontaktinformationen MÜSSEN immer aktuell sein und in praktikabler Form vorliegen. 

#### DER.2.1.A4 Benachrichtigung betroffener Stellen bei Sicherheitsvorfällen [Leiter IT, Notfallbeauftragter, Pressestelle, Datenschutzbeauftragter, Institutionsleitung]

Von einem Sicherheitsvorfall MÜSSEN alle betroffenen internen und externen Stellen zeitnah informiert werden. Dabei MUSS geprüft werden, ob der Datenschutzbeauftragte, der Betriebsrat/Personalrat sowie Mitarbeiter aus der Rechtsabteilung einbezogen werden müssen. Ebenso MÜSSEN die Meldepflichten für Behörden und regulierte Branchen berücksichtigt werden. Außerdem MUSS gewährleistet sein, dass betroffene Stellen über die erforderlichen Maßnahmen informiert werden.

#### DER.2.1.A5 Behebung von Sicherheitsvorfällen [Leiter IT, IT-Betrieb]

Damit ein Sicherheitsvorfall erfolgreich behoben werden kann, MUSS der Verantwortliche zunächst das Problem eingrenzen und die Ursache finden. Danach MUSS er die erforderlichen Maßnahmen zur Behebung auswählen und sich eine Freigabe vom Leiter IT holen, bevor er sie umsetzt. Anschließend MUSS die Ursache beseitigt und ein sicherer Zustand hergestellt (siehe DER.2.1.A6 *Wiederherstellung der Betriebsumgebung nach Sicherheitsvorfällen*) werden.

Es MUSS eine aktuelle Liste von internen und externen Sicherheitsexperten vorhanden sein, die bei Sicherheitsvorfällen für Fragen aus den verschiedenen erforderlichen Themenbereichen hinzugezogen werden können. Es MÜSSEN sichere Kommunikationsverfahren mit diesen internen und externen Stellen etabliert werden.

#### DER.2.1.A6 Wiederherstellung der Betriebsumgebung nach Sicherheitsvorfällen [Leiter IT, IT-Betrieb]

Um die Auswirkungen der Sicherheitsvorfälle zu beseitigen, MÜSSEN die betroffenen Komponenten vom Netz genommen und alle erforderlichen Daten gesichert werden, die Aufschluss über die Art und Ursache des aufgetretenen Problems geben könnten. Auf allen betroffenen Komponenten MÜSSEN das Betriebssystem und alle Applikationen auf Veränderungen untersucht werden.

Die Originaldaten MÜSSEN von schreibgeschützten Datenträgern wieder eingespielt werden. Dabei MÜSSEN alle sicherheitsrelevanten Konfigurationen und Patches mit aufgespielt werden. Wenn Daten aus Datensicherungen wieder eingespielt werden, MUSS sichergestellt sein, dass diese vom Sicherheitsvorfall nicht betroffen waren. Vor der Wiederinbetriebnahme nach einem Angriff MÜSSEN alle Passwörter auf den betroffenen Komponenten geändert werden. Die betroffenen Komponenten SOLLTEN einem Penetrationstest unterzogen werden, bevor sie wieder eingesetzt werden.

Bei der Wiederherstellung der sicheren Betriebsumgebung MÜSSEN die Benutzer in die Anwendungsfunktionstests einbezogen werden. Nachdem alles wiederhergestellt wurde, MÜSSEN die Komponenten inklusive der Netzübergänge gezielt überwacht werden, um erneute Angriffsversuche feststellen zu können.

Wird auf externe Dienstleister zurückgegriffen, um Störungen zu beheben, MUSS geregelt werden, welche Informationen über den Sicherheitsvorfall wem zugänglich gemacht werden.

### 3.2 Standard-Anforderungen

Gemeinsam mit den Basis-Anforderungen entsprechen die folgenden Anforderungen dem Stand der Technik im Bereich Behandlung von Sicherheitsvorfällen. Sie SOLLTEN grundsätzlich umgesetzt werden.

#### DER.2.1.A7 Etablierung einer Vorgehensweise zur Behandlung von Sicherheitsvorfällen

Damit Institutionen angemessen auf Sicherheitsvorfälle reagieren können, SOLLTE eine geeignete Vorgehensweise zur Behandlung von Sicherheitsvorfällen definiert werden. Die Abläufe, Prozesse und Vorgaben für die verschiedenen Sicherheitsvorfälle SOLLTEN dabei eindeutig geregelt und geeignet dokumentiert werden. Die Institutionsleitung SOLLTE die fertige Vorgehensweise in Kraft setzen und veröffentlichen. Die Vorgehensweise SOLLTE regelmäßig geprüft und aktualisiert werden.

#### DER.2.1.A8 Aufbau von Organisationsstrukturen zur Behandlung von Sicherheitsvorfällen

Für den Umgang mit Sicherheitsvorfällen SOLLTEN geeignete Organisationsstrukturen festgelegt werden. So SOLLTE ein Sicherheitsvorfall-Team aufgebaut werden, dessen Mitglieder je nach Art des Vorfalls einberufen werden können. Auch wenn das Sicherheitsvorfall-Team nur für einen konkreten Sicherheitsvorfall zusammentritt, SOLLTEN bereits im Vorfeld geeignete Mitglieder benannt und in ihre Aufgaben eingewiesen sein. Der Aufbau des Sicherheitsvorfall-Teams SOLLTE regelmäßig aktualisiert werden.

#### DER.2.1.A9 Festlegung von Meldewegen für Sicherheitsvorfälle [Leiter IT]

Für die verschiedenen Arten von Sicherheitsvorfällen SOLLTEN die jeweils passenden Meldewege aufgebaut sein. Es SOLLTE dabei sichergestellt sein, dass Mitarbeiter Sicherheitsvorfälle über verlässliche und vertrauenswürdige Kanäle schnell und einfach melden können.

Wird eine zentrale Anlaufstelle für die Meldung von Störungen oder Sicherheitsvorfällen eingerichtet, SOLLTE auch das an alle Mitarbeiter kommuniziert werden. 

Es SOLLTE eine Kommunikations- und Kontaktstrategie vorliegen. Darin SOLLTE geregelt sein, wer grundsätzlich informiert werden muss und wer informiert werden darf, durch wen das in welcher Reihenfolge erfolgt und in welcher Tiefe informiert wird. Es SOLLTE definiert sein, wer Informationen über Sicherheitsvorfälle an Dritte weitergibt. Ebenso SOLLTE sichergestellt sein, dass keine unautorisierten Personen Informationen über den Sicherheitsvorfall weitergeben.

#### DER.2.1.A10 Eindämmen der Auswirkung von Sicherheitsvorfällen [Notfallbeauftragter, Leiter IT, IT-Betrieb]

Parallel zur Analyse der Ursachen eines Sicherheitsvorfalls SOLLTE entschieden werden, ob es wichtiger ist, den aufgetretenen Schaden einzudämmen oder ihn aufzuklären. Um die Auswirkung eines Sicherheitsvorfalls abschätzbar zu machen, SOLLTEN ausreichend Informationen vorliegen. Für ausgewählte Sicherheitsvorfallsszenarien SOLLTEN bereits im Vorfeld Worst-Case-Betrachtungen durchgeführt werden.

#### DER.2.1.A11 Einstufung von Sicherheitsvorfällen [Leiter IT, IT-Betrieb]

Es SOLLTE ein einheitliches Verfahren festgelegt werden, um Sicherheitsvorfälle und Störungen einzustufen. Das Einstufungsverfahren für Sicherheitsvorfälle SOLLTE zwischen Sicherheitsmanagement und der Störungs- und Fehlerbehebung (Incident Management) abgestimmt sein.

#### DER.2.1.A12 Festlegung der Schnittstellen der Sicherheitsvorfallbehandlung zur Störungs- und Fehlerbehebung [Notfallbeauftragter]

Die Schnittstellen zwischen Störungs- und Fehlerbehebung, Notfallmanagement und Sicherheitsmanagement SOLLTEN analysiert werden. Dabei SOLLTEN auch eventuell gemeinsam benutzbare Ressourcen identifiziert werden.

Die bei der Störungs- und Fehlerbehebung beteiligten Mitarbeiter SOLLTEN für Belange der Sicherheitsvorfallbehandlung sowie des Notfallmanagements sensibilisiert werden. Das Sicherheitsmanagement SOLLTE lesenden Zugriff auf eingesetzte Incident-Management-Werkzeuge haben.

#### DER.2.1.A13 Einbindung in das Sicherheits- und Notfallmanagement [Notfallbeauftragter]

Als Teil des Sicherheitsmanagements SOLLTE die Behandlung von Sicherheitsvorfällen in der Sicherheitsleitlinie bzw. im Sicherheitskonzept der Institution geregelt werden. Die Behandlung von Sicherheitsvorfällen SOLLTE außerdem mit dem Notfallmanagement abgestimmt werden. Falls es in der Institution eine spezielle Rolle für Störungs- und Fehlerbehebung gibt, SOLLTE auch diese mit einbezogen werden.

#### DER.2.1.A14 Eskalationsstrategie für Sicherheitsvorfälle [Leiter IT]

Über die Kommunikations- und Kontaktstrategie (siehe DER.2.1.A9 *Festlegung von Meldewegen für Sicherheitsvorfälle*) hinaus SOLLTE eine Eskalationsstrategie formuliert werden. Diese SOLLTE zwischen den Verantwortlichen für Störungs- und Fehlerbehebung und dem Informationssicherheitsmanagement abgestimmt werden.

Die Eskalationsstrategie SOLLTE eindeutige Handlungsanweisungen enthalten, wer, auf welchem Wege, bei welcher Art von erkennbaren oder vermuteten Sicherheitsstörungen, in welchem Zeitraum zu involvieren ist. Es SOLLTE geregelt sein, zu welchen Maßnahmen eine Eskalation führt und welche Aktivitäten ausgelöst werden sollen.

Für die festgelegte Eskalationsstrategie SOLLTEN geeignete Werkzeuge ausgewählt werden. Diese SOLLTEN auch für vertrauliche Informationen geeignet sein. Es SOLLTE sichergestellt sein, dass die Werkzeuge auch während eines Sicherheitsvorfalls bzw. Notfalls verfügbar sind.

Die Eskalationsstrategie SOLLTE regelmäßig überprüft und gegebenenfalls aktualisiert werden. Die Checklisten (Matching Szenarios) für Störungs- und Fehlerbehebung SOLLTEN regelmäßig um sicherheitsrelevante Themen ergänzt bzw. aktualisiert werden. Die festgelegten Eskalationswege SOLLTEN in Übungen erprobt werden.

#### DER.2.1.A15 Schulung der Mitarbeiter der zentralen Anlaufstelle des IT-Betriebs zur Behandlung von Sicherheitsvorfällen [Leiter IT]

Die Mitarbeiter des Service Desk SOLLTEN die Richtlinien für die Behandlung von Sicherheitsvorfällen kennen. Ihnen SOLLTEN geeignete Hilfsmittel zur Verfügung stehen, damit sie solche Vorfälle erkennen können. Sie SOLLTEN in deren Bedienung ausreichend geschult sein. Die Mitarbeiter des Service Desk SOLLTEN den Schutzbedarf der betroffenen Systeme kennen. Die Checklisten des Service Desk SOLLTEN auch Fragen beinhalten, um Sicherheitsvorfälle identifizieren zu können.

#### DER.2.1.A16 Dokumentation der Behandlung von Sicherheitsvorfällen

Die Behebung von Sicherheitsvorfällen SOLLTE nach einem standardisierten Verfahren dokumentiert werden. Es SOLLTEN sowohl alle durchgeführten Aktionen inklusive der Zeitpunkte, als auch die Protokolldaten der betroffenen Komponenten dokumentiert werden. Dabei SOLLTE die Vertraulichkeit bei der Dokumentation und Archivierung der Berichte gewährleistet sein.

Die benötigten Informationen SOLLTEN in die jeweiligen Dokumentationssysteme eingepflegt werden, bevor die Störung als beendet und abgeschlossen markiert wird. Dafür SOLLTEN die erforderlichen Qualitätssicherungsanforderungen im Vorfeld mit dem Sicherheitsmanagement definiert werden.

#### DER.2.1.A17 Nachbereitung von Sicherheitsvorfällen

Sicherheitsvorfälle SOLLTEN standardisiert nachbereitet werden. Dabei SOLLTE untersucht werden, wie schnell Sicherheitsvorfälle erkannt und behoben wurden, ob die Meldewege funktionierten, ausreichend Informationen für die Bewertung verfügbar und ob die Detektionsmaßnahmen wirksam waren. Ebenso SOLLTE geprüft werden, ob die ergriffenen Maßnahmen und Aktivitäten wirksam und effizient waren.

Die Erfahrungen aus vergangenen Sicherheitsvorfällen SOLLTEN genutzt werden, um daraus Handlungsanweisungen für vergleichbare Sicherheitsvorfälle zu erstellen. Diese Handlungsanweisungen SOLLTEN den relevanten Personengruppen bekanntgegeben und auf Basis neuer Erkenntnisse regelmäßig aktualisiert werden.

Außerdem SOLLTE die Leitungsebene jährlich über die Sicherheitsvorfälle unterrichtet werden. Allerdings SOLLTE die Leitungsebene gleich unterrichtet werden, wenn es sofortigen Handlungsbedarf gibt. 

#### DER.2.1.A18 Weiterentwicklung der Prozesse durch Erkenntnisse aus Sicherheitsvorfällen und Branchenentwicklungen [Fachverantwortliche]

Die Reaktionen auf Sicherheitsvorfälle SOLLTEN analysiert und daraufhin untersucht werden, ob die Prozesse und Abläufe geändert oder weiterentwickelt werden müssen. Dabei SOLLTEN die in Reaktionen auf Sicherheitsvorfälle involvierten als auch die zuständigen Beteiligten über ihre jeweiligen Erfahrungen berichten.

Es SOLLTE geprüft werden, ob neue Entwicklungen im Incident Management und in der Forensik existieren und in die jeweiligen Dokumente und in die Abläufe eingebracht werden können. 

Werden Hilfsmittel und Checklisten z. B. für Service-Desk-Mitarbeiter eingesetzt, SOLLTE geprüft werden, ob diese um erforderliche relevante Fragestellungen und Informationen zu erweitern sind.

### 3.3 Anforderungen bei erhöhtem Schutzbedarf

Im Folgenden sind exemplarische Vorschläge für Anforderungen aufgeführt, die über das dem Stand der Technik entsprechende Schutzniveau hinausgehen und BEI ERHÖHTEM SCHUTZBEDARF in Betracht gezogen werden SOLLTEN. Die konkrete Festlegung erfolgt im Rahmen einer Risikoanalyse. Die jeweils in Klammern angegebenen Buchstaben zeigen an, welche Grundwerte durch die Anforderung vorrangig geschützt werden (C = Vertraulichkeit, I = Integrität, A = Verfügbarkeit).

#### DER.2.1.A19 Festlegung von Prioritäten für die Behandlung von Sicherheitsvorfällen(CIA)

Um die Ursachen von Sicherheitsvorfällen und die entstandenen Schäden effizient und in einer sinnvollen Reihenfolge beheben zu können, SOLLTEN die Prioritäten vorab festgelegt und regelmäßig aktualisiert werden. Dabei SOLLTE auch die vorgenommene Einstufung von Sicherheitsvorfällen berücksichtigt werden (siehe DER.2.1.A11 *Einstufung von Sicherheitsvorfällen*). 

Die Prioritäten SOLLTEN von der Institutionsleitung genehmigt und in Kraft gesetzt werden. Sie SOLLTEN allen Entscheidungsträgern bekannt sein, die mit der Behandlung von Sicherheitsvorfällen zu tun haben. Die festgelegten Prioritätsklassen SOLLTEN außerdem im Incident Management hinterlegt sein.

#### DER.2.1.A20 Einrichtung einer internen Meldestelle für Sicherheitsvorfälle(CIA)

Es SOLLTE eine interne Stelle zur Meldung von Sicherheitsvorfällen eingerichtet werden. Es SOLLTE gewährleistet sein, dass die Meldestelle zu den üblichen Arbeitszeiten erreichbar ist. Allerdings SOLLTE es zusätzlich möglich sein, dass Sicherheitsvorfälle auch außerhalb der üblichen Arbeitszeiten von Mitarbeitern gemeldet werden können. Die Mitarbeiter der Meldestelle SOLLTEN ausreichend geschult und für die Belange der Informationssicherheit sensibilisiert sein. Alle Informationen über Sicherheitsvorfälle SOLLTEN bei der Meldestelle vertraulich behandelt werden.

#### DER.2.1.A21 Einrichtung eines Expertenteams für die Behandlung von Sicherheitsvorfällen(CIA)

Um Sicherheitsvorfälle durch den gesamten Lebenszyklus des Sicherheitsvorfallbehandlungsprozesses kompetent begleiten zu können, SOLLTE hierfür ein Team mit erfahrenen und vertrauenswürdigen Spezialisten zusammengestellt werden. Neben dem technischen Verständnis SOLLTEN die Teammitglieder auch Kompetenzen in der Kommunikationsfähigkeit besitzen. Die Vertrauenswürdigkeit der Mitglieder des Expertenteams SOLLTE überprüft werden. Der Aufbau des Expertenteams SOLLTE regelmäßig aktualisiert werden.

Die Mitglieder des Expertenteams SOLLTEN in die Eskalations- und Meldewege eingebunden sein. Das Expertenteam SOLLTE für die Analyse von Sicherheitsvorfällen an den in der Institution eingesetzten Systemen ausgebildet werden. Die Mitglieder des Expertenteams SOLLTEN sich regelmäßig weiterbilden, sowohl zu den eingesetzten Systemen als auch zu Detektion und Reaktion auf Sicherheitsvorfälle. Dem Expertenteam SOLLTEN alle vorhandenen Dokumentationen sowie finanzielle und technische Ressourcen zur Verfügung stehen, um Sicherheitsvorfälle schnell und diskret zu behandeln.

Das Expertenteam SOLLTE geeignet in den Organisationsstrukturen berücksichtigt und integriert werden (siehe DER.2.1.A8 *Aufbau von Organisationsstrukturen zur Behandlung von Sicherheitsvorfällen*). Die Verantwortlichkeiten des Expertenteams SOLLTEN vorher mit denen des Sicherheitsvorfall-Teams abgestimmt werden (siehe DER.2.1.A4 *Festlegung von Verantwortlichkeiten und Ansprechpartnern bei Sicherheitsvorfällen*).

#### DER.2.1.A22 Überprüfung des Managementsystems zur Behandlung von Sicherheitsvorfällen(CIA)

Das Managementsystem zur Behandlung von Sicherheitsvorfällen SOLLTE regelmäßig geprüft werden, ob es noch aktuell und wirksam ist. Dazu SOLLTEN sowohl angekündigte als auch unangekündigte Übungen durchgeführt werden. Die Übungen SOLLTEN vorher mit der Leitungsebene abgestimmt sein. Es SOLLTEN die Messgrößen ausgewertet werden, die beispielsweise anfallen, wenn Sicherheitsvorfälle aufgenommen, gemeldet und eskaliert werden. 

Außerdem SOLLTEN Planspiele zur Behandlung von Sicherheitsvorfällen durchgeführt werden, um die notwendige Praxis zu fördern.

4 Weiterführende Informationen
------------------------------

### 4.1 Literatur

Weiterführende Informationen zu Gefährdungen und Sicherheitsmaßnahmen im Bereich "Behandlung von Sicherheitsvorfällen" finden sich unter anderem in folgenden Veröffentlichungen:

* #### [27001A16] ISO/IEC 27001: 2013 - Annex A.16 Information security incident management

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 2013, insbesondere Annex A, A.16 Information security incident management  
 <https://www.iso.org/obp/ui/#iso:std:iso-iec:27001:ed-2:v1:en>

 
* #### [27035] ISO/IEC 27035:2016

  

 Information technology- Security techniques- Information security management system- Requirements, ISO, 09.2011  
 <https://www.iso.org/standard/44379.html>

 
* #### [ISFSATS14] The Standard of Good Practice - Area SA System Access und TS1.4 Technical Security Management

  

 Information Security Forum (ISF), insbesondere Area SA (System Access) und TS1.4 (Technical Security Management; Identiy and Access Management), 06.2016

 
* #### [NIST80061] NIST Special Publication 800-61 Revision 2

  

 NIST, Computer Security Incident Handling Guide, 08.2012  
 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-61r2.pdf>

 
* #### [NST80083] NIST Special Publication 800-83 Revision 1

  

 NIST, Guide to Malware incident Prevention and Handling vor Desktops and Laptops, 07.2013  
 <http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-83r1.pdf>

 
5 Anlage: Kreuzreferenztabelle zu elementaren Gefährdungen
----------------------------------------------------------

Die folgenden elementaren Gefährdungen sind für den Baustein "Behandlung von Sicherheitsvorfällen" von Bedeutung.

* G 0.11 Ausfall oder Störung von Dienstleistern
* G 0.18 Fehlplanung oder fehlende Anpassung
* G 0.19 Offenlegung schützenswerter Informationen
* G 0.20 Informationen oder Produkte aus unzuverlässiger Quelle
* G 0.22 Manipulation von Informationen
* G 0.25 Ausfall von Geräten oder Systemen
* G 0.27 Ressourcenmangel
* G 0.29 Verstoß gegen Gesetze oder Regelungen
* G 0.30 Unberechtigte Nutzung oder Administration von Geräten und Systemen
* G 0.32 Missbrauch von Berechtigungen
* G 0.33 Personalausfall
* G 0.45 Datenverlust
* G 0.46 Integritätsverlust schützenswerter Informationen
Die Kreuzreferenztabellen finden Sie aufgrund ihres Umfangs im Downloadbereich.

