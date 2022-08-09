# Historical Weather App

By Edan Schwartz, Aug. 2022

## Usage

This script is available as a CLI tool. eg:

```sh
./historical_weather days-of-precip --city bos
```

For a full help text, use the `-h` flag:

```sh
./historical_weather -h
```

Help text is also available for subcommands, eg:

```sh
./historical_weather days-of-precip -h
```

## Requirements

This tool was developed using Python 3.9.10, and has not been tested in other versions of python.

If you do not have that version of python installed, you may also try running the app in a docker container. The provided [`docker_historical_weather`](./docker_historical_weather) script executes the `historical_weather` CLI tool in a `python:3.9.10` docker container:

```sh
./docker_historical_weather days-of-precip --city bos
```

No other libraries or dependencies are required.

## Shortcomings

The major shortcoming of this code is that it does **not include any automated testing**. This was a decision made in consideration of the time constraints.

I would generally start a project like this with test cases that cover basic functionality, and work from there. The code here is generally setup in way where each concern could be tested independently (ie. command logic vs. CSV parsing vs CLI arg parsing, etc).