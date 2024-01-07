cards = [
"4123456789123456",
"5123-4567-8912-3456",
"61234-567-8912-3456",
"4123356789123456",
"5133-3367-8912-3456",
"5123 - 3567 - 8912 - 3456"
]



def has_repeating_characters(s, threshold=4):
    count = 1  # Initialize the count for the first character
    last_char = s[0]  # Initialize the last character

    for char in s[1:]:
        if char == last_char:
            count += 1
            if count >= threshold:
                return True
        else:
            count = 1  # Reset count if the current character is different
            last_char = char

    return False

def validate_card(card):
    if (len(card.replace("-", "")) != 16):
        print("Invalid")
        return
    if (card[0] not in ["4", "5", "6"]):
        print("Invalid")
        return
    if ("-" in card):
        for group in card.split("-"):
            if len(group) != 4:
                print("Invalid")
                return
    numbers = [0,1,2,3,4,5,6,7,8,9]
    for c in card:
        if c!="-":
            try:
                c_int = int(c)
                if c_int not in numbers:
                    print("Invalid")
                    return
            except:
                print("Invalid")
                return
    
    if has_repeating_characters(card.replace("-", "")):
        print("Invalid")
        return
    
    print("Valid")



for card in cards:
    x = validate_card(card)