# Webnut Influx

Webnut Influx is a data collector that uses webnut's UI to scrape data and periodically collect these and send to influxdb to be graphed with Grafana or other tools.

I use it on a Raspberry PI with InfluxDB and Grafana.

## Installation

Clone this repository under `/opt` so that it creates `/opt/webnut-influx`. Then make sure to install all requirements using `sudo pip3 install -r requirements.txt`

Copy `config.sample.yml` to `sample.yml` and  update the fields for your environment.

Then just periodically run the script from cron by adding an entry to crontab using `sudo crontab -e`

It should look something like this:

```crontab
*/5 * * * * python3 /opt/webnut-influx/webnut-influx.py
```

The 5 above means it runs every 5 minutes, you can change this to whatever interval you need.

## Environment Variables

Environment variables will override your config.yml. You can setup the following environment variables to finetune your InfluxDB. Given that in most cases the script will run from the same host you probably only need to setup the password.

- `INFLUX_HOSTNAME` - hostname for influxdb, defaults to localhost
- `INFLUX_PORT` - port for the influxdb service, defaults to 8086
- `INFLUX_USERNAME` - username for influxdb, defaults to netmonitor
- `INFLUX_PASSWORD` - username for influxdb, defaults to ``
- `INFLUX_DATABASE` - username for influxdb, defaults to netmonitor