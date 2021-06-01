"""
Implement the RandomizedSet class:

    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present,
        false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present,
    false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one
        element exists when this method is called). Each element must have the same probability of being returned.

Example 1:

Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.

Constraints:
    -231 <= val <= 231 - 1
    At most 105 calls will be made to insert, remove, and getRandom.
    There will be at least one element in the data structure when getRandom is called.

Follow up: Could you implement the functions of the class with each function works in average O(1) time?

Learnings:
- Using a list allows O(1) constant time for getrandom and inserting, but not for removing
- Using a dict allows O(1) contant time for removing and basically localizing elements by key
- Best solution is to combine both data structure types: a list of numbers and a hashmap value -> index
- The key gotcha here is: when removing an element, we first find its index with the hashmap, then switch
    its position in the list with the last element and then call pop on list and pop or del the dict key
"""

import random


class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict, self.numbers = {}, []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dict:
            self.numbers.append(val)
            self.dict[val] = len(self.numbers) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            last_element, idx = self.numbers[-1], self.dict[val]
            self.numbers[idx], self.dict[last_element] = last_element, idx
            self.numbers.pop()
            self.dict.pop(val, 0)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.numbers[random.randint(0, len(self.numbers) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
