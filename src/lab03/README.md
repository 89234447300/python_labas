```
import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = text.casefold()
    if yo2e:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ')
    text = ' '.join(text.split())
    text = text.strip()
    return text

    
def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', text)

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
```


normalize
<img width="1418" height="707" alt="image" src="https://github.com/user-attachments/assets/fad3a665-5250-4afa-b064-63da2e672683" />

tokenize
<img width="782" height="666" alt="image" src="https://github.com/user-attachments/assets/87726fe9-ae65-452e-8d59-0ebf29d8e56b" />

count_freq + top_n
<img width="726" height="860" alt="image" src="https://github.com/user-attachments/assets/f591c63a-fcce-4f15-86ab-552d43d6dbb3" />




Задание B — src/text_stats.py (скрипт со stdin)
```
from src.lab03.lib.text import normalize, tokenize, count_freq, top_n
import sys
def main():
    text = sys.stdin.read()
    if not text.strip():
        print("Нет входных данных")
        return
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)

    if not tokens:
        print("В тексте не найдено слов")
        return

    total_words = len(tokens)
    freq_dict = count_freq(tokens)
    unique_words = len(freq_dict)
    top_words = top_n(freq_dict, 5)

    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    test_text = "Привет, мир! Привет!!!"

    print('$ echo "Привет, мир! Привет!!!" | python src/text_stats.py')
    normalized = normalize(test_text)
    tokens = tokenize(normalized)
    freq = count_freq(tokens)
    top = top_n(freq, 5)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")
    for word, count in top:
        print(f"{word}:{count}")
<img width="757" height="760" alt="image" src="https://github.com/user-attachments/assets/f6043e4d-964d-4707-9b94-d53dd2197549" />

