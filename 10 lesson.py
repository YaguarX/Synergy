#1
pets = {
    input('name:'):
        {
            'animal_type':input('type:'),
            'animal_age':int(input('age:')),
            'animal_owner':input('owner_name:')
        }
}
print(pets)

users_true = {
    'ivan':{
        'type':'monkey',
        'age':str(18),
        'name':'borya'
    },
    'sasha':{
        'type':'zheltyi_pitoon',
        'age':str(19),
        'name':'Kaa'
    }
}

for users_name, info_users in users_true.items():
    if users_name == 'sasha':
        print(f'Это' + info_users['type'] + ' по кличке ' + info_users['name'] + '. Возраст питомца: ' + info_users['age'] + ' лет. Имя владельца: ' + users_name)
#2
 for i in reversed(range(-5,11)):
     my_dict = {
         i:(i**i)
     }
     print(my_dict)