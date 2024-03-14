from collections import deque

def bfs_reachability(graph, start, end, max_depth):
    # 到達可能な深さを記録するセット
    reachable_depths = set()
    # (ノード, 現在の深さ)
    queue = deque([(start, 0)])
    
    while queue:
        vertex, depth = queue.popleft()
        
        # 次の深さが最大深さを超えていたらスキップ
        if depth > max_depth:
            continue
        
        # 目的地に到達したら、その深さを記録
        if vertex == end:
            reachable_depths.add(depth)
        
        # 隣接ノードをキューに追加
        for next_vertex in graph[vertex]:
            if depth + 1 <= max_depth:
                queue.append((next_vertex, depth + 1))
    
    return reachable_depths

# グラフの定義と探索の実行
graph = {
    'n1': ['n7','n2','n6'],
    'n2': ['n8','n1'],
    'n3': ['n9','n4','n24'],
    'n4': ['n3','n5','n25'],
    'n5': ['n4','n6','n26'],
    'n6': ['n5','n12','n27','n1'],
    'n7': ['n1','n8','n12'],
    'n8': ['n2','n13','n7'],
    'n9': ['n3','n14','n10'],
    'n10': ['n9','n11'],
    'n11': ['n15','n10','n12'],
    'n12': ['n6','n11','n7'],
    'n13': ['n8','n17','n14','n16'],
    'n14': ['n9','n13'],
    'n15': ['n11','n19','n16'],
    'n16': ['n15','n13'],
    'n17': ['n13','n20'],
    'n18': ['n22','n19'],
    'n19': ['n15','n18'],
    'n20': ['n17','n24','n21','n23'],
    'n21': ['n20','n22'],
    'n22': ['n18','n21','n23'],
    'n23': ['n27','n22','n20'],
    'n24': ['n20','n25','n3','n27'],
    'n25': ['n24','n26','n4'],
    'n26': ['n25','n27','n5'],
    'n27': ['n23','n26','n6','n24'],
}
start = 'n1'
end = 'n2'
max_depth = 48

reachable_depths = bfs_reachability(graph, start, end, max_depth)
print(f"Reachable depths: {sorted(list(reachable_depths))}")