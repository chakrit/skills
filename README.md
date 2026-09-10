# Chakrit Skills

Chakrit's personally published agent skills, distributed as an ACE school and as
ordinary skill directories.

| Skill                                    | Purpose                          | Maintained here |
|------------------------------------------|----------------------------------|-----------------|
| [fact-check](skills/fact-check/SKILL.md) | Verify claims and assess reviews | Yes             |
| [learn](skills/learn/SKILL.md)           | Adaptive technical tutoring      | Yes             |
| [kien-thai](skills/kien-thai/SKILL.md)   | Natural Thai writing             | Imported        |
| [kode-thai](skills/kode-thai/SKILL.md)   | Iterative Thai writing audits    | Imported        |

## Use the skills

Copy a complete directory from `skills/` into the skill directory supported by your
agent. Keep its references and scripts together. Install `kien-thai` alongside
`kode-thai`, which depends on it.

For ACE, subscribe another project to a local checkout of this school:

```sh
ace setup /path/to/skills
```

After this repository is published, projects can subscribe with `ace setup chakrit/skills`.

## Maintain the school

`school.toml` imports the two Thai skills. `ace.toml` selects PROD9 as the
workflow school used to maintain this repository; those workflow skills are not
published here.

Before refreshing imports, confirm that `ace paths school` resolves this checkout.
With this checkout selected as the target school, use `ace school pull` to refresh
its imports and `ace school validate` to check its configuration. `ace link` updates
the current project's workflow links from the school selected in `ace.toml`.

Edit `fact-check` and `learn` directly here. Changes to the imported Thai skills
belong in [chakrit/kien-thai](https://github.com/chakrit/kien-thai); a later pull
refreshes their local copies.

## Documentation and references

Each skill owns its `references/` and, when needed, `docs/` directory. Fact-check's
[design notes](skills/fact-check/docs/design.md) travel with its package.
Kien-thai's [research and maintenance docs](https://github.com/chakrit/kien-thai/tree/main/docs),
[corpus](https://github.com/chakrit/kien-thai/tree/main/corpus), and
[evaluation tooling](https://github.com/chakrit/kien-thai/tree/main/tests) remain
upstream; ACE imports the skill packages, not that development workspace.

## Sources

The direct ingestions started from these revisions:

- `fact-check`: `chakrit/fact-check` at
  `a88af9a75e06297a15c728d2907882a3e379eefe`.
- `learn`: `chakrit/learn` at
  `4a35557ed7b1fa330f184f9f15899fffb1714d67`.

Both are maintained here after ingestion and are not refreshed by `ace school pull`.
The Thai packages are refreshed through `school.toml` imports.

## License

[MIT](LICENSE) applies throughout this repository. Include the root license when
redistributing individual skill packages.
