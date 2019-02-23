# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Use the file name mbox-short.txt as the file name

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
lst = list()

for line in handle:
    line = line.strip()
    if not line.startswith("From "): continue
    spline = line.split()
    lst.append(spline[1])

for email in lst :
    counts[email] = counts.get(email, 0)+1

maxcount = None
maxemail = None
for email,count in counts.items() :
    if maxcount is None or count > maxcount:
        maxemail = email
        maxcount = count
print(maxemail, maxcount)
