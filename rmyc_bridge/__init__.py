import time
import threading as t

from . import serial
from . import sdk

from .blaster import *
from .chassis import *
from .game_msg import *
from .gimbal import *
from .robot import *

def main_loop() -> None:
    sdk.enter_sdk_mode()
    
    try:
        while True:
            data = serial.read_serial()

            if data.startswith("game msg push"):
                process(data)
        
            time.sleep(0.5)
    except:
        pass

    sdk.exit_sdk_mode()

def start_loop() -> None:
    """Start the main loop in a separate thread."""
    loop_thread = t.Thread(target=main_loop, daemon=True)
    loop_thread.start()