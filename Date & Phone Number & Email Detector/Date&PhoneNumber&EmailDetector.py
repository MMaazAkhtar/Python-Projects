
import re, pyperclip

regex = re.compile(r'''
                   (\d{1,2})   # day
                   (/|-)    # separator
                   (\d{1,2})   # month
                   (/|-)    # separator
                   (\d{2,4})  # year
                   ''', re.VERBOSE)

def date_validator(days,months,years):
    
    if months in[4,6,9,11] and 0 < days < 31:
        return True
    elif months in [1,3,5,7,8,10,12] and 0 < days < 32:
        return True
    elif months == 2 and 0 < days < 29:
        return True
    elif months == 2 and days == 29:
        if years % 4 == 0 and  years % 100 != 0:
            return True
    elif years % 4 == 0 and  years % 100 == 0:
        if years % 400 == 0:
            return True
        else:
            return False
    else:
        return False
    
    return False
text = str(pyperclip.paste())
matches = []
for groups in regex.findall(text):
    days,months,years = int(groups[0]),int(groups[2]),int(groups[4])
    if date_validator(days,months,years):
        date = '/'.join([groups[0], groups[2], groups[4]])
        matches.append(date)

phoneregex = re.compile(r'''(
(\d{3}|\(\d{3}\))? # area code
(\s|-|\.)? # separator
(\d{3}) # first 3 digits
(\s|-|\.) # separator
(\d{4}) # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
)''', re.VERBOSE)

emailregex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # username
    @                       # @ symbol
    [a-zA-Z0-9._%+-]+       # domain name
    (\.[a-zA-Z]{2,4})       # dot-something                                              
)''',re.VERBOSE)

for groups in phoneregex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += 'x' + groups[8]
    matches.append(phoneNum)
for groups in emailregex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to Clipboard')
    print('\n'.join(matches))
else:
    print("No dates or phone numbers or email addresses found.")