__Author__ = "Mouza Alameri"
__Date__= "06/05/2025"

from PIL import Image

pick = input("Do you want to see a text file or an img? For txt type 1, for img type 2: ")

if pick == "1":
    try: 
        with open("MouzaAlameri.txt", "r") as file:
            print(file.read())
    except Exception:
        print("ERROR BYE LOSER")

elif pick == "2":
    try: 
        img = Image.open("Mouza.png")  
        img.show()
    except Exception: 
        print("ERROR BYE! PFFTT ")

else: 
    print("pls stick to what was given to you")
