# Exercise 8: Update set1 by adding items from set2, except common items
# Given:

# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# Expected output:

# {70, 10, 20, 60}

def main():
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set1.symmetric_difference_update(set2)
    print(set1)
if __name__=="__main__":
    main()