counties=["Mombasa",
"Kwale",
"Kilifi",
"Tana River",
"Lamu",
"Taita Mak Taveta",
"Garissa",
"Wajir",
"Mandera",
"Marsabit",
"Isiolo",
"Meru",
"Tharaka-Nithi",
"Embu",
"Kitui",
"Machakos",
"Makueni",
"Nyandarua",
"Nyeri",
"Kirinyaga",
"Murang’a",
"Kiambu The",
"Turkana",
"West Pokot",
"Samburu",
"Trans-Nzoia",
"Uasin Gishu",
"Elgeyo-Marakwet",
"Nandi",
"Baringo",
"Laikipia",
"Nakuru",
"Narok",
"Kajiado",
"Kericho",
"Bomet",
"Kakamega",
"Vihiga",
"Bungoma",
"Busia",
"Siaya",
"Kisumu",
"Homa Bay",
"Migori",
"Kisii",
"Nyamira",
"Nairobi"]

counties_with_two_words=[]

for county in counties:
    if len(county.split())>1:
        counties_with_two_words.append(county)
for counties in counties_with_two_words:
    print(counties)
