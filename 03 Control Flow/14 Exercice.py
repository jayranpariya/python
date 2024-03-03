# 11 Exercice

# Display the even number ( 2 4 6 8) followed by this message "We have 4 even numbers"
# 2
# 4
# 6
# 8
# We have 4 even numbers

# Mosh anwser
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count = count + 1
        print(number)
print(f"we have {count} even number")


# In my anwser I did not count the numbers
