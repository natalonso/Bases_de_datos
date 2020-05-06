import csv

################################################################################
# PROCESAMIENTO DE LA VISTA PRODUCTS
################################################################################

csvfile_write = open('products_process.csv', 'w', newline='', encoding="utf-8")
write_csv = csv.writer(csvfile_write, delimiter=",")

csvfile_read = open('products.csv', 'r', newline='', encoding="utf-8")
reader = csv.reader(csvfile_read)

id=0
for row in reader:
    if id == 0:
        row.append('id_product')
    else:
        row.append(id)

    write_csv.writerow(row)
    id = id+1

################################################################################
# PROCESAMIENTO DE LA VISTA ORDERS
################################################################################

csvfile_write = open('orders_simplif_process.csv', 'w', newline='', encoding="utf-8")
write_csv = csv.writer(csvfile_write, delimiter=",")

csvfile_read = open('orders_simplif.csv', 'r', newline='', encoding="utf-8")
reader = csv.reader(csvfile_read)

id=0
for row in reader:
    if id == 0:
        row.append('id_order')
    else:
        row[1] = row[1].replace(' c','')
        row.append(id)

    write_csv.writerow(row)
    id = id+1