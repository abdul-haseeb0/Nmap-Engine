from core.base_scanner import BaseScanner


class OsDetection(BaseScanner):
    name = "OS Detection"
    description = "Detect the operating system of a target  (e.g. 192.168.0.115)"
    flags = ["-O"]