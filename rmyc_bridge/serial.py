import serial as s

serial_conn = s.Serial(
    port="/dev/ttyAMA0",
    baudrate=115200,
    bytesize=s.EIGHTBITS,
    parity=s.PARITY_NONE,
    stopbits=s.STOPBITS_ONE,
    timeout=10,
)

def read_serial() -> str:
    """
    从UART读取数据
    Returns:
        str: 读取到的数据
    """
    try:
        data = serial_conn.readline().decode('utf-8').strip()
        return data
    except s.SerialException as e:
        return ""
    except UnicodeDecodeError as e:
        return ""

def write_serial(data: str) -> bool:
    """
    向UART发送数据
    Args:
        data (str): 要发送的数据
    Returns:
        bool: 是否成功发送
    """
    try:
        serial_conn.write(data.encode('utf-8'))
        return True
    except s.SerialException as e:
        return False

__all__ = ["read_serial", "write_serial", ]