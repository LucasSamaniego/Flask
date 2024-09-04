import paho.mqtt.client as mqtt
import time

class MqttClient:
    def __init__(self, broker, port=1883, client_id=None, username=None, password=None):
        self.broker = broker
        self.port = port
        self.client_id = client_id
        self.username = username
        self.password = password
        self.client = mqtt.Client(client_id)
        
        # Configuração de autenticação, se fornecido
        if username and password:
            self.client.username_pw_set(username, password)

        # Definindo os callbacks
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        """Callback quando o cliente se conecta ao broker."""
        print(f"Conectado com código de resultado {rc}")

    def on_message(self, client, userdata, msg):
        """Callback quando uma mensagem é recebida de um tópico inscrito."""
        print(f"Mensagem recebida '{msg.payload.decode()}' no tópico '{msg.topic}'")

    def connect(self):
        """Conecta ao broker MQTT."""
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()  # Inicia o loop em um thread separado

    def subscribe(self, topic):
        """Inscreve o cliente em um tópico."""
        self.client.subscribe(topic)
        print(f"Inscrito no tópico '{topic}'")

    def publish(self, topic, message):
        """Publica uma mensagem em um tópico."""
        self.client.publish(topic, message)
        print(f"Mensagem '{message}' publicada no tópico '{topic}'")

    def disconnect(self):
        """Desconecta do broker MQTT."""
        self.client.loop_stop()  # Para o loop
        self.client.disconnect()
        print("Desconectado do broker MQTT")

mensagem = None

# Callback quando uma mensagem é recebida
def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico {msg.topic}: {msg.payload.decode()}")
    global mensagem = msg.payload.decode()

def conect_broker():
    if __name__ == "__main__":
        mqtt_broker = "test.mosquitto.org"  # Altere para o endereço do seu broker MQTT
        mqtt_port = 1883  # Altere se o broker usar uma porta diferente
        mqtt_client_id = "raspberry_pi_client"  # Opcional
        mqtt_username = None  # Altere se seu broker exigir autenticação
        mqtt_password = None  # Altere se seu broker exigir autenticação

        client = MqttClient(mqtt_broker, mqtt_port, mqtt_client_id, mqtt_username, mqtt_password)
        
        #client.connect()
        #client.subscribe("info")
    
    return client

def solicitar(item):
    raspberry = conect_broker() # Conecta o raspberry pi ao broker mqtt

    try:
        raspberry.publish("detail/item/publish", item)
    except KeyboardInterrupt:
        print("Interrompido pelo usuário")
    finally:
        raspberry.disconnect()

def receber():
    raspberry = conect_broker() # Conecta o raspberry pi ao broker mqtt
    raspberry.subscribe("detail/item/subscribe")
    raspberry.on_message = on_message
    raspberry.connect()

    # Mantém o cliente rodando para escutar mensagens
    #raspberry.loop_forever()

    count = 1
    raspberry.loop_start()

    try:
        # Mantenha o script rodando para que as mensagens possam ser recebidas
        while True:
            pass
    finally:
        # Pare o loop MQTT e desconecte-se quando o script for encerrado
        raspberry.loop_stop()
        raspberry.disconnect()
        if mensagem != None:
            return mensagem
        elif count == 10:
            return "Informação não recebida"
        count = count + 1

