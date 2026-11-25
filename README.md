# Location demonstration (experimental)

This Flask prototype handles browser location submissions and displays collected information in a dashboard. It is not suitable for public deployment in its current form.

## Privacy and safety limitations

The current backend collects precise coordinates and IP addresses, retains them in process memory, logs sensitive information, and exposes a dashboard without visible authentication. Debug mode is enabled. The news endpoint returns fabricated example headlines, not verified news.

Do not deploy or use this prototype to collect other people's data. Review consent, data minimization, access controls, deletion and debug settings before any further use. Use synthetic data for development.

## Repository layout

- `app.py`: Flask backend.
- `templates/`: HTML templates.
- `requirements.txt`: Python dependencies.

## License

Licensing is deferred pending ownership and privacy review.
