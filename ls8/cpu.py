"""CPU functionality."""

import sys


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # check the spec
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0

    def load(self):
        """Load a program into memory."""
        address = 0

        if len(sys.argv) != 2:
            print('Incorrect Usage Error: python ls8.py [filename]')
            sys.exit(1)

        # open the file
        filename = sys.argv[1]
        with open(filename) as program:
            for address, instruction in enumerate(program):
                self.ram[address] = instruction

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """ Handy function to print out the CPU state. You might want to call this from run() if you need help debugging."""

        print(
            f"TRACE: {self.pc} | {self.ram_read(self.pc)} {self.ram_read(self.pc + 1)} {self.ram_read(self.pc + 2)} |", end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        self.pc = 0
        running = True

        HLT = 1
        LDI = 130
        PRN = 71

        while running:
            command = self.ram_read(self.pc)

            if command == HLT:
                running = False
                sys.exit(0)
            elif command == LDI:
                register = self.ram_read(self.pc + 1)
                value = self.ram_read(self.pc + 2)
                self.reg[register] = value
                self.pc += 3
            elif command == PRN:
                reg = self.ram_read(self.pc+1)
                print(self.reg[reg])
                self.pc += 2
            else:
                self.trace()
                print(f"Unknown instruction: {command} at pc {self.pc}")
                sys.exit(1)

    def ram_read(self, mar):
        ''' Looks in memory and returns the value found there. Normally MAR (Memory Address Register) is an internal register in the CPU that stores the address to look at, however in this instance, the function just takes the MAR to read from and returns the value it finds there.'''
        return self.ram[mar]

    def ram_write(self, mar, mdr):
        ''' Accepts a mar and mdr (Memory Data Register) and it will write the value of the MDR at the given MAR. Like ram_read(), these registers are internally within a CPU, but instead they will be used as parameter names. '''
        self.ram[mar] = mdr
