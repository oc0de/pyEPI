def search_postings_list(L):
    if not L: return
    s, order = [L], 0
    while s:
        curr = s.pop()
        if curr and curr.order == -1:
            curr.order = order
            order += 1
            s += [curr.next, curr.jump]


def search_postings_list_recursive(L):
    def search_postings_list_helper(curr):
        if not curr: return
        if curr and curr.order == -1:
            curr.order = order
            order += 1
            search_postings_list_helper(curr.jump)
            search_postings_list_helper(curr.next)

    order = 0
    return search_postings_list_helper(L)
