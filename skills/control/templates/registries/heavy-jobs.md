# Heavy-job slots

Heavy jobs: full test suites, browser test runs, dependency installs, image builds,
native compiles. Machine control grants slots to org controls; an org control passes
its slot to one project and returns it when the project reports done.

## Slots

| Slot  | Takes                                           | Holder |
| ----- | ----------------------------------------------- | ------ |
| big   | one large job: image build, full suite, compile | none   |
| light | cache-backed installs, lint, type checks only   | none   |

## Gates

Check before each grant. Tune to this machine with chakrit.

- Hold the light slot while free memory is under 45%.
- Grant nothing while free disk is under 2 GiB.

## Queue

| Requested | Org | Project | Slot | Command | Expected duration |
| --------- | --- | ------- | ---- | ------- | ----------------- |

## Log

| Time | Org | Project | Event | Command or result |
| ---- | --- | ------- | ----- | ----------------- |
