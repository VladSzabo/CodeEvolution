from Evolution import Evolution
"""import os


print("TEST!!!!")
os.system('cd ..')
os.system('dir')
os.system('python Main.py')
"""


def main():
    file = open("settings.txt")

    species_per_generation = int((file.readline().split())[2])
    processes_per_run = int((file.readline().split())[2])
    lines_per_generation = (file.readline().split()[2]).split('-')
    lines_per_generation = [int(lines_per_generation[0]), int(lines_per_generation[1])]
    run_time = int((file.readline().split())[3])

    Evolution(species_per_generation, processes_per_run, lines_per_generation, run_time)


if __name__ == "__main__":
    main()