import os
import time
import re
import logging
from googletrans import Translator
from tqdm import tqdm

def setup_logging(log_dir, file_name):
    """
    Configura il logger per registrare i messaggi in un file.

    :param log_dir: Cartella in cui salvare i file di log.
    :param file_name: Nome del file di log.
    """
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file = os.path.join(log_dir, file_name)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, mode='w', encoding='utf-8')
        ]
    )

def translate_po_file(file_path, target_language, delay=0.5, log_dir="log"):
    """
    Traduci un file .po nella lingua desiderata e crea un nuovo file tradotto.

    :param file_path: Percorso del file .po da tradurre.
    :param target_language: Codice della lingua di destinazione (es. 'en', 'fr', 'de').
    :param delay: Ritardo (in secondi) tra le richieste di traduzione per evitare sovraccarichi.
    :param log_dir: Cartella in cui salvare i file di log.
    """
    file_name = f"logging_{os.path.basename(file_path).split('.')[0]}_{target_language}_translation.log"
    setup_logging(log_dir, file_name)
    
    start_date = time.strftime("%d/%m/%Y")
    start_time = time.time()  # Registra l'ora di inizio
    
    logging.info("Inizio traduzione del file .po")
    logging.info(f"Data di inizio: {start_date}")
    logging.info(f"Ora di inizio: {start_time}")
    error_count = 0
    errors = []

    if not os.path.isfile(file_path):
        logging.error(f"Il file {file_path} non esiste.")
        print(f"Errore: il file {file_path} non esiste.")
        return

    try:
        # Leggi il contenuto del file .po
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        translator = Translator()
        translated_lines = []
        in_msgid = False
        current_msgid = ""
        msgid_pattern = re.compile(r'^msgid \"(.*)\"$')
        msgstr_pattern = re.compile(r'^msgstr \"(.*)\"$')

        # Conta il numero di msgid da tradurre
        total_msgid = sum(1 for line in lines if msgid_pattern.match(line) and line.strip() != 'msgid ""')

        # Inizializza la barra di progresso
        with tqdm(total=total_msgid, desc="Traduzione in corso", unit="stringhe") as pbar:
            for line in lines:
                if match := msgid_pattern.match(line):
                    in_msgid = True
                    current_msgid = match.group(1)
                    translated_lines.append(line)  # Mantieni la riga originale
                elif msgstr_pattern.match(line) and in_msgid:
                    try:
                        if current_msgid.strip():
                            translation = translator.translate(current_msgid, dest=target_language).text
                            time.sleep(delay)  # Rispetta il limite API

                            # Logga la frase originale e la traduzione
                            logging.info(f"Traduzione completata: \nOriginale: '{current_msgid}'\nTraduzione: '{translation}'")
                        else:
                            translation = ""
                    except Exception as e:
                        error_count += 1
                        error_message = f"Errore durante la traduzione di '{current_msgid}': {e}"
                        errors.append(error_message)
                        logging.error(error_message)
                        print(f"Errore: {error_message}")
                        translation = current_msgid  # Fallback sulla stringa originale
                    translated_lines.append(f'msgstr "{translation}"\n')
                    in_msgid = False  # Reset per il prossimo msgid
                    pbar.update(1)  # Aggiorna la barra di progresso
                else:
                    translated_lines.append(line)  # Mantieni altre righe inalterate

        # Salva il file tradotto
        output_path = os.path.splitext(file_path)[0] + f"_{target_language}.po"
        try:
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.writelines(translated_lines)
            logging.info(f"File tradotto salvato in: {output_path}")
        except Exception as e:
            error_count += 1
            error_message = f"Errore durante il salvataggio del file tradotto: {e}"
            errors.append(error_message)
            logging.error(error_message)
            print(f"Errore: {error_message}")
    except Exception as e:
        error_count += 1
        error_message = f"Errore durante la lettura o la traduzione del file: {e}"
        errors.append(error_message)
        logging.error(error_message)
        print(f"Errore: {error_message}")

    end_time = time.time()  # Registra l'ora di fine
    total_time = end_time - start_time
    
    logging.info(f"Traduzione completata in {total_time:.2f} secondi.")
    logging.info(f"Data di fine: {time.strftime('%d/%m/%Y')}")
    logging.info(f"Ora di fine: {end_time}")
    logging.info(f"Errori totali: {error_count}")
    if errors:
        logging.info("Dettagli errori:")
        for error in errors:
            logging.info(f"- {error}")

    # Report finale
    print("\n--- Report Finale ---")
    print(f"Tempo totale: {total_time:.2f} secondi")
    print(f"Errori totali: {error_count}")
    if errors:
        print("\nDettagli errori:")
        for error in errors:
            print(f"- {error}")

if __name__ == "__main__":
    # Chiedi il percorso del file e la lingua di destinazione
    file_path = input("Inserisci il percorso del file .po: ").strip()
    target_language = input("Inserisci il codice della lingua di destinazione (es. 'it', 'en', 'fr'): ").strip()

    translate_po_file(file_path, target_language)
