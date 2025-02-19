## API Endpoints

The analytics backend provides the following REST API endpoints:

- `GET /api/v1/analytics/records/`: List all detection records
- `POST /api/v1/analytics/visitors/` Create a new detection record
- `GET /api/v1/analytics/stores/metrics/?store_id=<store_id>&date=<date>`: Retrieve a specific detection record (date is an optional parameter)
