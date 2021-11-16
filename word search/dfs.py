"""
Problem: https://leetcode.com/problems/word-search/

"""


################################################################################
# DFS
def dfs(visited, word_path, i, j):
    if word_path == word:
        return True

    if len(word_path) > len(word):
        return False

    if i < 0:
        return False

    if i >= len(board):
        return False

    if j < 0:
        return False

    if j >= len(board[0]):
        return False

    if (i, j) not in visited:
        visited[(i, j)] = True
        word_path += board[i][j]
        if any([
            dfs(visited, word_path, i + 1, j),
            dfs(visited, word_path, i - 1, j),
            dfs(visited, word_path, i, j + 1),
            dfs(visited, word_path, i, j - 1)
        ]):
            return True
        else:
            del visited[(i, j)]
            return False

    else:
        return False


################################################################################
# Main
if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"

    # driver code
    for i in range(len(board)):  # rows
        for j in range(len(board[0])):  # columns
            visited = {}
            word_path = ""
            current_row = i
            current_column = j

            if dfs(visited, word_path, current_row, current_column):
                print(True)

    print(False)
