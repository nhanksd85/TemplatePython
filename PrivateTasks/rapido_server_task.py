from Network.http import *
class RapidoServerTask:
    def __init__(self):
        return
    def uploadData(self):
        objHTTP = HTTP()
        objHTTP.httpGet("abc")
        return
    def uploadData(self, PH, TSS, AMONI, TEMP, DHT_TEMP, DHT_HUMI):
        objHTTP = HTTP()
        objHTTP.httpGet(PH, TSS, AMONI, TEMP, DHT_TEMP, DHT_HUMI)
        return