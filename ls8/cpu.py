"""CPU functionality."""

import sys

HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # check the spec
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.branchtable = {}
        self.branchtable[HLT] = self.handle_HLT
        self.branchtable[LDI] = self.handle_LDI
        self.branchtable[PRN] = self.handle_PRN
        self.branchtable[MUL] = self.handle_MUL

    def handle_HLT(self):
        sys.exit(0)

    def handle_LDI(self):
        register = self.ram_read(self.pc + 1)
        value = self.ram_read(self.pc + 2)
        self.reg[register] = value
        self.pc += 3

    def handle_PRN(self):
        reg = self.ram_read(self.pc+1)
        print(self.reg[reg])
        self.pc += 2

    def handle_MUL(self):
        register = self.ram_read(self.pc + 1)
        register2 = self.ram_read(self.pc + 2)
        self.reg[register] *= self.reg[register2]
        self.pc += 3

    def load(self):
        """Load a program into memory."""
        address = 0

        if len(sys.argv) != 2:
            print('Incorrect Usage Error: python ls8.py [filename]')
            sys.exit(1)

        # open the file
        filename = sys.argv[1]
        try:
            with open(filename) as program:
                for address, line in enumerate(program):
                    # ignore anything after # comments
                    instruction = line.split('#')[0].strip()
                    if instruction == '':
                        continue
                    else:
                        self.ram[address] = int(f"0b{instruction}", 2)
        except FileNotFoundError:
            print("File not found.")
            sys.exit(1)

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

        while running:
            command = self.ram_read(self.pc)
            if command in self.branchtable:
                self.branchtable[command]()
            else:
                print(f"Unknown instruction: {command} at pc {self.pc}")
                sys.exit(1)

    def ram_read(self, mar):
        ''' Looks in memory and returns the value found there. Normally MAR (Memory Address Register) is an internal register in the CPU that stores the address to look at, however in this instance, the function just takes the MAR to read from and returns the value it finds there.'''
        return self.ram[mar]

    def ram_write(self, mar, mdr):
        ''' Accepts a mar and mdr (Memory Data Register) and it will write the value of the MDR at the given MAR. Like ram_read(), these registers are internally within a CPU, but instead they will be used as parameter names. '''
        self.ram[mar] = mdr
