# Heavy-job slots

Heavy jobs: full test suites, browser test runs, dependency installs, image builds,
native compiles. Machine control grants slots to org controls and records the org as
holder; an org control keeps the slots it holds here, passes one to a project, records
the project as holder, and returns the slot when the project reports done.

| Slot  | Takes                                           | Holder |
| ----- | ----------------------------------------------- | ------ |
| big   | one large job: image build, full suite, compile | none   |
| light | cache-backed installs, lint, type checks only   | none   |
