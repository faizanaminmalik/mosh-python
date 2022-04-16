# One way to import sales by importing its modules
from sales import cal_shipping, cal_price
cal_price()
cal_shipping()


#*****************************
# Another way to import sales as object
import sales
sales.cal_price()
sales.cal_shipping()

# new folder had __pycache__ to cahe module loading