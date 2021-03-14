def namelist(names):
    name = ''

    if len(names) != 0:
        name_list = []

        for i in range(0, len(names) - 1):
            name_list.append(names[i]['name'])
            name = ', '.join(name_list)

        if name != '':
            name += ' & ' + names[-1]['name']
        else:
            name += names[-1]['name']

    return name
