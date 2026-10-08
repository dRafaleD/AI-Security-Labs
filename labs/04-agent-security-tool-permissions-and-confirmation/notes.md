# Day 4 — Agent Security, Tool Permissions, Authorization and Human Confirmation

[🇬🇧 English](notes.md) | [🇹🇷 Türkçe](notes.tr.md)

## Goal

Understand why an AI agent becomes more security-sensitive when it can take actions, not just generate text.

This day combines:

1. agent vs chatbot,
2. tool capabilities,
3. least privilege,
4. authentication vs authorization,
5. argument validation,
6. confirmation gates,
7. read vs write vs destructive actions,
8. tool result handling,
9. confused-deputy risk,
10. audit logging,
11. deterministic enforcement,
12. local tool-execution simulation.

Core rule:

> A model may propose an action; application code decides whether that action is allowed.

## 1. Chatbot vs agent

A plain chatbot mostly produces text:

~~~text
user -> model -> text
~~~

An agent can request actions:

~~~text
user
  ↓
model
  ↓
tool request
  ↓
application policy
  ↓
tool execution
~~~

The security impact is larger because bad reasoning can become a real side effect.

## 2. Capability matters

Risk depends on what a tool can do.

Examples:

- read a note,
- create a file,
- send an email,
- delete data,
- publish content,
- make a payment,
- change permissions.

A tool that can only read public data is not equivalent to one that can delete or publish.

## 3. Least privilege

Give the agent only the minimum capability required.

Bad default:

~~~text
read everything
write everything
delete everything
admin everywhere
~~~

Better:

~~~text
task
  ↓
minimum tool
  ↓
minimum scope
  ↓
minimum permission
  ↓
minimum duration
~~~

## 4. Authentication vs authorization

Authentication:

> Who is the user?

Authorization:

> Is this user allowed to perform this tool action?

The model should not decide this by guessing from conversation text.

Use server-side identity and policy.

## 5. Tool request pipeline

A secure tool request should pass several stages:

~~~text
model proposes tool
      ↓
tool exists?
      ↓
user authorized?
      ↓
arguments valid?
      ↓
scope allowed?
      ↓
confirmation needed?
      ↓
execute
      ↓
log result
~~~

Skipping these stages turns the model into an unsafe policy engine.

## 6. Argument validation

Even an allowed tool can receive dangerous or nonsensical arguments.

Validate:

- required fields,
- types,
- lengths,
- enums,
- resource identifiers,
- allowed scopes.

Do not pass arbitrary model-generated dictionaries directly into sensitive APIs.

## 7. Allowlisted tools

Prefer a fixed set of tools exposed by the application.

~~~text
allowed:
- read_note
- create_note

not exposed:
- arbitrary_shell
- arbitrary_sql
- arbitrary_http_admin
~~~

The model should not invent new privileged capabilities.

## 8. Read, write and destructive actions

Classify actions by impact.

### Read
Usually lower risk, but can still leak sensitive data.

### Write
Changes state.

### Destructive
Deletes, revokes, overwrites, publishes, or causes irreversible effects.

Higher-impact actions deserve stronger controls.

## 9. Human confirmation

For important actions:

~~~text
model drafts action
      ↓
application shows exact action
      ↓
user confirms
      ↓
server rechecks authorization
      ↓
tool executes
~~~

The confirmation should show what will actually happen.

Bad confirmation:

> Continue?

Better:

> Delete note "welcome"?

## 10. Confirmation is not authorization

A user clicking “yes” does not automatically make an unauthorized action acceptable.

Correct order:

~~~text
authorize
  ↓
validate
  ↓
confirm if required
  ↓
execute
~~~

## 11. Confused deputy

A confused deputy problem happens when a privileged component performs an action on behalf of someone who should not have that privilege.

In AI systems:

~~~text
low-privilege user
      ↓
persuasive prompt
      ↓
high-privilege agent/tool
      ↓
sensitive action
~~~

The defense is deterministic authorization at the tool boundary.

## 12. Model confidence is not permission

Statements such as:

> “I am sure this is authorized.”

or:

> “The user asked clearly.”

have no security meaning by themselves.

Permission must come from trusted application state.

## 13. Tool output can also be untrusted

A tool may return:

- webpage text,
- email,
- document content,
- API data.

The returned text can contain instruction-like content.

Tool output should stay data unless the application explicitly defines otherwise.

This connects to Day 2 and Day 3.

## 14. Local demo

Run:

~~~bash
python3 agent_tool_security_demo.py
~~~

No model or external API is used.

The demo contains three tools:

- read_note,
- create_note,
- delete_note.

It also has role-based policies and confirmation requirements.

## 15. What to observe

The demo shows:

- student can read,
- student cannot delete,
- admin may delete only after confirmation,
- arguments are validated before execution.

This is the main architecture pattern.

## 16. Tool schemas

A good tool definition should be narrow.

Example:

~~~json
{
  "tool": "read_note",
  "arguments": {
    "name": "welcome"
  }
}
~~~

This is better than:

~~~json
{
  "tool": "filesystem",
  "command": "anything"
}
~~~

Narrow tools reduce accidental and malicious capability.

## 17. Scope restrictions

Even a valid tool may need resource scope.

Example:

~~~text
GitHub tool
  ↓
only repository A
  ↓
only create issue
  ↓
no repository deletion
~~~

Do not grant organization-wide access if one repository is enough.

## 18. Secrets

The model should not need raw API tokens when the tool can hold credentials internally.

Better:

~~~text
model -> request "create issue"
tool service -> uses credential internally
~~~

not:

~~~text
credential -> model context -> generated tool call
~~~

Minimize secret exposure.

## 19. Audit logging

Useful agent-action logs include:

- user identity,
- requested tool,
- validated arguments,
- authorization result,
- confirmation result,
- execution result,
- timestamp,
- correlation/request ID.

Avoid logging credentials or unnecessary sensitive content.

## 20. Fail closed

If policy cannot determine whether an action is allowed:

~~~text
uncertain
   ↓
deny / require review
~~~

Do not silently default to privileged execution.

## 21. Idempotency and retries

Agents may retry actions.

A repeated “create payment” or “send email” can cause duplicate side effects.

For state-changing tools, consider:

- idempotency keys,
- duplicate detection,
- request IDs,
- retry-safe APIs.

## 22. Timeout and partial failure

A tool may time out after performing the action.

The agent may think it failed and retry.

Therefore:

~~~text
no response != definitely no side effect
~~~

This is a systems-security issue, not just an AI issue.

## 23. Mini challenge — email tool

Design:

- draft_email,
- send_email.

Rules:

- all users may draft,
- send requires authorization,
- recipient must be validated,
- exact message shown before confirmation,
- SMTP credential hidden from model,
- request ID prevents duplicate send.

## 24. Mini challenge — GitHub tool

Design an agent that can create issues in one repository.

Decide:

- allowed repo,
- allowed action,
- argument schema,
- authorization source,
- confirmation requirement,
- logging fields.

Explain why arbitrary repository/admin access is unnecessary.

## 25. Mini challenge — destructive action

Add a simulated archive_note tool.

Then decide whether it is:

- read,
- write,
- destructive.

Add the appropriate policy and confirmation requirement.

## 26. Review checklist

~~~text
1. Which tools exist?
2. Which are read/write/destructive?
3. Who may use each tool?
4. Are arguments schema-validated?
5. Is resource scope restricted?
6. Are credentials hidden from the model?
7. Does high-impact action require confirmation?
8. Is authorization rechecked at execution?
9. Are retries safe?
10. Are tool outputs treated as data?
11. Are actions audited?
12. Does failure default to deny?
~~~

## Exercises

1. Run the local demo.
2. Explain why student delete is denied.
3. Explain why admin delete still requires confirmation.
4. Add a read-only tool.
5. Add argument length validation.
6. Add a simulated archive tool.
7. Classify each tool by impact.
8. Design the email flow.
9. Design the GitHub issue flow.
10. Add request IDs to the demo.
11. Explain one retry problem.
12. Explain confused deputy in your own words.

## Questions

1. What makes an agent riskier than a chatbot?
2. What is least privilege?
3. Authentication vs authorization?
4. Why validate tool arguments?
5. Why use narrow tools?
6. Why can confirmation not replace authorization?
7. What is confused deputy?
8. Why should credentials stay outside model context?
9. Why can retries be dangerous?
10. Why should tool outputs remain untrusted data?
11. What should be logged?
12. What does fail closed mean?

## Main takeaway

~~~text
model proposes
   ↓
application validates
   ↓
application authorizes
   ↓
confirmation when needed
   ↓
bounded tool executes
   ↓
audit log
~~~

Agent security is mostly about controlling capabilities, not trusting model intent.
