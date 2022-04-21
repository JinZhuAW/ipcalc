'''
IP calculator to convert number to binary
'''
from utils import number_to_binary,ip_to_binary,number_to_ip_mask
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hello")
def read_hello():
    return {"Hello": "Joe"}

@app.post('/add')
def add(a,b = 10):
    x = int(a)
    y = int(b)
    result = x + y
    return {"value" : result}

@app.post('/2binary')
def to_binary(a_number):
    number_as_int = int(a_number)
    result = number_to_binary(number_as_int)
    return result


@app.post('/ip_to_binary')
def post_ip_and_mask_to_binary(ip,mask):
    mask = number_to_ip_mask(mask)
    result = ip_to_binary(ip)
    return {'ip': result, 'mask': mask}
# Convert number from decimal to binary

# print(f'the number: {250:08b}')

