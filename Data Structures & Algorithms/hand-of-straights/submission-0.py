class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if (len(hand) % groupSize) != 0:
            return False

        nGroups = len(hand) / groupSize
        freqMap = {}

        for i in range(len(hand)):
            if hand[i] not in freqMap:
                freqMap[hand[i]] = 0
            freqMap[hand[i]] += 1
        
        hand.sort()

        count = 0
        for i in range(len(hand)):
            # already consumed in a previous group
            if freqMap[hand[i]] == 0:
                continue

            currCard = hand[i]
            
            for count in range(groupSize):
                if currCard not in freqMap or freqMap[currCard] == 0:
                    return False

                freqMap[currCard] -= 1
                currCard += 1

        return True

            
