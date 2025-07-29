import os

from django.apps import AppConfig
from statsig_python_core import Statsig, StatsigOptions

statsig_client = None


class StatsigConfig(AppConfig):
    name = "app"

    def ready(self):
        """
        This function initializes external service clients when Django starts.
        """

        # For ease, defining global here
        global statsig_client
        print("Initializing Statsig client...")

        options = StatsigOptions()
        options.environment = "development"

        statsig_client = Statsig(os.environ.get("STATSIG_SECRET_KEY"), options)

        # Initialize Statsig
        statsig_client.initialize().wait()
        print("Statsig client initialized successfully.")

    def send_django_shutdown_signal(self, signal, frame):
        """
        This function handles graceful shutdown of external service clients.
        """
        # statsig.StatsigClient._stop_client()
        # sys.exit(0)
