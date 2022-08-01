/**
 * Find the Symmetric Difference
 * @param {} args
 * @returns 
 */

function sym(...args) {
    const s = new Set(args.reduce((acc, cur) => {
      if (acc.length === 0) {
        return cur;
      } else {
        const a = new Set(acc);
        const b = new Set(cur);
        return [
          ...acc.filter(x => !b.has(x)),
          ...cur.filter(x => !a.has(x))
        ];
      }
    }, []))
    return Array.from(s);
}
  
console.log(sym([1, 2, 3, 3], [5, 2, 1, 4], [3, 4, 7, 8, 9, 10]));
