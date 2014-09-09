#!/bin/sh

echo "Content-type: text/plain"
echo ""

HISTORY_PATH="/tmp/mnt/im_history"

remote_node_id=`echo "$QUERY_STRING" | sed -n 's/^.*remote_node_id=\([^&]*\).*$/\1/p'`

HISTORY_FILE=$HISTORY_PATH"/"$remote_node_id

cat "$HISTORY_FILE"

