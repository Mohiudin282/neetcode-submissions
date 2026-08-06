class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        //first of all we need to count the frequency of each element in the array
        unordered_map<int, int> count;
        for (auto i : nums){
            count[i]++;
        }
        vector<pair<int, int>> temp;
        for(auto i : count){
            temp.push_back({i.second, i.first});
        }
        sort(temp.rbegin(), temp.rend());
        vector<int> res;
        for(int i = 0; i < k; i++){
            res.push_back(temp[i].second);
        }
        return res;
    }
};
