# rmyc_bridge/__init__.py
# @author n1ghts4kura
# @date 2025-07-16

import time
import threading as t

from . import serial
from . import sdk

from . import blaster
from . import chassis
from . import game_msg
from . import gimbal
from . import robot

def main_loop() -> None:
    sdk.enter_sdk_mode()
    
    try:
        while True:
            data = serial.read_serial()

            if data.startswith("game msg push"):
                game_msg.process(data)
        
            time.sleep(0.5)
    except:
        pass

    sdk.exit_sdk_mode()

def start_loop() -> None:
    """Start the main loop in a separate thread."""
    loop_thread = t.Thread(target=main_loop, daemon=True)
    loop_thread.start()