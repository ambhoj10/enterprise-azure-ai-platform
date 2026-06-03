from azure.monitor.opentelemetry import configure_azure_monitor

from app.config import settings


def setup_telemetry():

    if not settings.APPLICATIONINSIGHTS_CONNECTION_STRING:
        return

    configure_azure_monitor(
        connection_string=(
            settings.APPLICATIONINSIGHTS_CONNECTION_STRING
        )
    )
