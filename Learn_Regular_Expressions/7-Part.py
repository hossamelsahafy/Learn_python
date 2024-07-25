#!/usr/bin/python3
# Re Module Split & Sub
import re

First_String = "I Love Cats"
First_Search = re.split(r"\s", First_String, 1)
print(First_Search)
print("=" * 100)
# =====================================================
Second_String = "How_To_Write_A-CV ?"
Second_Search = re.split(r"-|_", Second_String)
print(Second_Search)
print("#" * 100)
# ========================================================
# Get Words From URL
for c, i in enumerate(Second_Search, 1):
    if len(i) == 1:
        continue
    print("Words Number: {} => {}".format(c, i))
print("=" * 100)
# =========================================================
# SUB:
# Swap The whiteSpace With "-"
print(re.sub(r"\s", "-", First_String))
print(re.sub(r"\s", "-", First_String, 1))
# ===========================================================
