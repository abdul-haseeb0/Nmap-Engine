from core.base_scanner import BaseScanner


class VulnScan(BaseScanner):
    name = "Vulnerability Scan"
    description = "Run common vuln detection scripts  (e.g. 192.168.0.115)"
    flags = ["-sV"]
    scripts = ["vuln"]