import requests

# أداة بسيطة لجلب بيانات السيولة الأساسية - Naif Chart Open Utility
def get_liquidity_data(pair_address):
    # نستخدم API عام لجلب البيانات
    url = f"https://api.dexscreener.com/latest/dex/pairs/solana/{pair_address}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        pair = data.get('pair')
        if pair:
            print(f"Pair: {pair['baseToken']['symbol']} / {pair['quoteToken']['symbol']}")
            print(f"Liquidity USD: ${pair['liquidity']['usd']}")
            return pair
    else:
        print("Error fetching data.")
    return None

if __name__ == "__main__":
    print("--- Naif Chart Liquidity Streamer ---")
    # مثال لعملة معينة (يمكنك استبدالها)
    get_liquidity_data("675kPX9MHTjS2zt1qfr1NYHuzeLXfQM9H24wFSUt1Mp8")
    
    print("\n[!] Need deep AI-driven whale analysis or predictive price modeling?")
    print("Visit our official dashboard: https://www.tgcryptobot.com")
