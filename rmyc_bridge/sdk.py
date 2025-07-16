# rmyc_bridge/sdk.py
# SDK模式控制
# @author: n1ghts4kura
# @date: 2025-07-16

from . import serial

def enter_sdk_mode() -> None:
    """
    进入SDK模式。
    """
    serial.write_serial("command;")

def exit_sdk_mode() -> None:
    """
    退出SDK模式。
    """
    serial.write_serial("quit;")