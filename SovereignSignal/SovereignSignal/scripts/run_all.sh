#!/bin/bash
python3 src/api/main.py &
python3 src/tasks/scheduler.py &
echo 'System started.'