#! python3
# strongPasswordDetector.py - determines if password is strong. Passwords should be 8 characters long, contains uppercase , lowercase characters, and has digits

import re

passwordRegex = re.compile(r'(A-Za-z)(0-9)+')

samplePass = passwordRegex.findall("PARd00nMySw4G")
print(samplePass)