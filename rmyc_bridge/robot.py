# rmyc_bridge/robot.py
# 用于处理机器人运动模式。

from typing import Literal
from threading import Lock

from . import serial

IDENTIFIERS = (
    "chassis_lead", # 云台跟随底盘
    "gimbal_lead",  # 底盘跟随云台
    "free" # 自由模式
)

robot_mode = "free"  # 默认模式为自由模式
robot_mode_lock = Lock()

def process(data: str) -> None:
    """
    处理接收到的数据
    Args:
        data (str): 接收到的数据
    """
    global robot_mode

    if data == IDENTIFIERS[0]:
        with robot_mode_lock:
            robot_mode = IDENTIFIERS[0]
    elif data == IDENTIFIERS[1]:
        with robot_mode_lock:
            robot_mode = IDENTIFIERS[1]
    elif data == IDENTIFIERS[2]:
        with robot_mode_lock:
            robot_mode = IDENTIFIERS[2]
    else:
        robot_mode = "free"  # 如果数据不匹配任何模式，重置为自由模式

def get_robot_mode() -> str:
    """
    获取当前机器人模式
    Returns:
        str: 当前机器人模式
    """
    with robot_mode_lock:
        return robot_mode

def cmd_get_robot_mode() -> None:
    """
    发送 获取当前机器人模式 的指令。
    """
    serial.write_serial("robot mode ?;")

def cmd_set_robot_mode(mode: Literal["chassis_lead", "gimbal_lead", "free"] = "free") -> bool:
    """
    设置机器人运动模式
    Args:
        mode (Literal["chassis_lead", "gimbal_lead", "free"]): 机器人模式
            - "chassis_lead": 云台跟随底盘
            - "gimbal_lead": 底盘跟随云台
            - "free": 自由模式
    Returns:
        bool: 是否成功设置模式
    """
    if mode not in IDENTIFIERS:
        return False

    serial.write_serial(f"robot mode {mode};")
    return True