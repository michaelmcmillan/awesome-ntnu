sections = {}

with open('readme.md') as readme:
    current_section = None

    for line in readme.readlines():

        if line.startswith('##'):
            current_section = line[3::].rstrip()
            sections[current_section] = []

        if line.startswith('-'):
            list_element = line[2::]
            sections[current_section].append(list_element)

for section in sections:
    list_elements = sections[section]
    if not list_elements == sorted(list_elements, key=str.lower):
        raise ValueError('"%s" is not sorted alphabetically.' % section)
