from classes.db_classes.airport_queries import select_all_airports, select_airports_by_country, select_specific_airport
from geopy.distance import geodesic

probes = []
probes_counter = 1

#Ottaa l1 ja l2 monikot, palauttaa etäisyyden kilometreina
def current_distance(l1, l2):
        final_distance = geodesic(l1, l2).km
        return "%.2f" % final_distance

#Ottaa  sisään  toivotun määrän  palauttaita sekä verratavat koordinaatit. Palauttaa listan täynnä sanakirjoja lentokenttien nimen, icao-koodin ja  etäisyyksien kanssa
def select_closest_airports(amount, player_cordinates):
    airports = select_all_airports()
    airport_distances  = []
    for x in airports:
         distance = float(current_distance(player_cordinates, (x["lat"], x["lon"])))
         if distance == 0.0:
              continue
         temp_airport_dictionary = {"a_name": x["a_name"],"airport_icao": x["airport_icao"], "distance": distance}
         airport_distances.append(temp_airport_dictionary)
    airport_distances.sort(key=lambda a: float(a["distance"]))
    closest_airports = airport_distances[:amount]
    return closest_airports

#Hakijoiden logiikka
def probe_interaction(monsters):
     global probes
     global probes_counter
     placed_probe_amount = len(probes)
     if placed_probe_amount >= 5:
          print("Maksimi määrä aktiivisia hakijoita")
          remove_probe_question = input("Kirjoita 'P' postaaksesi hakijan: ").upper()
          if remove_probe_question == "P":
               for x in probes:
                    print(f"Numero: {x["number"]} | Sijainti: {x["icao"]} | Maa: {x["country"]}")
               poisto_kohde = input("Anna hakijan numero jonka haluat poistaa: ")
               probes = [x for x in probes if x.get("Numero") != poisto_kohde]
          else:
               for x in probes:
                    for monster in monsters:
                         distance = float(current_distance(probes['cordinates'], monster['cordinates']))
                         print(f"Hakija nr.{x['number']} | Sijainti: {x["icao"]} etäisyys {monster['name']} on {distance}km")
     elif placed_probe_amount < 5:
          place_probe = input("Kirjoita 'A' asettaaksesi hakijan: ").upper()   
          if place_probe == "A":   
               probe_question = select_airports_by_country(input("Kirjoita maan nimi englaniksi jonne haluat assettaa hakijan: ").upper())
               for x in probe_question:
                    print(f"Nimi: {x["airport_name"]} | Sijainti: {x["airport_icao"]}")
               airport = select_specific_airport(input("Anna lentokentän ICAO-koodi jonne haluat asentaa hakijan: ").upper())
               probes.append({"number": probes_counter, "icao": airport["airport_icao"], "country": airport["c_name"], "cordinates": (airport["lat"], airport["lon"])})
               probes_counter = probes_counter + 1
          for x in probes:
               for monster in monsters:
                    distance = float(current_distance(x['cordinates'], monster['cordinates']))
                    print(f"Hakija nr.{x['number']} | Sijainti: {x["icao"]} etäisyys {monster['name']} on {distance}km")
