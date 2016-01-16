'''
Write a function that converts a roman numeral into the integer that it represents
'''
# dictionary for roman character to decical look up
# 'Roman Character' => 'Decimal Value', lower integer value indicates lower precedence
ROMAN_NUMERAL_VALUES = {'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000}

def romanToDecimal(romanStr):
    '''
    Method to convert roman numeral to decical value
    '''
    prev = romanStr[0]

    decimalVal = ROMAN_NUMERAL_VALUES[prev]
    for ch in romanStr[1:]:
        if ROMAN_NUMERAL_VALUES[ch] <= ROMAN_NUMERAL_VALUES[prev]:
            # if the value of current roman character is less than or equal to previous then simply add to `decimalVal`
            decimalVal += ROMAN_NUMERAL_VALUES[ch]
        else:
            # if the value of current roman char is more than the previous character
            # add the current roman value to `decimalVal` and then substract previous character value twice
            decimalVal += (ROMAN_NUMERAL_VALUES[ch]- 2*ROMAN_NUMERAL_VALUES[prev])
        prev = ch
    return decimalVal

if __name__ == "__main__":

    decimalValue = romanToDecimal('IV')
    print decimalValue
    decimalValue = romanToDecimal('VIII')
    print decimalValue
    decimalValue = romanToDecimal('XIV')
    print decimalValue
    decimalValue = romanToDecimal('XXXIX')
    print decimalValue
    decimalValue = romanToDecimal('XLIX')
    print decimalValue
    decimalValue = romanToDecimal('XCI')
    print decimalValue