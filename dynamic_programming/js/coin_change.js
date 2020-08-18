coins = [1,6,5]
minimum_coin_change = Array(11).fill(0)

function no_of_change(money,coins)
{
    for(m=1;m<=money;m++)
    {
        minimum_coin_change[m] = Number.MAX_SAFE_INTEGER
        for(let coin of coins)
        {
            if(m >= coin)
            {  
                temp_min = minimum_coin_change[m-coin] + 1
                // console.log(temp_min)
                if(temp_min < minimum_coin_change[m])
                    {
                    minimum_coin_change[m] = temp_min
                    }
            }
        }
    }
    return minimum_coin_change[money]
}
console.log(no_of_change(10,coins))
console.log(minimum_coin_change)