# subbox

DELETE your GOOGLE account!

scripts to manage your "you"tube subscriptions

## Usage

Download past 24h videos to a folder named after todays date in iso format

```bash
./download.sh
```

Play videos: required macOS and VLC player installed

```bash
./play.sh
```

or specify the date

```bash
./play.sh 2021-01-15
```

## Setup

create a file called subscriptions containing channel url you want to subscribe to

```bash
echo 'https://www.youtube.com/c/3blue1brown' > subscriptions
```
