__Author__ = "Mouza Alameri"
__Date__ = "09/05/2025"



class ProcessScanner: 
     def __init__(self):
            self.processes = ["explorer.exe", "malware.exe", "chrome.exe"]
     def scan(self):
        for x in self.processes:
            if x == "malware.exe":
                print("Suspicious process detected: malware.exe")
            else:
                print(f"Process: {x}")

     def quarantine(self):
        if "malware.exe" in self.processes:
            self.processes.remove("malware.exe")
            print("malware.exe quarantined")
        else:
            print("No threats found")
   
