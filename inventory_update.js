function updateInventory(arr1, arr2) {
    const inventory = arr1.concat(arr2).map((item) => {
        return {count: item[0], name: item[1]}
    });
    const updObj = inventory.reduce((acc, cur) => {
        if (acc[cur.name]) {
            acc[cur.name].count += cur.count;
        } else {
            acc[cur.name] = { name: cur.name, count: cur.count };
        }
        return acc
    }, {});
    const updArr = [];
    for (const value of Object.values(updObj)) {
        updArr.push(value);
    }
    return updArr.map(item => [item.count, item.name]).sort(function(a, b){
        if(a[1] < b[1]) { return -1; }
        if(a[1] > b[1]) { return 1; }
        return 0;
    });
};

console.log(updateInventory(
    [
        [21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]
    ],
    [
        [2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]
    ]
));
