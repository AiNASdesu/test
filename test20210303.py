x = input("入力してね：")
file = open('InputText.txt', 'a')
file.write(x)
file.close()