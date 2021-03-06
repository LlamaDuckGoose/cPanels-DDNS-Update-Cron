import requests, socket, datetime
from datetime import datetime

homeUrl = "" #cPanels DDNS subdomain
DdnsUrl = "" #cPanels DDNS Url

def main():
    currentIp = getCurrentIp()
    hostIp = getDynamicIp()

    if (currentIp != hostIp):
        try:
            response = requests.get(DdnsUrl)
        except requests.exceptions.HTTPError as errH:
            print ('Http Error:', errH)
        except requests.exceptions.ConnectionError as errC:
            print ("Error Connecting:", errC)
        except requests.exceptions.Timeout as errR:
            print ("Timeout Error:", errR)
        except requests.exceptions.RequestException as errR:
            print ("OOps: Something Else", errR)

        current_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
         
        if response.status_code == 200:
            print(current_time, "Successfully updated DDNS:", response.text)
        else:
            print(current_time, "Failed updated DDNS")

def getCurrentIp():
    response = requests.get('https://api.ipify.org')

    try:
        if response:
            return(response.text)
        else:
            print("not found")
    except requests.exceptions.HTTPError as errH:
        print ('Http Error:', errH)
    except requests.exceptions.ConnectionError as errC:
        print ("Error Connecting:", errC)
    except requests.exceptions.Timeout as errR:
        print ("Timeout Error:", errR)
    except requests.exceptions.RequestException as errR:
        print ("OOps: Something Else", errR)

def getDynamicIp():
    response = socket.gethostbyname(homeUrl)
    
    try:
        if response:
            return(response)
        else:
            print("not found")
    except socket.error as err:
        print ("Caught exception socket.error :", err)

main()
