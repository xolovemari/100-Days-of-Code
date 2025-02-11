from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager

# Configuração inicial
flights = FlightSearch()
data = DataManager()
flight_data = FlightData(flights)
sms = NotificationManager()

# Adiciona cidades válidas (executar apenas uma vez)
# data.add_city("Rio de Janeiro", "GIG", 500)
# data.add_city("São Paulo", "GRU", 600)
# data.add_city("Brasília", "BSB", 700)

try:
    rows = data.get_row()
    print(f"Encontradas {len(rows)} cidades na planilha")
except Exception as e:
    print(f"Erro ao ler planilha: {e}")
    rows = []

for row in rows:
    try:
        if row["iataCode"] not in ["GIG", "GRU", "BSB"]:
            print(f"Ignorando {row['city']} ({row['iataCode']}) - código não suportado")
            continue

        print(f"Verificando voos para {row['city']}...")
        cheapest = flight_data.check_flight(row["iataCode"], row["lowestPrice"])
        
        if cheapest:
            print(f"Novo preço encontrado: R${cheapest['price']}")
            data.modify_price(row["id"], cheapest["price"])
            sms.send_sms(
                price=cheapest["price"],
                destiny=row["city"],
                departure=cheapest["date"],
                arrival=cheapest["return_date"]
            )

    except Exception as e:
        print(f"Erro processando {row['city']}: {e}")