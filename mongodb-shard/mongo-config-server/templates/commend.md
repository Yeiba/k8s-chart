kubectl exec -it config-server-0 -n mongo-shard -- mongosh --port 27019 --eval "rs.initiate();"
kubectl exec -it config-server-0 -n mongo-shard -- mongosh --port 27019 --eval "var cfg = rs.conf(); cfg.members[0].host='config-server-0.config-server:27019'; rs.reconfig(cfg);"
kubectl exec -it config-server-0 -n mongosh --port 27019 --eval "rs.add('config-server-1.config-server:27019'); rs.add('config-server-2.config-server:27019');"

kubectl exec -it config-server-0 -n mongo-shard -- mongosh --port 27019  --eval "rs.status()"
