#Validate a given public IP address to check if it follows the correct format (IPv4).


def ipChecker(ipAddr):
    ipOctets=ipv4Address.split(".")
    
    if len(ipOctets)!=4:
        return f"Invalid Ip"
    
    for octet in ipOctets:
        if not octet.isdigit():
            return f"Invalid Ip"
            
        if int(octet)<0 or int(octet)>255:
            return f"Invalid Ip"
        

    return f"Valid Ip"


ipv4Address=input("Enter ip to check")
print(ipChecker(ipv4Address))


# Validate a given email address to check if it’s a valid Gmail address, considering:
# ○ It should contain "@gmail.com".
# ○ The username before "@gmail.com" should contain only lowercase letters , numbers and permitted
# symbols.

# def emailChecker(emailId):
    
#     endSeq=emailId[-10:]
    
#     if endSeq!="@gmail.com":
#         return "Invalid Email"
#     usrName=emailId[:-10]
    
#     allowedSeq={".","_"}
    
#     for ch in usrName:
#         if not (ch.islower() or ch.isdigit() or ch in allowedSeq):
#             return "invalid email"
    
    
#     return "valid email"
    
    
# emailId=input("Enter your email ")
# print(emailChecker(emailId))