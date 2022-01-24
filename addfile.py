#Nota: lo script è stato scritto supponendo che il file (addfile.py) sia allo stesso livello della cartella "files"

import os, shutil, csv, argparse, sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type = str, help = "Nome del file da spostare completo di estensione (es.: 'trump.jpeg')")
    args = parser.parse_args()
    sys.stdout.write(str(move(args)))

def move(args):
    
    if os.getcwd().endswith("files") != True:
        os.chdir("files")
    else:
        pass

    while os.path.isfile(args.filename) != True or args.filename.split(".")[1] == "csv":
            print("Errore, il file non esiste nella cartella specificata o è un .csv (NON sono ammessi file .csv)")
            inp_2 = input("Immettere il nome del file completo di estensione (es.: 'trump.jpeg'):")
            args.filename = inp_2    
    
    
    #ESTENSIONI ACCETTATE 
    
    acc_docs = ["txt", "odt"]
    
    acc_images = ["png", "jpg", "jpeg"]
    
    acc_audio = ["mp3"]
    
    
    #CREAZIONE SOTTOCARTELLE ED ASSEGNAZIONE "TIPO" E "CARTELLA"
    
    tipo = ""
    cartella = ""
    
    if args.filename.split(".")[1] in acc_docs:
        tipo = "doc"
        cartella = "docs"
        if os.path.isdir(cartella) != True:
            os.makedirs(cartella)
        else:
            pass
    elif args.filename.split(".")[1] in acc_images:
        tipo = "image"
        cartella = "images"
        if os.path.isdir(cartella) != True:
            os.makedirs(cartella)
        else:
            pass
    else:
        tipo = "audio"
        cartella = "audio"
        if os.path.isdir(cartella) != True:
            os.makedirs(cartella)
        else:
            pass
    
    
    #CREAZIONE ED HEADER FILE RECAP.CSV ("W" MODE PERCHE' DEVO SCRIVERE L'HEADER SULLA PRIMA RIGA DEL FILE)
    
    if os.path.isfile("recap.csv") == False:
        with open('recap.csv', mode='w', newline="") as recap:
            recappino = csv.writer(recap, delimiter=',')
            recappino.writerow(["name", "type", "size(B)"])
    else:
        pass
    
    
    #APRO IL FILE RECAP.CSV IN "A" MODE (DEVO AGGIUNGERE, NON SOVRASCRIVERE)
    with open('recap.csv', mode='a', newline="") as recap:
        recappino = csv.writer(recap, delimiter=',')
        
        d = os.stat(args.filename)
        
        #STAMPO A SCHERMO LE INFORMAZIONI (NAME, TYPE, SIZE(B)) DEl FILE
        print(args.filename.split(".")[0], "type:{}".format(tipo), "size:{}B".format(d.st_size))
        
        #SCRIVO LE INFORMAZIONI (NAME, TYPE, SIZE(B)) DEl FILE ALL'INTERNO DEL FILE RECAP.CSV
        recappino.writerow([args.filename.split(".")[0], "{}".format(tipo), "{}".format(d.st_size)])
        
    #SPOSTO I FILES NELLE RELATIVE SOTTOCARTELLE
    shutil.move(args.filename, cartella)

    return ''

main()
