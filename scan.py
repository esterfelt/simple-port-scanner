import threading
import socket
import argparse

ports = {
    7: "ECHO",
    9: "DISCARD",
    13: "DAYTIME",
    21: "FTP",
    22: "SSH",
    23: "TELNET",
    25: "SMTP",
    26: "RSFTP",
    37: "TIME",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    69: "TFTP",
    79: "FINGER",
    80: "HTTP",
    81: "HTTP ALT",
    82: "XFER",
    83: "MIT-ML-DEV",
    88: "KERBEROS",
    109: "POP2",
    110: "POP3",
    111: "RPCBIND",
    113: "IDENT",
    119: "NNTP",
    123: "NTP",
    135: "RPC",
    137: "NETBIOS-NS",
    138: "NETBIOS-DGM",
    139: "NETBIOS-SSN",
    143: "IMAP",
    161: "SNMP",
    162: "SNMPTRAP",
    179: "BGP",
    199: "SMUX",
    389: "LDAP",
    427: "SLP",
    443: "HTTPS",
    444: "SNPP",
    445: "SMB",
    465: "SMTPS",
    500: "ISAKMP",
    512: "EXEC",
    513: "LOGIN",
    514: "SHELL",
    515: "LPD",
    520: "RIP",
    523: "IBM-DB2",
    546: "DHCPv6",
    547: "DHCPv6",
    548: "AFP",
    554: "RTSP",
    587: "SMTP SUBMISSION",
    631: "IPP",
    636: "LDAPS",
    873: "RSYNC",
    902: "VMWARE",
    989: "FTPS",
    990: "FTPS",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS",
    1194: "OPENVPN",
    1433: "MSSQL",
    1434: "MSSQL MON",
    1521: "ORACLE",
    1701: "L2TP",
    1723: "PPTP",
    1883: "MQTT",
    1900: "SSDP",
    2049: "NFS",
    2121: "FTP ALT",
    2181: "ZOOKEEPER",
    2375: "DOCKER",
    2376: "DOCKER TLS",
    2483: "ORACLE",
    2484: "ORACLE TLS",
    3000: "DEV SERVER",
    3128: "PROXY",
    3306: "MYSQL",
    3389: "RDP",
    3690: "SVN",
    4333: "SSH ALT",
    4444: "BACKDOOR",
    4500: "IPSEC NAT-T",
    4567: "MYSQL ALT",
    5000: "UPNP",
    5001: "IPERF",
    5060: "SIP",
    5222: "XMPP",
    5223: "XMPP SSL",
    5432: "POSTGRESQL",
    5555: "ADB",
    5601: "KIBANA",
    5631: "PCANYWHERE",
    5666: "NRPE",
    5800: "VNC HTTP",
    5900: "VNC",
    5984: "COUCHDB",
    6379: "REDIS",
    6443: "KUBERNETES API",
    6667: "IRC",
    7001: "WEBLOGIC",
    7002: "WEBLOGIC SSL",
    7077: "SPARK",
    8000: "HTTP ALT",
    8008: "HTTP ALT",
    8080: "HTTP PROXY",
    8081: "HTTP ALT",
    8086: "INFLUXDB",
    8088: "HADOOP",
    8443: "HTTPS ALT",
    8888: "HTTP ALT",
    9000: "FASTCGI",
    9042: "CASSANDRA",
    9092: "KAFKA",
    9200: "ELASTICSEARCH",
    9300: "ELASTIC CLUSTER",
    10000: "WEBMIN"
}

def scan_port(host, port):
    # AF_INET is an address family used for IPv4 networking (docs)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((host, port))
    s.close()

    if result == 0:
        print(f"{ports[port]}, {port} - открыт")

def scan_ports(host):
    # Using threads for speed
    threads = []

    for port in ports:
        th = threading.Thread(target=scan_port, args=(host, port))
        threads.append(th)
        th.start()

    for th in threads:
        th.join()
        
# Must use IP address when calling for script
parser = argparse.ArgumentParser()
parser.add_argument("ip", help="IP-address")

try:
    args = parser.parse_args()
except SystemExit:
    print("You need to provide an IP address to scan")
    exit()

ip = args.ip

# Launching
scan_ports(ip)
