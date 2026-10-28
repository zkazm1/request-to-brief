project_name = input("What is your project called? ")
sections = ["Objective", "Users", "Success criteria", "Budget"]
answers = {}
for section in sections:
    answer = input(f"{section}: ").strip()
    answers[section]=answer
    if(answer==""):
        print(f"you entered a blank for {section}.")
    else:
        print("You entered:", answer)

print("\nPROJECT BRIEF")
print(f"Project Name: {project_name}")
for x, y in answers.items():
    if y=="":
        y="Not specified"
    print(f"{x}: {y}")
