# Escape Character
'''
These are special characters used to represent non-printable or social charactes within a string
\ : Backslash,
\n: Newline,
\t: Tab,
\r: Carriage Return
'''

# print('I'll call you later') - Error
print('I\'ll call you later')
print("I'll call you later")
print("Prepare well for \"GATE-2024\" exam")

a = "Hello,\nABC!\n"
print(a)

y = "Hello,\tABC!"
print(y)

x = "no__benefits__of_study\rHuge_benefits"
print(x)