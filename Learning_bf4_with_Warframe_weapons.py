#Warframe_Weapons
import requests
from bs4 import BeautifulSoup
import numpy as np
import time


def weapon_finder(url):
    global weapon_list,link_list,data_list,value_list_global
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    weapon_entries = soup.find_all("a", class_="category-page__member-link")
    for entry in weapon_entries:
        print(type(entry))
        weapon_name = entry.text
        weapon_link = "https://warframe.fandom.com" + entry.get("href")
        if weapon_name.split(":")[0] in ['Category','Amp',"Conclave","User","Template"] or weapon_name.split("/")[0] in ["Blueprints"] or "Skin" in weapon_name.split(" ") or weapon_name in ["Necramech","Syndicate Weapons","Exalted Weapon","Orb Vallis Survival Collection","Kitgun","Incarnon"]:
            continue
        weapon_list.append(weapon_name)
        link_list.append(weapon_link)
    
        
    
def weapon_stat_finder(weapon):
    global weapon_list,link_list,data_list_global,value_list_global,tic2
    tic2 = time.perf_counter()
    pos = weapon_list.index(weapon)
    link = link_list[pos]
    data_list = []
    value_list = []
    
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    
    weapon_stats = soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color')
    
    div_element = soup.find_all("div", class_="pi-data-value pi-font")
    for i in div_element:
        value = i.get_text(strip=True)
        value_list.append(value)
        
    for k in weapon_stats:
        data_src = k.get("data-source")
        data_list.append(data_src)
        
        if data_src in ["UpdateInfoboxData","Introduced","Categories","DefaultUpgrades","Template:WeaponInfoboxAutomatic","Offerings"]:
            value_list.pop(data_list.index(data_src)) 
            data_list.pop(data_list.index(data_src)) 
            continue
        

    value_list_global.append(value_list)
    data_list_global.append(data_list)
            
            
def stat_database():
    global armas,weapon_list,link_list,data_list_global,value_list_global,weapon_data,urls,tic2
    tic = time.perf_counter()
    armas = {}
    for url in urls:
        weapon_finder(url)

    for weapon in weapon_list:
        weapon_stat_finder(weapon)
        weapon_data = {}

        for k in data_list_global[weapon_list.index(weapon)]: 
            weapon_data[k] = value_list_global[weapon_list.index(weapon)][data_list_global[weapon_list.index(weapon)].index(k)]
        armas[weapon] = weapon_data
        toc2 = time.perf_counter()
        print(f"{weapon} done in {toc2 - tic2:0.4f} seconds")
    toc = time.perf_counter()
    print(f"All data done in {toc - tic:0.4f} seconds")
    
    
    
    
def ask_weapon():
    global weapon
    weapon = input("What weaopn are you looking for?")
    print("")
    try:
        for i in urls:
            weapon_finder(i)
            try:
                weapon_stat_finder(weapon)
                break
            except ValueError:
                "next page"
        print('Name : ',weapon)
        for i in armas[weapon]: 
            print("+"+"-"*55+"+")
            print("|",i,":",armas[weapon][i]," "*(50-(len(i)+len(armas[weapon][i])))+"|") 
        print("+"+"-"*55+"+")
    except KeyError:
        pass
    
          
def start():
    global urls, weapon_list, link_list, value_list_global, data_list_global
    alphabeto = ["A","B","C","D","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    urls = ["https://warframe.fandom.com/wiki/Category:Weapons?from="+Inicial for Inicial in alphabeto]
    weapon_list = []
    link_list = []
    value_list_global = []
    data_list_global = []
    

start()
stat_database()
while True:
    preguntar_arma()
    if input("Want to look for another weapon?").upper() == "NO":
        break
print("Hope i was able to help you find the weapon you wanted, have a great day!")

  