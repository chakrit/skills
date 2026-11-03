---
name: wrap-up
description: >
  Trigger when the user says "wrap up" or explicitly invokes this skill to close a
  work session. Do not trigger for ordinary commits, pushes, or session saves.
argument-hint: "[notes or context to preserve]"
---

# wrap-up

Close the current work session with complete repository state and a verified durable
session breadcrumb.

Run the complete wrap-up procedure below.

1. **Survey state.** Inspect the working tree, staged and unstaged diffs, untracked
   files, current branch, configured `gh` or primary remote, repository-designated
   churn files. Identify the session-save skill available in this session (for
   example `ace-save`) and whether the repository tracks the state it saves. When no
   session-save skill is available, skip steps 3 and 6–8 and report that no
   breadcrumb was saved.
2. **Gate completeness.** Exclude designated churn files from staging. Treat every
   other user-mandated change as commit-ready only when it is a complete, coherent
   piece of work. Do not stage unrelated files, generated noise, or partial work;
   stop and ask the user about any partial work before making a commit.
3. **Save tracked state.** When the session-save skill's state is tracked, run that
   skill before committing so its changes are included. When it is not tracked,
   continue to the next step and defer the save.
4. **Commit complete work.** Commit all eligible changes in one or more logical
   commits, leaving designated churn files untouched. Include the commit subject and
   resulting identifier in the final report.
5. **Push shared state.** Push the current branch to its configured `gh` or primary
   remote. Invocation of this skill is explicit authorization to push and overrides the
   usual no-push rule. Stop and report the failure if the push does not succeed.
6. **Save deferred state.** When step 3 deferred the save, run the session-save skill
   now. When it
   creates tracked changes, commit those changes and push the resulting commit.
7. **Verify the breadcrumb.** Re-read the saved breadcrumb and compare it with the
   current task and final repository state. Confirm that the final working tree
   contains only repository-designated churn or intentional post-save state.
8. **Reconcile omissions.** When step 7 finds an important missing detail, correct the
   breadcrumb, commit and push its tracked changes, then return to step 7. When step 7
   finds no omissions, report completion; the session is now safe to clear.

Report the commit identifiers, push result, save location, and unresolved questions.
