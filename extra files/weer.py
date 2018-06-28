with open("knmi.txt") as k, open("lekkerweertje.csv", "w") as c:
    lines = 0
    variables = "STN,Date,TG,TN,TNH,TX,TXH"
    c.writelines(variables)
    for row in k:
        lines += 1
        if lines >= 16:
            c.writelines(''.join(row.split()) + "\n")
