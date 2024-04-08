from collections import defaultdict
supplier_products = defaultdict(lambda: defaultdict(int))

while True:
    try:
        line = input().split(" ")
        supplier = line[0]
        product = line[1]
        quantity = int(line[2])
        supplier_products[supplier][product] += quantity
    except EOFError:
        break

sorted_suppliers = sorted(supplier_products.keys())

for supplier in sorted_suppliers:
    print(supplier + ':')
    sorted_products = sorted(supplier_products[supplier].keys())
    for product in sorted_products:
        print(product, supplier_products[supplier][product])