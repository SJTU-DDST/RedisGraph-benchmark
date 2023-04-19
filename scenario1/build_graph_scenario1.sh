rg_host=$1
rg_port=$2

redisgraph-bulk-insert scenario1 --host ${rg_host} --port ${rg_port} \
--enforce-schema --skip-invalid-nodes --skip-invalid-edges --separator , --id-type INTEGER \
--nodes ./router.csv \
--relations ./relation.csv \
--index router:id --index router:ip