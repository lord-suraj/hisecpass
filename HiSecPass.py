# A Program To Create Highly Secure Passwords For Social Media Accounts.

# Author @lord_suraj

import random

from string import digits

from string import punctuation

from string import ascii_letters

symbols = ascii_letters + digits + punctuation

secure_random = random.SystemRandom()

password = "".join(secure_random.choice(symbols)for i in range(20))

print ("Your Highly Secure Password Is :" , password)

