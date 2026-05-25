class Node:
    """이중 연결 리스트의 노드를 정의하는 클래스"""
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """LRU 캐시를 관리하는 메인 클래스"""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node 매핑을 위한 딕셔너리
        
        # 더미(Dummy) Head와 Tail 노드 생성
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # --- Helper Methods (내부 구현용 캡슐화) ---
    def _add_node(self, node: Node) -> None:
        """항상 head 바로 뒤에 노드를 추가 (가장 최근 사용됨)"""
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node) -> None:
        """이중 연결 리스트에서 특정 노드를 제거"""
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node: Node) -> None:
        """기존 노드를 가장 최근 사용 상태로 갱신"""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> Node:
        """가장 오래된 노드(tail 바로 앞)를 제거하고 반환"""
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        return lru_node

    # --- Public API ---
    def get(self, key: int) -> int:
        """데이터를 조회하는 API"""
        node = self.cache.get(key)
        if not node:
            return -1
        
        # 조회된 데이터는 가장 최근에 사용된 것이므로 맨 앞으로 이동
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """데이터를 저장하는 API"""
        node = self.cache.get(key)
        
        if node:
            # 이미 존재하는 키라면 값을 업데이트하고 맨 앞으로 이동
            node.value = value
            self._move_to_head(node)
        else:
            # 새로운 키인 경우 새 노드 생성
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            
            # 용량을 초과한 경우 LRU 처리
            if len(self.cache) > self.capacity:
                lru_node = self._pop_tail()
                del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)