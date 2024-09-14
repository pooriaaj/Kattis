def extract_initials(name):
    return ''.join(part[0] for part in name.split('.'))

name = input()
print(extract_initials(name))
