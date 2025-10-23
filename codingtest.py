#1. 두 수의 합
def twoSum(nums, target):
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_map:
            return [num_map[complement], i]
        
        num_map[num] = i
        
    return []
#2. 팰린드롬 확인
import re

def isPalindrome(s):
    s_filtered = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return s_filtered == s_filtered[::-1]

#3. K번째로 큰 요소
import heapq

def findKthLargest(nums, k):
    min_heap = []
    
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    return min_heap[0]

#4. 이진 탐색
def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

#5. 피보나치 수열
def fib(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[n]

#6. 회의실 배정

def max_meetings(meetings):
    meetings.sort(key=lambda x: x[1])
    
    count = 0
    last_end_time = -1
    
    for start, end in meetings:
        if start >= last_end_time:
            count += 1
            last_end_time = end
            
    return count

from collections import Counter
import re

#7. 가장 흔한 단어
def most_frequent_word(text):
    text = re.sub(r'[^a-zA-Z\s]', ' ', text).lower()
    words = [word for word in text.split() if word]
    
    word_counts = Counter(words)
    
    if not word_counts:
        return None
    
    return word_counts.most_common(1)[0][0]


from collections import deque

#8. 미로 탈출
def solve_maze(maze):
    N = len(maze)
    M = len(maze[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    queue = deque([(0, 0, 1)])
    maze[0][0] = 0
    
    while queue:
        x, y, dist = queue.popleft()
        
        if x == N - 1 and y == M - 1:
            return dist
            
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = 0
                queue.append((nx, ny, dist + 1))
                
    return -1

#9. 모든 부분집합
def subsets(nums):
    result = []
    
    def dfs(index, path):
        result.append(path[:])
        
        for i in range(index, len(nums)):
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
            
    dfs(0, [])
    return result

#10. 괄호 유효성 검사
def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            
            if top_element != mapping[char]:
                return False
        else:
            stack.append(char)
            
    return not stack

# 11. 리스트 중복 제거
def remove_duplicates(nums):
    return list(set(nums))

# 12. 두 정렬 리스트 병합
def merge_sorted_lists(list1, list2):
    merged = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

# 13. 아나그램 확인
from collections import Counter

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)

# 14. 문자열 뒤집기 (in-place)
def reverseString(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s

# 15. 최대 부분 배열 합 (카데인 알고리즘)
def maxSubArray(nums):
    current_max = nums[0]
    global_max = nums[0]
    
    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        global_max = max(global_max, current_max)
        
    return global_max

# 16. 유니크 경로 수 (DP)
def uniquePaths(m, n):
    dp = [[0] * n for _ in range(m)]
    
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1
        
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    return dp[m-1][n-1]

# 17. 큐를 이용한 스택 구현
from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q

# 18. 단일 연결 리스트 역순 출력
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# 19. 비트 조작: 1의 개수 세기
def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i & (i - 1)] + 1
    return ans

# 20. 최소 신장 트리 가중치 (크루스칼 알고리즘 뼈대)
def find_mst_weight(n, edges):
    
    def find(parent, i):
        if parent[i] == i:
            return i
        parent[i] = find(parent, parent[i])
        return parent[i]

    def union(parent, rank, x, y):
        rootx = find(parent, x)
        rooty = find(parent, y)
        if rootx != rooty:
            if rank[rootx] < rank[rooty]:
                parent[rootx] = rooty
            elif rank[rootx] > rank[rooty]:
                parent[rooty] = rootx
            else:
                parent[rooty] = rootx
                rank[rootx] += 1
            return True
        return False

    edges.sort(key=lambda item: item[2])
    
    parent = list(range(n))
    rank = [0] * n
    mst_weight = 0
    num_edges = 0
    
    for u, v, weight in edges:
        if union(parent, rank, u, v):
            mst_weight += weight
            num_edges += 1
            if num_edges == n - 1:
                break
                
    return mst_weight if num_edges == n - 1 else -1

# 21. 배열 회전
def rotate(nums, k):
    n = len(nums)
    k = k % n
    
    def reverse(arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
            
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    return nums

# 22. 가장 긴 공통 접두사
def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    for i in range(1, len(strs)):
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# 23. 하나만 있는 숫자 (XOR 활용)
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# 24. 없는 숫자 (가우스 공식 활용)
def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# 25. 집털이 (DP)
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
        
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
    return dp[-1]

# 26. 조합 합 (백트래킹)
def combinationSum(candidates, target):
    result = []
    
    def backtrack(remain, combo, start):
        if remain == 0:
            result.append(list(combo))
            return
        if remain < 0:
            return
            
        for i in range(start, len(candidates)):
            combo.append(candidates[i])
            backtrack(remain - candidates[i], combo, i)
            combo.pop()
            
    backtrack(target, [], 0)
    return result

# 27. 섬의 개수 (DFS)
def numIslands(grid):
    if not grid:
        return 0
        
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        
        grid[r][c] = '0'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
        
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                count += 1
                dfs(r, c)
                
    return count

# 28. 유효한 스도쿠 (Hash Set 활용)
def isValidSudoku(board):
    n = 9
    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    boxes = [set() for _ in range(n)]
    
    for r in range(n):
        for c in range(n):
            val = board[r][c]
            if val == '.':
                continue
            
            box_index = (r // 3) * 3 + (c // 3)
            
            if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                return False
            
            rows[r].add(val)
            cols[c].add(val)
            boxes[box_index].add(val)
            
    return True

# 29. 세 수의 합 (투 포인터)
def threeSum(nums):
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
            
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
                
    return result

# 30. 최소 크기 부분 배열 합 (슬라이딩 윈도우)
def minSubArrayLen(target, nums):
    n = len(nums)
    min_len = float('inf')
    window_sum = 0
    left = 0
    
    for right in range(n):
        window_sum += nums[right]
        
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)
            window_sum -= nums[left]
            left += 1
            
    return min_len if min_len != float('inf') else 0

# 31. 스택을 이용한 큐 구현
class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self._transfer()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._transfer()
        return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out

    def _transfer(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

# 32. 이진 트리 최대 깊이 (DFS 재귀)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if root is None:
        return 0
    
    return 1 + max(maxDepth(root.left), maxDepth(root.right))

# 33. 대칭 이진 트리 확인
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def isSymmetric(root: TreeNode) -> bool:
    if root is None:
        return True
    
    def is_mirror(t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        
        return (t1.val == t2.val and 
                is_mirror(t1.right, t2.left) and 
                is_mirror(t1.left, t2.right))
                
    return is_mirror(root.left, root.right)

# 34. 주식 거래 최적 시점 (그리디)
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    return max_profit
