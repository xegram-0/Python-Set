# Exercise 2: Return a new set of identical items from two sets
# Given:

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# Expected output:

# {40, 50, 30}



def main():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set3 = set1.intersection(set2)
    print(set3)
if __name__=="__main__":
    main()