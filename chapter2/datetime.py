# %%
# date tests
from datetime import datetime

dt = datetime(2011, 10, 29, 20, 30, 21)

# Print date brazilian format
print(dt.strftime("%d/%m/%Y %Hh%M"))

# Print the current date.
current_date = date.today()
print(current_date.strftime("%d/%m/%Y"))

# %%
# Difference between dates
date1 = datetime(2011, 10, 15, 18)
date2 = datetime(2011, 10, 20, 20)

delta_t = date2 - date1

print(delta_t)
# %%
