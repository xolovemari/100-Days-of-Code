from datetime import datetime, timedelta

class FlightData:
    def __init__(self, flight_search):
        self.flights = flight_search
        self.today = datetime.now()

    def check_flight(self, destination, max_price):
        try:
            # Intervalo de 30 dias para sandbox
            start_date = (self.today + timedelta(days=1)).strftime("%Y-%m-%d")
            end_date = (self.today + timedelta(days=30)).strftime("%Y-%m-%d")
            
            # Formata datas corretamente
            departure_range = f"{start_date},{end_date}"
            return_range = f"{(self.today + timedelta(days=8)).strftime('%Y-%m-%d')},{(self.today + timedelta(days=37)).strftime('%Y-%m-%d')}"

            results = self.flights.flight_search(destination, departure_range, return_range)
            
            if not results.get('data'):
                return None

            filtered_flights = []
            for flight in results['data']:
                dep_date = flight['itineraries'][0]['segments'][0]['departure']['at'][:10]
                ret_date = flight['itineraries'][1]['segments'][0]['departure']['at'][:10]
                
                delta_days = (datetime.strptime(ret_date, "%Y-%m-%d") - datetime.strptime(dep_date, "%Y-%m-%d")).days
                price = float(flight['price']['total'])

                if delta_days == 7 and price <= max_price:
                    filtered_flights.append({
                        "date": dep_date,
                        "return_date": ret_date,
                        "price": price,
                        "flight": flight,
                    })

            return min(filtered_flights, key=lambda x: x['price']) if filtered_flights else None

        except Exception as e:
            print(f"Erro detalhado: {str(e)}")
            return None