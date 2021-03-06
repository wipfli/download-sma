# download-sma
Download weather station measurements from MeteoSchweiz and store them in InfluxDB

The weather measurements are downloaded from https://data.geo.admin.ch/ch.meteoschweiz.messwerte-aktuell/VQHA80.csv and the parameter naming convention is:

```
tre200s0     °C             Lufttemperatur 2 m über Boden; Momentanwert
rre150z0     mm             Niederschlag; Zehnminutensumme
sre000z0     min            Sonnenscheindauer; Zehnminutensumme
gre000z0     W/m²           Globalstrahlung; Zehnminutenmittel
ure200s0     %              Relative Luftfeuchtigkeit 2 m über Boden; Momentanwert
tde200s0     °C             Taupunkt 2 m über Boden; Momentanwert
dkl010z0     °              Windrichtung; Zehnminutenmittel
fu3010z0     km/h           Windgeschwindigkeit; Zehnminutenmittel
fu3010z1     km/h           Böenspitze (Sekundenböe); Maximum
prestas0     hPa            Luftdruck auf Stationshöhe (QFE); Momentanwert
pp0qffs0     hPa            Luftdruck reduziert auf Meeresniveau (QFF); Momentanwert
pp0qnhs0     hPa            Luftdruck reduziert auf Meeresniveau mit Standardatmosphäre (QNH); Momentanwert
ppz850s0     gpm            Geopotentielle Höhe der 850 hPa-Fläche; Momentanwert
ppz700s0     gpm            Geopotentielle Höhe der 700 hPa-Fläche; Momentanwert
dv1towz0     °              Windrichtung vektoriell; Zehnminutenmittel; Instrument 1
fu3towz0     km/h           Windgeschwindigkeit Turm; Zehnminutenmittel
fu3towz1     km/h           Böenspitze (Sekundenböe) Turm; Maximum
ta1tows0     °C             Lufttemperatur Instrument 1
uretows0     %              Relative Luftfeuchtigkeit Turm; Momentanwert
tdetows0     °C             Taupunkt Turm
```

## install

```bash
python3 -m venv venv
source venv/bin/activate
pip install requests
pip install influxdb
pip install pandas
```

Test with

```python
python download.py
```
