from __future__ import absolute_import, unicode_literals
from celery import task
from Coin.models import BitcoinEntry
import requests

def get_last_since_utc():
    entry = BitcoinEntry.objects.latest('id')
    return str(entry.getUTC())

"""
@task()
def get_bitcoin_entry():
    print("Atempting to Retreive Bitcoin Entry Data")
    try:
        print("Atempting to Retreive Bitcoin Entry Data")
        result = [BitcoinEntry.object.latest('date')]
        r = requests.get("https://api.kraken.com/0/public/OHLC?pair=xbtgbp&interval=1&since=" + get_last_since_utc())
        entry = r.json()['result']['XXBTZGBP'][-1]
        time = entry['result']['XXBTZGBP'][-1][0]
        priceofcoin = entry['result']['XXBTZGBP'][-1][1]
        newEntry = BitcoinEntry(utc=str(time), price=priceofcoin)
        newEntry.save()
    except:
        print("[ERROR] Couldn't get Bitcoin")
        return

    print("[SUCCESS] Got the bitcoin data")
    return
"""
@task()
def get_bitcoin_entry():
    print("Attempting to retreive Bitcoin Entry Data")
    counter = 0
    try:
        r = requests.get("https://api.kraken.com/0/public/OHLC?pair=xbtgbp&interval=1&since=" + get_last_since_utc())
        entries = r.json()['result']['XXBTZGBP']
        for entry in entries:
            utc_time = entry[0]
            price_of_coin = entry[1]

            newEntry = BitcoinEntry(utc=str(utc_time), price=price_of_coin)
            newEntry.save()
            counter += 1

    except:
        print("[ERROR] Couldn't get the bitcoin data")
        return

    print("[SUCCESS] Added " + str(counter) + "(s) to the database")
    return
