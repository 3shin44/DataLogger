from dotenv import load_dotenv
import os

# 專案內部PY引用路徑
import sys
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)
from logbox.logbox import loggerBox

def getEnvVariable(envName):
    load_dotenv()
    envValue = None
    try:
        envValue = os.getenv(envName)
    except:
        loggerBox(f'get env variable {envName} error')
    finally:
        return envValue