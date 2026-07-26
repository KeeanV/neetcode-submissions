class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_map = defaultdict(int)
        for i in nums:
            my_map[i] += 1
        my_heap = []
        for val, frq in my_map.items():
            heapq.heappush(my_heap, (frq,val))
            if len(my_heap) > k:
                heapq.heappop(my_heap)
        result = []
        for frq, val in my_heap:
            result.append(val)
        return result