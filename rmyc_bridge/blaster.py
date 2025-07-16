from . import serial

def set_blaster_bead(num: int) -> None:
    """
    设置单次发射量
    Args:
        num (int): 发射量，范围[1, 5]
    Raises:
        ValueError: 如果num不在范围[1, 5]内
    """
    serial.write_serial(f"blaster bead {num};")

def blaster_fire() -> None:
    """
    发射子弹
    """
    serial.write_serial("blaster fire;")

