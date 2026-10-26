project_name = input("What is your project called? ")
objective = input("What outcome do you want? ").strip()
users = input("Who will use the result? ")
success = input("What will a successful result look like? ")

print("\nPROJECT BRIEF")
print("Project:", project_name)
if objective == "":
    print("Missing information: please describe your project objective. ")
else: 
    print("Objective:", objective)
if users == "":
    print("Missing information: please describe your project users. ")
else: print("Users:", users)
print("Success:", success)