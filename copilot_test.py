import os
import platform

def print_system_uptime():
    system = platform.system()
    if system == "Windows":
        # On Windows, use 'net stats srv' and parse the output
        import subprocess
        try:
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    print(f"System uptime: {line.strip()}")
                    return
            print("Unable to determine system uptime on Windows.")
        except Exception as e:
            print(f"Error: {e}")
    elif system in ("Linux", "Darwin"):
        # On Linux and macOS, use the 'uptime' command
        try:
            uptime = os.popen("uptime -p").read().strip()
            print(f"System uptime: {uptime}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Unsupported OS: {system}")

if __name__ == "__main__":
    print_system_uptime()
