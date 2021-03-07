import telnetlib

clients = {}

def main():
    clients = read_file()

    for client in clients:
        client_ip_address = clients[client]
        show_run = telnet(client_ip_address)
        wrire_file(client, show_run)


def read_file():
    with open('client_ip.txt', mode='r') as f:
        ftext = f.readlines()

        for ip_address in ftext:
            field_split = ip_address.split(' ')
            hostname = field_split[0]
            ip_address = field_split[1]
            rep_ip_address = ip_address.replace('\n', '')
            clients[hostname] = rep_ip_address

        f.close()

    return clients

def wrire_file(client, show_run):
    with open(client + 'txt', mode='w') as wf:
        wf.writelines(show_run)
    wf.close()


def telnet(client_ip_address):
    tn = telnetlib.Telnet(client_ip_address)

    tn.read_until(b'Password:')
    tn.write(b'cisco' + b'\n')
    tn.read_until(b'>')

    tn.write(b'en' + b'\n')

    tn.read_until(b'Password:')
    tn.write(b'cisco' + b'\n')

    tn.read_until(b'#')
    tn.write(b'ter len 0' + b'\n')
    tn.write(b'show run' + b'\n')

    tn.read_until(b'#')
    tn.write(b'exit' + b'\n')

    show_run = tn.read_all().decode('ascii')
    return show_run

    tn.close()


if __name__ == '__main__':
    main()

