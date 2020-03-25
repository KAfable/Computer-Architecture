# Computer Architecture

## RAM

- think of it as a big array of bytes that you can access by index
- each element in RAM can store one byte, an 8bit number
- values larger than that are stored in sequential addresses
- CPU communicates with RAM via memory bus

## CPU

- Register
  - stores information that can be accessed at ultra high speed (faster than RAM)
  - similar to variables that the CPU has as its disposal
  - fixed names like RO, R1, or EAX, EBX
- Instructions
  - stored in RAM with other data
  - just numbers
  - humans use mnemonics to refer to instruction in a readable way
- Clock
  - click on a modern CPU triggers a few billion times per second
  - clock cycle is measued in hz
- Cores
  - CPU can share RAM, but perform instructions independent of each other

## Concurrency

- each hardware component can only do one thing at once
- duplicate hardware components
- time sharing - not true parallelism, but concurrency by time sharing

## Bitwise Operations

- work on numeric values, versus boolean only working with boolean values
- AND, OR, NOT
- XOR, NOR, NAND
- bitwise operations apply to multibit numbers
- need to know what a bitwise AND or a bitwise OR, going column by column
- need to know how bitshifting works for sprint challenge

## Stack

- when handling interrupts, the entire CPU state is saved on the stack

## Interrupts

- when a peripheral needs to alert the CPU that it needs attention
