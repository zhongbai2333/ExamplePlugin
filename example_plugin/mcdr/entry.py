from mcdreforged.api.all import *
from connect_core.api.mcdr import get_plugin_control_interface

__mcdr_server, _control_interface = None, None


# MCDR Start point
def on_load(server: PluginServerInterface, _):
    global __mcdr_server, _control_interface
    __mcdr_server = server
    _control_interface = get_plugin_control_interface("example_plugin", "example_plugin.mcdr.entry", server)

    _control_interface.info("Hello")


def new_connect(server_list):
    """有新的连接"""
    _control_interface.info(server_list)


def del_connect(server_list):
    """有断开连接"""
    _control_interface.info(server_list)


def connected():
    """连接成功"""
    _control_interface.info("Connected!")


def disconnected():
    """断开连接"""
    _control_interface.info("Disconnected!")


def recv_data(server_id: str, data: dict):
    """收到数据包"""
    _control_interface.info(data)


def recv_file(server_id: str, file: str):
    """收到文件"""
    _control_interface.info(file)
