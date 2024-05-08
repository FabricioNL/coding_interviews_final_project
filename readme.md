# Problem

Given a set of cities connected by flights, represented as a list of flights where each flight contains the origin city, destination city, and the price, along with three integers representing the source city, destination city, and the maximum number of stops allowed, the objective is to find the cheapest price to reach the destination city from the source city with at most k stops.

## Definitions

- **Flights**: Represented as a list of triples `[from_i, to_i, price_i]`, indicating a flight from city `from_i` to city `to_i` with cost `price_i`.
- **Source (src)**: The starting city.
- **Destination (dst)**: The target city.
- **Stops (k)**: The maximum number of stops allowed during the journey.

### Additional information

- If there is no valid route satisfying the constraints, return `-1`.
- The cost of a route is the sum of the prices of all flights taken.

## Examples

Given the following inputs:

- flights = [[0,1,100] , [1,2,100] , [0,2,500]]
- src = 0
- dst = 2
- k = 1

The cheapest price from city 0 to city 2 with at most 1 stop is 200 (0 -> 1 -> 2).

## Hints

- Think about how to traverse the flights to find the cheapest route with at most k stops.
- Consider using techniques like breadth-first search (BFS) or dynamic programming (DP) to efficiently explore all possible routes.

## Solution

To solve this problem efficiently, we can use a dynamic programming approach or implement a modified version of breadth-first search (BFS) to explore all possible routes from the source city to the destination city with at most k stops.

Here's an outline of the solution:

1. Initialize a data structure to store the minimum cost to reach each city with a given number of stops.
2. Start with the source city and perform BFS, considering each flight as a potential next stop.
3. Keep track of the number of stops and the total cost for each visited city.
4. Update the minimum cost to reach each city with the current number of stops if a cheaper route is found.
5. Continue BFS until either the destination city is reached or the maximum number of stops is exceeded.

By following this approach, you can efficiently find the cheapest price to reach the destination city from the source city with at most k stops.

## Complexity

### Breadth-First Search (BFS) Approach

**Time Complexity**: 
- In the worst case, the BFS traversal visits each vertex and edge once. Therefore, the time complexity is O(V + E), where V is the number of vertices (cities) and E is the number of edges (flights).

**Space Complexity**: 
- The space complexity for BFS depends on the number of vertices visited during the traversal. In the worst case, the space complexity is O(V), where V is the number of vertices.

### Dynamic Programming Approach

**Time Complexity**: 
- In the dynamic programming approach, we iterate over all vertices and consider all possible combinations of stops. Therefore, the time complexity is O(V^2 * k), where V is the number of vertices and k is the maximum number of stops allowed.

**Space Complexity**: 
- In dynamic programming, we need to store the minimum cost to reach each vertex with a given number of stops. Therefore, the space complexity is O(V * k), where V is the number of vertices and k is the maximum number of stops allowed.
