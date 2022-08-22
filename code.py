import yagmail


sender = 'testusermamuka@gmail.com'
password = 'wwkpaokwxozpuoma'

receiver = input("Sheiyvanet maili: ")

subject = input("Sheiyvanet subject: ")
content = input("Sheiyvanet risi gagzavnac gindat: ")



yag = yagmail.SMTP(sender, password)
yag.send(receiver, subject, content)


print("maili warmatebit gaigzavna!")

