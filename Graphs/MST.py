import cv2
import heapq
from Graphs.video import create_video
from Graphs.Draw_graph import draw
pq = []

final_tree = []
final_tree_dic = {}
tst_graph = {
    "s": [("c", 7), ("g", 2), ("b", 3)],
    "b": [("s", 3), ("g", 4)],
    "c": [("s", 7), ("g", 4), ("e", 5), ("d", 1)],
    "d": [("c", 1), ("g", 5), ("f", 8)],
    "e": [("c", 5), ("f", 7)],
    "f": [("e", 7), ("d", 8)],
    "g": [("b", 4), ("d", 5), ("c", 4), ("s", 2)],
}
visited = set()
for edge in tst_graph["s"]:
    heapq.heappush(pq, (edge[1], "s", edge[0]))
visited.add("s")
i = 1
while pq.__len__() > 0:
    weight, start, end = heapq.heappop(pq)
    if end in visited:
        continue
    draw(tst_graph, final_tree_dic, i)
    draw(final_tree_dic, {}, i * -1)
    final_tree.append([start, weight, end])
    if start not in final_tree_dic:
        final_tree_dic[start] = []
    final_tree_dic[start].append((end, weight))
    if end not in final_tree_dic:
        final_tree_dic[end] = []
    final_tree_dic[end].append((start, weight))
    visited.add(end)
    i += 1
    for edge in tst_graph[end]:
        if edge[0] not in visited:
            heapq.heappush(pq, (edge[1], end, edge[0]))

print(len(tst_graph), len(final_tree))
if len(tst_graph) != len(final_tree)+1:
    print("not connected tree")
    exit(1)
draw(tst_graph, final_tree_dic, i)
draw(final_tree_dic, {}, i*-1)
print(final_tree)
create_video(i)

vide = cv2.VideoCapture("final.avi")
_, frame = vide.read()
print("click 'c' to move to next state")
while _:
    cv2.imshow("frame", frame)
    _, frame = vide.read()
    if cv2.waitKey(0) & 0xFF == ord("c"):
        continue

