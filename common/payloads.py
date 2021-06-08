"""Payloads for testing the JIRA API."""
from datetime import datetime

DASHBOARDS = {
    "CREATE_OK": {
        "name": f"Test dashboard {datetime.now()}",
        "description": "Some test description",
        "sharePermissions": []
    },
    "CREATE_FAIL_1": {
        "name": f"Test dashboard {datetime.now()}",
        "description": "Some test description",
        "sharePermissions": {}  # incorrect field
    }
}
