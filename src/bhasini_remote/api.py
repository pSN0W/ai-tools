from model import Model
from request import ModelRequest
from quart import Quart, request
import aiohttp

#from fastapi import FastAPI, Body
app = Quart(__name__)
#app.client = aiohttp.ClientSession()
#app = FastAPI()

@app.before_serving
async def startup():
    app.client = aiohttp.ClientSession()

@app.route('/translate', methods=['POST'])
async def translate():
    data = await request.get_json()
    req = ModelRequest(**data)
    print(req.to_json())
    model = Model(app)
    return await model.inference(req)
