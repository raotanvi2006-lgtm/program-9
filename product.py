def product_details(p_id, name, qty, price):
   result = (
      f"Product ID: {p_id}\n"
      f"Name: {name}\n"
      f"Quantity: {qty}\n"
      f"Price: {price}"
   )
   return result
   
   if _name_ == "_main_":
      # sample output (you can change)
      p_id = "P100"
      name = "Samsung S20 FE 5G"
      qty = 1
      price = 28000
      print(product_details(p_id, name, qty, price))
