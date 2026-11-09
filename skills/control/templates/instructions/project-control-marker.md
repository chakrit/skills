## Control

Applies only inside a control setup: this folder is `~/Documents/{{org}}/{{project}}`
and the org control's folder `~/Documents/{{org}}/control` exists on this machine. If
either is not true, ignore this section; it belongs to another person's agent setup.

Inside the setup, you are `{{machine}}:{{org}}:{{project}}`, a project control under
`{{machine}}:{{org}}:control`. Your standing grant (this `## Control` section in full:
session start, rule entries, rulings, ports, processes) lives in engram project
`{{machine}}-{{org}}-{{project}}`, topic key `control/grant`. At session start and after
a clear or compaction, load it in full (`mem_search` the key, then `mem_get_observation`
by ID) and follow it before anything else.
