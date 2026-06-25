from core.base_scanner import BaseScanner


class PingScan(BaseScanner):
    name = "Ping Scan"
    description = "Discover live hosts on a subnet (eg. 192.168.0.1/24)"
    flags = ["-sn"]