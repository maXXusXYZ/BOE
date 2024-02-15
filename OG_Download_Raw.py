import requests
from datetime import datetime
import os

def download_boja_xml(download_path):
    url = "https://www.juntadeandalucia.es/boja/distribucion/boja.xml"
    response = requests.get(url)
    if response.status_code == 200:
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"BOJA-{today}.xml"
        full_path = os.path.join(download_path, filename)  # Combine path and filename
        with open(full_path, 'wb') as file:
            file.write(response.content)
        print(f"File successfully downloaded and saved as {full_path}")
    else:
        print("Failed to download the file.")

def download_boa_xml(download_path):
    url = "https://www.boa.aragon.es/cgi-bin/EBOA/BRSCGI?CMD=RSSLST&DOCS=1-200&BASE=BOLE&SEC=BOARSS&SEPARADOR=&PUBL-C=lafechaxx"
    response = requests.get(url)
    if response.status_code == 200:
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"BOA-{today}.xml"
        full_path = os.path.join(download_path, filename)  # Combine path and filename
        with open(full_path, 'wb') as file:
            file.write(response.content)
        print(f"File successfully downloaded and saved as {full_path}")
    else:
        print("Failed to download the file.")

def download_doe_xml(download_path):
    url = "https://doe.juntaex.es/rss/rss.php?seccion=6"
    response = requests.get(url)
    if response.status_code == 200:
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"DOE-{today}.xml"
        full_path = os.path.join(download_path, filename)  # Combine path and filename
        
        with open(full_path, 'wb') as file:
            file.write(response.content)
        print(f"File successfully downloaded and saved as {full_path}")
    else:
        print("Failed to download the file.")

def download_dog_xml(download_path):
    url = "https://www.xunta.gal/diario-oficial-galicia/rss/Sumario_es.rss"
    response = requests.get(url)
    if response.status_code == 200:
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"DOG-{today}.xml"
        full_path = os.path.join(download_path, filename)
        
        with open(full_path, 'wb') as file:
            file.write(response.content.decode('utf-8').encode('utf-8'))  # Decode and encode in utf-8 to handle encoding
        print(f"File successfully downloaded and saved as {full_path}")
    else:
        print("Failed to download the file.")

def download_borm_xml(download_path):
    url = "https://www.borm.es/rss/boletin.xml"
    response = requests.get(url, verify=False)
    if response.status_code == 200:
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"BORM-{today}.xml"
        full_path = os.path.join(download_path, filename)
        
        with open(full_path, 'wb') as file:
            # Ensures correct handling of the response's encoding
            file.write(response.content)
        print(f"File successfully downloaded and saved as {full_path}")
    else:
        print("Failed to download the file.")

def download_bocm_xml(download_path):
    url = "https://www.bocm.es/ultimo-boletin.xml"
    response = requests.get(url)
    if response.status_code == 200:
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"BOCM-{today}.xml"
        full_path = os.path.join(download_path, filename)
        
        with open(full_path, 'wb') as file:
            file.write(response.content)
        print(f"File successfully downloaded and saved as {full_path}")
    else:
        print("Failed to download the file.")

def download_bocyl_xml(download_path):
    url = "https://bocyl.jcyl.es/rss.do"
    response = requests.get(url)
    if response.status_code == 200:
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"BOCYL-{today}.xml"
        full_path = os.path.join(download_path, filename)
        
        with open(full_path, 'wb') as file:
            file.write(response.content)
        print(f"File successfully downloaded and saved as {full_path}")
    else:
        print("Failed to download the file.")

# Example usage with a specified path
download_path_BOCYL = r"C:\Users\marcos.garcia\LIGHTSOURCE HOLDINGS 2 LIMITED\Development Spain - Documents\D400 Knowledge Center\D420 Market Intelligence\421 Intelligence Sources\OG_Pubs\BOCYL"
download_bocyl_xml(download_path_BOCYL)
download_path_BOCM = r"C:\Users\marcos.garcia\LIGHTSOURCE HOLDINGS 2 LIMITED\Development Spain - Documents\D400 Knowledge Center\D420 Market Intelligence\421 Intelligence Sources\OG_Pubs\BOCM"
download_bocm_xml(download_path_BOCM)
download_path_BORM = r"C:\Users\marcos.garcia\LIGHTSOURCE HOLDINGS 2 LIMITED\Development Spain - Documents\D400 Knowledge Center\D420 Market Intelligence\421 Intelligence Sources\OG_Pubs\BORM"
download_borm_xml(download_path_BORM)
download_path_DOG = r"C:\Users\marcos.garcia\LIGHTSOURCE HOLDINGS 2 LIMITED\Development Spain - Documents\D400 Knowledge Center\D420 Market Intelligence\421 Intelligence Sources\OG_Pubs\DOG"
download_dog_xml(download_path_DOG)
download_path_DOE = r"C:\Users\marcos.garcia\LIGHTSOURCE HOLDINGS 2 LIMITED\Development Spain - Documents\D400 Knowledge Center\D420 Market Intelligence\421 Intelligence Sources\OG_Pubs\DOE"
download_doe_xml(download_path_DOE)
download_path_BOA = r"C:\Users\marcos.garcia\LIGHTSOURCE HOLDINGS 2 LIMITED\Development Spain - Documents\D400 Knowledge Center\D420 Market Intelligence\421 Intelligence Sources\OG_Pubs\BOA"
download_boa_xml(download_path_BOA)
download_path_BOJA = r"C:\Users\marcos.garcia\LIGHTSOURCE HOLDINGS 2 LIMITED\Development Spain - Documents\D400 Knowledge Center\D420 Market Intelligence\421 Intelligence Sources\OG_Pubs\BOJA"
download_boja_xml(download_path_BOJA)
