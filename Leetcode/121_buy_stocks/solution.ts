function maxProfit(prices: number[]): number {
  let curr_price = prices[0];
  let profit = 0;

  for (let price of prices) {
    curr_price = Math.min(price, curr_price);
    profit = Math.max(profit, price - curr_price);
  }

  return profit;
}
