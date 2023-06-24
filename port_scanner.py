import socket

import common_port as services

def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    closed_ports = []
    
    ip_address = convert_to_ip_or_hostname(target)
   
    
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            # Attempt to connect to the target host and port
            sock.settimeout(1)  # Set a timeout for the connection attempt
            result = sock.connect_ex((target, port))
            
            if result == 0:
                open_ports.append(port)
            else:
                closed_ports.append(port)
        
        except socket.error:
            return  "Error: Invalid IP address"
        
        finally:
            sock.close()
    if verbose:
        print(f'Open ports for {target} ({ip_address})\nPORT\tSERVICE')
        for port in open_ports:
            print(f'{port}\t{services[port]}')
    
    else:
        return open_ports


def convert_to_ip_or_hostname(address):
    try:
        if '.' in address:
            # Hostname to IP address conversion
            ip_address = socket.gethostbyname(address)
            return ip_address
        else:
            # IP address to hostname conversion
            hostname = socket.gethostbyaddr(address)[0]
            return hostname
    except socket.error as e:
        return "Error: Invalid hostname"

                            