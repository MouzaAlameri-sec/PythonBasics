
__Author__ = "Mouza Alameri "
__Date__ = "08/05/2025"

import os

class Payload: 
    def run(self):
        if os.path.exists("target.txt"):
            print("Payload executed!")
        else:
            print("Target not found... standing by.")

p = Payload()
p.run()


        