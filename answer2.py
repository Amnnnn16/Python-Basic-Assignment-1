import random
import string

def pswd_genrator():
    
    #create a character pool for mandatory
    lowercase=string.ascii_lowercase
    upper=string.ascii_uppercase
    digit=string.digits
    special="$#%!@*"
    pswd=[random.choice(lowercase),random.choice(upper),random.choice(digit),random.choice(digit),random.choice(special)]
    extras=random.sample(lowercase+upper+digit+special,11)
    pswd.extend(extras)
    return "".join(pswd)

print(pswd_genrator())