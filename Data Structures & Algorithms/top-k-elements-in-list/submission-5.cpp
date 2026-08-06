class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count;
        for (int num : nums) {
            count[num]++;
        }
        vector<pair<int, int>> tmp;
        for(auto& s : count){
            tmp.push_back({s.second, s.first});
        }
        sort(tmp.rbegin(), tmp.rend());

        vector<int> res;
        for(int i = 0; i < k; ++i){
            res.push_back(tmp[i].second);
        }
        return res;
    }
};