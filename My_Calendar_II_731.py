class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlapped = []

    def book(self, start: int, end: int) -> bool:
        """
        range search, brutal force: https://zxi.mytechroad.com/blog/geometry/leetcode-731-my-calendar-ii/
        Time Complexity: O(n^2)

        Space Complexity: O(n)

        """
        for s, e in self.overlapped:
            if not (end <= s or e <= start):
                # overlapped twice
                return False
        for s, e in self.booked:
            if not (end <= s or e <= start):
                # overlapped first time
                # add overlapping range
                self.overlapped.append([max(s, start), min(e, end)])
        self.booked.append([start, end])
        return True


from sortedcontainers import SortedDict
class MyCalendarTwo2:

    def __init__(self):
        # delta event counter at a specific time
        self.delta_event_counter = SortedDict()

    def book(self, start: int, end: int) -> bool:
        """ range query
        https://www.youtube.com/watch?v=rRMdxFA-8G4
        复杂度错了，看comments
        Time Complexity: O(n^2)

        Space Complexity: O(n)

        """
        if start not in self.delta_event_counter:
            self.delta_event_counter[start] = 1
        else:
            self.delta_event_counter[start] += 1
        if end not in self.delta_event_counter:
            self.delta_event_counter[end] = -1
        else:
            self.delta_event_counter[end] -= 1
        counter = 0
        for time, count in self.delta_event_counter.items():
            counter += count
            if counter == 3:
                self.delta_event_counter[start] -= 1
                self.delta_event_counter[end] += 1
                return False
            if time > end:
                break

        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)