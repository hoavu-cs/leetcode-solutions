class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        number_char_table = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], \
                        '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], \
                        '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return [char for char in number_char_table[digits[0]]]

        recursive_res = self.letterCombinations(digits[1:])
        return [char + s for char in number_char_table[digits[0]] for s in recursive_res]
        

        