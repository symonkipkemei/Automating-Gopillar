
# It is easier to copy the link rather than copy the ID

projectLink = "https://app.gopillar.com/contests/5ea7b1055bbf36002633245c/submissions"
print(len(projectLink))
projectID = projectLink[34:58]
print(projectID)

print("\n")

projectLink = "https://app.gopillar.com/contests/5eae0ef35bbf36002633d32e/submissions"
projectID = projectLink[34:58]
print(projectID)

print("\n")

projectLink = input("Insert the project link: ")
projectID = projectLink[34:58]
print(projectID)