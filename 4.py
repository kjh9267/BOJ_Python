def solution(needs, robot_count):
    result = [0]
    component_count = len(needs[0])
    picked_robots = [False for _ in range(component_count)]

    if robot_count > component_count:
        return len(needs)

    dfs(0, 0, needs, robot_count, component_count, picked_robots, result)

    return result[0]


def dfs(cur, depth, needs, robot_count, component_count, picked_robots, result):
    if depth == robot_count:
        can_make_count = check_can_make_count(needs, picked_robots)
        result[0] = max(result[0], can_make_count)
        return

    for index in range(cur, component_count):
        picked_robots[index] = True
        dfs(index + 1, depth + 1, needs, robot_count, component_count, picked_robots, result)
        picked_robots[index] = False


def check_can_make_count(needs, picked_robots):
    count = 0

    for need in needs:
        if can_make(need, picked_robots):
            count += 1

    return count


def can_make(need, picked_robots):
    not_need = 0

    for component, is_need in enumerate(need):
        if is_need == not_need:
            continue
        if not picked_robots[component]:
            return False

    return True


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    print(solution([ [ 1, 0, 0 ], [1, 1, 0], [1, 1, 0], [1, 0, 1], [1, 1, 0], [0, 1, 1] ]	, 2))
    print(solution([[1]], 12))
    print(solution([[1]], 2))
    print(solution([[1]], 1))