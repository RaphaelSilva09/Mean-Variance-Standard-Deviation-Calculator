# This entrypoint file to be used in development. Start by reading README.md
from mean_var_std import calculate
from unittest import main

# Run unit tests automatically
main(module='test_module', exit=False)

# prints the results
print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))