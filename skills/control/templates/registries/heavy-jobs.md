# Heavy-job slots

Heavy jobs: full test suites, browser test runs, dependency installs, image builds,
native compiles. Machine control grants slots to org controls; an org control passes
its slot to one project and returns it when the project reports done.

| Slot  | Takes                                           | Holder |
| ----- | ----------------------------------------------- | ------ |
| big   | one large job: image build, full suite, compile | none   |
| light | cache-backed installs, lint, type checks only   | none   |
