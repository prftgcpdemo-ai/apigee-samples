if [ -z "$PROJECT" ]; then
  echo "No PROJECT variable set"
  exit
fi

if [ -z "$APIGEE_ENV" ]; then
  echo "No APIGEE_ENV variable set"
  exit
fi

if [ -z "$APIGEE_HOST" ]; then
  echo "No APIGEE_HOST variable set"
  exit
fi

if [ -z "$SA_TOKEN" ]; then
  SA_TOKEN=$(gcloud auth print-access-token)
fi

echo "Creating Vertex AI index and endpoint"

curl --location --request POST \
"https://$REGION-aiplatform.googleapis.com/v1/projects/$PROJECT/locations/$REGION/indexes" \
--header "Authorization: Bearer $SA_TOKEN" \
--header 'Content-Type: application/json' \
--data-raw \
'{"displayName": "semantic-cache-index", "description": "semantic-cache-index", "metadata": {"config": {"dimensions": "768","approximateNeighborsCount": 150,"distanceMeasureType": "DOT_PRODUCT_DISTANCE","featureNormType": "NONE","algorithmConfig": {"treeAhConfig": {"leafNodeEmbeddingCount": "10000","fractionLeafNodesToSearch": 0.05}},"shardSize": "SHARD_SIZE_MEDIUM"},},"indexUpdateMethod": "STREAM_UPDATE"}'

gcloud ai index-endpoints create \
--display-name=semantic-cache-index-endpoint \
--public-endpoint-enabled \
--region=$REGION \
--project=$PROJECT

INDEX_ENDPOINT_ID=$(gcloud ai \
index-endpoints list \
--project=$PROJECT \
--region=$REGION \
--format="json" | jq -c -r \
'.[] | select(.displayName="semantic-cache-index-endpoint") | .name | split("/") | .[5]' \
) && INDEX_ID=$(gcloud ai \
indexes list \
--project=$PROJECT \
--region=$REGION \
--format="json" | jq -c -r \
'.[] | select(.displayName="semantic-cache-index") | .name | split("/") | .[5]' \
) && gcloud ai index-endpoints \
deploy-index \
$INDEX_ENDPOINT_ID \
--deployed-index-id=semantic_cache_index_endpoint_deployment \
--display-name=semantic-cache-index-endpoint-deployment \
--index=$INDEX_ID \
--region=$REGION \
--project=$PROJECT

echo "Successfully created INDEX_ENDPOINT_ID=$INDEX_ENDPOINT_ID"


