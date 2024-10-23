import time
from threading import Thread

# Event-Broker (in einem echten System könnte das z. B. Kafka sein)


class EventBroker:
    def __init__(self):
        self.subscribers = {}

    # Füge neue Subscriber hinzu (die auf ein Ereignis warten)
    def subscribe(self, event_type, subscriber):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(subscriber)

    # Veröffentliche ein Ereignis und benachrichtige alle Subscriber
    def publish(self, event_type, data):
        if event_type in self.subscribers:
            for subscriber in self.subscribers[event_type]:
                # Startet den Subscriber in einem separaten Thread
                Thread(target=subscriber, args=(data,)).start()

# Event Consumer: Zahlungssystem


def payment_service(order):
    print(f"Zahlung für Bestellung {order['order_id']} wird bearbeitet...")
    time.sleep(2)  # Simuliert Bearbeitungszeit
    print(f"Zahlung für Bestellung {order['order_id']} abgeschlossen.")

# Event Consumer: Lagerbestandsprüfung


def inventory_service(order):
    print(
        f"Lagerbestandsprüfung für Bestellung {order['order_id']} wird durchgeführt...")
    time.sleep(1)  # Simuliert Bearbeitungszeit
    if order['item_count'] > 0:
        print(f"Lagerbestände für Bestellung {order['order_id']} verfügbar.")
    else:
        print(
            f"Lagerbestände für Bestellung {order['order_id']} nicht verfügbar.")

# Event Producer: Bestellung aufgeben


def place_order(broker, order):
    print(f"Bestellung {order['order_id']} wurde aufgegeben.")
    broker.publish("order_placed", order)


# Hauptprogramm zur Simulation
if __name__ == "__main__":
    broker = EventBroker()

    # Subscriber (Zahlung und Lagerbestand) für das Ereignis "order_placed" registrieren
    broker.subscribe("order_placed", payment_service)
    broker.subscribe("order_placed", inventory_service)

    # Neue Bestellung aufgeben
    order = {"order_id": 123, "item_count": 5}

    # Ereignis "Bestellung aufgeben" wird ausgelöst
    place_order(broker, order)
