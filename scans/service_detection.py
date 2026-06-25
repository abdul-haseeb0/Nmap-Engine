from core.base_scanner import BaseScanner


class ServiceDetection(BaseScanner):
    name = "Service Detection"
    description = "Detect services and versions on open ports  (e.g. 192.168.0.115)"
    flags = ["-sV"]