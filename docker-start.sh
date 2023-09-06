export JOB_ID="1234"
export NUM_IMAGES="8"
export CREDENTIALS=$(cat keyfile.json)
export BUCKET_NAME="envision-jobs"

docker run -e JOB_ID=$JOB_ID -e NUM_IMAGES=$NUM_IMAGES -e CREDENTIALS=$CREDENTIALS -e BUCKET_NAME=$BUCKET_NAME ml-job