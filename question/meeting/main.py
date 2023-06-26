def main() -> None:
    global cnt, MEETING_TIME, line, speechLogs, P
    cnt = 0

    N = 4
    line = "ABCD"

    MEETING_TIME = 5
    P = {e: i for i, e in enumerate(line)}

    speechLogs = [-4 for _ in range(N)]

    line = "ABC??"

    print("A   B   C   D")

    dfs(0)
    print(cnt)


def dfs(time):
    global cnt
    if time == MEETING_TIME:
        cnt += 1
        return

    if line[time] == "?":
        for i, speechTime in enumerate(speechLogs):
            if speechTime + 3 < time:
                speechLogs[i] = time
                print(speechLogs)
                dfs(time + 1)
                speechLogs[i] = speechTime
    else:
        origTime = speechLogs[P[line[time]]]
        speechLogs[P[line[time]]] = time
        print(speechLogs)
        dfs(time + 1)
        speechLogs[P[line[time]]] = origTime


if __name__ == "__main__":
    main()
