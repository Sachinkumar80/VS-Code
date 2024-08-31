# Buit in Function for Data manipulation.

number = [1,2,3,4,5,87,54]
print(max(number))   #  Output 87
print(min(number))   #  Output 1
print(len(number))   #  Output 7
print(sum(number))   # Output 156 

message = "work hard for your family, make your parents proud of you !"
print(message.capitalize())
print(message)

# dir() function
print(dir(message))
print(dir([]))
print(dir({}))
print(dir(""))

print(message.upper())
print(message.islower())
print(message.isupper())

print(message.find("proud"))
print(message[18:46])
print(message.find("not"))

ip = ("192", "168", "77", "63")
print(".".join(ip))
print("+".join(ip))
print("/".join(ip))

tools = ["Vagrant", "bash", "cli", "automation", "cloud"]
print(tools)

tools.append("Jenkins")
print(tools)

tools.extend(["Cloudformation"])
print(tools)

tools.insert(2,"Ansible")
print(tools)

tools.pop()
tools.pop()
tools.pop()
print(tools)

