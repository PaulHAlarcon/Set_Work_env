import sys
import yaml
import os

def crea_cartella(nome_cartella):
    if not os.path.exists(nome_cartella):
        os.makedirs(nome_cartella)
        print(f"Cartella '{nome_cartella}' creata con successo.")
    else:
        print(f"La cartella '{nome_cartella}' esiste già.")

def crea_file(nome_file, contenuto=''):
    with open(nome_file, 'w') as file:
        file.write(contenuto)
    print(f"File '{nome_file}' creato con successo.")

def load_set( file_path=None):
    if file_path!=None:
        with open(file_path, 'r') as file:
            try:
                data = yaml.safe_load(file)
            except yaml.YAMLError as e:
                print(f"Errore durante la lettura del file YAML: {e}")
    else:
        data={'Dirs':["Data","output","lib"] ,'file':["test.py","main.py","main.ipynb",".env",".env.cfg",".gitignore"]}
    for key in data:
        if key=='Dirs':
            for n_dir in data[key]:
                crea_cartella(n_dir)
        if key=='file':
            for n_dir in data[key]:
                crea_file(n_dir, contenuto='')

if __name__=='__main__':
    if len(sys.argv)>1 :
        file_path = sys.argv[1]
    else:
        file_path=None 
    load_set(file_path)
    sys.exit(1)