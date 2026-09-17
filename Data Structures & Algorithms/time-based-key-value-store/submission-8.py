class TimeMap:
    """
    1. stores multiple values for the same key but different timestamps (val1, ts1), (val2, ts2)
    2. set: stores key, val, timestamp
    3. get: returns val from most recent timestamp else ""

    hashMap {
        key1: [ts1, ts2] [val1, val2)
        key2: (ts1, val1), (val2, ts2)
    }
    """

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [[], []]
        self.store[key][0].append(timestamp)
        self.store[key][1].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        idx =  self.find(timestamp, self.store[key][0])
        if idx == -1:
            return ""

        return self.store[key][1][idx]

    def find(self, target, timestampList):
        left, right = 0, len(timestampList) - 1

        while left <= right:
            mid = (left + right) // 2

            if timestampList[mid] == target:
                return mid
            elif timestampList[mid] < target:
                # Valid, but maybe there's a closer timestamp to the right
                left = mid + 1
            else:
                # Too large
                right = mid - 1
        
        return right

