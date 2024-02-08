#!/bin/bash
echo "Testing APIs..."
python initialize_database.py
python test_api.py
echo "Testing complete"
