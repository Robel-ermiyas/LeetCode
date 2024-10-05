# time complexity = O(nlogn)
# space complexity = O(1) = constant
class Solution:
     def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  
        light, heavy = 0, 
        len(people) - 1 
        boats = 0 
        while light <= heavy:
            if people[light] + people[heavy] <= limit:  
                light += 1  # Move the light pointer to the right
            heavy -= 1 
            boats +=1
        return boats
