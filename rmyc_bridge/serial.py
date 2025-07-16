# rmyc_bridge/serial.py
# 用于UART串口通信的模块
# @author: n1ghts4kura
# @date: 2025-07-16

import serial as s
from threading import Lock

serial_conn = s.Serial(
    port="/dev/ttyAMA0",
    baudrate=115200,
    bytesize=s.EIGHTBITS,
    parity=s.PARITY_NONE,
    stopbits=s.STOPBITS_ONE,
    timeout=10,
)
# serial_conn_lock = Lock()

def read_serial() -> str:
    """
    从UART读取数据
    Returns:
        str: 读取到的数据
    """
    # serial_conn_lock.acquire()
    data = ""

    try:
        data = serial_conn.readline().decode('utf-8').strip()
    except s.SerialException as e:
        pass
    except UnicodeDecodeError as e:
        pass

    # serial_conn_lock.release()
    return data

def write_serial(data: str) -> bool:
    """
    向UART发送数据
    Args:
        data (str): 要发送的数据
    Returns:
        bool: 是否成功发送
    """
    result = False
    # serial_conn_lock.acquire()

    try:
        serial_conn.write(data.encode('utf-8'))
        result = True
    except s.SerialException as e:
        pass
    
    # serial_conn_lock.release()
    return result

__all__ = ["read_serial", "write_serial", ]