import heapq

def cables_join(cables):
    heap = cables.copy()
    heapq.heapify(heap)
    connection_costs = 0

    while len(heap) > 1:

        first_elem = heapq.heappop(heap)
        second_elem = heapq.heappop(heap)
        new_elem = first_elem + second_elem
        connection_costs += new_elem
        print(f"Взято кабелі: {first_elem} + {second_elem}. Новий кабель: {new_elem}")
        heapq.heappush(heap, new_elem)

    print(f"Витрати на зʼєднання були {connection_costs}")

lines = [6, 12, 3, 4, 15, 7, 2]

cables_join(lines)
print(f"Значення суми масиву для перевірки: {sum(lines)}")