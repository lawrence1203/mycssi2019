# students = ["Alice", "Javi", "Damien"]
# students.append("Delilah")
# print(students)
#
# students = ["Alice", "Javi", "Damien"]
# students.insert(1, "Zoe")
# print(students)
#
# students = ["Alice", "Javi", "Damien", "Javi"]
# students.remove("Javi")
# print(students)
#
#
# smith_siblings = ["Emily", "Monique", "Giovanni", "Sonny", "Nate", "Hunter"]
# for name in smith_siblings:
#     print(name + " Smith")
#
# print("There are " + str(len(smith_siblings)) + " Smith siblings")
#
# smith_siblings = ["Emily", "Monique", "Giovanni", "Brianna", "Javi"]
# for index in range(len(smith_siblings)):
#     smith_siblings[index] = smith_siblings[index] + " Smith"
#
# print(smith_siblings)
#
#
# superheroes = ["Spiderman", "Wonder Woman", "Storm", "Kamala Khan", "Bumblebee", "Jessica Jones"]
#
# for name in superheroes:
#     print(name)
#
# demoted_hero = str(raw_input("What superhero do you want to eliminate from the top 5? "))
#
# if demoted_hero in superheroes:
#     superheroes.remove(demoted_hero)
#     print("Top 5 Heroes:", superheroes)
# else:
#     print("Hero not found.")

# names = ["Rickon", "Bran", "Arya", "Sansa", "Jon", "Robb"]
#
# names[::-1]
#
# print(names[4:2:-1])

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

abb = str(raw_input("What state abbreviation would you like to know the full name of? "))

if abb in states:
    print(states[abb])

student = [
    {
    "name": "Lawrence",
    "age": 18,
    "HairColor": "Black"
    }
]
