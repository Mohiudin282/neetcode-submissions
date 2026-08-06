class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res;
        for(int i = 0; i < nums.size(); i++){
            int j = 0; int k = 1;
            while(j < nums.size()){
                if(j != i){
                    k *= nums[j];
                    j++;
                }
                else{
                    j++;
                }
            }
            res.push_back(k);
        }
        return res;
    }
};
