import threading as t

def main_loop() -> None:
    while True:
        pass

def start_loop() -> None:
    """Start the main loop in a separate thread."""
    loop_thread = t.Thread(target=main_loop, daemon=True)
    loop_thread.start()