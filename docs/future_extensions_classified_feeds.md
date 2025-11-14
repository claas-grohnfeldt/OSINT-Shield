# Future Extensions – Classified Feeds

## Drop-in connectors

- Implement a new subclass of `BaseConnector` (e.g., `ClassifiedSigintConnector`, `InternalSensorConnector`).
- Fetch from the secured source (message bus, S3, Kafka) and map outputs to the same `NormalizedRecord` fields.
- Tag `source_type` with `FUTURE_CLASSIFIED_SIGINT` or `FUTURE_INTERNAL_LOGS` to preserve provenance.

## Schema considerations

- `Source` already stores type + description; extend with `classification_level` if needed.
- `Event` can hold extra metadata via the JSON column—mark records as `classified: true` or add release controls.
- Additional entity types (e.g., asset IDs) fit naturally in the `Entity` table.

## Processing pipeline

- Classified feeds automatically benefit from the classifier, NER, clustering, and scoring modules.
- Use feature flags or ACLs at the API layer to hide sensitive events from unapproved clients.
- Add connector-specific health metrics so analysts know whether sensitive feeds are live.

This separation keeps the public OSINT prototype reusable while preparing the path for restricted data.
