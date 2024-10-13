# TODO Найдите количество книг, которое можно разместить на дискете
pages = 100
lines_per_page = 50
symbols_per_line = 25
bytes_per_symbol = 4
disk_size_mb = 1.44

disk_size_bytes = disk_size_mb * 1024 * 1024
book_size_bytes = pages * lines_per_page * symbols_per_line * bytes_per_symbol
books_on_disk = round(disk_size_bytes // book_size_bytes)
print("Количество книг, помещающихся на дискету:", books_on_disk)
