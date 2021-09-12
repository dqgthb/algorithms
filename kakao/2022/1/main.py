def solution(id_list, report, k):

    N = len(id_list)
    str2id = {name:id_ for id_, name in enumerate(id_list)}
    reporters = [set() for _ in range(N)]
    mails = [0] * N

    for line in report:
        from_, to = line.split()
        from_ = str2id[from_]
        to = str2id[to]
        reporters[to].add(from_)

    for arr in reporters:
        if len(arr) >= k:
            for user in arr:
                mails[user] += 1

    return mails












def main():
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2
    ans = solution(id_list, report, k)
    print(ans)

    id_list = ["con", "ryan"]
    report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 3
    ans = solution(id_list, report, k)
    print(ans)


if __name__ == "__main__":
    main()