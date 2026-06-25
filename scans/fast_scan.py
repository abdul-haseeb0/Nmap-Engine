from core.base_scanner import BaseScanner


class FastScan(BaseScanner):
    name = "Fast Triage Scan"
    description = "Rapidly scan the top 100 most common ports for quick analysis"
    flags = ["-F", "-T4"]