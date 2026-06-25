from core.base_scanner import BaseScanner


class AggressiveScanner(BaseScanner):
    name = "Aggressive Scan"
    description = "Intense Scan (Versions, OS, Scripts, Traceroute)"
    flags = ["-A"]