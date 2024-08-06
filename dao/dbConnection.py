# 專案內部PY引用路徑
import sys
import os
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)
from logbox.logbox import loggerBox

from influxdb_client import InfluxDBClient
from envVariableGetter.getEnvVariable import getEnvVariable

def create_influxdb_client():
    # Get Env Variables
    url = getEnvVariable("influxDBurl")
    token = getEnvVariable("influxDBtoken")
    org = getEnvVariable("influxDBorg")

    client = InfluxDBClient(url=url, token=token, org=org)

    try:
        health = client.health()
        if health.status == "pass":
            loggerBox(f"Connection pass. version: {health.version}")
            return client
        else:
            loggerBox("Connection error.", health.message)
            client.close()
            return None
    except Exception as e:
        loggerBox("Connection exception:", e)
        client.close()
        return None
    
if __name__ == "__main__":
    create_influxdb_client()