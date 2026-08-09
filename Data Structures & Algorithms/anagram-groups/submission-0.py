class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            result = [strs]
        
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1

            result[tuple(count)].append(word)
        
        return list(result.values())
            


        # import string
        # letters = string.ascii_lowercase

        # word_dict = {}
        # for word in strs:
        #     letter_count = 
        #     for ch in word:



        # for i in range(len(strs)):
        #     sub_result = [strs[i]]
        #     separated_word = []
        #     for ch in strs[i]:
        #         separated_word.append(ch)
        #         sorted(separated_word)
        #     for j in range(i + 1, len(strs)):
        #         if len(strs[j]) == len(strs[i]):
        #             potential_word = []
        #             for ch in strs[j]:
        #                 potential_word.append(ch)
        #                 if sorted(potential_word) == separated_word:
        #                   sub_result.append(strs[j])  
        #     result.append(sub_result)

        # return result              
                        
        #     current_list = []
        #     current_word = sorted(strs[i].split)
        #     current_list.append(strs[i])
        # # sorted modifies OG list, .sort does not modify list
        #     for j in range(i + 1, len(strs)):
        #         if sorted(strs[j].split) == current_word:
        #             current_list.append(strs[j])







            
        