class StockSpanner:

    def __init__(self):
        self.stock_price = []

    def next(self, price: int) -> int:
        span = 1

        while self.stock_price and self.stock_price[-1][0] <= price:

            span += self.stock_price.pop()[-1]

        self.stock_price.append([price, span])
        return span

