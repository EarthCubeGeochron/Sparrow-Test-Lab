export SPARROW_LAB_NAME="Test Lab"
export SPARROW_ENV="development"
export SPARROW_PLUGIN_DIR="$SPARROW_CONFIG_DIR/plugins"
export SPARROW_COMPOSE_OVERRIDES="$SPARROW_CONFIG_DIR/pgweb-addon/docker-compose.override.yaml"

# Get "secret" config values from an overrides file.
source "$SPARROW_CONFIG_DIR/sparrow-config.overrides.sh"
