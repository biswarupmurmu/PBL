# Application Configuration

app.config.from_envvar('YOURAPPLICATION_SETTINGS')
## Bash
$ export OURAPPLICATION_SETTINGS=/path/to/settings.cfg
$ flask run
 * Running on http://127.0.0.1:5000/

## CMD
> set OURAPPLICATION_SETTINGS=\path\to\settings.cfg
> flask run
 * Running on http://127.0.0.1:5000/

## Powershell
> $env:OURAPPLICATION_SETTINGS = "\path\to\settings.cfg"
> flask run
 * Running on http://127.0.0.1:5000/


# Flask WT Forms
intigrity error
form validation