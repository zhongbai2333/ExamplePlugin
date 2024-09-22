from mcdreforged.api.all import *

__mcdr_server = None


# MCDR Start point
def on_load(server: PluginServerInterface, _):
    global __mcdr_server
    __mcdr_server = server

    __mcdr_server.logger.info("Hello")
