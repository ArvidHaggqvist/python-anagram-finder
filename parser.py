# Swedish anagram finder, only works in swedish!

ordlista = {}

ins = open( "ordlista.txt", "r" )
for line in ins:
    line = line.strip()
    ordlista[line.split(" ")[0]] = len(line.split(" ")[0])
ins.close()

'''
def permutations(word):
    if len(word)<=1:
        return [word]

    #get all permutations of length N-1
    perms=permutations(word[1:])
    char=word[0]
    result=[]
    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result
'''
def sort_str(s):
    return ''.join(sorted(s))

word = raw_input("Skriv ditt ord: ")
#possible_anagrams = permutations(word)
results = []
'''
for el in possible_anagrams:
    if el in ordlista and el != word and el not in results:
        results.append(el)

'''

for key, val in ordlista.items():
    if val == len(word):
        if sort_str(key) == sort_str(word) and key != word and key not in results:
            results.append(key)

if results == []:
    print "Inga anagram hittades."
else:
    print "Dessa anagram hittades:\n"
    for anagram in results:
        print anagram
