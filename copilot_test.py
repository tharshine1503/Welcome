import os
import platform

def print_uptime():
    # For Unix/Linux/Mac systems
    if platform.system() != "Windows":
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            hours = int(uptime_seconds // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            seconds = int(uptime_seconds % 60)
            print(f"System uptime: {hours}h {minutes}m {seconds}s")
    else:
        # For Windows systems
        import subprocess
        output = subprocess.check_output("net stats workstation", shell=True, text=True)
        for line in output.split('\n'):
            if "Statistics since" in line:
                print(f"System uptime info: {line}")

if __name__ == "__main__":
    print_uptime()
