# jbp = "The Joe Budden podcast"
# capitalize("new joe Budden")
# len(jbp)
# lower("hello world")

s = " welcome to python\t"
# s1 = s.capitalize()
# s2 = s.title()
# s3 = s.lower()
# s4 = s.upper()
# s5 = s.swapcase()
# s7 = "ABABAB".replace("AB", "ET", 2)

# j = s.lstrip()
# jj = s.rstrip()
# jmj = s.strip()

# jus = input("Enter a string").rstrip()


# print(jus)

# s1 = " Welcome "
# s2 = " welcome "

# isEqual = s1 == s2
# isEqual = s1.lower() == s2.lower()
# b = s1.startswith("AAA")
# bs = s1.endswith("aaa")
# x = s1[0]
# s3 = s1 + s2
# s3 = s1.lower()
# s1[1:]
# x = s1.find('e')

# letterGrade = input("Enter a letter grade: ").upper()

# if letterGrade == 'A':
#   print("The numberic value for grade: ", letterGrade, "is", 4)
# elif letterGrade == 'B':
#   print("Enter a letter grade: ", letterGrade, "is", 3)
# elif letterGrade == 'C':
#   print("Enter a letter grade: ", letterGrade, 2)
# elif letterGrade == 'D':
#   print("Enter a letter grade: ", letterGrade, 1)
# elif letterGrade == 'F':
#   print("Enter a letter grade: ", letterGrade, 0)
# else: print(letterGrade, "is an invalid grade")

# year = int(input("Enter a year: "))
# month = input("Enter a month: ")




# message = "python is fun".upper()

# hexDigit = input("Enter a hex digit: ")
# hexDigit = hexDigit.upper()
# if hexDigit == "B":
#   print("The binary value is ", 1011)
# else: print("Invalid input")

# months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
# days =  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# year = int(input("Enter a year: "))
# month = input("Enter month: ")


# if month not in months:
#   print(month, "is not a correct month name")

# else:
#   leap = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)

#   if leap and month == "Feb":
#     print(month, year, "has 29 days")
#   else:
#     print(month, year, 'has', days[month.index(month)] ,'days')
  
year = int(input("Enter a year: "))
month = input("Enter a month (first three letters with the first letter in uppercase): ")

if month == "Jan" or month == "Mar" or month == "May" \
or month == "Jul" or month == "Aug" or month == "Oct" or month == "Dec":
  print(month, year, "has 31 days")
elif month == "Apr" or month == "Jun" or month == "Sep" or month == "Nov":
  print(month, year, "has 30 days")
elif month == "Feb":
  if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(month, year, "has 29 days")
  else:
      print(month, year, "has 28 days")
else:
  print(month, "is not a correct month name ")