class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> temp;
        for(const auto&i : strs){
            string sortedI = i;
            sort(sortedI.begin(), sortedI.end());
            temp[sortedI].push_back(i);
        }

        vector<vector<string>> res;
        for(auto i : temp){
            res.push_back(i.second);
        }

        return res;
    }
};
