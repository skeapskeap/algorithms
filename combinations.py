def find_combinations(nums: str) -> set:
    if len(nums) == 2:
        orig = nums
        reverse = nums[::-1]
        return set((orig, reverse))

    result = set()
    for idx, char in enumerate(nums):
        # берём текущий элемент
        # он будет подставляться в начало строки
        base = char

        # берём строку без текущего элемента
        less = nums[:idx] + nums[idx+1:]

        '''
        ищем все комбинации этой строки
        это те данные, которые вернулись из глубин стэка
        '''
        combinations = find_combinations(less)

        # к каждой строке в получившемся
        # множестве добавляем в начало base
        for unique_string in combinations:
            new_elem = base + unique_string
            '''
            result - это то, что возвращается вверх по рекурсии
            ближе к началу стэка
            '''
            result.add(new_elem)
    return result


if __name__ == '__main__':
    nums = '0123'
    result = find_combinations(nums)
    for item in result:
        print(item)
    print(f'Количество комбинаций: {len(result)}')
