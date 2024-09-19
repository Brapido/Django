# ===============================================================
# Dictionary stores key-value pair (entries/entry)
# change check sent back
def dictionary():
    user_dictionary = {
        "danp": "Dan Pickles",
        "howiej": "Howard Jonhnson"
    }

    username = input("Add a Username: ")
    name = input("What is the user's full name? ")

    user_dictionary[username] = name
    print(user_dictionary[username])

    search = input("Search by username: ")
    # .get(first parameter if found prints value from dictionary,
    # second parameter prints if variable not found in
    # dictionary
    print(user_dictionary.get(search, "Value not found"))


def scramble(r, s):
    if len(r) == 0:
        # base case all letters are used
        print(s)
    else:
        # Recursive case: For each call to scramble()
        # move a letter from remaining to scrambled
        for i in range(len(r)):
            # the letter at index i will be scrambled
            scramble_letter = r[i]
            # scrambles remaining letters  *figure out what :     : is doing later
            remaining_letter = r[:i] + r[i + 1:]
            # recursive call to scramble letters
            scramble(remaining_letter, s + scramble_letter)


def fib(v1, v2, run_cnt):
    print(v1, '+', v2, '=', v1 + v2)

    if run_cnt <= 1:
        pass
    else:
        fib(v2, v1 + v2, run_cnt - 1)
