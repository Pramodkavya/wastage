
# import requests
# import websocket
# import json
# import pprint
# import urllib.parse
# import os
# from datetime import datetime
# import os
# import sys
# import json
# import datetime
# import requests
# import dateutil.parser
# import pandas as pd
# from kiteconnect import KiteConnect, KiteTicker
# ENCTOKEN = get_enctoken()

import time
from kiteconnect import KiteConnect, KiteTicker
global tws

ENCTOKEN = "loveyoutrading"
print(f"🔑 Using ENCTOKEN: {ENCTOKEN}")
tws = KiteTicker(api_key="pramod",
                 access_token=ENCTOKEN + '&user_id=' + "GI6585",
                 )


# token_id = 4577537  # 256265
token_id = 256265  # nifty 50

# global tws


def on_ticks(ws, data):
    print(f"Ticks: {data}")


# tws = KiteTicker(api_key="pramod",
#                  access_token=ENCTOKEN + '&user_id=' + "GI6585",
#                  )
tws.on_ticks = on_ticks
tws.connect(threaded=True)

while not tws.is_connected():
    time.sleep(1)

# subscribe only to crudeoil token
tws.subscribe([token_id])
tws.set_mode(tws.MODE_FULL, [token_id])

print(f"✅ Subscribed to {token_id} ticks")
while True:
    time.sleep(1)
