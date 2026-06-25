from core.base_scanner import BaseScanner


class UdpScan(BaseScanner):
    name = "UDP Port Scan"
    description = "Scan for open UDP services (DNS/DHCP/SNMP) on top 50 common ports"
    flags = ["-sU", "--top-ports", "50"]