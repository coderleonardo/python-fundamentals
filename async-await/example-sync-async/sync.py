import time 

def calculate_revenue(prices):
    total_revenue = 0
    for price in prices:
        total_revenue += price
        print(f"Revenue: {price}")
        time.sleep(1)
    return total_revenue

def calculate_cost(costs):
    total_cost = 0
    for cost in costs:
        total_cost += cost
        print(f"Cost: {cost}")
        time.sleep(2)
    return total_cost

def calculate_profit(prices, costs):

    revenue = calculate_revenue(prices)
    cost = calculate_cost(costs)
    time.sleep(3)  # Simulate some processing delay
    # Log the profit calculation
    print(f"Calculating profit: Revenue = {revenue}, Cost = {cost}")
    return revenue - cost


if __name__ == "__main__":
    prices = [100, 200, 300]
    costs = [50, 100, 150]

    print("Starting profit calculation...")
    profit = calculate_profit(prices, costs)
    print(f"Profit: {profit}")
