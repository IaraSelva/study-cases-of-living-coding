def suggestedProducts(products, searchWord):
    suggested = []
    products.sort()
    first_letters = ""

    for char in searchWord:
        first_letters += char
        suggested.append([product for product in products if product.startswith(first_letters)][:3])
    
    return suggested

print(suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))