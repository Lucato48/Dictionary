meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "SHEESH": "Leggera disapprovazione",
            "CREEPY": "Spaventoso, inquietante",
            "PARA": "Preoccuparsi per qualcosa, paranoiarsi",
            "CHILL": "Tranquillo, calmo",
            "LMAO": "Risposta a qualcosa di veramente molto divertente",
            "NGL": "Modo per esprimere sincera onestà"
            }
for i in range(5):
    parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")
    if parola in meme_dict.keys():
        print(meme_dict[parola])
    else:
        print("ERROR!")
