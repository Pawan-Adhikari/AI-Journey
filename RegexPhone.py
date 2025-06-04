#RegexPhone.py
#Use re module and regex format to match phone number from string

import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d)')

mo = phoneNumRegex.search('My phone number is 458-324-452.')

print(phoneNumRegex)

print(mo)

print('The phone number found is: ' + mo.group())

    