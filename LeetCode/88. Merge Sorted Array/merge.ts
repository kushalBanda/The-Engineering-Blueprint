function merge(nums1: number[], m: number, nums2: number[], n: number): number[] {
    const combinedList = nums1.slice(0, m).concat(nums2.slice(0, n));
    combinedList.sort((a, b) => a - b);
    
    for (let i = 0; i < combinedList.length; i++) {
        nums1[i] = combinedList[i];
    }
    return nums1;
}

console.log(merge([1,2,3,0,0,0], 3, [2,5,6], 3));