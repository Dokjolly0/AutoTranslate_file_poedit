
# README

## Traduzione di File .po

### Descrizione del Progetto
Questo programma Python permette di tradurre file .po in una lingua desiderata utilizzando l'API di Google Translate. Durante il processo, vengono gestiti eventuali errori e creati log dettagliati per monitorare l'operazione. Il risultato finale è un file .po tradotto e un report dettagliato con il tempo impiegato e gli eventuali errori riscontrati.

### Funzionalità
- Traduzione automatica delle stringhe `msgid` in un file .po.
- Gestione degli errori con log dettagliati.
- Creazione di un file tradotto con il suffisso della lingua desiderata (esempio: `file_it.po` per italiano).
- Visualizzazione della barra di progresso durante la traduzione.

### Prerequisiti
Per utilizzare il programma, è necessario installare:

- Python 3.6 o superiore.
- Le seguenti librerie Python:
  - `googletrans`
  - `tqdm`

Puoi installarle eseguendo:
```bash
pip install googletrans tqdm
```

### Struttura del Programma
1. **Configurazione del Logging:**
   I messaggi di log vengono salvati in una directory specifica (default: `log`) e includono informazioni come data, ora e dettagli sugli errori.

2. **Traduzione:**
   Il programma legge il file .po, traduce le stringhe `msgid` e genera un nuovo file con le stringhe `msgstr` tradotte.

3. **Gestione degli Errori:**
   Gli errori durante la traduzione o il salvataggio del file vengono catturati, registrati nei log e riportati nel report finale.

4. **Barra di Progresso:**
   Una barra di avanzamento indica il numero di stringhe tradotte.

### Come Utilizzare il Programma
1. Clona o scarica il repository del progetto.
2. Esegui il programma:
   ```bash
   python nome_programma.py
   ```
3. Inserisci il percorso del file .po che vuoi tradurre.
4. Inserisci il codice della lingua di destinazione (esempio: `en` per inglese, `fr` per francese, `it` per italiano).
5. Attendi il completamento della traduzione. Al termine, troverai il file tradotto nella stessa directory del file originale.

### Parametri
- **file_path:** Percorso del file .po da tradurre.
- **target_language:** Codice della lingua di destinazione (ISO 639-1).
- **delay:** Ritardo tra le richieste di traduzione (default: 0.5 secondi).
- **log_dir:** Cartella in cui salvare i log (default: `log`).

### Log
I file di log vengono salvati nella directory specificata (default: `log`) con il formato:
```
logging_<nome_file>_<lingua>_translation.log
```
Il log include:
- Data e ora di inizio e fine traduzione.
- Numero totale di errori.
- Dettagli di ogni errore.

### Esempio di Output
Se il file originale è `example.po` e la lingua di destinazione è `it`, il file tradotto sarà salvato come `example_it.po`.

### Errori Comuni
1. **File non trovato:** Assicurarsi che il percorso del file sia corretto.
2. **Errore API:** Gli errori di traduzione possono derivare da problemi di connessione o limiti API. In tal caso, il programma utilizza la stringa originale come fallback.

### Contribuire
Se desideri migliorare il progetto, puoi:
- Segnalare bug.
- Proporre nuove funzionalità.
- Contribuire con il codice.

### Licenza
Questo progetto è rilasciato sotto la licenza MIT. Puoi usarlo liberamente per scopi personali e commerciali.

---

### Contatti
Per qualsiasi domanda o supporto, contatta: [tuo.email@esempio.com](mailto:tuo.email@esempio.com)
