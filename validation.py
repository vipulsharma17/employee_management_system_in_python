def isMobileValid(str):
    if len(str)==10:
        if str.isdigit():
            return True
        else:
            return False
    else:
        return  False
def isDateValid(str):
    #  format is "dd-mm-yyyy"
    
    day, month, year = map(int, str.split('/'))
    

    #  maximum days for each month
    max_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if year is a leap year
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        max_days[1] = 29

    #if month and day are within valid ranges
    if month < 1 or month > 12 or day < 1 or day > max_days[month - 1]:
        return False

    # if the year is not in the future
    from datetime import datetime
    current_year = datetime.now().year
    if year > current_year:
        return False

    return True
def isAgeValid(a):
    
    if a.isdigit():
        return True

    else:
         return False
def isGenderValid(str):
    lst=['male','female']
    if str.lower() not in lst:
        return False
    else:
        return True

def isNameValid(str):
    if str != "":
        l=str.split()
        for i in l:
            if (not i.isalpha()):
                return False
    else:
        return False
    for i in l:
        if not(i[0].isupper()):
            return False
    return True

def isPanValid(str):
    if len(str)==10:
        s1=str[0:5]
        s2=str[5:9]
        s3=str[-1]
        if not s1.isalpha():
           return False
        if not s2.isdigit():
            return False
        if not s3.isalpha():
            return False
        return True
    else:       
            return False
def isAadharValid(n):
    if len(n) ==12:
        if n.isdigit():

            return True
    else:
        return False
        