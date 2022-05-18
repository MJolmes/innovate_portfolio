import random
cast = [
    "Bill Murray - Dr. Peter Venkman",
    "Dan Aykroyd - Dr. Raymond Stantz",
    "Sigourney Weaver - Dana Barrett",
    "Harold Ramis - Dr. Egon Spengler",
    "Rick Moranis - Louis Tully",
    "Annie Potts - Janine Melnitz",
    "William Atherton - Walter Peck",
    "Ernie Hudson - Winston Zeddemore",
    "David Margulies - Mayor",
]
quote = [
    "Back off, man. I'm a scientist. -- Dr. Peter Venkman",
    "He slimed me. -- Dr. Peter Venkman",
    "That's a big Twinkie. -- Winston Zeddmore",
    "Print is dead. -- Dr. Egon Spengler",
    "Human sacrifice. Dogs and cats living together. Mass hysteria. -- Dr. Peter Venkman",
    "I collect spores, molds and fungus. -- Dr. Egon Spengler",
    "Listen! You smell something? -- Dr. Raymond Stanz",
    "I'm fuzzy on the whole good/bad thing. What do you mean, bad? -- Dr. Peter Venkman"

]

def choice():
    anwser = input("Please enter C for a cast member or Q for a quote -- ").lower()
    if anwser == ("c"):
        rand_cast = (random.choice(cast))
        print(f"{rand_cast} was a member of the cast!")
    elif anwser == ("q"):
        rand_quote = (random.choice(quote))
        print(f"Quote -- {rand_quote}")
    else:
        print('Please anwser with C for cast or Q for quote.')
        choice()

choice()