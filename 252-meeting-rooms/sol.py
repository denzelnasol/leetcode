# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
# determine if a person could attend all meetings.

# Example 1:
# Input: [[0,30],[5,10],[15,20]]
# Output: false

# Example 2:
# Input: [[7,10],[2,4]]
# Output: true

from typing import List


class MeetingRoom:
    def CanAttendAllMeetings(self, meetings: List[List[int]]) -> bool:
        meetings.sort(key=lambda i: i[0])
        
        for i, meeting in enumerate(meetings):
            if i == 0:
                continue
            
            prevMeeting = meetings[i-1]
            if meeting[0] < prevMeeting[1]:
                return False
            
        return True


meetingRoomTest = MeetingRoom()

test1 = [[0,30],[5,10],[15,20]]
print(meetingRoomTest.CanAttendAllMeetings(test1))

test2 = [[7,10],[2,4]]
print(meetingRoomTest.CanAttendAllMeetings(test2))