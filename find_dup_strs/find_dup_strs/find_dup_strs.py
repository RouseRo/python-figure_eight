def find_duplicate_positions(strings):
    duplicates = {}
    for index, string in enumerate(strings):
        if string in duplicates:
            duplicates[string].append(index)
        else:
            duplicates[string] = [index]

    result = []
    for string, positions in duplicates.items():
        if len(positions) > 1:
            result.append([string] + positions)

    return result


def main():
    # Example usage
    strings = ["DUP01", "abcd2", "DUP01", "ABCD4", "ABCD5", "DUP01"]
    print("input:", strings)
    expected = find_duplicate_positions(strings)
    print("expected:", expected)
    # Expected output: [['DUP01', 0, 2, 5]]

if __name__ == "__main__":
    main()
