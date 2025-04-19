from dotenv import load_dotenv
import os

load_dotenv()

# GPIO BCM codes
GPIO_PIN_OPEN = int(os.getenv("GPIO_PIN_OPEN", 2))
GPIO_PIN_STOP = int(os.getenv("GPIO_PIN_STOP", 3))
GPIO_PIN_CLOSE = int(os.getenv("GPIO_PIN_CLOSE", 4))

