# Deadpan Forecast — Updraft City

[![make.fun](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/berkahmuse/deadpan-forecast-berkahmuse/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/berkahmuse/deadpan-forecast-berkahmuse/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

Entry for the [Deadpan Forecasts for Cities That Do Not Exist](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c) bounty on [make.fun](https://make.fun).

## The forecast

> Updraft City: rain falls upward at 14 miles an hour tonight, so residents carry their umbrellas upside down and street sweepers work the sky.

One line, 141 characters. Updraft City is a city where the rain falls *up*,
so everyday life has quietly adapted around it: umbrellas are carried upside
down, and the street sweepers do their work in the sky. Delivered deadpan,
exactly as a TV meteorologist would read it off the map.

## How it works

`main.py` (Python 3.13, standard library only) writes the single forecast line
to `/output/entry.txt`. The program is fully deterministic: a fixed string, no
input, no randomness, no network — every run produces byte-identical output.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
