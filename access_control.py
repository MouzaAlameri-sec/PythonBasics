__Author__="Mouza Alameri"
__Date__ = "04/05/2025"
__Github__ ="https://github.com/MouzaAlameri-sec" 


username = input("please give me ur username : " )
password = input("Give me a password :   ")

users= {
    "Mouza" : "SuperAdmin",
    "Alameri" : "1234",
    "sec" : "cat" 
    }

if username in users and users[username] == password: 
    print("Great access granted")

else: 
    print("tough luck homie - NO ACCESS")