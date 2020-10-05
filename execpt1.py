import sys

try:

    raise ValueError

    print("Raising an exception.")

except ValueError:

    print("ValueErro Exception!")

    sys.exit()

finally:

    print("Taking care of last minute details.")

 

print("This code will never execute.")