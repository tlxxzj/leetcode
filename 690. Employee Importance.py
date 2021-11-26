"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        em = {}
        for employee in employees:
            em[employee.id] = employee
        ret = 0
        q = [id]
        while len(q) > 0:
            employee = em[q.pop()]
            ret += employee.importance
            q += employee.subordinates
        return ret