# helpers.py
from app_config import get_logger

def calculate_statistics(data):
    logger = get_logger()
    logger.debug('Calculating statistics')
    try:
        # Calculation logic
        stats = sum(data) / len(data)
        logger.debug(f'Statistics calculated: {stats}')
        return stats
    except Exception as e:
        logger.error(f'Statistics calculation failed: {e}')
        return None
