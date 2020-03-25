import sys

# op codes
HALT = 1
PRINT_NUM = 3
SAVE = 130  # Save a value to a register
PRINT_REGISTER = 71  # Print a value from a register
ADD = 6  # regA += regB
MUL = 162

memory = [None] * 256

register = [0] * 8

pc = 0
reg = 0
running = True


def load_memory(filename):
    '''Takes a file and loads it up into the emulated LS8's memory.'''
    address = 0
    try:
        with open(filename) as f:
            for line in f:
                # ignore comments
                comment_split = line.split("#")
                # strip out whitespace
                num = comment_split[0].strip()
                # ignore blank lines
                if num == '':
                    # what does continue do?
                    continue
                val = int(num, 2)
                memory[address] = val
                address += 1
    except FileNotFoundError:
        print("File not found")
        sys.exit(2)


if len(sys.argv) != 2:
    print("Error: Correct Usage is: simple.py filename")
    sys.exit(1)

filename = sys.argv[1]
load_memory(filename)

while running:
    command = memory[pc]

    if command == HALT:
        running = False
        pc += 1

    elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 2

    elif command == SAVE:
        num = memory[pc + 2]
        reg = memory[pc + 1]
        print(f'looking for {reg}')
        print(f'register in save {register}')
        register[reg] = num
        pc += 3

    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(register[reg])
        pc += 2

    elif command == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        pc += 3

    elif command == MUL:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] *= register[reg_b]
        pc += 3

    else:
        print(f"Unknown instruction: {command}")
        sys.exit(1)
