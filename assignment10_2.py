# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# Use the file name mbox-short.txt as the file name

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
lst = list()

for line in handle:
    line = line.strip()
    if not line.startswith("From "): continue
    spline = line.split()[5].split(":")
    lst.append(spline)

for hour in lst :
    counts[hour[0]] = counts.get(hour[0], 0) + 1

for hour,count in sorted(counts.items()) :
    print(hour, count)
