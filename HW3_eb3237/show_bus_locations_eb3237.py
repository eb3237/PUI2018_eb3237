import requests, sys

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key={}&VehicleMonitoringDetailLevel=calls&LineRef={}'.format(sys.argv[1], sys.argv[2])

data = requests.get(url).json()

activity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print('Bus Line:', sys.argv[2])
print('Number of Active Buses:', len(activity))

for i in range(len(activity)):
    location = activity[i]['MonitoredVehicleJourney']['VehicleLocation']
    print('Bus {} is at latitude {} and longitude {}'.format(
        i, location['Latitude'], location['Longitude']
    ))