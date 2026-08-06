class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int res = 0;
        unordered_set<int> store(nums.begin(), nums.end());
        for(int i : nums){
            int curr = i; int streak = 0;
            while(store.find(curr) != store.end()){
                streak++;
                curr++;
            }
            res = max(res, streak);
        }
        return res;
    }
};
