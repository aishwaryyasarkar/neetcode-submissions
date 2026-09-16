class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key]=[(timestamp, value)]
        else:
            self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        else:
            candidate = self.timeMap[key]
            return self.search(candidate, timestamp)

    def search(self, candidate: List, timestamp: int) -> str:
        start = 0
        end = len(candidate) - 1

        while start <= end:
            mid = (start + end) // 2

            ts, val = candidate[mid]

            if timestamp == ts:
                return val
            elif timestamp > ts:
                start = mid + 1
            elif timestamp < ts:
                end = mid - 1

        if end >= 0:
            return candidate[end][1]
        else:
            return ""

        
