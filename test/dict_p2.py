favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for i in favorite_languages.keys():
    print(i)

for i in favorite_languages:
    print(i)

for i in sorted(favorite_languages.keys()):
    print(i)

for i in favorite_languages.values():
    print(i)

for i in set(favorite_languages.values()):
    print(i)