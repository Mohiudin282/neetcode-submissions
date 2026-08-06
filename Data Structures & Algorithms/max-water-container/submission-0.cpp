class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;
        int maxWater = 0;
        int width, height, currWater;
        while(l < r){
            width = r - l;
            height = min(heights[l], (heights[r]));
            currWater = height * width;
            maxWater = max(currWater, maxWater);
            // now only move pointers according to size of the slit
            if(heights[l] < heights[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return maxWater;
    }
};
