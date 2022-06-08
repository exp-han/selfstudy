// 1st Approach - Naive
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        int size = nums.size();
        for (int i = 0; i < size; i++) {
            int remainder = target - nums[i];
            for (int j = i+1; j < size; j++) {
                if (remainder == nums[j]) {
                    result.push_back(i);
                    result.push_back(j);
                    break;
                }
            }
            if (result.size() == 2) {
                break;
            }
        }
        return result;
    }
};

// 2nd Approach - Using unordered map
// unordered map 공부하고 다시 볼 것