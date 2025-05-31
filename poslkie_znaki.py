import csv
import sys
import os

def replace_polish_chars(text):
    if text is None:
        return text
    replacements = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ż': 'z', 'ź': 'z',
        'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
        'Ó': 'O', 'Ś': 'S', 'Ż': 'Z', 'Ź': 'Z',
    }
    for pl_char, en_char in replacements.items():
        text = text.replace(pl_char, en_char)
    return text

def clean_csv_polish_chars(filename, delimiter=','):
    print(f"Rozpoczynam czytanie pliku: {filename}")
    rows = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        for i, row in enumerate(reader, start=1):
            new_row = [replace_polish_chars(cell) for cell in row]
            rows.append(new_row)
            if i % 1000 == 0:
                print(f"Wczytano {i} wierszy...")

    print(f"Zakończono czytanie pliku. Łącznie wierszy: {len(rows)}")
    temp_filename = filename + '.tmp'
    print(f"Zapisuję do pliku tymczasowego: {temp_filename}")
    with open(temp_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        writer.writerows(rows)
    print("Zapis zakończony, nadpisuję oryginalny plik...")
    os.replace(temp_filename, filename)
    print("Gotowe!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Użycie: python skrypt.py <ścieżka_do_pliku.csv> [delimiter]")
        sys.exit(1)
    path_to_csv = sys.argv[1]
    delimiter = sys.argv[2] if len(sys.argv) > 2 else ','
    clean_csv_polish_chars(path_to_csv, delimiter)
