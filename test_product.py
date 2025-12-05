from product import product_details
def test_product_details():
  expected_output=(
    "Product ID:P100\n"
    "Name:Samsung S20 FE 5G\n"
    "Quantity:1\n"
    "Price:28000"
  )
  assert product_details("P100e","Samsung S20 FE 5G",1,28000)==expected_output
