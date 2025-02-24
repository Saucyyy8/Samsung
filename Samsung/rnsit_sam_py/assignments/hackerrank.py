def arrangeStudents(n, boys, girls):
    # Write your code here
    assert 1 <= n <= 100
    assert len(boys) == n and len(girls) == n
    assert all(1 <= i <= 100 for i in boys + girls)

    boys.sort()
    girls.sort()

    ans = []
    for i, j in zip(boys, girls):
        ans.append(i)
        ans.append(j)

    if (ans == sorted(ans)):
        return "YES"

    ans = []
    for i, j in zip(girls, boys):
        ans.append(i)
        ans.append(j)

    if (ans == sorted(ans)):
        return "YES"

    return "NO"