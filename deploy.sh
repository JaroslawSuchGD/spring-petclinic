#!/bin/bash

gcloud compute ssh --zone $1 $2 --command="$COMMAND"