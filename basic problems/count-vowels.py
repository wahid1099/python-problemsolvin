def count_vowels(sentences):
    count=0
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for chr in sentences:
        if chr in vowels:
            count+=1
    return count

print(count_vowels("Hello world"))