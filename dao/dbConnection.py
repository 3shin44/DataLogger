from influxdb_client import InfluxDBClient
from envVariableGetter.getEnvVariable import getEnvVariable

import importlib
logbox = importlib.import_module('logbox.logbox')

def create_influxdb_client():
    # Get Env Variables
    url = getEnvVariable("influxDBurl")
    token = getEnvVariable("influxDBtoken")
    org = getEnvVariable("influxDBorg")

    client = InfluxDBClient(url=url, token=token, org=org)

    try:
        health = client.health()
        if health.status == "pass":
            logbox.loggerBox(f"Connection pass. version: {health.version}")
            return client
        else:
            logbox.loggerBox("Connection error.", health.message)
            client.close()
            return None
    except Exception as e:
        logbox.loggerBox("Connection exception:", e)
        client.close()
        return None
    
if __name__ == "__main__":
    create_influxdb_client()