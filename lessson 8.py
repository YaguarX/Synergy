def is_poli(word):
    reversed_str = word[::-1]
    return word == reversed_str

print(is_poli('walag'))
print(is_poli('walaw'))

#2 sposob

good = 'walaw'

if good[::1] == good[::-1]:
    print('True')
else:
    print('False')

wagi = 'Eto    nuzhno napisat    s  normalnymi probelami   '
desic = ' '.join(wagi.split())
print(desic)
