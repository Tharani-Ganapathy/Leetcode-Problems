class Solution:
    def singleNumber(self, nums: List[int]) -> int:
#         dup_dict = {}
#         for i in nums:
#             if i in dup_dict:
#                 dup_dict[i] = False
#             else:
#                 dup_dict[i] = True
                
#         for k,v in dup_dict.items():
#             if v:
#                 return k
        res = 0
        for num in nums:
            res ^= num
            print("******",res)
        return res
