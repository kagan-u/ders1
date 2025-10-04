sozluk = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "CREEPY" : "Korkunç",
            "SHEESH" :"Onaylamamak"
            }
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if word in sozluk.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    print(sozluk[word])
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Onu söyleyemiyoruz maalesef")
