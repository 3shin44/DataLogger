# SERVER LOGGER
from datetime import datetime
import logging
import os

def get_logger(log_name, log_dir, log_file_prefix):
    # 產生對應檔案名稱
    current_date = datetime.now().strftime("%Y-%m-%d")
    log_file_path = os.path.join(log_dir, f"{log_file_prefix}_{current_date}.log")
    
    # 建立logger
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.INFO)
    
    # 確保不重複添加處理器
    if not logger.handlers:
        file_handler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


# loggerBox: 傳入字串訊息, 將加入時間戳記並寫入專案夾中log/資料夾下並以日期做區分
def loggerBox(msg):
    # 獲取專案根目錄
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # LOG檔案存放目錄, 檢查並建立有無存在
    log_dir = os.path.join(project_dir, 'log')
    os.makedirs(log_dir, exist_ok=True)
    
    logger = get_logger('serverLog', log_dir, 'serverLog')
    logger.info(msg)
    
    
if __name__ == "__main__":
    loggerBox("logbox test")