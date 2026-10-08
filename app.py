import streamlit as st

st.set_page_config(page_title='Confartigianato | Orientamento medico-legale', page_icon='🩺', layout='wide')

JOBS = {
    'Autotrasportatore': {
        'tasks': ['Guida prolungata', 'Carico e scarico merci', 'Movimentazione manuale di carichi', 'Manutenzione del veicolo', 'Turni notturni'],
        'exposures': ['Vibrazioni al corpo intero', 'Posture sedute prolungate', 'Rumore', 'Gas di scarico', 'Stress e ritmi di lavoro'],
    },
    'Operaio edile': {
        'tasks': ['Sollevamento e trasporto materiali', 'Lavori in quota', 'Uso di utensili vibranti', 'Demolizioni', 'Posa e finiture'],
        'exposures': ['Polveri e silice', 'Rumore', 'Vibrazioni mano-braccio', 'Movimenti ripetitivi', 'Posture incongrue', 'Agenti chimici'],
    },
    'Parrucchiere': {
        'tasks': ['Taglio e piega', 'Colorazioni e decolorazioni', 'Lavaggi', 'Uso di phon e piastre', 'Gestione del salone'],
        'exposures': ['Lavoro in piedi prolungato', 'Movimenti ripetitivi degli arti superiori', 'Prodotti cosmetici e sensibilizzanti', 'Lavoro umido', 'Posture incongrue'],
    },
}

st.title('Confartigianato · Orientamento medico-legale')
st.caption('Prototipo dimostrativo per colloquio preliminare. Non sostituisce visita, accertamento medico-legale o decisione degli enti.')
st.warning('Usare esclusivamente dati fittizi o anonimizzati. Non inserire nomi, codici fiscali, referti identificabili o altri dati sanitari personali in questa versione.')

with st.sidebar:
    st.header('Percorso')
    pathway = st.radio('Ambito di valutazione', ['INAIL · possibile origine lavorativa', 'INPS · capacità lavorativa'], index=0)
    job = st.selectbox('Professione', list(JOBS))
    st.info('Il questionario è adattato alla professione, ma le risposte non costituiscono una diagnosi.')

st.subheader('1. Attività lavorativa')
years = st.number_input('Anni complessivi nella professione', min_value=0, max_value=70, value=10, step=1)
hours = st.number_input('Ore lavorative settimanali (indicative)', min_value=0, max_value=100, value=40, step=1)
tasks = st.multiselect('Mansioni effettivamente svolte', JOBS[job]['tasks'])
other_tasks = st.text_area('Altre mansioni o precisazioni', height=70)
exposures = st.multiselect('Esposizioni o fattori di rischio riferiti', JOBS[job]['exposures'])
exposure_frequency = st.selectbox('Frequenza delle esposizioni segnalate', ['Non definita', 'Occasionale', 'Settimanale', 'Quotidiana'])
protection = st.selectbox('Misure di prevenzione/protezione riferite', ['Da verificare', 'Generalmente presenti', 'Parziali', 'Assenti'])

st.subheader('2. Problema di salute e decorso')
problem = st.text_area('Sintomi, patologie o esiti di infortunio riferiti (senza dati identificativi)', height=100)
onset = st.selectbox('Esordio del problema', ['Non precisato', 'Improvviso', 'Graduale', 'Successivo a un evento specifico'])
injury = st.checkbox('È riferito un infortunio o un evento acuto sul lavoro')
if injury:
    event_description = st.text_area('Dinamica dell’evento, data approssimativa e conseguenze riferite', height=80)
else:
    event_description = ''
preexisting = st.selectbox('Condizioni preesistenti o cause extraprofessionali', ['Da approfondire', 'Riferite', 'Non riferite'])

st.subheader('3. Conseguenze funzionali')
limits = st.multiselect('Attività attualmente limitate', [
    'Sollevare o trasportare pesi', 'Camminare o salire scale', 'Restare in piedi',
    'Restare seduto a lungo', 'Guidare', 'Usare mani e arti superiori',
    'Mantenere l’attenzione', 'Tollerare sostanze o ambienti di lavoro', 'Altre attività'
])
impact = st.select_slider('Interferenza riferita con il lavoro abituale', options=['Nessuna', 'Lieve', 'Moderata', 'Importante', 'Molto importante'], value='Moderata')
work_status = st.selectbox('Situazione lavorativa attuale', ['Lavora senza modifiche', 'Lavora con adattamenti', 'Assente dal lavoro', 'Ha cambiato mansione', 'Non lavora', 'Non precisata'])

st.subheader('4. Documentazione disponibile')
docs = st.multiselect('Documenti già disponibili', [
    'Certificati medici', 'Referti specialistici', 'Esami strumentali', 'Documentazione di pronto soccorso',
    'Denuncia/certificazione di infortunio', 'Documentazione delle mansioni',
    'Valutazione dei rischi/esposizioni', 'Giudizio del medico competente', 'Documentazione previdenziale'
])

st.subheader('5. Orientamento preliminare')
if 'INAIL' in pathway:
    st.info('Approfondire cronologia, esposizione concreta, plausibilità del nesso causale o concausale e possibili fattori alternativi. Il solo svolgimento della professione non dimostra l’origine lavorativa.')
    suggestions = ['Ricostruzione documentata di mansioni, tempi ed esposizioni', 'Documentazione clinica cronologica pertinente', 'Valutazione medico-legale del nesso causale/concausale']
    if injury:
        suggestions.append('Documentazione dell’evento acuto, della dinamica e delle prime cure')
    if exposures:
        suggestions.append('Verifica di DVR, misurazioni ambientali e dati del medico competente, ove disponibili')
else:
    st.info('Approfondire la riduzione della capacità di lavoro in occupazioni confacenti alle attitudini, considerando storia lavorativa, capacità residue e requisiti previdenziali. Non è necessario dimostrare un’origine professionale della patologia.')
    suggestions = ['Documentazione clinica aggiornata e prognosi funzionale', 'Descrizione delle capacità residue e delle attività ancora sostenibili', 'Storia professionale, competenze e mansioni compatibili', 'Verifica separata dei requisiti amministrativi e contributivi']
if limits:
    suggestions.append('Valutazione specialistica mirata alle limitazioni riferite, se ritenuta necessaria dal medico')

st.markdown('**Punti da verificare dal medico**')
for item in suggestions:
    st.write('• ' + item)

summary = '\n'.join([
    'SCHEDA PRELIMINARE — SOLO USO DIMOSTRATIVO',
    f'Percorso: {pathway}', f'Professione: {job}',
    f'Anni di attività: {years}; ore/settimana: {hours}',
    f'Mansioni: {", ".join(tasks) or "Non indicate"}',
    f'Altre mansioni: {other_tasks or "Non indicate"}',
    f'Esposizioni riferite: {", ".join(exposures) or "Non indicate"}',
    f'Frequenza: {exposure_frequency}; protezioni: {protection}',
    f'Problema riferito: {problem or "Non descritto"}',
    f'Esordio: {onset}; evento acuto sul lavoro: {"Sì" if injury else "No"}',
    f'Dettagli evento: {event_description or "Non indicati"}',
    f'Fattori preesistenti/extraprofessionali: {preexisting}',
    f'Limitazioni: {", ".join(limits) or "Non indicate"}',
    f'Interferenza riferita: {impact}; stato lavorativo: {work_status}',
    f'Documenti disponibili: {", ".join(docs) or "Nessuno indicato"}',
    'VERIFICHE PROPOSTE (non prescrizioni automatiche):',
    *['- ' + s for s in suggestions],
    'Esito: nessuna determinazione automatica di diagnosi, nesso causale, invalidità o diritto a prestazioni.'
])

with st.expander('Visualizza scheda riepilogativa'):
    st.text(summary)
st.download_button('Scarica scheda preliminare (.txt)', summary, file_name='scheda_preliminare_demo.txt', mime='text/plain')
st.caption('Le informazioni restano nella sessione corrente dell’applicazione; non è previsto un archivio clinico in questa versione. Evitare comunque dati personali reali.')
