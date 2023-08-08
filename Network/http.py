import requests
class HTTP:
    ID_STATION = 14
    PH = 11
    AMONI = 12
    TSS = 13
    TEMP = 15
    TEMP_DHT = 16
    HUMI_DHT = 17

    def __init__(self):

        return
    def httpGet(self, url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 NPNLab'}

        url = "https://rapido.npnlab.com/api/rapido/push?station_id=" + str(self.ID_STATION)

        url = url + "&sensors[0].id=4&sensors[0].value=" + '%.2f' % self.PH
        url = url + "&sensors[1].id=5&sensors[1].value=" + '%.2f' % self.TSS
        url = url + "&sensors[2].id=1009&sensors[2].value=" + '%.2f' % self.AMONI


        x = requests.get(url=url, headers=headers, verify=False)
        print("Sending http request...", url)
        print(x.json())
        return
    def httpGet(self, ph, tss, amoni, temp, temp_dht, humi_dht):
        self.PH = ph
        self.TSS = tss
        self.AMONI = amoni
        self.TEMP = temp
        self.TEMP_DHT = temp_dht
        self.HUMI_DHT = humi_dht

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36 NPNLab'}

        url = "https://rapido.npnlab.com/api/rapido/push?station_id=" + str(self.ID_STATION)
        url = url + "&sensors[0].id=1&sensors[0].value=" + '%.2f' % self.TEMP
        url = url + "&sensors[1].id=4&sensors[1].value=" + '%.2f' % self.PH
        url = url + "&sensors[2].id=5&sensors[2].value=" + '%.2f' % self.TSS
        url = url + "&sensors[3].id=1005&sensors[3].value=" + '%.2f' % self.TEMP_DHT
        url = url + "&sensors[4].id=1006&sensors[4].value=" + '%.2f' % self.HUMI_DHT
        url = url + "&sensors[5].id=1009&sensors[5].value=" + '%.2f' % self.AMONI


        x = requests.get(url=url, headers=headers, verify=False)
        print("Sending http request...", url)
        print(x.json())
        return