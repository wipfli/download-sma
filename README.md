# download-sma
Download weather station measurements from MeteoSchweiz and store them in InfluxDB

## install

```bash
python3 -m venv venv
source venv/bin/activate
pip install requests
pip install influxdb
```

Test with

```python
python download.py
```
