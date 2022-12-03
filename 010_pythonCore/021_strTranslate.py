# maketrans метод класса str возвращает dict
table1 = str.maketrans("0123456789",
                       "\N{bengali digit zero}"
                       "\N{bengali digit one}"
                       "\N{bengali digit two}"
                       "\N{bengali digit three}"
                       "\N{bengali digit four}"
                       "\N{bengali digit five}"
                       "\N{bengali digit six}"
                       "\N{bengali digit seven}"
                       "\N{bengali digit eight}"
                       "\N{bengali digit nine}")

# можно и так, что тоже самое, ведь "" это строка
table_dig_to_cir = "".maketrans("0123456789",
                                "\N{circled digit zero}"
                                "\N{circled digit one}"
                                "\N{circled digit two}"
                                "\N{circled digit three}"
                                "\N{circled digit four}"
                                "\N{circled digit five}"
                                "\N{circled digit six}"
                                "\N{circled digit seven}"
                                "\N{circled digit eight}"
                                "\N{circled digit nine}")

table_cir_to_dig = "".maketrans(
    "\N{circled digit zero}"
    "\N{circled digit one}"
    "\N{circled digit two}"
    "\N{circled digit three}"
    "\N{circled digit four}"
    "\N{circled digit five}"
    "\N{circled digit six}"
    "\N{circled digit seven}"
    "\N{circled digit eight}"
    "\N{circled digit nine}",
    "0123456789")

print("20749".translate(table_dig_to_cir))
print("②⓪⑦④⑨".translate(table_cir_to_dig))
print('\u2461\u24ea\u2466\u2463\u2468',
      '\u2461\u24ea\u2466\u2463\u2468'.translate(table_cir_to_dig))
