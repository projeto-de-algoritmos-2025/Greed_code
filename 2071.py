from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self, tasks: list[int], workers: list[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        
        def check(k: int) -> bool:
            tarefas = tasks[:k]
            trabalhadores = SortedList(workers[-k:])
            p = pills

            for i in range(k - 1, -1, -1):
                dificuldade = tarefas[i]
                if trabalhadores and trabalhadores[-1] >= dificuldade:
                    trabalhadores.pop()
                else:
                    if p == 0:
                        return False
                    idx = trabalhadores.bisect_left(dificuldade - strength)
                    if idx == len(trabalhadores):
                        return False
                    trabalhadores.pop(idx)
                    p -= 1
            return True

        low, high = 0, min(len(tasks), len(workers))
        resposta = 0

        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                resposta = mid
                low = mid + 1
            else:
                high = mid - 1

        return resposta
