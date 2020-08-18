(money,coins)
// {
//     for(m=1;m<=money;m++)
//     {
//         minimum_coin_change[m] = Number.MAX_SAFE_INTEGER
//         for(let coin in coins)
//         {
//             if(m >= coin)
//             {
//                 temp_min = minimum_coin_change[m-coin] + 1
//                 if(temp_min < minimum_coin_change[m])
//                     {
//                     minimum_coin_change[m] = temp_min
//                     }
//             }
//         }
//     }
//     return minimum_coin_change[money]
// }
// console.log(no_of_change(10,coins))
// console.log(minimum_coin_