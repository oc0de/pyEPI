import collections

MatchResult = collections.namedtuple('MatchResult', ('winning_team', 'losing_team'))
def check_dfs(matches, team_a, team_b):
    def build_graph():
        graph = collections.defaultdict(set)
        for match in matches:
            graph[match.winning_team].add(match.losing_team)

        return graph

    def is_reachable_dfs(graph, curr, dest, visited=set()):
        if curr == dest: return True
        if curr in visited or curr not in graph: return False
        visited.add(curr)

        return any(is_reachable_dfs(graph, team, dest)
                    for team in graph[curr])

    return is_reachable_dfs(build_graph(), team_a, team_b)

def check_bfs(matches, team_a, team_b):
    def build_graph():
        graph = collections.defaultdict(set)
        for match in matches:
            graph[match.winning_team].add(match.losing_team)
        return graph

    def is_reachable_bfs(graph, curr, dest):
        visited, q = set(), [curr]
        visited.add(curr)
        while q:
            just_reached = q.pop(0)
            if just_reached == dest: return True
            if just_reached in graph:
                for team in graph[just_reached]:
                    if team not in visited:
                        q += team,
                        visited.add(team)
        return False

    return is_reachable_bfs(build_graph(), team_a, team_b)






matches = [
    MatchResult('Texas', 'Cal'), MatchResult('Cal', 'Stanford'),
    MatchResult('Stanford', 'Texas'), MatchResult('Stanford', 'MIT'),
    MatchResult('Stanford', 'CIT'), MatchResult('UCLA', 'USC')
]
assert check_dfs(matches, 'Texas', 'MIT') == True
assert check_dfs(matches, 'Cal', 'UCLA') == False

assert check_bfs(matches, 'Texas', 'MIT') == True
assert check_bfs(matches, 'Cal', 'UCLA') == False
