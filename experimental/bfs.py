from collections import deque

def bfs_paths(graph, start, end, max_depth):
    queue = deque([(start, [start], None, 0)])  # (現在のノード, パス, 直前のノード, 深さ)
    while queue:
        (vertex, path, prev, depth) = queue.popleft()
        
        # 最大深さを超えていたら探索を止める
        if depth > max_depth:
            continue
        
        # 現在のノードから進める全てのノードに対してループ
        for next in graph[vertex]:
            # 直前のノードには戻らない
            if next != prev:
                if next == end:
                    # エンドに到達したパスと深さを返す
                    yield path + [next], depth + 1
                    # 次のノードへ進む。直前のノードを更新する
                    queue.append((next, path + [next], vertex, depth + 1))
                else:
                    # 次のノードへ進む。直前のノードを更新する
                    queue.append((next, path + [next], vertex, depth + 1))

# グラフの定義（隣接リスト）
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

max_depth = 20
paths = list(bfs_paths(graph, 'n1', 'n2', max_depth))
for path, depth in paths:
    print(f"Path: {' -> '.join(path)}, Depth: {depth}")