def subtotal(*prices):
    """Return the sum of all prices. Returns 0 if no prices given."""
    return sum(prices)

def apply_discount(amount, percent=10):
    """Return amount after subtracting a percentage discount."""
    return amount - (amount * percent / 100)

def add_tax(amount, rate=0.18):
    """Return amount with tax added."""
    return amount + (amount * rate)

amount = subtotal(250, 400, 120)
print(f"Subtotal: {amount}")
discounted_amount = apply_discount(amount, 15)
print(f"Amount after discount: {discounted_amount}")
taxed_amount = add_tax(discounted_amount)
print(f"Amount after tax: {taxed_amount}")