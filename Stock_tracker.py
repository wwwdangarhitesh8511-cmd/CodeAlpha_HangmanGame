def stock_portfolio():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 170,
        "MSFT": 400
    }
    
    portfolio = {}
    print("📈 Stock Portfolio Tracker માં તમારું સ્વાગત છે!")

    while True:
        stock_symbol = input("\nશેરનું નામ લખો (અથવા પૂરું કરવા 'exit' લખો): ").upper()
        if stock_symbol == 'exit':
            break
        
        if stock_symbol not in stock_prices:
            print("⚠️ આ શેર ઉપલબ્ધ નથી.")
            continue
            
        try:
            quantity = int(input(f"{stock_symbol} ના કેટલા શેર ખરીદ્યા છે: "))
            if quantity < 0:
                print("⚠️ સંખ્યા પોઝિટિવ હોવી જોઈએ.")
                continue
            portfolio[stock_symbol] = quantity
        except ValueError:
            print("⚠️ સાચો આંકડો લખો.")

    print("\n--- પોર્ટफोलિયો રિપોર્ટ ---")
    tot_inv = 0
    for stock, qty in portfolio.items():
        cost = stock_prices[stock] * qty
        tot_inv += cost
        print(f"શેર: {stock} | ક્વોન્ટિટી: {qty} | કિંમત: ${cost}")

    print("-" * 30)
    print(f"💰 કુલ રોકાણ: ${tot_inv}")

if __name__ == "__main__":
    stock_portfolio()
