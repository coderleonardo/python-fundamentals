import asyncio

async def calculate_revenue(prices):
    total_revenue = 0
    for price in prices:
        total_revenue += price
        print(f"Revenue: {price}")
        await asyncio.sleep(1)
    return total_revenue

async def calculate_cost(costs):
    total_cost = 0
    for cost in costs:
        total_cost += cost
        print(f"Cost: {cost}")
        await asyncio.sleep(2)
    return total_cost

async def calculate_profit(prices, costs):
    revenue_task = asyncio.create_task(calculate_revenue(prices))
    cost_task = asyncio.create_task(calculate_cost(costs))

    await asyncio.sleep(3)  # Simulate some processing delay
    print(f"Calculating profit: Revenue = {revenue_task}, Cost = {cost_task}")

    revenue = await revenue_task
    cost = await cost_task
    return revenue - cost

if __name__ == "__main__":
    prices = [100, 200, 300]
    costs = [50, 100, 150]

    print("Starting profit calculation...")
    profit = asyncio.run(calculate_profit(prices, costs))
    print(f"Profit: {profit}")
