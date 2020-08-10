const prompt = require('prompt-sync')({sigint: true});

function compute_min_refills(distance, tank, stops) {
    var current_refill, fuel, min_refills, prvs_refill;
    stops.push(distance)
    stops.unshift(0)
    console.log(stops)
    console.log(stops)
    min_refills = 0;
    prvs_refill = 0;
    current_refill = 0;
    fuel = tank;
    while ((stops[current_refill] < distance)) {
        while (((stops[current_refill] < distance) && (fuel >= (stops[(current_refill + 1)] - stops[prvs_refill])))) {
            current_refill += 1;
        }
        if ((current_refill === prvs_refill)) {
            return (- 1);
        }
        if ((stops[current_refill] !== distance)) {
            min_refills += 1;
            fuel = tank;
        }
        prvs_refill = current_refill;
    }
    return min_refills;
}

const d = prompt()
const m = prompt()
const n = prompt()
var stops = prompt()
stops = stops.split(' ').map(val => parseFloat(val)).filter(val => !Number.isNaN(val));
console.log(stops)
console.log(compute_min_refills(d, m, stops));

//# sourceMappingURL=car_fueling.js.map
