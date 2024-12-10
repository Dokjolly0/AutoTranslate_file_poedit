import os
from googletrans import Translator

def translate_po_file(file_path, target_language):
    """
    Traduci un file .po nella lingua desiderata e crea un nuovo file tradotto.

    :param file_path: Percorso del file .po da tradurre.
    :param target_language: Codice della lingua di destinazione (es. 'en', 'fr', 'de').
    """
    if not os.path.isfile(file_path):
        print(f"Il file {file_path} non esiste.")
        return

    # Leggi il contenuto del file .po
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    translator = Translator()
    translated_lines = []
    in_msgid = False
    current_msgid = ""

    # Processo per riga
    for line in lines:
        if line.startswith("msgid"):
            in_msgid = True
            current_msgid = line[7:].strip().strip('"')
            translated_lines.append(line)  # Mantieni la riga originale
        elif line.startswith("msgstr") and in_msgid:
            if current_msgid:
                try:
                    translation = translator.translate(current_msgid, dest=target_language).text
                except Exception as e:
                    print(f"Errore durante la traduzione: {e}")
                    translation = current_msgid  # Fallback sulla stringa originale in caso di errore
            else:
                translation = ""
            translated_lines.append(f'msgstr "{translation}"\n')
            in_msgid = False  # Reset per il prossimo msgid
        else:
            translated_lines.append(line)  # Mantieni altre righe inalterate

    # Salva il file tradotto
    output_path = os.path.splitext(file_path)[0] + f"_{target_language}.po"
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.writelines(translated_lines)

    print(f"File tradotto salvato in: {output_path}")

if __name__ == "__main__":
    # Chiedi il percorso del file e la lingua di destinazione
    file_path = input("Inserisci il percorso del file .po: ").strip()
    target_language = input("Inserisci il codice della lingua di destinazione (es. 'it', 'en', 'fr'): ").strip()

    translate_po_file(file_path, target_language)


# C:\ButterflyShared\butterfly-pos\ButterflyPOS\ButterflyPOS.Shared.BL\locale\de\LC_MESSAGES\de.po