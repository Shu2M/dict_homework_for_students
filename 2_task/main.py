"""Второе задание.

Вы очень любите считать. Не важно что, где и когда, главное посчитать все, что
можно. Вам на вход приходит текст. Ваша программа должна посчитать количество
слов в этом тексте и вывести на печать 10 самых частых слов. Если слова
встречаются одинаковое количество раз, то они должны быть отсортированы по
алфавиту.

Ограничения:
- игнорируем знаки препинания (тире, запятые, многоточия и т.п.)
- слово, это все то, что отделено пробелом, символом табуляции или символом
перевода строки.
- регистр игнорируется
- слова короче 3-х символов игнорируются.


Советы:
1) почитать про регулярные выражения в питоне, для визуального представления
можно пользоваться сайтом https://regex101.com/
2) вспомнить про sorted, почитать про lambda функции и сортировку с их помощью

для тестирования запустить pytest 2_task/test.py
"""
import re
from collections import Counter


def top_10_most_common_words(text: str) -> dict[str, int]:
    """Функция возвращает топ 10 слов, встречающихся в тексте.

    Args:
        text: исходный текст

    Returns:
        словарь типа {слово: количество вхождений}
    """
    words = re.findall(r'\b\w{3,}\b', text.lower())
    sorted_common_words = sorted(Counter(words).items())
    return dict(
        sorted(
            sorted_common_words,
            key=lambda word_info: word_info[1],
            reverse=True,
        )[:10],
    )
