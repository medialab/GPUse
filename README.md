# GPUse

Simple lightweight (serverless & database free) web dashboard for monitoring historical GPUs uses & metrics on a machine (includes Percent use, Memory, Energy, Temperature, Fan Speed & list of running processes).


## Install

- First clone the repository in some directory accessible to your system's web server, for instance `/var/www/html/` :

```bash
git clone https://github.com/medialab/GPUse
cd GPUse
```

- Create a dedicated Python environment using pyenv (simple install using [pyenv-installer](https://github.com/pyenv/pyenv-installer?tab=readme-ov-file#pyenv-installer)) and install the `gpustat` dependency within:

```bash
pyenv virtualenv 3.12
pyenv activate gpuse
pip install -r requirements.txt
pyenv deactivate
```

- Setup a cron job running every minute to read and archive GPU metrics using `crontab -e` and adding the following line at the bottom:

```
# m h  dom mon dow   command
  * *   *   *   *    bash <ABSOLUTE PATH TO YOUR INSTALL DIRECTORY>/save_snapshot.sh
```

- Serve the directory on the web with Nginx or Apache, or for quick tests with:

```bash
python -m http.server 8888
```

- Visit the dashboard in a browser, for instance with the above python server example at:

http://localhost:8888


## Credits & License

Built by [@boogheta](https://github.com/boogheta) from [@medialab](https://github.com/medialab) for daily monitoring uses of our GPU equipped servers for computational social sciences uses.

Released as Free Libre Open Source software under the [AGPL v3 license](./LICENSE).
