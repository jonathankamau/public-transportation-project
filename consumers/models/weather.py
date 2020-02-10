"""Contains functionality related to Weather"""
import json
import logging


logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        
        try:
            json_value = json.loads(message.value())
            self.temperature = json_value.get("temperature")
            self.status = value.get("status")
            logger.info("process_message has completed successfully")
        except Exception as e:
            logger.info(f"ERROR: {e}\nweather process_message is incomplete - skipping")
