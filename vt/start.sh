#!/bin/bash

python -m vttest.run_local_database --port 12345 --web_dir2 /vt/web/vtctld2/app "$@"
