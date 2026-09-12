#creating a simple dictionary structure

phone_number = {
    'Aakash' : '9489484949',
    'Hemanth' : '9595949494',
    'Siddhant' : '9231325312'
}

#accesing a persons phone number with the key
print(phone_number['Hemanth'])

#adding new phone numbers or updating existing
phone_number['Saurav'] = '8457548856' #adding
phone_number['Aakash'] = '7896781641' #updating

for name in phone_number:
    print("Name:",name,',Phone number:',phone_number[name])
