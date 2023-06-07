import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration


sentry_sdk.init(
    dsn="https://e3fe0a5a58064795a16a6aef8b96aeb7@o4505312330711040.ingest.sentry.io/4505312335888384",
    integrations=[
        FlaskIntegration(),
    ],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)

@app.route('/debug-sentry')
def trigger_error() -> str:
    division_by_zero = 'hello'
    return division_by_zero


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
