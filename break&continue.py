# Break Statement
for i in "DevOps":
    print(i)
    if i == "O":
        print("found my data")
        break
print("Out of the loops")

# Continue Statement
for i in "DevOps":
    print(i)
    if i == "O":
        print("found my data")
        continue
    print(f"value of i is {i}")
print("Out of the loops")

# Break example 2 
import random
company = ["IBM", "Wipro", "HCLTech", "TCS"]

random.shuffle(company)
print(company)

LUCKY = random.choice(company)
print(LUCKY)

for com in company:
    print(f"*********** Giving interview in {com}")
    if com ==  LUCKY:
        print("####################")
        print(f"{LUCKY} IT company, You got selection based on your interview. ! Good luck")
        print()
        break
    print("XXXXXXXXX")
    print("Test Failed")

# Continue Again example 2 
import random
company = ["IBM", "Wipro", "HCLTech", "TCS"]

random.shuffle(company)
print(company)

LUCKY = random.choice(company)
print(LUCKY)

for com in company:
    print(f"*********** Giving interview in {com}")
    if com ==  LUCKY:
        print("####################")
        print(f"{LUCKY} IT company, You got selection based on your interview. ! Good luck")
        print()
        continue
    print("XXXXXXXXX")
    print("Test Failed")



