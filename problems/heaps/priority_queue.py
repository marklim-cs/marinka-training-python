'''
implement a priority queue using binary search heap
find parent node = (i-1)//2 
where i is current node
find non_leaf node = n//2 - 1
where n = len(arr)
'''
from typing import Any
import copy

class PriorityQueue:
    def __init__(self):
        self._heap = []

    def push(self, priority: int, value: Any):
        data = (priority, value)
        self._heap.append(data)

        self._heapify_up(len(self._heap)-1)

    def _heapify_up(self, i):
        if i == 0:
            return
        inserted_node_indx = i
        parent_node_indx = (i - 1) // 2

        if self._heap[inserted_node_indx][0] < self._heap[parent_node_indx][0]:
            self._heap[inserted_node_indx], self._heap[parent_node_indx] = self._heap[parent_node_indx], self._heap[inserted_node_indx]
            self._heapify_up(parent_node_indx)
        return

    def pop(self) -> Any:
        if not self._heap:
            return None

        root_result = self._heap[0]
        last_element_index = len(self._heap)-1
        self._heap[0] = self._heap[last_element_index]
        self._heapify_down(self._heap, 0)

        return root_result



    def _heapify_down(self, arr: list, i: int):
        if i > len(arr)-1:
            return
        current_element = i
        smallest = i

        left_child_index = 2 * i + 1
        right_child_index = 2 * i + 2

        if left_child_index < len(arr) and self._heap[left_child_index][0] < self._heap[smallest][0]:
            smallest = left_child_index
        if right_child_index < len(arr) and self._heap[right_child_index][0] < self._heap[smallest][0]:
            smallest = right_child_index

        if smallest != current_element:
            self._heap[smallest], self._heap[current_element] = self._heap[current_element], self._heap[smallest]
            self._heapify_down(arr, smallest)
        return

    def show(self):
        deep_copy_heap = copy.deepcopy(self._heap)
        return deep_copy_heap