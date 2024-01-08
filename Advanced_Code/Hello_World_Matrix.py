#!/usr/bin/python3
import string
import time
import random

target = "Hello World"
# All lowercase and uppercase letters, plus space
characters = string.ascii_letters + " "
# For each character in the target string
for target_index in range(len(target)):
    # Try each possible character
    for char in characters:
        # If it's the first character, start with 'H'
        if target_index == 0 and char != "H":
            continue
        # Print the characters found so far
        print(target[:target_index], end="")
        # Print the current character
        print(char, end="")
        # Fill the rest of the line with random characters
        print(
            "".join(
                random.choice(characters) for _ in range(len(target) - target_index - 1)
            )
        )
        # Wait a bit to simulate "hacking"
        time.sleep(0.1)
        if char == target[target_index]:
            break
    # Print the found character and move on to the next
    print(target[: target_index + 1])
