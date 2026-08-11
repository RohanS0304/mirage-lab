import subprocess
import re
from collections import defaultdict

result = subprocess.run(
    ["sudo", "journalctl", "-u", "ssh", "--since", "today"],
    capture_output=True,
    text=True
)

logs = result.stdout.splitlines()

failed_logs = [
    line for line in logs
    if "Failed password" in line or "Invalid user" in line
]

connections = defaultdict(set)

for line in failed_logs:
    ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
    port_match = re.search(r"port (\d+)", line)

    if ip_match and port_match:
        ip = ip_match.group(1)
        port = port_match.group(1)

        connections[ip].add(port)

print("=== SSH Security Monitor v4 ===")

if not connections:
    print("\n✅ No failed SSH authentication activity detected.")
else:
    print("\nSource IP analysis:")

    for ip, ports in connections.items():
        attempts = len(ports)

        print(f"\nIP: {ip}")
        print(f"Unique connections: {attempts}")

        if attempts >= 3:
            print("🚨 ALERT: Possible brute-force activity")
        else:
            print("⚠️ Authentication activity detected")
