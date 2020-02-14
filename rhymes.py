'''
File: rhymes.py
Author: Justin Nichols
Purpose: Find all words that have perfect rhymes with a given word(out of a
         given list)
CSC120, Section 1, Fall 18
'''


def parse_prons_file():
    '''
    Take a file with the pronunciation of different words and break it into
            manageable parts
    Parameters: n/a
    Returns: lines_list, a 2d list. Elements are lists containing the word
             and the pronunciation guide for each  syllble
    Pre-Condition: 
    Post-Condition: the return value is a 2d list
    '''
    fname = input()
    lines_list = open(fname).readlines()
    for i in range(len(lines_list)):
        lines_list[i] = lines_list[i].split()

    return lines_list


def make_dict(lines_list):
    '''
    Makes a dict where the keys are words known (to this program) and the values
        are all the known pronunciations for each key
    Parameters: lines_list, a list of given words and given pronuncuations
    Returns: pron_dict, see above
    Pre-Condition: lines_list is a 2d list
    Post-Condition: pron_dict has the properties described above
    '''
    pron_dict = {}

    for line in lines_list:
        if line[0] not in pron_dict:
            pron_dict[line[0]] = []
        pron_dict[line[0]].append(line[1:])

    return pron_dict



def prim_stress_pos(pl):
    '''
    Purpose: finds the syllable that receives the most emphasis in a word
    Parameters: pl, a list of the phonemes in a word
    Return: i, the index value of the syllable which receives the primary
            stress
    Pre-Condition: pl is a list that actually has a primary-stress syllable
    Post-Condition: i is an int
    '''
    for i in range (len(pl)):
        if pl[i][-1] == '1':
            return i

        
def is_perfect_rhyme(word_pl, cand_pl, pron_dict, word):
    '''
    determines whether a word in the pronunciations dict is a perfect rhyme
        with the queried word
    Parameters: word_pl, a list of phonemes for the word being queried
                cand_pl, a list of phonemes for the potential match currently
                    being checked
                pron_dict, a dict containing known words and all their known
                    pronunciations
                word, a str. The current word being queried
    Return: One of two bools: True or False
    Pre-Condition: the word being queried must actually have a primary-stress
                   syllable. All parameters must have types specified above
    Post-Condition:  always returns a bool
    '''
    #making sure current word in dict does in fact have a primary stress
    is_cand = False
    for phoneme in cand_pl:
        if '1' in phoneme:
            is_cand = True

    #seeing if current word rhymes perfectly with queried word
    if is_cand:
        prim_stress_word = prim_stress_pos(word_pl)
        prim_stress_cand = prim_stress_pos(cand_pl)
        cond1 = (word_pl[prim_stress_word:] == cand_pl[prim_stress_cand:])
        if not (prim_stress_word == 0 or prim_stress_cand == 0):
            cond2 = (word_pl[prim_stress_word -1] !=
                     cand_pl[prim_stress_cand - 1])
        elif (prim_stress_word == 0 and prim_stress_cand == 0):
            cond2 = False
        else:
            cond2 = True
     
        return (cond1 and cond2)

    return False


def gather_rhymes(pron_dict, word):
    '''
    finds all words that rhyme perfectly with the queried word and puts them in
        a list
    Parameters: pron_dict, a dict containing known words and all their known
                    pronunciations
                word, a str. The current word being queried
    Return: rhymes_list, a list of all words that rhyme perfectly with the
                queried word. Will contain duplicates if a known word has
                multiple different pronuncuations that each rhyme with the
                queried word
    Pre-Condition: all parameters have types specified above
    Post-Condition: rhymes_list is a list (possible empty) of str's
    '''
    rhymes_list = []
    for word_pl in pron_dict[word]:
        for cand in pron_dict:
            for cand_pl in pron_dict[cand]:
                if is_perfect_rhyme(word_pl, cand_pl, pron_dict, word):
                    rhymes_list.append(cand)
            
    return rhymes_list 
    
                   
def main():
    lines_list = parse_prons_file()
    word = input().upper()
    pron_dict = make_dict(lines_list)

    rhymes_list = gather_rhymes(pron_dict, word)
    
    for rhyme in rhymes_list:
        print(rhyme)

        
main()
