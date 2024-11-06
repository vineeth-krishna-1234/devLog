class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        
        flights = [0] * n
        for start , end , seats in bookings:
            flights[start-1] =flights[start-1]+ seats
            if end<n:
                flights[end] = flights[end] - seats
        for index in range(1,n):
            flights[index]=flights[index]+flights[index-1]
        return flights