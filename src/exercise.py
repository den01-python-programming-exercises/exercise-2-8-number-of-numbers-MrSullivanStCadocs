def main():
    #write your code below this line
    totalNumbers = 0

    while True:
      number = int(input("Give a number:"))
      if (number == 0):
        break
    
      if (number != 0):
        totalNumbers = totalNumbers + 1

    print("Number of numbers: " + str(totalNumbers))

if __name__ == '__main__':
    main()
