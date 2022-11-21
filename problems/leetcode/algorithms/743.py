# 743 - Network Delay Time, https://leetcode.com/problems/network-delay-time/description/


# solution 1 - Bellman-Ford algorithm
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf') for _ in range(n)]
        dist[k-1] = 0
        for _ in range(n-1):
            for u, v, w in times:
                if v < float('inf'):
                    dist[v - 1] = min(dist[v - 1], dist[u - 1] + w)
        return max(dist) if max(dist) < float('inf') else -1


# solution 2 - Bellman-Ford algorithm with slight optimization
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf') for _ in range(n)]
        dist[k-1] = 0
        while True:
            changed = False
            for u, v, w in times:
                if v < float('inf'):
                    if dist[u - 1] + w < dist[v - 1]:
                        dist[v - 1] = dist[u - 1] + w
                        changed = True
            if not changed:
                break
        return max(dist) if max(dist) < float('inf') else -1