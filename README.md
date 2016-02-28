Other_tools
===========

Description
-----------
Just some scripts that have helped me in the past that I thought I'd share. Each should have its own usage.

udpshell
--------
A simple remote access tool that passes and executes commands to a remote client.

**Usage**

    usage: udpshell.py [-h]
                   [--client server_ip server_port sleep_value | --server bind_ip bind_port]
    optional arguments:
      -h, --help            show this help message and exit
      --client server_ip server_port sleep_value
                        starts client mode
      --server bind_ip bind_port
                        starts server mode

**Running udpshell**

Server mode:

    udpshell.py --server 127.0.0.1 62300

Client mode:

    udpshell.py --client 127.0.0.1 62300 15
