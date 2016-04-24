def patternCount(pattern, text):
    count = 0

    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            count += 1

    return count
