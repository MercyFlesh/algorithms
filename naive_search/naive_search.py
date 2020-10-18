def naive_search(text, pattern):
    length_text = len(text)
    length_pattern = len(pattern)
    result = list()
    
    for i in range(length_text - length_pattern + 1):
        if text[i:i+length_pattern] == pattern:
            result.append(i)

    return result


if __name__ == "__main__":
    text = "abcdabcjabc"
    pattern = "abc"
    print(naive_search(text, pattern))
