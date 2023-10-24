def print_pattern(n):
  
  for i in range(n):
    for j in range(n):
      if i == j or i + j == n - 1:
        print("*", end="")
      else:
        print(" ", end="")
    print()

if __name__ == "__main__":
  n = int(input("Enter the number of rows and columns: "))
  print_pattern(n)
def print_diamond_pattern(n):
  
  for i in range(n):
    for j in range(n):
      if abs(i - j) <= n - 1 - i:
        print("*", end="")
      else:
        print(" ", end="")
    print()

if __name__ == "__main__":
  n = int(input("Enter the number of rows and columns: "))
  print_diamond_pattern(n)
