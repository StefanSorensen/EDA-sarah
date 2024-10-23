# Sarahs Reise zur Event Driven Architecture

Dieses Repository enthält ein einfaches Python-Beispiel, um die Prinzipien der **Event Driven Architecture (EDA)** anhand einer fiktiven Geschichte von Sarahs E-Commerce-Geschäft zu veranschaulichen. Der Beispielcode zeigt, wie verschiedene Services (z. B. Zahlungsabwicklung und Lagerbestandsprüfung) auf Ereignisse asynchron reagieren können.

## Überblick über die Geschichte

Sarah ist Inhaberin eines wachsenden E-Commerce-Unternehmens. Mit zunehmendem Geschäftsumfang benötigt sie eine skalierbarere und reaktionsschnellere Systemarchitektur, um verschiedene Geschäftsprozesse wie Zahlungen und Lagerbestandsverwaltung effizienter zu handhaben. Um dies zu erreichen, setzt sie auf eine **Event Driven Architecture** (EDA), bei der unterschiedliche Services auf Ereignisse asynchron reagieren. Dies verbessert die Effizienz und Skalierbarkeit ihres Systems.

In diesem Beispiel:
- Der **Event-Broker** fungiert als Ereignisvermittler (wie z. B. Kafka in einem echten System).
- **Zahlungsservice** und **Lagerbestandsservice** sind Abonnenten, die auf das Ereignis `order_placed` reagieren.
- **Place Order** ist der Ereignisproduzent, der das Aufgeben einer Bestellung simuliert.

## Schlüsselkonzepte im Code

- **Event Broker**: Verwaltet die Registrierung von Services für bestimmte Ereignisse und das Veröffentlichen (Broadcasten) dieser Ereignisse an die Abonnenten.
- **Event Producer**: Generiert Ereignisse (z. B. das Aufgeben einer Bestellung), die an die Abonnenten gesendet werden.
- **Event Consumers**: Services, die auf bestimmte Ereignisse hören und darauf reagieren (z. B. Zahlungsabwicklung, Lagerbestandsprüfung).

## Erste Schritte

### Voraussetzungen

Um das Beispiel auszuführen, benötigen Sie Python. Falls Python noch nicht installiert ist, können Sie es von der [offiziellen Website](https://www.python.org/downloads/) herunterladen.

### Ausführen des Codes

1. Laden Sie das Repository herunter oder kopieren Sie die Skriptdatei.
2. Öffnen Sie ein Terminal oder eine Eingabeaufforderung und navigieren Sie zum Verzeichnis mit der Skriptdatei.
3. Führen Sie das Skript mit folgendem Befehl aus:

   ```bash
   python sarahs_eda_journey.py
   ```

Das Ausführen des Skripts simuliert Sarahs E-Commerce-System, in dem:
- Eine neue Bestellung aufgegeben wird.
- Die Zahlungs- und Lagerbestandsservices auf das Ereignis `order_placed` reagieren.

### Beispielhafte Ausgabe

```bash
Bestellung 123 wurde aufgegeben.
Zahlung für Bestellung 123 wird bearbeitet...
Lagerbestandsprüfung für Bestellung 123 wird durchgeführt...
Lagerbestände für Bestellung 123 verfügbar.
Zahlung für Bestellung 123 abgeschlossen.
```

### Code Erläuterung

- **EventBroker Klasse**:
    - Diese Klasse verwaltet die Event-Abonnenten und broadcastet Ereignisse an die entsprechenden Abonnenten.
    - Wichtige Methoden:
        - `subscribe(event_type, subscriber)`: Registriert einen Service für ein bestimmtes Ereignis.
        - `publish(event_type, data)`: Broadcastet ein Ereignis an alle registrierten Abonnenten.
        
- **Zahlungsservice**:
    - Dieser Service simuliert die Zahlungsabwicklung, indem er eine Nachricht druckt und die Ausführung für 2 Sekunden pausiert (um reale Latenzzeiten nachzuahmen).

- **Lagerbestandsservice**:
    - Dieser Service überprüft, ob die bestellten Artikel auf Lager sind, und reagiert entsprechend.

- **Place Order Funktion**:
    - Diese Funktion simuliert das Aufgeben einer Bestellung, die das `order_placed` Ereignis auslöst.

### Hauptmerkmale des Event Driven Ansatzes

- **Lose Kopplung**: Die Services (Zahlungs- und Lagerbestandssysteme) sind vom Bestellsystem entkoppelt. Sie reagieren nur auf Ereignisse und müssen nichts über einander wissen.
- **Asynchrone Verarbeitung**: Services werden parallel ausgeführt, was die Leistung und Skalierbarkeit verbessert.
- **Skalierbarkeit**: Das Hinzufügen neuer Services oder das Ändern vorhandener hat keinen Einfluss auf das Gesamtsystem, was es einfach macht, Sarahs Geschäftsplattform zu erweitern.

## Funktionsweise

1. **Event Producer (Bestellung aufgeben)**: Wenn eine neue Bestellung aufgegeben wird, sendet das System ein `order_placed` Ereignis an den `EventBroker`.
   
2. **Event Consumers (Zahlungs- und Lagerbestandsservice)**: Diese beiden Services sind Abonnenten des `order_placed` Ereignisses. Sobald das Ereignis veröffentlicht wird:
   - Beginnt der Zahlungsservice mit der Zahlungsabwicklung.
   - Der Lagerbestandsservice prüft, ob die Artikel auf Lager sind.

Beide Services arbeiten **parallel**, um sicherzustellen, dass Sarahs System effizient und reaktionsschnell bleibt.

## Erweiterungen

Dieses Beispiel kann erweitert werden, um zusätzliche Services oder Ereignistypen hinzuzufügen. Einige Beispiele könnten sein:
- **Versandservice**: Dieser könnte auf das Ereignis `payment_completed` hören und den Versandprozess auslösen.
- **Benachrichtigungsservice**: Dieser könnte Kunden über den Status ihrer Bestellung informieren, sobald sie bearbeitet und versandt wurde.

## Tools für Event Driven Architekturen in der Praxis

In einem echten System könnte Sarah folgende Tools verwenden:
- **Kafka** oder **RabbitMQ** als Message/Event Broker.
- **Microservices** für die Zahlungs-, Bestands- und Versandabwicklung.
- **Docker** und **Kubernetes** für skalierbare Deployments.

Für weitere Informationen zur Event Driven Architecture und wie sie Ihr Geschäft unterstützen kann, lesen Sie meinen vollständigen Blogbeitrag [hier](https://soerensen.dev/event-driven-architecture-grundlagen/).

---

Dies ist nur der Beginn von Sarahs Reise in die Welt der Event Driven Architecture. Bleiben Sie dran für weitere Updates und Beispiele!

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei `LICENSE`.
