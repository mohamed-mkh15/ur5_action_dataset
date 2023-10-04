#!/usr/bin/env python3

import sys
import os
from mongo_connector import MongoConnector
from rest_app import RESTApp

if __name__ == "__main__":
    db_connector = MongoConnector(host="mongo_db",
                                  port=27017, 
                                  db_name="logging_db", 
                                  login="root", 
                                  password="root")
    
    app = RESTApp(host="0.0.0.0", 
                port=os.environ.get("GUI_BACKEND_PORT", 8012),
                db_connector=db_connector)
    app.run()