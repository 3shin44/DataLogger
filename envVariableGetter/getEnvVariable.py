from dotenv import load_dotenv
import os
import importlib
logbox = importlib.import_module('logbox.logbox')

def getEnvVariable(envName):
    load_dotenv()
    envValue = None
    try:
        envValue = os.getenv(envName)
    except:
        logbox.loggerBox(f'get env variable {envName} error')
    finally:
        return envValue