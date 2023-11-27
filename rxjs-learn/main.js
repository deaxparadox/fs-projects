const { range, filter, map } = rxjs;

range(1, 200)
    .pipe(
        filter((x) => x % 2 === 1),
        map((x) => x + x)
    )
    .subscribe((x) => console.log(x));

// [1, 2, 3, 4].reduce((a, b) {
//     if (a > b) {
        
//     }
// })