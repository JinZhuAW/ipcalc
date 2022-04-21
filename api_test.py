from requests import request
import requests

api_url = "http://127.0.0.1:8000/"

def ip_to_binary(ip,mask):
    '''call the ip to binary function in the API we created
    
    ip: the ip address in decimal
    mask :the netmask in decimal
    '''
    #Combin the url with the function we created
    url = api_url + "ip_to_binary"
    #Set up parameters which will be sent
    params = {'ip' : ip,'mask' : mask}
    #Send the parameters and get the response by using requests.post method
    response = requests.post(url = url,params= params)
    return response

if __name__=="__main__":
    #Ask user for inputs
    ip_address = input("Please type in the IP address: ")
    mask = input("Please type in the Netmask(i.e.24): ")
    #Sending both parameters to the API and geting response back
    response = ip_to_binary(ip_address,mask)
    #Parsing the response json and get the ip in binary
    binary_ip = response.json()["ip"]
    #Parsing the response json and get the netmask in binary
    binary_mask = response.json()["mask"]
    #Print out the results
    print(f'{"":=<90}')
    print(f'{"Address:":10}{ip_address:30}{binary_ip:50}')
    print(f'{"Netmask:":10}{mask:30}{binary_mask:50}')

    
