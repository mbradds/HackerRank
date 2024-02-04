#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    highest = 0
    for w in word:
        location = h[ord(w.upper()) - ord('A')]
        if location > highest:
            highest = location
    return highest*len(word)

if __name__ == '__main__':
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    word = "zabc"
    result = designerPdfViewer(h, word)
