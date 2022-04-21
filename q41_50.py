# q41
ticker = "btc_krw"
print(ticker.upper())

# q42
ticker = "btc_krw"
print(ticker.lower())

# q43
str = "hello"
print(str.capitalize())

# q44
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

# q45
print(file_name.endswith(("xlsx", "xls")))

# q46
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

# q47
a = "hello world"
print(a.split(" "))

# q48
ticker = "btc_krw"
print(ticker.split("_"))

# q49
date = "2020-05-01"
date_sp = date.split("-")
print(f"년도 : {date_sp[0]} 월 : {date_sp[1]} 일 : {date_sp[2]}")

# q50
data = "039490        "
print(data.rstrip())