from bs4 import BeautifulSoup as bs
import requests
import json

# url = 'https://query2.finance.yahoo.com/v1/finance/screener?crumb=soALzbXoa1j&lang=en-US&region=US&formatted=true&corsDomain=finance.yahoo.com'
# url = 'https://query1.finance.yahoo.com/v1/finance/screener?crumb=soALzbXoa1j&lang=en-US&region=US&formatted=true&corsDomain=finance.yahoo.com'
url = 'https://query1.finance.yahoo.com/v1/finance/screener?crumb=soALzbXoa1j&lang=en-US&region=US&formatted=true&corsDomain=finance.yahoo.com'

body = {
    "size": 25,
    "offset": 0,
    "sortField": "intradaymarketcap",
    "sortType": "DESC",
    "quoteType": "EQUITY",
    "topOperator": "AND",
    "query": {
        "operator": "AND",
        "operands": [
            {
                "operator": "or",
                "operands": [
                    {
                        "operator": "EQ",
                        "operands": ["region", "us"]
                    }
                ]
            },
            {
                "operator": "gt",
                "operands": [
                    "lastclosemarketcap.lasttwelvemonths",
                    1000000000
                ]
            }
        ]
    },
    "userId": "3TCJEQCXOUUVV4TQT6EXZ45WDE",
    "userIdType": "guid"
}

b2 = {
    "size": 100,
    "offset": 300,
    "sortField": "intradaymarketcap",
    "sortType": "DESC",
    "quoteType": "EQUITY",
    "topOperator": "AND",
    "query": {
        "operator": "AND",
        "operands": [
                {
                    "operator": "or",
                    "operands": [
                        {
                            "operator": "EQ",
                            "operands": ["region", "us"]
                        }
                    ]
                },
            {
                    "operator": "gt",
                    "operands": [
                        "lastclosemarketcap.lasttwelvemonths",
                        1000000000
                    ]
            }
        ]
    },
    "userId": "3TCJEQCXOUUVV4TQT6EXZ45WDE",
    "userIdType": "guid"
}

b3 = {
    "size": 100,
    "offset": 300,
    "sortField": "intradaymarketcap",
    "sortType": "DESC",
    "quoteType": "EQUITY",
    "topOperator": "AND",
    "query": {
        "operator": "AND",
        "operands": [
            {
                "operator": "or",
                "operands": [
                    {
                        "operator": "EQ",
                        "operands": [
                            "region",
                            "us"
                        ]
                    }
                ]
            },
            {
                "operator": "gt",
                "operands": [
                    "lastclosemarketcap.lasttwelvemonths",
                    1000000000
                ]
            }
        ]
    },
    "userId": "3TCJEQCXOUUVV4TQT6EXZ45WDE",
    "userIdType": "guid"
}

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'Cookie': 'APID=1A56232e44-3877-11ea-b6c0-06f6d094411e; F=d=WaoRGDs9vEn9PP.1j_CNj8cibYltyfAfX8_WQ7A-; Y=v=1&n=7a4f8hpf4rh8t&l=2l0h60iqu/o&p=m2i06np00000000&r=7d&intl=us; AO=u=1; A1=d=AQABBG0PM14CENue9kV3Ri4E562p0QZUluQFEgEAAQKfOV4cX9xH0iMA_SMAAAcIS4UgXqTrZncID2HBBzjoVWxXCxXwUGS5RgkBBwoBBw&S=AQAAAknBUSdrtZNFBH7LI512U_o; A3=d=AQABBG0PM14CENue9kV3Ri4E562p0QZUluQFEgEAAQKfOV4cX9xH0iMA_SMAAAcIS4UgXqTrZncID2HBBzjoVWxXCxXwUGS5RgkBBwoBBw&S=AQAAAknBUSdrtZNFBH7LI512U_o; GUC=AQEAAQJeOZ9fHEIgKwRt; ucs=tr=1584477160000; T=af=JnRzPTE1ODQzOTA3NjEmcHM9NjNaYlp3SUY4QnhpWFhJWV95UnZmZy0t&d=bnMBeWFob28BZwEzVENKRVFDWE9VVVZWNFRRVDZFWFo0NVdERQFzbAFNemN3TWdFNU1URTNOams1TkRVLQFhYwFBUE0yN2VaUQFhbAFjdmFyZ2FzMDQBc2MBZGVza3RvcF93ZWIBZnMBWGduTWpHUmVPRlB5AXp6AXBublplQmtiSAFhAVFBRQFsYXQBeVBGT2VC&sk=DAAXuHJVNAe8.S&ks=EAA9zbosqn2hjNqBCmbydxAJA--~G&kt=EAAnC1nA7hr04oK6JCHaYIveQ--~I&ku=FAAeT0VUl3NYTtkZrKe4D.UmO9rf6hb4aSZgHwY5WpW2KB69ahpQ4EvtiEacpcYnO_eXrdeR9We011Gs_7zo.VctlQank8R4KeWh6ejgO923oOlSuEPF_d_pgT0namYuArHckwbavD3dHPnFn34_z2qErj1XSjNR6e6I2M2crK2G1I-~A; PH=fn=qq3v4YceiMiTi7T41qw-&l=en-US&i=us; PRF=t%3DMSFT; B=7epnbkhf211ab&b=4&d=Nvgr5AVtYFp_VoFBt.HB&s=od&i=YcEHOOhVbFcLFfBQZLlG; APIDTS=1584908451; A1S=d=AQABBG0PM14CENue9kV3Ri4E562p0QZUluQFEgEAAQKfOV4cX9xH0iMA_SMAAAcIS4UgXqTrZncID2HBBzjoVWxXCxXwUGS5RgkBBwoBBw&S=AQAAAknBUSdrtZNFBH7LI512U_o&j=US; A1=d=AQABBG0PM14CENue9kV3Ri4E562p0QZUluQFEgEAAQKfOV4cX9xH0iMA_SMAAAcIS4UgXqTrZncID2HBBzjoVWxXCxXwUGS5RgkBBwoBBw&S=AQAAAknBUSdrtZNFBH7LI512U_o; A3=d=AQABBG0PM14CENue9kV3Ri4E562p0QZUluQFEgEAAQKfOV4cX9xH0iMA_SMAAAcIS4UgXqTrZncID2HBBzjoVWxXCxXwUGS5RgkBBwoBBw&S=AQAAAknBUSdrtZNFBH7LI512U_o; A1S=d=AQABBG0PM14CENue9kV3Ri4E562p0QZUluQFEgEAAQKfOV4cX9xH0iMA_SMAAAcIS4UgXqTrZncID2HBBzjoVWxXCxXwUGS5RgkBBwoBBw&S=AQAAAknBUSdrtZNFBH7LI512U_o&j=US; B=7epnbkhf211ab&b=4&d=Nvgr5AVtYFp_VoFBt.HB&s=od&i=YcEHOOhVbFcLFfBQZLlG; GUC=AQEAAQJeOZ9fHEIgKwRt',
    'content-type': 'application/json',
    'accept-encoding': 'gzip, deflate, br',
    # :authority: query2.finance.yahoo.com
    # :method: POST
    # :path: /v1/finance/screener?crumb=soALzbXoa1j&lang=en-US&region=US&formatted=true&corsDomain=finance.yahoo.com
    # :scheme: https
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-length': '836',
    'origin': 'https://finance.yahoo.com',
    'referer': 'https://finance.yahoo.com/screener/unsaved/1d8abe15-0805-4b16-be75-bb3fb9f9abfd?count=100&offset=300',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'host': 'query1.finance.yahoo.com',
    'connection': 'keep-alive',
    'postman-token': 'c7b79eca-cbea-4b95-b8f7-92ada0844d05',
    'Cache-Control': 'no-cache'
}

# cookie = {
# 	'__cfduid':'d9cb92273acbe2c9a2d76a655d2f6d0761582569839',
# 	 '_ga':'GA1.2.390211893.1582569841',
# 	 '_gid':'GA1.2.856486047.1584421137',
# 	 '_gat_gtag_UA_32729706_1':1,
# 	 '.ASPXAUTH':'810E31344AE13B2513166A2D4519E576750B7C8E244479F256AA686BD54A713FB0DE93924FA238480EBEB7E7703EDE42CCE93A515A0323998412F109CEC671150A1C34EAD3CAB4C4AB0E7F1FA0FDD4F1EA25625F7C132E541EDBFDD9CB8CDEE777A138ACAEF677F9D706770063F82817A8A8CC681A88D90875AD9249A6A44D0FC3354A1D00624FA072B433DE64CC13928B59ED5E0A422E04269ACA92D5B15335E00D24368E68819EF28DA96CA595B750'
# }

b4 = json.loads(
    '{"size":100,"offset":300,"sortField":"intradaymarketcap","sortType":"DESC","quoteType":"EQUITY","topOperator":"AND","query":{"operator":"AND","operands":[{"operator":"or","operands":[{"operator":"EQ","operands":["region","us"]}]},{"operator":"gt","operands":["lastclosemarketcap.lasttwelvemonths",1000000000]}]},"userId":"3TCJEQCXOUUVV4TQT6EXZ45WDE","userIdType":"guid"}')
try:
    resObj = requests.post(url, json=b2, headers=headers)
    res = resObj.text
    print('CVAR: type resObj:', type(resObj))
    print('CVAR: resObj\n\n', resObj)
    print('CVAR: res\n\n', res)
except Exception as e:
    print('CVAR: e...\n\n', e)

exit()

soup = bs(res, 'html.parser')
tables = soup.find_all('table')
# Data is in the last table
table = tables[len(tables) - 1]
rows = table.find_all('tr')

print()
print('Name', '\t\t\t\t\t', 'Ticker')
print(':::::::::::::::::::::::::::::::::::::::::::::::::')
print()

for tr in rows:
    td = tr.find_all('td')
    # print(td)
    if(len(td) > 1):
        # First two columns hold name and ticker respectively
        print(td[0].text, '\t', td[1].text)

print()


def main():
    pass


if __name__ == '__main__':
    main()

'''
https://query2.finance.yahoo.com/v1/finance/screener?crumb=soALzbXoa1j&lang=en-US&region=US&formatted=true&corsDomain=finance.yahoo.com

body = {
  "size":25,
  "offset":0,
  "sortField":"intradaymarketcap",
  "sortType":"DESC",
  "quoteType":"EQUITY",
  "topOperator":"AND",
  "query":{
    "operator":"AND",
    "operands":[
      {
        "operator":"or",
        "operands":[
          {
            "operator":"EQ",
            "operands":["region","us"]
          }
        ]
      },
      {
        "operator":"gt",
        "operands":[
          "lastclosemarketcap.lasttwelvemonths",
          1000000000
        ]
      }
    ]
  },
  "userId":"3TCJEQCXOUUVV4TQT6EXZ45WDE",
  "userIdType":"guid"
}
'''
