#include <iostream>
#include <vector>  // Include the vector header for using std::vector

class Solution {
public:
    int majorityElement(std::vector<int>& nums) {
        // Moore's Voting Algorithm

        int n = nums.size();
        int freq = 0, ans = 0;

        for (int i = 0; i < n; i++) {
            // If freq is zero, we choose the current element as a potential candidate
            if (freq == 0) {
                ans = nums[i];
            }

            // Increase or decrease the frequency of the candidate element
            if (nums[i] == ans) {
                freq++;
            } else {
                freq--;
            }
        }

        return ans;
    }
};

int main() {
    // Test case
    Solution solution;
    std::vector<int> nums = {3, 2, 3}; // Example input
    std::cout << "Majority Element: " << solution.majorityElement(nums) << std::endl;
    return 0;
}
