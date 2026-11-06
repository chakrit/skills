# Heavy-job slots

Heavy jobs: full test suites, browser test runs, dependency installs, image builds,
native compiles. Machine control owns these slots, and this is the only record of
them. A project asks its org control, which relays the request here. Holder is the
project as `<org>:<project>`, or `none`; free the slot when the org control relays the
done report.

| Slot  | Takes                                           | Holder |
| ----- | ----------------------------------------------- | ------ |
| big   | one large job: image build, full suite, compile | none   |
| light | cache-backed installs, lint, type checks only   | none   |
