def get_words_count(text):
    return len(text.split())

def get_letters_frequency(text):
    freq = {}
    for char in text.lower():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1
    return freq

def get_alphabetical_phrases(text):
    # Разбиваем по запятой
    parts = text.lower().split(',')
    # Убираем пробелы по краям и пустые строки
    clean_parts = [p.strip() for p in parts if p.strip()]
    # Сортируем (в Python сортировка строк идет по алфавиту)
    return sorted(clean_parts)

def main():
    raw_text = (
"""So she was considering in her own mind, as well as she could,
for the hot day made her feel very sleepy and stupid,
whether the pleasure of making a daisy-chain would be worth the trouble
of getting up and picking the daisies, when suddenly a White Rabbit 
with pink eyes ran close by her."""
    )
    print(f"1. Total words: {get_words_count(raw_text)}")

    print("\n2. Letter frequencies:")
    letters = get_letters_frequency(raw_text)
    for char in sorted(letters):
        print(f"'{char}': {letters[char]}", end=" | ")

    print("\n\n3. Phrases in alphabetical order:")
    phrases = get_alphabetical_phrases(raw_text)
    for i, phrase in enumerate(phrases, 1):
        print(f"{i}. {phrase}")

main()