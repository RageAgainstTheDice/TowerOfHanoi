def move(start_position, end_position):
    print(f'Move disc from {start_position} to {end_position}.')


def hanoi(num_disks, start_position, helper_position, end_position):
    if num_disks == 0:
        pass
    else:
        hanoi(num_disks - 1, start_position, end_position, helper_position)
        move(start_position, end_position)
        hanoi(num_disks - 1, helper_position, start_position, end_position)


if __name__ == '__main__':
    disks = int(input('Enter number of disks to use in hanoi problem: '))
    print(f'(There are {pow(2, disks) - 1} steps.)')
    hanoi(disks, 'A', 'B', 'C')

