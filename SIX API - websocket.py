#!/usr/bin/env python
import asyncio
import websockets
import json 
import ssl
import random

url = "wss://bfi-mvp-streaming.six-group.com/api/bfi-wss-prices-auth/v1"
                                                                                                     
certificate_path = './ch52991-hackathon1'
ssl_ctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_ctx.load_cert_chain(f'{certificate_path}/signed-certificate.pem', f'{certificate_path}/private-key.pem')
                    
gql_request = """subscription {
   startStream(
        streamId: "{streamId}" 
        scheme: TICKER_BC 
        ids: ["ABBN_4"] 
        conflationType: INTERVAL
        conflationInterval:"300ms"
   ) {
    type
    requestedId
    requestedScheme
    qualityOfService
    last {
      value
      unixTimestamp
      size
    }
    high {
      value
      unixTimestamp
    }
    low {
      value
      unixTimestamp
    }       
    bestBid {
      value
      unixTimestamp
    }
    bestAsk {
      value
      unixTimestamp
    }
    orderBook {
      position
      side
      size
      value
      unixTimestamp
    }
  }
}"""

gql_close_request = """mutation { closeStream(streamId: "{streamId}") {
   type
   requestedId
   requestedScheme
} }"""

def jsonify_query(gql_query:str) :
  return json.dumps({ "query": gql_query })
  
async def events(url:str, graphql_request:str):
  global gql_close_request
  global ssl_ctx
  
  streamId = f"sid-{random.randint(0, 100_000)}"
  gql_request.replace("{streamId}", streamId)
  gql_close_request.replace("{streamId}", streamId)
  
  
  headers = { }
  async with websockets.connect(url, extra_headers=headers, ssl=ssl_ctx) as websocket:
    await websocket.send(jsonify_query(graphql_request))

    message_count = 50
    while message_count>0:
      message_count -=1
      print(message_count)
      try:
        message = await asyncio.wait_for(websocket.recv(), 1)      
        data = json.loads(message)
        if "errors" in data: 
          print(f"< {data}")
          break
        elif "data" in data:
          print(json.dumps(data, indent=2))
          #decode_msg(data['data'])
      except (asyncio.TimeoutError):
        print(f"Remaining time: {message_count}")
        
      if message_count==3:  
        print(f"===> CLOSE STREAM <===")
        await websocket.send(jsonify_query(gql_close_request))
        
asyncio.get_event_loop().run_until_complete(events(url, gql_request))