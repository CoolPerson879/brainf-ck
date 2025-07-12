#!/usr/bin/env python3
"""
Simple Brainf*ck Interpreter

This interpreter supports the 8 basic brainf*ck commands:
> : Move pointer right
< : Move pointer left
+ : Increment cell value
- : Decrement cell value
. : Output cell value as ASCII character
, : Input character and store in cell
[ : Jump forward to matching ] if cell is 0
] : Jump back to matching [ if cell is not 0
"""

import sys
import os


class BrainfuckInterpreter:
    def __init__(self):
        self.memory = [0] * 30000  # 30,000 cells initialized to 0
        self.pointer = 0           # Memory pointer
        self.code = ""             # Brainf*ck code
        self.code_pointer = 0      # Code pointer
        self.input_buffer = ""     # Input buffer
        self.output_buffer = ""    # Output buffer
    
    def load_code(self, code):
        """Load brainf*ck code into the interpreter"""
        # Filter out non-brainf*ck characters
        valid_chars = set('><+-.,[]')
        self.code = ''.join(c for c in code if c in valid_chars)
        self.code_pointer = 0
    
    def run(self, input_text=""):
        """Run the loaded brainf*ck code"""
        self.input_buffer = input_text
        self.output_buffer = ""
        input_index = 0
        
        while self.code_pointer < len(self.code):
            command = self.code[self.code_pointer]
            
            if command == '>':
                self.pointer += 1
                if self.pointer >= len(self.memory):
                    self.memory.extend([0] * 1000)  # Extend memory if needed
            
            elif command == '<':
                self.pointer -= 1
                if self.pointer < 0:
                    self.pointer = 0  # Prevent going below 0
            
            elif command == '+':
                self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 256
            
            elif command == '-':
                self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 256
            
            elif command == '.':
                self.output_buffer += chr(self.memory[self.pointer])
                print(chr(self.memory[self.pointer]), end='')
            
            elif command == ',':
                if input_index < len(self.input_buffer):
                    self.memory[self.pointer] = ord(self.input_buffer[input_index])
                    input_index += 1
                else:
                    # If no input available, set to 0
                    self.memory[self.pointer] = 0
            
            elif command == '[':
                if self.memory[self.pointer] == 0:
                    # Jump forward to matching ]
                    bracket_count = 1
                    while bracket_count > 0 and self.code_pointer < len(self.code) - 1:
                        self.code_pointer += 1
                        if self.code[self.code_pointer] == '[':
                            bracket_count += 1
                        elif self.code[self.code_pointer] == ']':
                            bracket_count -= 1
            
            elif command == ']':
                if self.memory[self.pointer] != 0:
                    # Jump back to matching [
                    bracket_count = 1
                    while bracket_count > 0 and self.code_pointer > 0:
                        self.code_pointer -= 1
                        if self.code[self.code_pointer] == ']':
                            bracket_count += 1
                        elif self.code[self.code_pointer] == '[':
                            bracket_count -= 1
            
            self.code_pointer += 1
        
        return self.output_buffer


def run_brainfuck_file(filename, input_text=""):
    """Run a brainf*ck file"""
    try:
        with open(filename, 'r') as f:
            code = f.read()
        
        interpreter = BrainfuckInterpreter()
        interpreter.load_code(code)
        output = interpreter.run(input_text)
        
        return output
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error running '{filename}': {e}")
        return None


def main():
    """Main function to run the interpreter"""
    if len(sys.argv) < 2:
        print("Usage: python brainfuck_interpreter.py <filename.bf> [input]")
        print("Example: python brainfuck_interpreter.py helloworld.bf")
        sys.exit(1)
    
    filename = sys.argv[1]
    input_text = sys.argv[2] if len(sys.argv) > 2 else ""
    
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    print(f"Running {filename}...")
    print("-" * 40)
    
    output = run_brainfuck_file(filename, input_text)
    
    print("\n" + "-" * 40)
    if output is not None:
        print(f"Program completed successfully.")
    else:
        print("Program failed to run.")


if __name__ == "__main__":
    main()