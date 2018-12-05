#Make dictionaries

hair_color = {"black": "CCAGCAATCGC", "brown": "GCCAGTGCCG", "blonde": "TTAGCTATCGC"}
facial_shape = {"square": "GCCACGG", "round": "ACCACAA", "oval": "AGGCCTCA"}
eye_color = {"blue": "TTGTGGTGGC", "green": "GGGAGGTGGC", "brown": "AAGTAGTGAC"}
gender = {"female": "TGAAGGACCTTC", "male": "TGCAGGAACTTC"}
race = {"white": "AAAACCTCA", "black": "CGACTACAG", "asian": "CGCGGGCCG"}

#Criminal DNA

criminal = input("Please enter the DNA of the criminal: ")

#Searching for hair color


if criminal.find(hair_color["black"]) is not -1:
    hair_color = "black"
elif criminal.find(hair_color["brown"]) is not -1:
    hair_color = "brown"
elif criminal.find(hair_color["blonde"]) is not -1:
    hair_color = "blonde"
else:
    hair_color = "undetermined"

#Searching for facial_shape

if criminal.find(facial_shape["square"]) is not -1:
    facial_shape = "square"
elif criminal.find(facial_shape["round"]) is not -1:
    facial_shape = "round"
elif criminal.find(facial_shape["oval"]) is not -1:
    facial_shape = "oval"
else:
    facial_shape = "undetermined"

#Searching for eye color

if criminal.find(eye_color["blue"]) is not -1:
    eye_color = "blue"
elif criminal.find(eye_color["green"]) is not -1:
    eye_color = "green"
elif criminal.find(eye_color["brown"]) is not -1:
    eye_color = "brown"
else:
    eye_color = "undetermined"

#searching for gender:

if criminal.find(gender["female"]) is not -1:
    gender = "female"
elif criminal.find(gender["male"]) is not -1:
    gender = "male"
else:
    gender = "undetermined"

#Searching for race:

if criminal.find(race["white"]) is not -1:
    race = "white"
elif criminal.find(race["black"]) is not -1:
    race = "black"
elif criminal.find(race["asian"]) is not -1:
    race = "asian"
else:
    race = "undetermined"

#Print characteristics
print("The criminal has following characteristics: \n " + "Hair color - " + hair_color + "\n Facial shape - " + facial_shape + "\n Eye color - " + eye_color + "\n Gender - " + gender + "\n Race - " + race)

#Line break for readability

print("\n")

#Determine Culprit

if gender == "female":
    if hair_color == "blonde":
        print("The culprit is Eva")
    elif hair_color == "brown":
        print("The culprit is Larisa")
    else:
        print("The culprit is unknown")
else:
    if hair_color == "brown":
        print("The culprit is Miha")
    elif hair_color == "black":
        print("The culprit is Matej")
    else:
        print("The culprit is unknown")