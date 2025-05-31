import csv
import argparse

def transform_data(input_file, output_file, log_file):

    # Wczytaj pierwszą linię, aby sprawdzić separator
    with open(input_file, "r", encoding="windows-1250") as infile:
        first_line = infile.readline()
        delimiter = ";" if ";" in first_line else ","

    with open(input_file, "r", encoding="windows-1250", newline="") as infile, \
         open(output_file, "w", encoding="utf-8", newline="") as outfile, \
         open(log_file, "w", encoding="utf-8") as log:

        reader = csv.reader(infile, delimiter=delimiter, quotechar='"')
        writer = csv.writer(outfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for line_number, row in enumerate(reader, start=1):

            # --- CZĘŚĆ 1: Scalanie kolumn 29 i 30 ---
            try:
                if len(row) > 30:
                    col_29_raw = row[28].strip()
                    col_30_raw = row[29].strip()

                    is_valid_30 = (
                        col_30_raw.isdigit() and 
                        (int(col_30_raw) < 100 or col_30_raw.startswith("0"))
                    )

                    if is_valid_30 and col_29_raw.isdigit():
                        merged = f"{col_29_raw}.{col_30_raw}"
                        row = row[:28] + [merged] + row[30:]
            except Exception as e:
                log.write(f"Błąd w linii {line_number}: {str(e)}\n")

            # --- CZĘŚĆ 2: Scalanie kolumn 40 i 41 lub 41 i 42 ---
            modified = False
            if len(row) > 41:
                try:
                    a = int(row[40].strip().replace('"', ''))
                    b = int(row[41].strip().replace('"', ''))
                    merged = f"{a}.{b}"
                    row = row[:40] + [merged] + row[42:]
                    modified = True
                except (ValueError, IndexError):
                    pass

            if not modified and len(row) > 42:
                try:
                    a = int(row[41].strip().replace('"', ''))
                    b = int(row[42].strip().replace('"', ''))
                    merged = f"{a}.{b}"
                    row = row[:41] + [merged] + row[43:]
                    modified = True
                except (ValueError, IndexError):
                    pass

            # --- CZĘŚĆ 2: Analiza kolumn 225–245 ---
            start = 224
            end = min(len(row), 245)
            max_run = 0
            current_run = 0
            run_indices = []
            best_run_indices = []

            for i in range(start, end):
                val = row[i].strip().replace('"', '')
                try:
                    float(val.replace(",", "."))
                    current_run += 1
                    run_indices.append(i)
                    if current_run > max_run:
                        max_run = current_run
                        best_run_indices = run_indices.copy()
                except ValueError:
                    current_run = 0
                    run_indices = []

            if max_run <= 11:
                pass
            elif max_run == 12:
                found = False
                for idx in best_run_indices[:-1]:
                    try:
                        first = float(row[idx].strip().replace(",", ".").replace('"', ''))
                        second = float(row[idx + 1].strip().replace(",", ".").replace('"', ''))
                        if first == 0 and second != 0:
                            merged = f"{int(first)}.{str(second).replace('.', '').replace(',', '')}"
                            row = row[:idx] + [merged] + row[idx + 2:]
                            found = True
                            break
                    except:
                        continue
                if not found:
                    log.write(f"Wiersz {line_number}: 12 kolejnych liczb, ale brak pary (0, X)\n")
            else:
                log.write(f"Wiersz {line_number}: więcej niż 12 kolejnych liczb - wiersz pominięty\n")
                continue

            # --- CZĘŚĆ 3: Scalanie liczb w kolumnach 246–255 ---
            start3 = 236
            end3 = 245
            i = start3
            while i < end3 - 1:
                if len(row) <= i:
                    i += 1
                    continue
                val1 = row[i].strip().replace('"', '')
                val2 = row[i+1].strip().replace('"', '')
                try:
                    float(val1.replace(",", "."))
                    float(val2.replace(",", "."))
                    merged = f"{val1}.{val2}".replace(",", "")
                    row = row[:i] + [merged] + row[i+2:]
                    end3 -= 1
                except ValueError:
                    i += 1

            # --- CZĘŚĆ 4: Jeśli 272 to liczba, usuń kolumnę 271 ---
            if len(row) > 271:
                val_272 = row[271].strip().replace('"', '')
                try:
                    float(val_272.replace(",", "."))
                    row = row[:270] + row[271:]
                except ValueError:
                    pass

            writer.writerow(row)

def main():
    parser = argparse.ArgumentParser(description="Transformacja danych PSP.")
    parser.add_argument("input", help="Ścieżka do pliku wejściowego CSV")
    parser.add_argument("output", help="Ścieżka do pliku wyjściowego CSV")
    parser.add_argument("log", help="Ścieżka do pliku logu")

    args = parser.parse_args()
    transform_data(args.input, args.output, args.log)

if __name__ == "__main__":
    main()
