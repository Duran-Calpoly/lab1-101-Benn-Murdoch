pass
def check_multiple(number):
    return number % 3 == 0 and number % 5 == 0


def check_password(input_string): 
    password = "Python123"
    if input_string == password:
        return "access granted"
    else :
        return "access denied"
    


def calculate_federal_tax(salary): 
    if salary <= 11_000 :
        return salary*0.1
    elif salary <= 44_725:
        return salary* 0.12
    elif salary <= 95_375:
        return salary*0.22
    else: 
        return salary*0.24

#done