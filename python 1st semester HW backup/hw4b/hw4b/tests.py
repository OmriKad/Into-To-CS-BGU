from hw4b import *

print('---  1.1 subset_sum_count ---')
print(subset_sum_count([7, 6, 18, 20], 14))
print(subset_sum_count([7, 6, 1, 20], 14))
print(subset_sum_count([7, 6, 20, 1, 13, 1], 14))


print('---  1.2 subset_sums ---')
print(subset_sums([7, 8, 7], 14))
print(subset_sums([7, 6, 5, 1, 14, 13], 14))
print(subset_sums([7, 8, 17], 14))


print('---  1.3 subset_sum_memo ---')
print(subset_sum_memo([7, 6, 18, 20], 14))
print(subset_sum_memo([7, 6, 5, 1, 14, 13], 14))
print(subset_sum_memo([1, 1, 1, 1, 1, 1, 1, 1, 1], 10))


print('---  1.4 subset_sum_with_repeats ---')
print(subset_sum_with_repeats([1, 3, 5], 5))
print(subset_sum_with_repeats ([1, 2, 3, 4, 5], 5))
print(subset_sum_with_repeats ([1, 2, 3], 4))


print('---  2.1 abc_words ---')
print(abc_words(1))
print(abc_words(3))


print('---  2.2 char_to_char_words ---')
print(char_to_char_words('A', 'B', 4))
print(char_to_char_words('D', 'F', 2))
print(char_to_char_words('Q', 'Q', 5))


print('---  3 solve_maze_monotonic ---')
print(solve_maze_monotonic([[1, 2, 3], [2, 0, 4], [3, 4, 5]]))
print(solve_maze_monotonic([[1, 2, 3], [2, 0, 5], [3, 4, 5]]))
print(solve_maze_monotonic([[1, 2, 3, 4, 5], [12, 11, 10, 4, 6], [13, 9, 9, 8, 7], [14, 9, 9, 8, 7], [15, 16, 17, 18, 19]]))
print(solve_maze_monotonic([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]))
print(solve_maze_monotonic([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 6]]))
print(solve_maze_monotonic([[19]]))
