# One way to import sales by importing its modules
# add file __init__.py in ecommerce folder
from Module_package.ecommerce.sales import cal_shipping, cal_price
cal_price()
cal_shipping()


#*****************************
# Another way to import sales as object
from Module_package.ecommerce import sales

sales.cal_price()
sales.cal_shipping()

# new folder had __pycache__ to cahe module loading