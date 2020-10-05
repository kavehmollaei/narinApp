import pstats
import os

print(os.getcwd())
p = pstats.Stats('profile.stat')
p.print_stats()
p.print_callees()
p.print_callers()
