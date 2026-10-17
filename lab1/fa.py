import sys


def transition_fun(pattern: str, alphabet: set) -> list[dict[str, int]]:
    m = len(pattern)
    delta = [{} for _ in range(m + 1)]

    for q in range(m + 1):
        for a in alphabet:
            k = min(m, q + 1)
            candidate = pattern[:q] + a

            while k > 0 and not candidate.endswith(pattern[:k]):
                k -= 1

            delta[q][a] = k

    return delta


def fa(text: str, pattern: str) -> list[int]:
    n = len(text)
    m = len(pattern)

    if m == 0 or n < m:
        return []

    alphabet = set(text).union(set(pattern))
    delta = transition_fun(pattern, alphabet)

    matches = []
    q = 0

    for i in range(n):
        q = delta[q].get(text[i], 0)
        if q == m:
            shift = i - m + 1
            matches.append(shift)

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

    shifts = fa(text, pattern)

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