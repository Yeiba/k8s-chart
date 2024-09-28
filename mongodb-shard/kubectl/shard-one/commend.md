kubectl exec -it shard1-0 -n mongo-shard -- mongosh --port 27019 --eval "rs.initiate();"
kubectl exec -it shard1-0 -n mongo-shard -- mongosh --port 27019 --eval "var cfg = rs.conf(); cfg.members[0].host='shard1-0.shard1:27017'; rs.reconfig(cfg);"
kubectl exec -it shard1-0 -n mongosh --port 27019 --eval "rs.add('shard1-1.shard1:27017'); rs.add('shard1-2.shard1:27017');"

kubectl exec -it shard1-0 -n mongo-shard -- mongosh --port 27019  --eval "rs.status()"
