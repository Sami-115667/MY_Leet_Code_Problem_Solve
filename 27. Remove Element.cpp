class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
            int c=nums.size();
      
        int count=0;
        for(int i=0;i<c;i++){
            if(val!=nums[i]){
               
                nums[count]=nums[i];
                count++;
            }
        }


        return count;


        
    }
    
};