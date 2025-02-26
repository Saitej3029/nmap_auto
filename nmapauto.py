import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def main():
    target = input("Enter target IP or hostname: ").strip()

    commands = [
        f"nmap -sn {target}",                   # Ping Scan
        f"nmap -sV {target}",                   # Service Version Detection
        f"nmap -O {target}",                    # OS Detection
        f"nmap -A {target}",                    # Aggressive Scan
        f"nmap -p 1-1024 {target}",             # Scan Specific Ports
        f"nmap -F {target}",                    # Fast Scan
        f"nmap {target} {target}",              # Scan Multiple Targets
        f"nmap {target}.0/24",                  # Scan a Specific Range of IPs
        f"nmap -T4 {target}",                   # Aggressive Timing
        f"nmap -sS {target}"                    # Stealth Scan (SYN Scan)
    ]

    for command in commands:
        print(f"\nRunning command: {command}")
        output = run_command(command)
        print(output)

if __name__ == "__main__":
    main()

