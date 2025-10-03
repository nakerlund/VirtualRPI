# Virtual RPI IoT

Detta VS Code projekt använder en Dev Container baserat på Docker Compose som inkluderar en virtuell Raspberry Pi.

Dessa tjänster startas och har båda användarnamn "admin" med lösenordet "password":

- [InfluxDb](http://localhost:8086)
- [Grafana](http://localhost:3000)

Denna övning går ut på att ansluta den virtuella Raspberry Pi enheten till InfluxDb och skicka upp sensor data.

## Steg för steg

Skapa en api nyckel i [InfluxDb](http://localhost:8086) och skriv in den i variabeln `token` i [influxdb-demo-client.py](influxdb-demo-client.py).

Glöm inte att spara.

Öppna terminalen `bash` och kör rad för rad av detta script:

```bash

# Skicka filen influxdb-demo-client till RPIn
scp -P 2222 influxdb-demo-client.py root@rpi:~

# Logga in med SSH
ssh -p2222 root@rpi

# Sätt upp en python miljö med venv
python -m venv client

# Flytta filen influxdb-demo-client.py till client katalogen
mv influxdb-demo-client.py client

# Navigera till client katalogen
cd client

# Starta python miljön
source bin/activate

# Installera influxdb_client paketet med pip i python miljön
pip install influxdb_client

# Kör klienten
python influxdb-demo-client.py
```

Verifiera att data laddas upp på [InfluxDb](http://localhost:8086) i Data Explorer. 
Klicka i battery_data och battery_measurment och sen på knappen submit.

Öppna [Grafana](http://localhost:3000) och lägg till en InfluxDB data source.
Kör gärna med `Flux`och använd samma credential som användes i [influxdb-demo-client.py](influxdb-demo-client.py).

Quary language: Flux
Url: http://influxdb:8086
Organization: my-org

Verifiera att Grafana hämtas data från InfluxDb genom att köra frågan i explore data:
```Flux
from(bucket: "battery_data")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r["_measurement"] == "battery_measurement")
```

## RPI Lagringsutrymme

Om den virtuella RPI enheten får slut på lagringsutrymme så kan det utökas:

- Stäng Dev Containern i VS code om den är öppen
- Gå till projektets katalog i PowerShell
- Kör: `docker run --rm -it -v $PWD/dist:/dist ptrsr/pi-ci resize 3G`
- Öppna Dev Containern i VS Code igen
- Logga in på RPI med SSH och verifiera ledigt utrymme med `df -h`
