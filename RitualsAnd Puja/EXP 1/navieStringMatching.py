def naive_string_matching(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i)

    return occurrences

def main():
    text = "AABAACAADAABAAABAA"
    pattern = "AABA"
    occurrences = naive_string_matching(text, pattern)
    if occurrences:
        print("Pattern found at positions:", occurrences)
    else:
        print("Pattern not found in the text.")

if __name__ == "__main__":
    main()
