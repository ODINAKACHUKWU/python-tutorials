"""Module displaying Python keywords, their count and version."""

import keyword
import sys

print("This is the list of Python keywords: ", keyword.kwlist)
print("The number of Python keywords is: ", len(keyword.kwlist))

print("This is the version of Python you are using: ", sys.version)
print("This is the version info: ", sys.version_info)

# Comments start with a hash (#)
