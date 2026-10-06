#[start:stop:step]
#Sentence = abcdefghj

# p[::-2] → scrolls backwards jumping from 2 to 2: "jhfdb" (will take de char 9,7,5,3,1)
# [:5] → get the first 5 (there are already only 5): "jhfdb"
# [::-1] → invert: "bdfhj"
# [3:] → from index 3 to the end: "hj"