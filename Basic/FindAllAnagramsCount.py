'''
Given a string S, find the number of "unordered anagrammatic pairs" of substrings.
(Slight modification to find permuation index question 'FindPermutationIndex.py')


Complete questions with examples: https://www.hackerrank.com/challenges/sherlock-and-anagrams
'''

class Utils():
    @classmethod
    def getFrequency(cls, inputString):
        '''
        Function to  return character frequency for a given string
        '''
        if inputString is None:
            return {}

        charFrequencyDictionary = {} # dictionary is a hash DS
        # iterate over each character and calculate frequency
        for char in inputString:
            if not charFrequencyDictionary.has_key(char):
                charFrequencyDictionary[char] = 0
            charFrequencyDictionary[char] += 1
        return charFrequencyDictionary

    @classmethod
    def isAnagram(cls, sourceChFeqDict, targetChFeqDict):
        '''
        Function to check if the two strings are anagram, given character frequency dictionary for two
        '''
        freqMatch = True
        for (char, count) in targetChFeqDict.items():
            # target string is not an anagram if
            # i) a character from target string is not present in sourceChFeqDict (indicated by missing key)
            # ii) the character frequency in targetChFeqDict for a given character does not match frequency in sourceChFeqDict
            if not sourceChFeqDict.has_key(char) or sourceChFeqDict[char] != count:
                freqMatch = False
                break
        return freqMatch



def countAnagrams(sourceStr, targetStr):
    '''
    Function to find all the index in targetStr from where a permutation of sourceStr starts
    '''
    targetChFeqDict = Utils.getFrequency(targetStr)
    windowLength = len(targetStr)

    # compute the frequency of first window in the source string
    sourceChFeqDict = Utils.getFrequency(sourceStr[0:windowLength])
    sourceStringLen = len(sourceStr)
    anagramsCount = 0

    # check if the first sub-string of length windowLenght starting at 0 is a permutation
    if Utils.isAnagram(sourceChFeqDict, targetChFeqDict):
        anagramsCount += 1

    startIdx = 1
    while startIdx < (sourceStringLen-windowLength+1):
        endIdx = startIdx+windowLength-1
        addChar =  sourceStr[endIdx]
        rmChar = sourceStr[startIdx-1]

        # increment start index by whole string length if the new character is not at all in target string
        if not targetChFeqDict.has_key(addChar):
            startIdx = endIdx+1
            sourceChFeqDict = Utils.getFrequency(sourceStr[startIdx:startIdx+windowLength])
        else:
            # reduce the frequency of character removed
            if sourceChFeqDict.has_key(rmChar):
                sourceChFeqDict[rmChar] -= 1

            # add the frequency of character added
            if not sourceChFeqDict.has_key(addChar):
                sourceChFeqDict[addChar] = 0
            sourceChFeqDict[addChar] += 1

        # if anagram (i.e. permutation) then add the start index to output list
        if Utils.isAnagram(sourceChFeqDict, targetChFeqDict):
            anagramsCount += 1
        startIdx += 1

    return anagramsCount

if __name__ == "__main__":
    S = "abba"

    inputStrLength = len(S)
    anagramaticSubStringCount = 0
    # iterate through all possible length of anagrams i.e. from string of length 1 to string of length n
    for anagramLength in range(1, inputStrLength):
        # iterate through forward indices of the string to search for anagrams
        for sIdx in range(0, inputStrLength-anagramLength):
            targetString = S[sIdx:(sIdx+anagramLength)]
            sourceString = S[(sIdx+1):]
            anagramaticSubStringCount += countAnagrams(sourceString, targetString)
    print anagramaticSubStringCount
