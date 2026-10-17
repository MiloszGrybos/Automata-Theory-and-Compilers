import sys


def prefix_fun(pattern: str) -> list[int]:
    m = len(pattern)
    pi = [0] * m
    k = 0

    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]

        if pattern[k] == pattern[q]:
            k += 1

        pi[q] = k

    return pi


def kmp(text: str, pattern: str) -> list[int]:
    n = len(text)
    m = len(pattern)

    if m == 0 or n < m:
        return []

    pi = prefix_fun(pattern)
    matches = []
    q = 0

    for i in range(n):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]

        if pattern[q] == text[i]:
            q += 1

        if q == m:
            shift = i - m + 1
            matches.append(shift)
            q = pi[q - 1]

    return matches


def main():
    if len(sys.argv) != 3:
        print(f"Użycie: python {sys.argv[0]} <wzorzec> <nazwa pliku>")
        sys.exit(1)

    pattern = sys.argv[1]
    filename = sys.argv[2]

    try:
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Błąd: Nie znaleziono pliku '{filename}'.")
        sys.exit(1)

    shifts = kmp(text, pattern)

    if shifts:
        print(
            f"Znaleziono {len(shifts)} wystąpień wzorca na pozycjach (indeksowane od 0):"
        )
        for s in shifts:
            print(f"- przesunięcie: {s}")
    else:
        print("Nie znaleziono wystąpień wzorca.")


if __name__ == "__main__":
    main()