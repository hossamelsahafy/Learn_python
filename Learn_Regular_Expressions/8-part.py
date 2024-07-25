#!/usr/bin/python3
# Group Training's & Flags
import re

ElZero_Video = "https://www.youtube.com/watch?v=MLb7pPOEJlg&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs&index=102"
# That Is Valid Link You Can Watch It To Learn More!
search = re.search(
    r"(https?):\/\/(www)?(\w+)\.(\w+)?(\d+)?(.+)", ElZero_Video, re.IGNORECASE
)
print(search.group())
print(search.groups())
