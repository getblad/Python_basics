from sys import argv

hours = int(argv[1])
hourly_rate = int(argv[2])
bonuses = int(argv[3])

print(f'Заработная плата сорудников {hours * hourly_rate / bonuses}')