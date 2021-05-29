# stand = {"Jotaro": "Star Platinum"}
#
# print(stand["Jotaro"])

# stands = {"Jotaro": "Star Platinum", "Avdol": "Magician's Red", "Kakyoin": "Hierophant Green", "Polnareff": "Silver Chariot"}
#
# stand = stands["Avdol"]
#
# print(stand)

# # Magician's Fire is the wrong name of Avdol's Stand
# stands = {"Jotaro": "Star Platinum", "Avdol": "Magician's Fire", "Kakyoin": "Hierophant Green", "Polnareff": "Silver Chariot"}
#
# stands["Avdol"] = "Magician's Red"
#
# print(stands)

# stands = {"Jotaro": "Star Platinum", "Avdol": "Magician's Fire", "Kakyoin": "Hierophant Green", "Polnareff": "Silver Chariot"}
#
# stands.pop("Kakyoin")
#
# print(stands)

# stands = {"Jotaro": "Star Platinum", "Avdol": "Magician's Fire", "Kakyoin": "Hierophant Green",
#           "Polnareff": "Silver Chariot"}
#
# kakyoinStand = stands.pop("Kakyoin")
#
# print(kakyoinStand)
# print(stands)

# stands = {"Jotaro": "Star Platinum", "Avdol": "Magician's Fire", "Kakyoin": "Hierophant Green",
#           "Polnareff": "Silver Chariot"}
#
# stands.clear()
#
# print(stands)

# stands = {"Jotaro": "Star Platinum", "Avdol": "Magician's Fire", "Kakyoin": "Hierophant Green",
#           "Polnareff": "Silver Chariot"}
#
# stands["Iggy"] = "The Fool"
#
# print(stands)

# stands = {"Jotaro": "Star Platinum", "Avdol": "Magician's Fire", "Kakyoin": "Hierophant Green",
#           "Polnareff": "Silver Chariot", "Dio": ["Za Warudo", "Za Warudo Over Heaven"]}
#
# print(stands["Dio"])

# stands = {"Jotaro": "Star Platinum", "Avdol": "Magician's Fire", "Kakyoin": "Hierophant Green",
#           "Polnareff": "Silver Chariot", "Dio": ["Za Warudo", "Za Warudo Over Heaven"]}
#
# print(stands["Dio"][0])

stands = {"Jotaro": "Star Platinum", "Avdol": "Magician's Fire", "Kakyoin": "Hierophant Green",
          "Polnareff": "Silver Chariot", "Dio": ["Za Warudo", "Za Warudo Over Heaven"]}

heavenAscensionDioStand = stands["Dio"][1]

print(heavenAscensionDioStand)
