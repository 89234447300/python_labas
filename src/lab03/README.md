Задание A — src/lib/text.py

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    text = ' '.join(text.split())
    text = text.strip()
    return text
# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка"))
# print(normalize("Hello\r\nWorld"))
# print(normalize("  двойные   пробелы  "))

import re
def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)
# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    c = {}
    for w in tokens:
        cu = c.get(w, 0)
        c[w] = cu + 1
    return c
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    t = []
    for w, count in freq.items():
        t.append((-count, w))
    t.sort()
    result = []
    for neg_count, w in t:
        result.append((w, -neg_count))
    return result[:n]
tok = ["a", "b", "a", "c", "b", "a"]
freq = count_freq(tok)
# print(top_n(freq, n=2))
tok_2 = ["bb", "aa", "bb", "aa", "cc"]
freq_2 = count_freq(tok_2)
# print(top_n(freq_2, n=2))
normalize
<img width="1418" height="707" alt="image" src="https://github.com/user-attachments/assets/fad3a665-5250-4afa-b064-63da2e672683" />

tokenize
<img width="782" height="666" alt="image" src="https://github.com/user-attachments/assets/87726fe9-ae65-452e-8d59-0ebf29d8e56b" />

count_freq + top_n
<img width="726" height="860" alt="image" src="https://github.com/user-attachments/assets/f591c63a-fcce-4f15-86ab-552d43d6dbb3" />




Задание B — src/text_stats.py (скрипт со stdin)
<img width="757" height="954" alt="image" src="https://github.com/user-attachments/assets/21521597-da2c-4fe3-b177-dc0fa16638b3" />
<img width="757" height="760" alt="image" src="https://github.com/user-attachments/assets/f6043e4d-964d-4707-9b94-d53dd2197549" />

