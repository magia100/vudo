from geopy.geocoders import Nominatim
nom = Nominatim(scheme="http")
nom = nom.geocode("1657 N. Miami ave, Miami, FL 33136")
print (nom.latitude)
