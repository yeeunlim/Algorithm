class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix or not matrix[0]:
            return []
        
        result = []
        
        # 4개의 경계면 초기화
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # 왼쪽 -> 오른쪽 이동
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1  # 윗행 탐색 완료로 경계 축소
            
            # 위 -> 아래 이동
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1  # 우측열 탐색 완료로 경계 축소
            
            # 오른쪽 -> 왼쪽 이동 (남은 행이 있는지 확인)
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1  # 아랫행 탐색 완료로 경계 축소
                
            # 아래 -> 위 이동 (남은 열이 있는지 확인)
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1  # 좌측열 탐색 완료로 경계 축소
                
        return result