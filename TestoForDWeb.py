import subprocess


output_file = 'drivers.txt'
with open(output_file, 'w') as file:
    subprocess.run(['driverquery', '/FO', 'CSV'], stdout=file)

with open(output_file, 'r') as file:
    lines = file.readlines()
    headers = lines[0].strip().split(',')
    type_index = headers.index('"Type"')

    print('"File System":')
    for line in lines[1:]:
        columns = line.strip().split(',')
        if columns[type_index].strip('"') == 'File System':
            print(line.strip())

