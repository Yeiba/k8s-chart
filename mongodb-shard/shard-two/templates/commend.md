kubectl exec -it shard2-0  -n mongo-shard -- mongosh --port 27017 --eval "rs.initiate();"
kubectl exec -it shard2-0 -n mongo-shard -- mongosh --port 27017 --eval "var cfg = rs.conf(); cfg.members[0].host='shard2-0.shard2:27017'; rs.reconfig(cfg);"
kubectl exec -it shard2-0 -n mongosh --port 27017 --eval "rs.add('shard2-1.shard2:27017'); rs.add('shard2-2.shard2:27017');"

kubectl exec -it shard2-0 -n mongo-shard -- mongosh --port 27017  --eval "rs.status()"
