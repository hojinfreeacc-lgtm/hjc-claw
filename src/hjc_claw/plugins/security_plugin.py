import socket
import hashlib
import platform
import subprocess
from .base import BasePlugin
from ..core.registry import PluginMetadata, registry

@registry.register
class SecurityPlugin(BasePlugin):
    def get_metadata(self):
        return PluginMetadata(
            name="security_toolkit",
            description="Security auditing and ethical hacking tools",
            intents=[
                {
                    "intent": "port_scan",
                    "keywords": ["port scan", "scan ports", "open ports", "network scan", "포트 스캔"],
                    "action": "scan_ports"
                },
                {
                    "intent": "hash_gen",
                    "keywords": ["hash", "md5", "sha256", "generate hash", "해시 생성"],
                    "action": "generate_hash"
                },
                {
                    "intent": "network_info",
                    "keywords": ["network info", "ip address", "local ip", "mac address", "네트워크 정보"],
                    "action": "get_network_info"
                }
            ]
        )

    def scan_ports(self, **kwargs):
        target = "127.0.0.1"
        common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306, 3389, 8080]
        open_ports = []
        
        result = f"🔍 Scanning common ports on {target}...\n"
        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            if sock.connect_ex((target, port)) == 0:
                open_ports.append(port)
            sock.close()
        
        if open_ports:
            result += "✅ Open ports found:\n" + "\n".join([f"  - Port {p}" for p in open_ports])
        else:
            result += "❌ No common open ports detected."
        return result

    def generate_hash(self, paths=None, **kwargs):
        if not paths: return "Error: No file path provided for hashing."
        target = paths[0]
        try:
            sha256_hash = hashlib.sha256()
            with open(target, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return f"🔒 SHA-256 Hash for '{target}':\n{sha256_hash.hexdigest()}"
        except Exception as e:
            return f"Error: {str(e)}"

    def get_network_info(self, **kwargs):
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        os_info = f"{platform.system()} {platform.release()}"
        
        return (
            f"🌐 Network Configuration:\n"
            f"  - Hostname: {hostname}\n"
            f"  - Local IP: {local_ip}\n"
            f"  - OS: {os_info}\n"
            f"  - Architecture: {platform.machine()}"
        )
