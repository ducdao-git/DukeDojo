class Solution2:  # Optimized: runtime O(target + n), space O(target)
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        car_times = [0] * target
        for i in range(len(position)):
            car_times[position[i]] = (target - position[i]) / speed[i]

        # instead of sorting, we just calculate the time of car at each position (if car exist)
        car_times = [t for t in car_times if t > 0]

        # consider car from near target to further out, if car take long time,
        # other car will catch up and make a fleet, else the car will not catch up and create a new fleet
        max_time = 0
        fleet_count = 0
        for t in car_times[::-1]:
            if t > max_time:
                max_time = t
                fleet_count += 1

        return fleet_count


class Solution:  # runtime O(nlogn), space O(n)
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars = sorted(cars, key=lambda c: c[0], reverse=True)

        fleet_count = 0
        fleet_stack = []
        for c in cars:
            time_reach_des = (target - c[0]) / c[1]

            flag = 0
            while fleet_stack and time_reach_des > fleet_stack[0]:
                flag = 1
                fleet_stack.pop()

            fleet_count += flag
            fleet_stack.append(time_reach_des)

        return fleet_count + 1


# Question URL: https://neetcode.io/problems/car-fleet/question?list=neetcode150
# Solution: stack -- runtime O(nlogn), space O(n)
#   add to stack if time to dest is smaller than the car at the front of the fleet.
#   pop all cars from stack if time larger than time of the front car (i.e. new fleet)
sol_test = Solution()
print(sol_test.carFleet(target=10, position=[0, 4, 2], speed=[2, 1, 3]))
