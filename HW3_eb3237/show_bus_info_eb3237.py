import requests, sys, csv

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}'.format(sys.argv[1], sys.argv[2])

data = requests.get(url).json()

activity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

with open(sys.argv[3], 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Latitude', 'Longitude', 'Stop Name', 'Stop Status'])
    for item in activity:
        location = item['MonitoredVehicleJourney']['VehicleLocation']
        point = item['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]
        writer.writerow([
            location['Latitude'],
            location['Longitude'],
            point['StopPointName'],
            point['Extensions']['Distances']['PresentableDistance']
        ])
