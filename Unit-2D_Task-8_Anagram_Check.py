# Check whether two strings are anagrams

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Remove spaces and convert to lowercase, then sort
s1 = sorted(str1.replace(" ", "").lower())
s2 = sorted(str2.replace(" ", "").lower())

print("First string:", str1)
print("Second string:", str2)

if s1 == s2:
    print(f"'{str1}' and '{str2}' are Anagrams")
else:
    print(f"'{str1}' and '{str2}' are NOT Anagrams")
  Enter first string: listen
Enter second string: silent
First string: listen
Second string: silent
'listen' and 'silent' are Anagrams
Enter first string: hello
Enter second string: world
First string: hello
Second string: world
'hello' and 'world' are NOT Anagrams
