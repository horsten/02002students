"""Exercise 5.11. Best Buy."""

def best_buy(prices: list, money: int, start_index: int, reverse: bool) -> int:
    """Return the number of items that can be bought with the given amount of money. The function should be able to handle arbitrary starting points and to run the list in reverse.
    
    :param prices: list of prices
    :param money: amount of money
    :param start_index: starting index in list
    :param reverse: boolean to indicate if list should be run in reverse
    :return: number of items that can be bought with the given amount of money
    """
    available = 0
    if reverse:
        prices = prices[::-1]
        start_index = len(prices)-start_index-1
    for item in range(start_index, len(prices)):
        if prices[item] <= money:
            money -= prices[item]
            available += 1
    return available

    items = 0
    index = start_index
    if reverse:
        increment = -1
    else:
        increment = 1
    while (index >= 0) and (index < len(prices)):
        if (money < prices[index]):
            #print (f'Can\'t afford item {index} for {prices[index]}, money left is {money}, ending shopping trip.')
            break
        #print (f'Buying item {index} for {prices[index]}, money left is {money-prices[index]}.')
        money -= prices[index]
        items += 1
        index += increment
    return items

if __name__ == "__main__":
    testcases = [ 'best_buy(prices, 10, 0, False)', 'best_buy(prices, 3, 1, False)', 'best_buy(prices, 8, 4, True)', 'best_buy(prices, 10, 4, True)' ]
    prices = [3, 2, 1, 3, 5]
    for t in testcases:
        print(f'{t}: {eval(t)}')
