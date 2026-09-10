# Difficult to read
price=1250
quantity=3
discount=10
result=price*quantity-discount/100*price*quantity


# Better
price = 1250
quantity = 3
discount_percent = 10

total_price = price * quantity
discount_amount = total_price * discount_percent / 100
final_price = total_price - discount_amount

print(f"Final price: {final_price:.2f}")