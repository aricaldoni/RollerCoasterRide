print("Welcome to the Rollercoaster Ride. You will be charged accordingly:")
height = int(input("Please enter your height in cm without decimals: "))
age = int(input("What is your age?: "))
bill = 0

#For all heigher than 120 cm
if height >= 120:
  if age < 12:
    bill = 5
  elif age <= 18:
    bill = 7
  elif age >= 45 and age <= 55:
    bill = 0
  else:
    bill = 12

  #Add $3 to bill
  photo = input("Do you want your picture taken? (Y / N): ")    
  if photo == "Y":
    bill += 3
#Happens if Y and if N so respects indentation
  print(f"Your final bill is $ {bill}.")
#For those lower than 120 cm    
else:
  print("Sorry, drink more milk and come back later!.")


