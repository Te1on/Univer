def get_partition(S):
    parts = []
    while S:
        # Создаю упорядоченный по частоте встречаемости набор символов

        letters_set = set(S)
        count_of_letters = [S.count(letter) for letter in letters_set]
        letters = [v for v, k in sorted(zip(letters_set, count_of_letters),
                                        key=lambda x: x[1], reverse=True)]

        # Весь смысл в том, чтобы найти наиболее длинный участок строки
        # с одинаковыми символами, а затем увеличивать его исходя из букв
        # внутри. В данном случае берется 'q' и программа смотрит внутри
        # интервала между первым и последним символом 'q' какие там еще
        # символы и тоже смотрит где впервые встречаются и где заканчиваются.

        a = S.find(letters[0])
        b = S.rfind(letters[0])
        seq_len = 0
        check = False
        while not check:
            sublet = set(S[a: b + 1])
            for letter in sublet:
                start_index = S.find(letter)
                end_index = S.rfind(letter)
                if start_index < a:
                    a = start_index
                elif end_index > b:
                    b = end_index
            if seq_len == b - a:   # Здесь проходит проверка на изменение длины подстроки
                check = True    # Если все в порядке то выходим из цикла
            else:
                seq_len = b - a     # Иначе проходим цикл заново
        # В конце можем добавить нашу подстроку в список parts
        parts.append(S[a: b + 1])
        # А затем "удалить" ее из основной строки для удобства
        if a != 0 and b != len(S):
            S = S[:a] + S[b + 1:]

        elif a == 0:
            S = S[b + 1:]

    return parts


if __name__ == "__main__":
    print(get_partition("ffffaaaa"))
