from app import db, models

def getStationsList():
	stations = models.Station.query.all()
	stations_list = []
	for station in stations:
		stations_list.append((station.name,station.name))
	return stations_list
	
