
__Author__ = "Mouza Alameri"
__Date__ = "12/05/2025"

class Logz:
    logs = [
        "User: admin | IP: 192.168.1.10 | Status: SUCCESS",
        "User: guest | IP: 203.0.113.5 | Status: FAILED",
        "User: admin | IP: 10.0.0.5 | Status: FAILED",
        "User: root | IP: 198.51.100.12 | Status: SUCCESS",
        "User: guest | IP: 192.168.1.15 | Status: FAILED"
    ]

    log_entries = iter(logs)

class Status(Logz):
    def check_failed_logins(self):
        log_iter = iter(self.logs)
        while True:
            try:
                entry = next(log_iter)
                if "FAILED" in entry:
                    print(f" Suspicious Login Detected: {entry}")
            except StopIteration:
                break

class Userz(Logz):
    def show_users(self):
        user_iter = iter(self.logs)
        while True:
            try:
                entry = next(user_iter)
                user = entry.split(" | ")[0].split(": ")[1]
                print(f"👤 User: {user}")
            except StopIteration:
                break

class IP(Logz):
    def show_ips(self):
        ip_iter = iter(self.logs)
        while True:
            try:
                entry = next(ip_iter)
                ip = entry.split(" | ")[1].split(": ")[1]
                print(f" IP Address: {ip}")
            except StopIteration:
                break


print("==STATUS CHECK==")
Status().check_failed_logins()
print("\n==USER LIST==")
Userz().show_users()
print("\n==IP LIST==")
IP().show_ips()
