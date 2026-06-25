from core.base_scanner import BaseScanner


class SynStealthScan(BaseScanner):
    name = "SYN Stealth Scan"
    description = "Semi-open stealth scan; quiet, fast, and accurate (Requires Root/Sudo)"
    flags = ["-sS", "-Pn"]