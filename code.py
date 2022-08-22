import yagmail


baza = {}




sender = input("Sheiyvanet maili: ")

if sender not in baza:

    password = input("\nSheiyvanet paroli: ")

    baza[sender] = password



receiver = input("\nSheiyvanet adresati: ")

subject = input("\nSheiyvanet subject: ")
content = input("\nSheiyvanet risi gagzavnac gindat: ")



yag = yagmail.SMTP(sender, baza[sender])
yag.send(receiver, subject, content)


print("maili warmatebit gaigzavna!")


input()
