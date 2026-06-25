import subprocess


class BaseScanner:

    name = "Base Scanner"
    description = "Base Class"
    flags = []
    scripts = []

    def run(self, target):

        command = ["nmap"] + self.flags

        if self.scripts:
            command += [f"--script={','.join(self.scripts)}"]

        command += [target]

        try:
            result = subprocess.run(
                command,
                check=True,
                text=True,
                capture_output=True,
            )
            return result.stdout

        except subprocess.CalledProcessError as e:
            print(f"[!] Scan failed (exit code {e.returncode})")
            if e.stderr:
                print(f"    Details: {e.stderr.strip()}")

        except FileNotFoundError:
            print("[!] Nmap binary not found when executing command.")

        except PermissionError:
            print("[!] Permission denied. Some nmap scans require root/sudo privileges.")

        except Exception as e:
            print(f"[!] Unexpected error: {e}")

        return None