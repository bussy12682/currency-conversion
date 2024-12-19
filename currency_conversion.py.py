#Write a code for converting 10 different currencies to naira which takes the input ten different currencies, their conversion rate and 
#output the result
currencies = ["Usd", "canadian_dollar", "euro", "swiss_franc", "indian_rupee", "brazilian_real", "chinese_yuan", "australia_dolla", "japan_yen", "british_pound", "rusian_ruble", "south_african_rand", "mexican_peso", "saudi_riyals", "turkish_lira", "south_korean_won", "singapore_dollar", "malaysia_ringgit","egypt_pound", "aregentine_peso", "kenyan_shilling", "ghanaian_cedi", "ugandan_shilling"]

# rusian_ruble = 14
# south_african_rand = 42
# mexican_peso = 53
# saudi_riyals = 210
# turkish_lira = 31
# south_korean_won = 1
# singapore_dollar = 567
# malaysia_ringgit = 157
# egypt_pound = 41.80
# aregentine_peso = 4.18
# kenyan_shilling = 5.73
# ghanaian_cedi = 660.34
# ugandan_shilling = 0.21
# Usd = 1533
# canadian_dollar = 1192
# euro = 1703
# swiss_franc = 1820
# indian_rupee = 9
# brazilian_real = 149
# chinese_yuan = 112
# australia_dollar = 985
# japan_yen = 12
# british_pound = 1966


print("There are twenty three (23) currencies listed above ")
print()

#user input
question = input(f'Do you want to convert any currency "yes" or "no":')
if question == "yes":
  print("ok")
elif question == "no":
  exit()

Account = input(f'Do you have an account "yes" or "no":')  
if Account == "yes":
        print("ok you can proceed")
elif Account == "no":
        print("Ok, you have to create an account before you can make any conversion")

# #bank_creation
print("pls create a bank account")

first_name = input("pls enter your first name")
middle_name = input("pls enter your second name")
last_name = input("pls enter your third name")
phone_number = int(input("input your phone number"))
Nin_number = int(input("enter your Nin number"))


#persons details
print(first_name)
print(middle_name)
print(last_name)
print(phone_number)
print(Nin_number)

print("creation of bank in process")
print("........")
print("........")
print("Bank successfully created")

currency_choice = input("Which currency do you want to convert? ")
if currency_choice in currencies:
      print("currency found")
else: 
 print("Currency not found, pls input the right text")
amount_to_be_converted = int(input("how much do you wanna convert? "))

print("Checking for currency rate.........")
print("..........")
print("Currency rate updated")

#convertion level
if currency_choice == currencies[0]:
        conversion = amount_to_be_converted * 1533
        print("conversion successfully made")
        print(f'your amount after conversion is {conversion}')
        print("NOTE: As currency rate rises, it will be updated over here")
        exit()
       
elif currency_choice == currencies[1]:
         conversion = amount_to_be_converted * 1192
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[2]:
         conversion = amount_to_be_converted *  1702 
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[3]:
         conversion = amount_to_be_converted * 1820  
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[4]:
         conversion = amount_to_be_converted * 9 
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[5]:
         conversion = amount_to_be_converted * 149 
         print("conversion successfully made") 
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[6]:
         conversion = amount_to_be_converted * 112  
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[7]:
         conversion = amount_to_be_converted * 985
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[8]:
         conversion = amount_to_be_converted * 12
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[9]:
         conversion = amount_to_be_converted * 1966
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[10]:
         conversion = amount_to_be_converted * 14
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[11]:
         conversion = amount_to_be_converted * 42
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[12]:
         conversion = amount_to_be_converted * 53
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[13]:
         conversion = amount_to_be_converted * 210
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[14]:
         conversion = amount_to_be_converted * 31
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[15]:
         conversion = amount_to_be_converted * 1
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[16]:
         conversion = amount_to_be_converted * 567
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[17]:
         conversion = amount_to_be_converted * 157
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()  
elif currency_choice == currencies[18]:
         conversion = amount_to_be_converted * 41.80
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[19]:
         conversion = amount_to_be_converted * 4.18
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[20]:
         conversion = amount_to_be_converted * 5.73
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[21]:
         conversion = amount_to_be_converted * 660.34
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()
elif currency_choice == currencies[22]:
         conversion = amount_to_be_converted * 0.21
         print("conversion successfully made")
         print(f'your amount after conversion is {conversion}')
         print("NOTE: As currency rate rises, it will be updated over here")
         exit()  
else:
 print("input the right currency")    

#created by enoch