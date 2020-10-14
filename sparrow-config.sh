export SPARROW_LAB_NAME="Test Lab"
export SPARROW_ENV="production"
export COMPOSE_PROJECT_NAME="sparrow_test_lab"
export SPARROW_PLUGIN_DIR="$SPARROW_CONFIG_DIR/plugins"
export SPARROW_COMPOSE_OVERRIDES="$SPARROW_CONFIG_DIR/pgweb-addon/docker-compose.override.yaml"
export SPARROW_DB_PORT=54391
export SPARROW_HTTP_PORT=5099

# Get "secret" config values from an overrides file.
source "$SPARROW_CONFIG_DIR/sparrow-config.overrides.sh"
