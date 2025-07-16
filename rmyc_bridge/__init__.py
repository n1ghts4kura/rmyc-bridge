import threading as t

from . import serial
from . import sdk

def main_loop() -> None:
    sdk.enter_sdk_mode()
    
    while True:
        data = serial.read_serial()



    sdk.exit_sdk_mode()

def start_loop() -> None:
    """Start the main loop in a separate thread."""
    loop_thread = t.Thread(target=main_loop, daemon=True)
    loop_thread.start()