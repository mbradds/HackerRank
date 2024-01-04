def minion_game(string):
    def is_vowel(letter):
        vowels = "aeiouAEIOU"
        return letter in vowels
    # your code goes here
    points_vowel, points_cons = 0, 0
    s = len(string)
    for index in range(s):
        if is_vowel(string[index]):
            points_vowel = points_vowel + (s-index)
        else:
            points_cons = points_cons + (s-index)
            
    if points_vowel < points_cons:
        print('Stuart ' + str(points_cons))
    elif points_vowel > points_cons:
        print('Kevin ' + str(points_vowel))
    else:
        print('Draw')
    return None

if __name__ == '__main__':
    # s = input()
    s = "banana"
    minion_game(s)