#!/usr/bin/env python3
"""
Simple test runner for all brainf*ck files
"""

import os
import sys
from brainfuck_interpreter import run_brainfuck_file


def test_all_bf_files():
    """Test all .bf files in the current directory"""
    bf_files = [f for f in os.listdir('.') if f.endswith('.bf')]
    
    print("Testing all brainf*ck files:")
    print("=" * 50)
    
    for bf_file in sorted(bf_files):
        print(f"\nRunning {bf_file}:")
        print("-" * 30)
        
        try:
            output = run_brainfuck_file(bf_file)
            if output is not None:
                print(f"✓ {bf_file} executed successfully")
            else:
                print(f"✗ {bf_file} failed to execute")
        except Exception as e:
            print(f"✗ {bf_file} error: {e}")
    
    print("\n" + "=" * 50)
    print("Testing completed!")


if __name__ == "__main__":
    test_all_bf_files()