#include <iostream>
#include <vector>  // Include vector from the standard library

class Solution {
public:
    int singleNumber(std::vector<int>& nums) {  // Use std::vector here
        int result = 0;
        for(int val : nums) {
            result ^= val;  // XOR each value
        }
        return result;
    }
};

int main() {
    Solution solution;
    std::vector<int> nums = {4, 1, 2, 1, 2};  // Example input
    std::cout << solution.singleNumber(nums) << std::endl;  // Expected output: 4
    return 0;
}
