# Implementing Statsig in Django

You will need to define an environment variable `STATSIG_SECRET_KEY` with your Statsig secret key.

Then we bootstrap the project.

```shell
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run Django server
./manage.py runserver
```

You will see it bootstrap Statsig. Now ctrl+c to stop the server.

Observe you get this warning:

```text
2025-07-29T21:16:37.481Z WARN  [Statsig::StatsigRuntime] Attempt to shutdown runtime from inside runtime
2025-07-29T21:16:37.519Z WARN  [Statsig::StatsigRuntime] Attempt to shutdown runtime from inside runtime
```
