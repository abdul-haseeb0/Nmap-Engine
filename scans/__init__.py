from .ping_scan import PingScan
from .service_detection import ServiceDetection
from .os_detection import OsDetection
from .vuln_scanner import VulnScan
from .aggressive_scan import AggressiveScanner
from .syn_stealth_scan import SynStealthScan
from .udp_scan import UdpScan
from .web_tech_scan import WebTechScan
from .fast_scan import FastScan

REGISTRY = [
    PingScan(),
    ServiceDetection(),
    OsDetection(),
    VulnScan(),
    AggressiveScanner(),
    SynStealthScan(),
    WebTechScan(),
    UdpScan(),
    FastScan()
]