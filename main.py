print("Welcome to the Rollercoaster Ride. You will be charged after your answers.")
height = int(input("Please enter your height in cm without decimals: "))
age = int(input("What is your age?: "))
photo = input("Do you want your picture taken? (Y / N): ")
bill = 0

#For all heigher than 120 cm
if height >= 120:
  print("You can ride.")
  if age < 12:
    bill = 5
    print("Please pay $5.")
  elif age <= 18:
    bill = 7
    print("Please pay $7.")
  else:
    bill = 12
    print("Please pay $12.")
  #Add $3 to bill      
  if photo == "Y":
    bill += 3

#Happens if Y and if N so respects indentation
  print(f"Your final bill is $ {bill}.")
#For those lower than 120 cm    
else:
  print("Sorry, drink more milk and come back later!.")


