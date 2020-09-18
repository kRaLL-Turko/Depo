# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from tabulate import tabulate

from w_bs4.coinMarketCap import coinMarket
from w_bs4.nobetciEczane import nobetciEczane
from w_pandas.doviz import dovizVerileri

def md_github(veri):
    """
    Verilen veriyi github md tablo diline çevirir...
    """

    return tabulate(veri, headers='keys', tablefmt='github')

with open("coinMarket.md", "w+") as coin:
    coin.write(md_github(coinMarket('json_veri')))

with open("nobetciEczane.md", "w+") as nobetci:
    nobetci.write(md_github(nobetciEczane('çanakkale', 'merkez', 'json_veri')))

with open("dovizVerileri.md", "w+") as doviz:
    doviz.write(md_github(dovizVerileri('json_veri')))