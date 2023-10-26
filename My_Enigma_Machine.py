def rotor_rotation(rotor):
    '''This function generates the rotation of a rotor.'''
    x = rotor[0]
    rotor.pop(0)
    rotor.append(x)

def set_rotor_position(rotor, key_position):
    '''This function rotates the rotor until it's in the initial position based on the given key.'''
    i = key[key_position]
    while rotor[0].split('-')[0] != i:
        i = key[key_position]
        while rotor[0].split('-')[0] != i:
            rotor_rotation(rotor)

def enigma_sequence(key, word):
    '''This function first assigns values to each rotor, the keyboard, and the reflector. 
    Then, it uses the index to find the tuple in the rotor that matches the previous letter's position. 
    It continues this process until it reads the entire word. 
    In the case where the right rotor has the tuple (v-m) in the first position, the middle rotor rotates. 
    And if the middle rotor has the tuple (q-q) in the first position, then the left rotor rotates. 
    Regarding the reflector, based on the position of the letter given in the previous rotor, it searches for a letter, sets that position to (''), 
    and then searches for the position where the other identical letter was originally.'''
    result = ''
    keyboard = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    reflector = ['A','B','C','D','E','F','G','D','I','J','K','G','M','K','M','I','E','B','F','T','C','V','V','J','A','T']
    left_rotor = [('A-E'),('B-K'),('C-M'),('D-F'),('E-L'),('F-G'),('G-D'),('H-Q'),('I-V'),('J-Z'),('K-N'),('L-T'),('M-O'),('N-W'),('O-Y'),('P-H'),('Q-X'),('R-U'),('S-S'),('T-P'),('U-A'),('V-I'),('W-B'),('X-R'),('Y-C'),('Z-J')]
    middle_rotor = [('A-A'),('B-J'),('C-D'),('D-K'),('E-S'),('F-I'),('G-R'),('H-U'),('I-X'),('J-B'),('K-L'),('L-H'),('M-W'),('N-T'),('O-M'),('P-C'),('Q-Q'),('R-G'),('S-Z'),('T-N'),('U-P'),('V-Y'),('W-F'),('X-V'),('Y-O'),('Z-E')]
    right_rotor = [('A-B'),('B-D'),('C-F'),('D-H'),('E-J'),('F-L'),('G-C'),('H-P'),('I-R'),('J-T'),('K-X'),('L-V'),('M-Z'),('N-N'),('O-Y'),('P-E'),('Q-I'),('R-W'),('S-G'),('T-A'),('U-K'),('V-M'),('W-U'),('X-S'),('Y-Q'),('Z-O')]
    middle = False
    left = False

    set_rotor_position(left_rotor, 0)
    set_rotor_position(middle_rotor, 1)
    set_rotor_position(right_rotor, 2)

    for letter in word:
        
        if right_rotor[0].split('-')[0] == 'V':
            middle = True
            
        if middle_rotor[0].split('-')[0] == 'Q':
            left = True
        
        reflector = ['A','B','C','D','E','F','G','D','I','J','K','G','M','K','M','I','E','B','F','T','C','V','V','J','A','T']
        current_letter = letter
        position = keyboard.index(current_letter)
        
        rotor_rotation(right_rotor)
        
        if middle:
            rotor_rotation(middle_rotor)
        
        middle = False
        if right_rotor[0].split('-')[0] == 'V':
            middle = True
            
        if left:
            rotor_rotation(left_rotor)
        
        left = False
        if middle_rotor[0].split('-')[0] == 'Q':
            left = True
            
        for i in right_rotor:
            if right_rotor.index(i) == position:
                current_letter = i.split('-')[1]
                break
            
        for i in right_rotor:
            if i.split('-')[0] == current_letter:
                position = right_rotor.index(i)
                break

        for i in middle_rotor:
            if middle_rotor.index(i) == position:
                current_letter = i.split('-')[1]
                break
            
        for i in middle_rotor:
            if i.split('-')[0] == current_letter:
                position = middle_rotor.index(i)
                break

        for i in left_rotor:
            if left_rotor.index(i) == position:
                current_letter = i.split('-')[1]
                break
            
        for i in left_rotor:
            if i.split('-')[0] == current_letter:
                position = left_rotor.index(i)
                break

        current_letter = reflector[position]
        reflector[position] = ''
        position = reflector.index(current_letter)
        
        for i in left_rotor:
            if left_rotor.index(i) == position:
                current_letter = i.split('-')[0]
                break

        for i in left_rotor:
            if i.split('-')[1] == current_letter:
                position = left_rotor.index(i)
                break
            
        for i in middle_rotor:
            if middle_rotor.index(i) == position:
                current_letter = i.split('-')[0]
                break
            
        for i in middle_rotor:
            if i.split('-')[1] == current_letter:
                position = middle_rotor.index(i)
                break

        for i in right_rotor:
            if right_rotor.index(i) == position:
                current_letter = i.split('-')[0]
                break
            
        for i in right_rotor:
            if i.split('-')[1] == current_letter:
                position = right_rotor.index(i)
                break
            
        result += keyboard[position]
    return result

key = input('What is your encryption key? ').upper()
word = input('What do you want to encrypt/decrypt? ').upper()
word = word.split(' ')
for i in word:
    print(enigma_sequence(key, i), end=' ')
