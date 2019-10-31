limit = int(input("Enter upper limit: "))
sequence = "1 1"

file = open(str(limit) + "_len.txt","w")

print("\n1 1")

for n in range(2, limit + 1):
  p = n
  highest_n = n
  while p != 1:
    if p % 2 == 0:
      p = p / 2
    else:
      p = (3 * p) + 1

    if p > highest_n:
      highest_n = int(p)

  sequence += ("\n" + str(n) + " " + str(highest_n))
  print(str(n) + " " + str(highest_n))

print("\nFile " + file.name + " created.")

file.write(sequence)
file.close()
