'''
Maximum stock profit based on price trend for the day that can be made by buying 1 stock first and then selling it.
'''


def findStockProfit(priceTrend):
    '''
    Method to find maximum stock profit that can be made
    '''
    gMax, gMin, lMin = priceTrend[0], priceTrend[0], priceTrend[0]

    for sp in priceTrend[1:]:
        lMin = min(lMin, sp)
        if sp > gMax:
            gMax = sp
            gMin = lMin

    return gMax - gMin


if __name__ == "__main__":
    # case 1: single price point; expected: 0 (no profit)
    assert 0 == findStockProfit([6])
    # case 2: non-increasing price trend; expected: 0 (no profit)
    assert 0 == findStockProfit([10, 9, 9 , 7, 6])
    # case 3: non-decreasing price trend; expected profit: 4
    assert 4 == findStockProfit([6, 6, 8, 9, 10])
    # case 4: constant price trend; expected: 0 (no profit)
    assert 0 == findStockProfit([5, 5, 5, 5, 5, 5])
    # case 5: dec-inc-dec price trend; expected profit: 6
    # to test that min value is captured correctly (i.e. before the max price)
    assert 6 == findStockProfit([10, 7, 5, 8, 11, 2, 3, 1])
    # case 6: dec-inc-dec-inc price trend; expected profit: 14
    assert 14 == findStockProfit([10, 7, 5, 8, 11, 2, 3, 1, 15])
    # case 7: dec-inc price trend; expected profit: 10
    assert 10 == findStockProfit([10, 7, 5, 8, 11, 12, 13, 14, 15])

    print "All test cases passed"