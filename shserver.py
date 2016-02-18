from sys import argv

import socket


def bind_svr(bind_ip, bind_port):
    '''
    :param bind_ip: String IPv4 addr the controller will bind to.
    :param bind_port: Int IPv4 UDP port the controller will bind to.
    :return: Nothing
    '''
    svr_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    svr_sock.bind((bind_ip, bind_port))
    print 'Binding the server on %s:%d' % (bind_ip, bind_port)

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
    bind_svr(bind_ip, int(bind_port))


if __name__ == '__main__':
    (scriptname, bind_ip, bind_port) = argv
    main()
