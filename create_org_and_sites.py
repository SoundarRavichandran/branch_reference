import os
import logging as logger

org_id = os.environ['Org_ID']
site_count = os.environ['Number_Of_Sites']
node_distribution = os.environ['Node_Site_Distribution']
tel_frequency = os.environ.get('Node_Telemetry_Frequency')

# org_id = "some_org_id"
# site_count = 2
# node_distribution = {"site1": 4, "site2": 10}
# tel_frequency = 30

class TestCreateOrgSites:

    def test_create_org_site(self):
        logger.info(f"Variables are {org_id}, {site_count}, {node_distribution}, {tel_frequency}")


