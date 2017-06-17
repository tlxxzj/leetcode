bool canPartition(int* nums, int numsSize) {
    if (numsSize <=0) return false;
    int max = numsSize * 100;
    bool *dp = malloc(max * sizeof(bool));
    memset(dp, 0, max * sizeof(bool));
    dp[0] = true;
    bool ret = false;
    int sum = 0;
    for(int i=0;i<numsSize; ++i)
    {
        sum += nums[i];
        for(int j=max-1; j>=nums[i]; --j)
        {
            dp[j] |= dp[j-nums[i]];
        }
    }
    if (!(sum&1))
    {
        ret = dp[sum>>1];
    }
    free(dp);
    return ret;
}