class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort if not sorted properly based on the first element

        intervals = sorted(intervals, key=lambda x: x[0])
        return_array = []
        index = 1
        start_element = intervals[0]
        while index < len(intervals):
            if (
                intervals[index][0] >= start_element[0]
                and intervals[index][0] <= start_element[1]
            ):
                start_element[1] = (
                    start_element[1]
                    if start_element[1] > intervals[index][1]
                    else intervals[index][1]
                )
            else:
                return_array.append(start_element)
                start_element = intervals[index]
            index += 1
        return_array.append(start_element)
        return return_array
