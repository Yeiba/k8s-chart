
kubectl exec -it mongos -n mongo-shard -- mongosh --port 27017 --eval "sh.addShard('shard1ReplSet/shard1-0.shard1:27017'); sh.addShard('shard2ReplSet/shard2-0.shard2:27017');"

kubectl exec -it mongos -n mongo-shard -- mongosh --port 27017  --eval "sh.status()"
