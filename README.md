# brainf*ck
The most goated language to ever exist.
If you program software using brainf*ck, you are an absolute gigachad. You have earned my respeccct.

## What's in this repository

This repository contains:
- **brainf*ck programs** (`.bf` files): Various brainf*ck programs
- **brainfuck_interpreter.py**: A Python-based brainf*ck interpreter
- **Other language files**: Some programs in Rust and TypeScript

## How to run the brainf*ck programs

Use the included Python interpreter:

```bash
python brainfuck_interpreter.py <filename.bf>
```

Examples:
```bash
python brainfuck_interpreter.py helloworld.bf
python brainfuck_interpreter.py hellos.bf
python brainfuck_interpreter.py i-use-arch-btw.bf
```

## Test all programs

Run all brainf*ck programs at once:
```bash
python test_all.py
```

## Available Programs

- **helloworld.bf**: Classic "Hello World!" program
- **hellos.bf**: Prints multiple greetings
- **i-use-arch-btw.bf**: A fun program for Arch Linux users

## About Brainf*ck

Brainf*ck is an esoteric programming language created in 1993 by Urban Müller. It consists of only 8 commands:
- `>` : Move pointer right
- `<` : Move pointer left  
- `+` : Increment cell value
- `-` : Decrement cell value
- `.` : Output cell value as ASCII character
- `,` : Input character and store in cell
- `[` : Jump forward to matching `]` if cell is 0
- `]` : Jump back to matching `[` if cell is not 0  
