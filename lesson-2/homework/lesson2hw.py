date_birth=int(input())
current_year=int(input())
age=current_year-date_birth
print(age);

txt="LMaasleitbtui"
print(txt[::2]);

txt='MsaatmiazD'
print(txt[::2]);

txt="I'am John. I am from London"
print(txt.split()[5]);

txt='California'
print(txt[::-1]);

txt='California'
print(len(txt));

numbers = list(map(int, input().split()))
print(max(numbers));

def is_palindrome(word):
    
    word = word.lower()
   
    return word == word[::-1]


word = input("Enter a word: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.");

import re

def extract_domain(email):
    
    match = re.search(r'@([a-zA-Z0-9.-]+)', email)
    if match:
        return match.group(1)
    else:
        return None


email = input("Enter your email address: ")
domain = extract_domain(email)
if domain:
    print(f"The domain of the email is: {domain}")
else:
    print("Invalid email address.");

import random
import string

def generate_password(length=12):
    
    char_set = string.ascii_letters + string.digits + string.punctuation
    
   
    password = ''.join(random.choices(char_set, k=length))
    return password


password = generate_password(16)
print("Generated Password:", password);
      
