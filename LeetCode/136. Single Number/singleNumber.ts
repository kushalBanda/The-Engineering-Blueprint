export function singleNumber(nums: number[]): number {
    const seen: { [key: number]: number } = {};
    for (const num of nums ) {
        seen[num] = (seen[num] || 0) + 1
    } 
    for (const [num, count] of Object.entries(seen)) {
        if (count === 1) {
            return Number(num);
        }
    }
    return 0;
}

console.log(singleNumber([4, 1, 2, 1, 2]))